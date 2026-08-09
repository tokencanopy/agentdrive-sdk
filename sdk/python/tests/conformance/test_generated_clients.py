"""Live TCP conformance for both generated Python transports.

The server in this module is deliberately small, but it is not a mocked
``ApiClient``: both generated clients serialize real HTTP requests and send
them over a loopback socket.  The scenarios pin the contract features that are
easy for a generator or transport upgrade to silently damage.
"""

from __future__ import annotations

import asyncio
import json
import threading
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import parse_qs, urlsplit

import pytest

from agentdrive_sdk.generated.async_client.api.artifacts_api import (
    ArtifactsApi as AsyncArtifactsApi,
)
from agentdrive_sdk.generated.async_client.api.drives_api import (
    DrivesApi as AsyncDrivesApi,
)
from agentdrive_sdk.generated.async_client.api_client import ApiClient as AsyncApiClient
from agentdrive_sdk.generated.async_client.configuration import (
    Configuration as AsyncConfiguration,
)
from agentdrive_sdk.generated.async_client.exceptions import (
    ApiException as AsyncApiException,
)
from agentdrive_sdk.generated.async_client.models.drive_create_in import (
    DriveCreateIn as AsyncDriveCreateIn,
)
from agentdrive_sdk.generated.sync.api.artifacts_api import (
    ArtifactsApi as SyncArtifactsApi,
)
from agentdrive_sdk.generated.sync.api.drives_api import DrivesApi as SyncDrivesApi
from agentdrive_sdk.generated.sync.api_client import ApiClient as SyncApiClient
from agentdrive_sdk.generated.sync.configuration import (
    Configuration as SyncConfiguration,
)
from agentdrive_sdk.generated.sync.exceptions import ApiException as SyncApiException
from agentdrive_sdk.generated.sync.models.drive_create_in import (
    DriveCreateIn as SyncDriveCreateIn,
)

TOKEN = "generated-core-conformance-token"
DRIVE_ID = "drv_1111111111111111"
MISSING_DRIVE_ID = "drv_ffffffffffffffff"
ROOT_FOLDER_ID = "fld_2222222222222222"
REVISION = "rev_3333333333333333"
ARTIFACT_ID = "art_4444444444444444"
ETAG = f'"{REVISION}"'
CREATED_AT = "2026-08-09T12:00:00Z"


def _drive() -> dict[str, Any]:
    return {
        "id": DRIVE_ID,
        "workspace_id": "tcws_conformance",
        "created_by": "tcagt_conformance",
        "name": "generated-core",
        "metadata": {"source": "wire-test"},
        "revision": REVISION,
        "root_folder_id": ROOT_FOLDER_ID,
        "storage_bytes": 0,
        "retrieval_bytes": 0,
        "created_at": CREATED_AT,
        "updated_at": CREATED_AT,
        "deleted_at": None,
        "state": "active",
    }


def _artifact() -> dict[str, Any]:
    return {
        "id": ARTIFACT_ID,
        "drive_id": DRIVE_ID,
        "parent_id": ROOT_FOLDER_ID,
        "name": "conformance.txt",
        "content_type": "text/plain",
        "content_preview": "hello generated core",
        "effective_visibility": "private",
        "labels": [],
        "metadata": {"source": "wire-test"},
        "head_version_id": "ver_5555555555555555",
        "revision": REVISION,
        "state": "active",
        "created_at": CREATED_AT,
        "updated_at": CREATED_AT,
        "deleted_at": None,
    }


@dataclass
class _WireState:
    lock: threading.Lock = field(default_factory=threading.Lock)
    api_requests: list[dict[str, Any]] = field(default_factory=list)
    sink_requests: list[dict[str, str | None]] = field(default_factory=list)
    idempotent_drives: dict[str, tuple[str, dict[str, Any]]] = field(
        default_factory=dict
    )
    multipart_content_type: str | None = None
    multipart_body: bytes = b""

    def record_api(self, handler: BaseHTTPRequestHandler) -> None:
        with self.lock:
            self.api_requests.append(
                {
                    "method": handler.command,
                    "path": handler.path,
                    "authorization": handler.headers.get("Authorization"),
                    "idempotency_key": handler.headers.get("Idempotency-Key"),
                    "if_none_match": handler.headers.get("If-None-Match"),
                }
            )


