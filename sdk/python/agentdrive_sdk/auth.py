"""Token providers for Hub-issued AgentDrive access tokens.

AgentDrive does not mint or refresh credentials.  The SDK only caches the
short-lived access token returned by Hub and asks the provider for a new one
when the expiry skew is reached.
"""

from __future__ import annotations

import base64
import json
import threading
import time
import urllib.parse
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Protocol

import urllib3


@dataclass(frozen=True)
class AccessToken:
    """A bearer token and its absolute expiry time in Unix seconds."""

    value: str
    expires_at: float | None = None

    def usable(self, *, now: float | None = None, skew_seconds: float = 60) -> bool:
        if not self.value:
            return False
        if self.expires_at is None:
            return True
        return self.expires_at - (time.time() if now is None else now) > skew_seconds


class TokenProvider(Protocol):
    """Synchronous provider interface used by the generated transport bridge."""

    @property
    def refreshable(self) -> bool:
        """Whether a 401 may cause the provider to renew once."""

    def get_token(self, *, force_refresh: bool = False) -> AccessToken:
        """Return a usable token, renewing when requested or near expiry."""


class TokenProviderError(RuntimeError):
    """The configured token provider could not obtain a bearer token."""


class StaticTokenProvider:
    """Provider for a token supplied by the caller.

    Static providers deliberately do not retry a 401 with a second request:
    there is no renewal operation to perform.
    """

    refreshable = False

    def __init__(self, token: str | AccessToken) -> None:
        self._token = _coerce_token(token)

    def get_token(self, *, force_refresh: bool = False) -> AccessToken:
        del force_refresh
        if not self._token.value:
            raise TokenProviderError("access token must not be empty")
        return self._token


class CallableTokenProvider:
    """Adapter for applications that already own OAuth token renewal."""

    refreshable = True

    def __init__(self, callback: Callable[[bool], str | AccessToken]) -> None:
        self._callback = callback

    def get_token(self, *, force_refresh: bool = False) -> AccessToken:
        return _coerce_token(self._callback(force_refresh))


class OAuthClientCredentialsProvider:
    """Lazy Hub OAuth client-credentials provider.

    The provider sends the long-lived client secret only to Hub.  It stores
    the access token in memory and discards any refresh-token field returned by
    a non-conforming authorization server.
    """

    refreshable = True

    def __init__(
        self,
        token_endpoint: str,
        client_id: str,
        client_secret: str,
        *,
        resource: str = "https://drive.tokencanopy.com",
        scopes: tuple[str, ...] = (),
        expiry_skew_seconds: float = 60,
        timeout_seconds: float = 10,
        http: urllib3.PoolManager | None = None,
    ) -> None:
        if not token_endpoint.startswith(("https://", "http://")):
            raise ValueError("token_endpoint must be an absolute HTTP URL")
        if not client_id or not client_secret:
            raise ValueError("client_id and client_secret are required")
        self.token_endpoint = token_endpoint
        self.client_id = client_id
        self.client_secret = client_secret
        self.resource = resource
        self.scopes = tuple(scopes)
        self.expiry_skew_seconds = expiry_skew_seconds
        self.timeout_seconds = timeout_seconds
        self._http = http or urllib3.PoolManager()
        self._lock = threading.Lock()
        self._cached: AccessToken | None = None

    def get_token(self, *, force_refresh: bool = False) -> AccessToken:
        cached = self._cached
        if not force_refresh and cached and cached.usable(skew_seconds=self.expiry_skew_seconds):
            return cached
        with self._lock:
            cached = self._cached
            if not force_refresh and cached and cached.usable(skew_seconds=self.expiry_skew_seconds):
                return cached
            token = self._fetch()
            self._cached = token
            return token

    def _fetch(self) -> AccessToken:
        fields = {
            "grant_type": "client_credentials",
            "resource": self.resource,
        }
        if self.scopes:
            fields["scope"] = " ".join(self.scopes)
        basic = base64.b64encode(
            f"{self.client_id}:{self.client_secret}".encode("utf-8")
        ).decode("ascii")
        response = self._http.request(
            "POST",
            self.token_endpoint,
            body=urllib.parse.urlencode(fields).encode("ascii"),
            headers={
                "Authorization": f"Basic {basic}",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json",
            },
            timeout=urllib3.Timeout(total=self.timeout_seconds),
            preload_content=True,
            redirect=False,
        )
        try:
            raw = response.data.decode("utf-8")
            payload: Any = json.loads(raw) if raw else {}
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise TokenProviderError("Hub returned an invalid token response") from exc
        if response.status < 200 or response.status >= 300:
            description = payload.get("error_description") if isinstance(payload, dict) else None
            raise TokenProviderError(
                description or f"Hub token request failed with HTTP {response.status}"
            )
        if not isinstance(payload, dict) or not isinstance(payload.get("access_token"), str):
            raise TokenProviderError("Hub token response did not include access_token")
        expires_in = payload.get("expires_in")
        try:
            lifetime = float(expires_in) if expires_in is not None else None
        except (TypeError, ValueError) as exc:
            raise TokenProviderError("Hub token response included invalid expires_in") from exc
        if lifetime is not None and lifetime <= 0:
            raise TokenProviderError("Hub token response included non-positive expires_in")
        return AccessToken(
            value=payload["access_token"],
            expires_at=time.time() + lifetime if lifetime is not None else None,
        )


def _coerce_token(value: str | AccessToken) -> AccessToken:
    if isinstance(value, AccessToken):
        return value
    if isinstance(value, str):
        return AccessToken(value=value)
    raise TypeError("token provider must return str or AccessToken")
