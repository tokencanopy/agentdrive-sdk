"""The caller-oriented AgentDrive client and one shared transport bridge."""

from __future__ import annotations

import asyncio
import random
import time
import urllib.parse
from dataclasses import dataclass
from typing import Any

from pydantic import ValidationError as PydanticValidationError

from .auth import AccessToken, TokenProvider
from .errors import (
    AgentDriveError,
    AuthenticationError,
    NetworkError,
    raise_typed_error,
)
from .generated.api_client import ApiClient as GeneratedApiClient
from .generated.configuration import Configuration
from .generated.exceptions import ApiException as GeneratedApiException
from .iteration import CursorItems, CursorPages


CANONICAL_BASE_URL = "https://drive.tokencanopy.com"
DEFAULT_SHARE_BASE_URL = "https://share.tokencanopy.com"


@dataclass(frozen=True)
class RetryPolicy:
    """Bounded retry policy for reads and idempotent mutations."""

    max_attempts: int = 3
    backoff_seconds: float = 0.1
    max_backoff_seconds: float = 1.0
    jitter: float = 0.0
    retry_statuses: frozenset[int] = frozenset({429, 502, 503, 504})

    def __post_init__(self) -> None:
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")
        if self.backoff_seconds < 0 or self.max_backoff_seconds < 0 or self.jitter < 0:
            raise ValueError("retry delays must not be negative")


@dataclass(frozen=True)
class _Invocation:
    data: Any
    status_code: int | None
    headers: dict[str, str]
    raw: Any