class _QuietHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, _format: str, *_args: object) -> None:
        return

    def _write(
        self, status: int, body: bytes, headers: dict[str, str] | None = None
    ) -> None:
        self.send_response(status)
        for name, value in (headers or {}).items():
            self.send_header(name, value)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body:
            try:
                self.wfile.write(body)
            except (BrokenPipeError, ConnectionResetError):
                # Raw-response and redirect tests may intentionally close the
                # loopback connection before the fixture finishes its write.
                pass

    def _json(
        self,
        status: int,
        value: dict[str, Any],
        headers: dict[str, str] | None = None,
    ) -> None:
        merged = {"Content-Type": "application/json", **(headers or {})}
        self._write(status, json.dumps(value, separators=(",", ":")).encode(), merged)


class _SinkHandler(_QuietHandler):
    state: _WireState

    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        with self.state.lock:
            self.state.sink_requests.append(
                {
                    "authorization": self.headers.get("Authorization"),
                    "cookie": self.headers.get("Cookie"),
                }
            )
        self._write(
            200, b"signed content", {"Content-Type": "application/octet-stream"}
        )


class _AgentDriveHandler(_QuietHandler):
    state: _WireState
    redirect_url: str

    def _route(self) -> tuple[str, dict[str, list[str]]]:
        parsed = urlsplit(self.path)
        assert parsed.path.startswith("/drive/"), parsed.path
        return parsed.path.removeprefix("/drive"), parse_qs(parsed.query)

    def _authenticated(self) -> bool:
        if self.headers.get("Authorization") == f"Bearer {TOKEN}":
            return True
        self._json(
            401,
            {
                "error": {
                    "code": "AUTHENTICATION_REQUIRED",
                    "message": "missing or invalid bearer token",
                }
            },
            {
                "WWW-Authenticate": 'Bearer realm="agentdrive"',
                "X-Request-Id": "req_auth",
            },
        )
        return False

    def _not_found(self) -> None:
        self._json(
            404,
            {"error": {"code": "NOT_FOUND", "message": "resource not found"}},
            {"X-Request-Id": "req_missing"},
        )

    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        self.state.record_api(self)
        path, query = self._route()
        if not self._authenticated():
            return

        if path == "/v0/drives":
            if query.get("cursor") == ["page-2"]:
                page = {"items": [], "next_cursor": None}
            else:
                page = {"items": [_drive()], "next_cursor": "page-2"}
            self._json(200, page, {"X-Request-Id": "req_list"})
            return

        if path == f"/v0/drives/{MISSING_DRIVE_ID}":
            self._not_found()
            return

        artifact_path = f"/v0/drives/{DRIVE_ID}/artifacts/{ARTIFACT_ID}"
        if path == artifact_path:
            if self.headers.get("If-None-Match") == ETAG:
                self._write(304, b"", {"ETag": ETAG, "X-Request-Id": "req_304"})
            else:
                self._json(
                    200,
                    _artifact(),
                    {"ETag": ETAG, "X-Request-Id": "req_artifact"},
                )
            return

        if path == f"{artifact_path}/content":
            self._write(
                307,
                b"",
                {
                    "Location": self.redirect_url,
                    "ETag": ETAG,
                    "X-Request-Id": "req_redirect",
                },
            )
            return

        self._not_found()

    def do_POST(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        self.state.record_api(self)
        path, _query = self._route()
        if not self._authenticated():
            return

        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)

        if path == "/v0/drives":
            key = self.headers.get("Idempotency-Key")
            if not key:
                self._json(
                    400,
                    {
                        "error": {
                            "code": "IDEMPOTENCY_REQUIRED",
                            "message": "key required",
                        }
                    },
                    {"X-Request-Id": "req_idem_missing"},
                )
                return
            decoded = json.loads(body)
            signature = json.dumps(decoded, sort_keys=True, separators=(",", ":"))
            with self.state.lock:
                previous = self.state.idempotent_drives.get(key)
                if previous is None:
                    response = _drive()
                    self.state.idempotent_drives[key] = (signature, response)
                elif previous[0] == signature:
                    response = previous[1]
                else:
                    response = None
            if response is None:
                self._json(
                    409,
                    {
                        "error": {
                            "code": "IDEMPOTENCY_KEY_REUSE",
                            "message": "body changed",
                        }
                    },
                    {"X-Request-Id": "req_idem_reuse"},
                )
                return
            self._json(
                201,
                response,
                {
                    "ETag": ETAG,
                    "Location": f"/v0/drives/{DRIVE_ID}",
                    "X-Request-Id": "req_create",
                },
            )
            return

        if path == f"/v0/drives/{DRIVE_ID}/artifacts":
            with self.state.lock:
                self.state.multipart_content_type = self.headers.get("Content-Type")
                self.state.multipart_body = body
            self._json(
                201,
                _artifact(),
                {
                    "ETag": ETAG,
                    "Location": f"/v0/drives/{DRIVE_ID}/artifacts/{ARTIFACT_ID}",
                    "X-Request-Id": "req_upload",
                },
            )
            return

        self._not_found()