class AgentDriveClient:
    """Synchronous ergonomic client over the generated v0 core."""

    def __init__(
        self,
        *,
        token_provider: TokenProvider | None = None,
        base_url: str = CANONICAL_BASE_URL,
        share_base_url: str = DEFAULT_SHARE_BASE_URL,
        generated_api_client: GeneratedApiClient | None = None,
        retry_policy: RetryPolicy | None = None,
        request_timeout: float | tuple[float, float] | None = None,
        inline_upload_limit: int = 15 * 1024 * 1024,
    ) -> None:
        self.base_url = _absolute_origin(base_url)
        self.share_base_url = _absolute_origin(share_base_url)
        self.token_provider = token_provider
        self.retry_policy = retry_policy or RetryPolicy()
        self.request_timeout = request_timeout
        self.inline_upload_limit = inline_upload_limit
        if inline_upload_limit <= 0:
            raise ValueError("inline_upload_limit must be positive")

        if generated_api_client is None:
            configuration = Configuration(host=self.base_url, ignore_operation_servers=True)
            generated_api_client = GeneratedApiClient(configuration)
        else:
            generated_api_client.configuration._base_path = self.base_url
            generated_api_client.configuration.ignore_operation_servers = True
        self.generated_api_client = generated_api_client

        from .generated.api.artifacts_api import ArtifactsApi
        from .generated.api.changes_api import ChangesApi
        from .generated.api.downloads_api import DownloadsApi
        from .generated.api.drives_api import DrivesApi
        from .generated.api.folders_api import FoldersApi
        from .generated.api.grants_api import GrantsApi
        from .generated.api.navigation_api import NavigationApi
        from .generated.api.search_api import SearchApi
        from .generated.api.shares_api import SharesApi
        from .generated.api.uploads_api import UploadsApi
        from .generated.api.versions_api import VersionsApi

        self._apis = {
            "artifacts": ArtifactsApi(generated_api_client),
            "changes": ChangesApi(generated_api_client),
            "downloads": DownloadsApi(generated_api_client),
            "drives": DrivesApi(generated_api_client),
            "folders": FoldersApi(generated_api_client),
            "grants": GrantsApi(generated_api_client),
            "navigation": NavigationApi(generated_api_client),
            "search": SearchApi(generated_api_client),
            "shares": SharesApi(generated_api_client),
            "uploads": UploadsApi(generated_api_client),
            "versions": VersionsApi(generated_api_client),
        }

        from .resources import (
            ArtifactResource,
            ChangeResource,
            DriveResource,
            EntryResource,
            FolderResource,
            GrantResource,
            SearchResource,
            ShareResource,
            UploadResource,
            VersionResource,
        )

        self.drives = DriveResource(self)
        self.entries = EntryResource(self)
        self.folders = FolderResource(self)
        self.artifacts = ArtifactResource(self)
        self.versions = VersionResource(self)
        self.search = SearchResource(self)
        self.changes = ChangeResource(self)
        self.grants = GrantResource(self)
        self.shares = ShareResource(self)
        self.uploads = UploadResource(self)

    def close(self) -> None:
        """Release the generated urllib3 connection pool."""

        pool = getattr(self.generated_api_client.rest_client, "pool_manager", None)
        clear = getattr(pool, "clear", None)
        if clear is not None:
            clear()

    def __enter__(self) -> AgentDriveClient:
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        del exc_type, exc, traceback
        self.close()

    def _invoke(
        self,
        operation: str,
        kwargs: dict[str, Any],
        *,
        mutation: bool = False,
        idempotency_key: str | None = None,
        retry: bool = True,
    ) -> _Invocation:
        """Invoke one generated operation with shared auth/retry semantics."""

        api_name, method_name = _OPERATION_MAP[operation]
        method = getattr(self._apis[api_name], method_name + "_with_http_info")
        call_kwargs = dict(kwargs)
        if mutation:
            call_kwargs["idempotency_key"] = idempotency_key or new_idempotency_key()
        attempts = self.retry_policy.max_attempts if retry else 1
        refreshed = False
        for attempt in range(attempts):
            self._prepare_auth(force_refresh=False)
            try:
                response = method(
                    **call_kwargs,
                    _request_timeout=self.request_timeout,
                )
                return _invocation(response)
            except GeneratedApiException as exc:
                status = exc.status if isinstance(exc.status, int) else None
                if (
                    status == 401
                    and not refreshed
                    and self.token_provider is not None
                    and self.token_provider.refreshable
                ):
                    self._prepare_auth(force_refresh=True)
                    refreshed = True
                    continue
                if status in self.retry_policy.retry_statuses and attempt + 1 < attempts:
                    self._sleep(attempt)
                    continue
                raise_typed_error(exc, operation=operation)
            except PydanticValidationError as exc:
                raise AgentDriveError(
                    "generated request validation failed",
                    status_code=400,
                    code="INVALID_REQUEST",
                    operation=operation,
                    cause=exc,
                ) from exc
            except AgentDriveError:
                raise
            except Exception as exc:
                if attempt + 1 < attempts:
                    self._sleep(attempt)
                    continue
                raise NetworkError(
                    str(exc) or type(exc).__name__, operation=operation, cause=exc
                ) from exc
        raise AssertionError("retry loop exhausted without a result")

    def _prepare_auth(self, *, force_refresh: bool) -> AccessToken | None:
        if self.token_provider is None:
            return None
        try:
            token = self.token_provider.get_token(force_refresh=force_refresh)
        except AgentDriveError:
            raise
        except Exception as exc:
            raise AuthenticationError(
                "could not obtain an AgentDrive access token",
                code="TOKEN_PROVIDER_ERROR",
                cause=exc,
            ) from exc
        self.generated_api_client.configuration.access_token = token.value
        return token

    def _sleep(self, attempt: int) -> None:
        delay = min(
            self.retry_policy.max_backoff_seconds,
            self.retry_policy.backoff_seconds * (2**attempt),
        )
        if self.retry_policy.jitter:
            delay += random.uniform(0, self.retry_policy.jitter)
        if delay:
            time.sleep(delay)

    def _pages(
        self,
        loader: Any,
        *,
        cursor: str | None = None,
        max_pages: int | None = None,
    ) -> CursorPages[Any]:
        return CursorPages(loader, initial_cursor=cursor, max_pages=max_pages)

    def _items(self, pages: CursorPages[Any]) -> CursorItems[Any]:
        return CursorItems(pages)

    async def async_call(self, method: Any, *args: Any, **kwargs: Any) -> Any:
        """Run one synchronous facade method without a second transport."""

        return await asyncio.to_thread(method, *args, **kwargs)


class AsyncAgentDriveClient:
    """Async facade bridge backed by one :class:`AgentDriveClient`."""

    def __init__(self, **kwargs: Any) -> None:
        self._sync = AgentDriveClient(**kwargs)
        self.drives = _AsyncResourceProxy(self._sync.drives)
        self.entries = _AsyncResourceProxy(self._sync.entries)
        self.folders = _AsyncResourceProxy(self._sync.folders)
        self.artifacts = _AsyncResourceProxy(self._sync.artifacts)
        self.versions = _AsyncResourceProxy(self._sync.versions)
        self.search = _AsyncResourceProxy(self._sync.search)
        self.changes = _AsyncResourceProxy(self._sync.changes)
        self.grants = _AsyncResourceProxy(self._sync.grants)
        self.shares = _AsyncResourceProxy(self._sync.shares)
        self.uploads = _AsyncResourceProxy(self._sync.uploads)

    async def __aenter__(self) -> AsyncAgentDriveClient:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        del exc_type, exc, traceback
        await asyncio.to_thread(self._sync.close)

    async def close(self) -> None:
        await asyncio.to_thread(self._sync.close)


class _AsyncResourceProxy:
    def __init__(self, resource: Any) -> None:
        self._resource = resource

    def __getattr__(self, name: str) -> Any:
        method = getattr(self._resource, name)
        if not callable(method):
            return method

        async def invoke(*args: Any, **kwargs: Any) -> Any:
            value = await asyncio.to_thread(method, *args, **kwargs)
            return value

        return invoke


def new_idempotency_key() -> str:
    """Create an opaque key safe to reuse across retries of one mutation."""

    import uuid

    return "sdk-" + uuid.uuid4().hex


def strong_if_match(revision: str) -> str:
    """Turn a bare revision into the strong ETag used by the API."""

    value = str(revision).strip()
    if not value:
        raise ValueError("revision must not be empty")
    if value == "*" or value.startswith("W/"):
        raise ValueError("If-Match requires one strong revision")
    if value.startswith('"') and value.endswith('"'):
        return value
    return f'"{value}"'


def _absolute_origin(value: str) -> str:
    parsed = urllib.parse.urlsplit(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("base URL must be an absolute HTTP(S) URL")
    if parsed.query or parsed.fragment:
        raise ValueError("base URL must not contain a query or fragment")
    return value.rstrip("/")


def _invocation(response: Any) -> _Invocation:
    if hasattr(response, "data"):
        headers = getattr(response, "headers", None) or {}
        return _Invocation(
            data=response.data,
            status_code=getattr(response, "status_code", None),
            headers={str(key).lower(): str(value) for key, value in dict(headers).items()},
            raw=response,
        )
    return _Invocation(data=response, status_code=None, headers={}, raw=response)


# Each entry is the sole handwritten mapping from a facade operation to its
# generated operation.  Wire paths and schemas remain generated output.
_OPERATION_MAP: dict[str, tuple[str, str]] = {
    "drives_list": ("drives", "drives_list"),
    "drives_create": ("drives", "drives_create"),
    "drives_read": ("drives", "drives_read"),
    "drives_update": ("drives", "drives_update"),
    "drives_delete": ("drives", "drives_delete"),
    "drives_restore": ("drives", "drives_restore"),
    "drives_usage": ("drives", "drives_usage"),
    "entries_list": ("navigation", "entries_list"),
    "lookup": ("navigation", "lookup"),
    "folders_list": ("folders", "folders_list"),
    "folders_create": ("folders", "folders_create"),
    "folders_read": ("folders", "folders_read"),
    "folders_update": ("folders", "folders_update"),
    "folders_delete": ("folders", "folders_delete"),
    "folders_restore": ("folders", "folders_restore"),
    "folders_copy": ("folders", "folders_copy"),
    "artifacts_list": ("artifacts", "artifacts_list"),
    "artifacts_create": ("artifacts", "artifacts_create"),
    "artifacts_read": ("artifacts", "artifacts_read"),
    "artifacts_update": ("artifacts", "artifacts_update"),
    "artifacts_delete": ("artifacts", "artifacts_delete"),
    "artifacts_restore": ("artifacts", "artifacts_restore"),
    "artifacts_copy": ("artifacts", "artifacts_copy"),
    "artifacts_content": ("artifacts", "artifacts_content"),
    "versions_list": ("versions", "versions_list"),
    "versions_append": ("versions", "versions_append"),
    "versions_read": ("versions", "versions_read"),
    "versions_restore": ("versions", "versions_restore"),
    "versions_content": ("versions", "versions_content"),
    "drive_search": ("search", "drive_search"),
    "changes_list": ("changes", "changes_list"),
    "grants_list": ("grants", "grants_list"),
    "grants_create": ("grants", "grants_create"),
    "grants_read": ("grants", "grants_read"),
    "grants_update": ("grants", "grants_update"),
    "grants_revoke": ("grants", "grants_revoke"),
    "shares_list": ("shares", "shares_list"),
    "shares_create": ("shares", "shares_create"),
    "shares_read": ("shares", "shares_read"),
    "shares_revoke": ("shares", "shares_revoke"),
    "shares_rotate": ("shares", "shares_rotate"),
    "uploads_create": ("uploads", "uploads_create"),
    "uploads_read": ("uploads", "uploads_read"),
    "uploads_delete": ("uploads", "uploads_delete"),
    "uploads_complete": ("uploads", "uploads_complete"),
    "download_capabilities_create": ("downloads", "download_capabilities_create"),
}