def _start_server(
    handler: type[BaseHTTPRequestHandler],
) -> tuple[ThreadingHTTPServer, threading.Thread]:
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


@pytest.fixture
def wire_server() -> tuple[str, _WireState]:
    state = _WireState()

    sink_handler = type("SinkHandler", (_SinkHandler,), {"state": state})
    sink, sink_thread = _start_server(sink_handler)
    sink_url = f"http://127.0.0.1:{sink.server_port}/signed-content"

    api_handler = type(
        "AgentDriveHandler",
        (_AgentDriveHandler,),
        {"state": state, "redirect_url": sink_url},
    )
    api, api_thread = _start_server(api_handler)
    try:
        yield f"http://127.0.0.1:{api.server_port}/drive", state
    finally:
        api.shutdown()
        sink.shutdown()
        api.server_close()
        sink.server_close()
        api_thread.join(timeout=2)
        sink_thread.join(timeout=2)


def _assert_multipart(state: _WireState) -> None:
    assert state.multipart_content_type is not None
    assert state.multipart_content_type.startswith("multipart/form-data; boundary=")
    assert b'name="content"' in state.multipart_body
    assert b"hello generated core" in state.multipart_body
    assert b'name="name"' in state.multipart_body
    assert b"conformance.txt" in state.multipart_body
    assert b'name="parent_id"' in state.multipart_body
    assert ROOT_FOLDER_ID.encode() in state.multipart_body


def _header(headers: Any, name: str) -> str | None:
    """Read headers without assuming a generated transport's casing policy."""
    wanted = name.casefold()
    return next(
        (str(value) for key, value in headers.items() if str(key).casefold() == wanted),
        None,
    )


def _assert_redirect_not_followed(state: _WireState) -> None:
    # Phase 1 deliberately exposes 307 to callers. Phase 2 may follow the
    # signed URL, but must build a new unauthenticated request to do so.
    assert state.sink_requests == []
    content_requests = [r for r in state.api_requests if r["path"].endswith("/content")]
    assert content_requests[-1]["authorization"] == f"Bearer {TOKEN}"


def test_sync_generated_client_live_wire_conformance(
    wire_server: tuple[str, _WireState],
) -> None:
    base_url, state = wire_server

    with SyncApiClient(SyncConfiguration(host=base_url)) as unauthenticated:
        with pytest.raises(SyncApiException) as exc_info:
            SyncDrivesApi(unauthenticated).drives_list()
    assert exc_info.value.status == 401
    assert exc_info.value.headers.get("WWW-Authenticate", "").startswith("Bearer")

    configuration = SyncConfiguration(host=base_url, access_token=TOKEN)
    with SyncApiClient(configuration) as api_client:
        drives = SyncDrivesApi(api_client)
        artifacts = SyncArtifactsApi(api_client)

        first = drives.drives_list_with_http_info(limit=1)
        assert first.status_code == 200
        assert _header(first.headers, "X-Request-Id") == "req_list"
        assert [item.id for item in first.data.items] == [DRIVE_ID]
        assert first.data.next_cursor == "page-2"
        second = drives.drives_list(limit=1, cursor=first.data.next_cursor)
        assert second.items == []
        assert second.next_cursor is None

        request = SyncDriveCreateIn(name="generated-core")
        created = drives.drives_create_with_http_info("idem-sync", request)
        replay = drives.drives_create("idem-sync", request)
        assert created.status_code == 201
        assert _header(created.headers, "ETag") == ETAG
        assert created.data.id == replay.id == DRIVE_ID

        uploaded = artifacts.artifacts_create(
            DRIVE_ID,
            "idem-sync-upload",
            ("conformance.txt", b"hello generated core"),
            "conformance.txt",
            ROOT_FOLDER_ID,
            content_type="text/plain",
            metadata={"source": "wire-test"},
        )
        assert uploaded.id == ARTIFACT_ID
        assert uploaded.effective_visibility == "private"
        _assert_multipart(state)

        conditional = artifacts.artifacts_read_without_preload_content(
            DRIVE_ID,
            ARTIFACT_ID,
            if_none_match=ETAG,
        )
        assert conditional.status == 304
        assert _header(conditional.headers, "ETag") == ETAG
        conditional.release_conn()

        with pytest.raises(SyncApiException) as missing:
            drives.drives_read(MISSING_DRIVE_ID)
        assert missing.value.status == 404
        assert "NOT_FOUND" in (missing.value.body or "")

        redirect = artifacts.artifacts_content_without_preload_content(
            DRIVE_ID, ARTIFACT_ID
        )
        assert redirect.status == 307
        assert (_header(redirect.headers, "Location") or "").endswith("/signed-content")
        redirect.release_conn()

    assert len(state.idempotent_drives) == 1
    _assert_redirect_not_followed(state)


async def _run_async_conformance(base_url: str, state: _WireState) -> None:
    async with AsyncApiClient(AsyncConfiguration(host=base_url)) as unauthenticated:
        with pytest.raises(AsyncApiException) as exc_info:
            await AsyncDrivesApi(unauthenticated).drives_list()
    assert exc_info.value.status == 401
    assert exc_info.value.headers.get("WWW-Authenticate", "").startswith("Bearer")

    configuration = AsyncConfiguration(host=base_url, access_token=TOKEN)
    async with AsyncApiClient(configuration) as api_client:
        drives = AsyncDrivesApi(api_client)
        artifacts = AsyncArtifactsApi(api_client)

        first = await drives.drives_list_with_http_info(limit=1)
        assert first.status_code == 200
        assert _header(first.headers, "X-Request-Id") == "req_list"
        assert [item.id for item in first.data.items] == [DRIVE_ID]
        assert first.data.next_cursor == "page-2"
        second = await drives.drives_list(limit=1, cursor=first.data.next_cursor)
        assert second.items == []
        assert second.next_cursor is None

        request = AsyncDriveCreateIn(name="generated-core")
        created = await drives.drives_create_with_http_info("idem-async", request)
        replay = await drives.drives_create("idem-async", request)
        assert created.status_code == 201
        assert _header(created.headers, "ETag") == ETAG
        assert created.data.id == replay.id == DRIVE_ID

        uploaded = await artifacts.artifacts_create(
            DRIVE_ID,
            "idem-async-upload",
            ("conformance.txt", b"hello generated core"),
            "conformance.txt",
            ROOT_FOLDER_ID,
            content_type="text/plain",
            metadata={"source": "wire-test"},
        )
        assert uploaded.id == ARTIFACT_ID
        assert uploaded.effective_visibility == "private"
        _assert_multipart(state)

        conditional = await artifacts.artifacts_read_without_preload_content(
            DRIVE_ID,
            ARTIFACT_ID,
            if_none_match=ETAG,
        )
        assert conditional.status_code == 304
        assert _header(conditional.headers, "ETag") == ETAG
        await conditional.aclose()

        with pytest.raises(AsyncApiException) as missing:
            await drives.drives_read(MISSING_DRIVE_ID)
        assert missing.value.status == 404
        assert "NOT_FOUND" in (missing.value.body or "")

        redirect = await artifacts.artifacts_content_without_preload_content(
            DRIVE_ID,
            ARTIFACT_ID,
        )
        assert redirect.status_code == 307
        assert (_header(redirect.headers, "Location") or "").endswith("/signed-content")
        await redirect.aclose()

    assert len(state.idempotent_drives) == 1
    _assert_redirect_not_followed(state)


def test_async_generated_client_live_wire_conformance(
    wire_server: tuple[str, _WireState],
) -> None:
    base_url, state = wire_server
    asyncio.run(_run_async_conformance(base_url, state))
