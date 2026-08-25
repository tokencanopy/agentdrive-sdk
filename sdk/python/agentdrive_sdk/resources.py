"""Handwritten resource helpers mapped one-to-one to generated operations."""

from __future__ import annotations

import hashlib
import os
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

import urllib3

from .client import AgentDriveClient, strong_if_match
from .generated.models.artifact_copy_in import ArtifactCopyIn
from .generated.models.artifact_update_in import ArtifactUpdateIn
from .generated.models.download_capabilities_create_request import (
    DownloadCapabilitiesCreateRequest,
)
from .generated.models.download_capabilities_create_request_target import (
    DownloadCapabilitiesCreateRequestTarget,
)
from .generated.models.download_capabilities_create_request_target_one_of import (
    DownloadCapabilitiesCreateRequestTargetOneOf,
)
from .generated.models.download_capabilities_create_request_target_one_of1 import (
    DownloadCapabilitiesCreateRequestTargetOneOf1,
)
from .generated.models.drive_create_in import DriveCreateIn
from .generated.models.drive_update_in import DriveUpdateIn
from .generated.models.folder_copy_in import FolderCopyIn
from .generated.models.folder_create_in import FolderCreateIn
from .generated.models.folder_update_in import FolderUpdateIn
from .generated.models.grant_create_in import GrantCreateIn
from .generated.models.grant_update_in import GrantUpdateIn
from .generated.models.share_create_in import ShareCreateIn
from .generated.models.uploads_create_request import UploadsCreateRequest
from .generated.models.uploads_create_request_content import UploadsCreateRequestContent
from .generated.models.uploads_create_request_content_checksum import (
    UploadsCreateRequestContentChecksum,
)
from .generated.models.uploads_create_request_target import UploadsCreateRequestTarget
from .generated.models.uploads_create_request_target_one_of import (
    UploadsCreateRequestTargetOneOf,
)
from .generated.models.uploads_create_request_target_one_of1 import (
    UploadsCreateRequestTargetOneOf1,
)
from .iteration import CursorItems, CursorPages, Page
from .paths import (
    InvalidPathError,
    ensure_safe_destination,
    iter_safe_files,
    normalize_relative_path,
    split_parent_path,
)


class _Resource:
    def __init__(self, client: AgentDriveClient) -> None:
        self.client = client

    def _revision(self, revision: str | None) -> str:
        if revision is None:
            raise ValueError("revision is required for an existing-state mutation")
        return strong_if_match(revision)

    def _parent_id(
        self,
        drive_id: str,
        *,
        parent_id: str | None,
        parent_path: str | None,
    ) -> str:
        if parent_id is not None and parent_path is not None:
            raise ValueError("provide parent_id or parent_path, not both")
        if parent_id is not None:
            return parent_id
        if parent_path is not None:
            resolved = self.client.entries.lookup(drive_id, parent_path, type="folder")
            if resolved.type != "folder":
                raise ValueError("parent_path did not resolve to a folder")
            return resolved.id
        return self.client.drives.get(drive_id).root_folder_id


class DriveResource(_Resource):
    def list(
        self,
        *,
        lifecycle: str = "active",
        limit: int | None = None,
        cursor: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "drives_list",
            {"lifecycle": lifecycle, "limit": limit, "cursor": cursor},
        ).data

    def iter_pages(
        self,
        *,
        lifecycle: str = "active",
        limit: int | None = None,
        cursor: str | None = None,
        max_pages: int | None = None,
    ) -> CursorPages[Any]:
        return self.client._pages(
            lambda next_cursor: _page_from(
                self.list(lifecycle=lifecycle, limit=limit, cursor=next_cursor), "items"
            ),
            cursor=cursor,
            max_pages=max_pages,
        )

    def iter_items(self, **kwargs: Any) -> CursorItems[Any]:
        return self.client._items(self.iter_pages(**kwargs))

    def get(self, drive_id: str, *, if_none_match: str | None = None) -> Any:
        return self.client._invoke(
            "drives_read",
            {"drive_id": drive_id, "if_none_match": if_none_match},
            retry=True,
        ).data

    def create(
        self,
        name: str,
        *,
        metadata: dict[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "drives_create",
            {"drive_create_in": DriveCreateIn(name=name, metadata=metadata or {})},
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def update(
        self,
        drive_id: str,
        *,
        revision: str,
        name: str | None = None,
        metadata: dict[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        if name is None and metadata is None:
            raise ValueError("provide name or metadata")
        return self.client._invoke(
            "drives_update",
            {
                "drive_id": drive_id,
                "if_match": self._revision(revision),
                "drive_update_in": DriveUpdateIn(name=name, metadata=metadata),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def delete(
        self,
        drive_id: str,
        *,
        revision: str,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "drives_delete",
            {"drive_id": drive_id, "if_match": self._revision(revision)},
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def restore(
        self,
        drive_id: str,
        *,
        revision: str,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "drives_restore",
            {"drive_id": drive_id, "if_match": self._revision(revision)},
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def usage(self, drive_id: str) -> Any:
        return self.client._invoke("drives_usage", {"drive_id": drive_id}).data


class EntryResource(_Resource):
    def list(
        self,
        drive_id: str,
        *,
        parent_id: str | None = None,
        type: str | None = None,
        name: str | None = None,
        label: str | None = None,
        content_type: str | None = None,
        updated_after: datetime | None = None,
        updated_before: datetime | None = None,
        state: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
    ) -> Any:
        parent = parent_id or self.client.drives.get(drive_id).root_folder_id
        return self.client._invoke(
            "entries_list",
            {
                "drive_id": drive_id,
                "parent_id": parent,
                "type": type,
                "name": name,
                "label": label,
                "content_type": content_type,
                "updated_after": updated_after,
                "updated_before": updated_before,
                "state": state,
                "limit": limit,
                "cursor": cursor,
            },
        ).data

    def iter_pages(self, drive_id: str, **kwargs: Any) -> CursorPages[Any]:
        cursor = kwargs.pop("cursor", None)
        max_pages = kwargs.pop("max_pages", None)

        def load(next_cursor: str | None) -> Page[Any]:
            response = self.list(drive_id, cursor=next_cursor, **kwargs)
            items = tuple(
                getattr(entry, "actual_instance", None) or entry
                for entry in response.entries
            )
            return Page(
                items=items,
                next_cursor=response.next_cursor,
                raw=response,
            )

        return self.client._pages(load, cursor=cursor, max_pages=max_pages)

    def iter_items(self, drive_id: str, **kwargs: Any) -> CursorItems[Any]:
        return self.client._items(self.iter_pages(drive_id, **kwargs))

    def lookup(self, drive_id: str, path: str, *, type: str | None = None) -> Any:
        return self.client._invoke(
            "lookup",
            {"drive_id": drive_id, "path": normalize_relative_path(path), "type": type},
        ).data


class FolderResource(_Resource):
    def list(
        self,
        drive_id: str,
        *,
        lifecycle: str = "active",
        limit: int | None = None,
        cursor: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "folders_list",
            {
                "drive_id": drive_id,
                "lifecycle": lifecycle,
                "limit": limit,
                "cursor": cursor,
                "parent_id": parent_id,
                "name": name,
            },
        ).data

    def iter_pages(self, drive_id: str, **kwargs: Any) -> CursorPages[Any]:
        cursor = kwargs.pop("cursor", None)
        max_pages = kwargs.pop("max_pages", None)
        return self.client._pages(
            lambda next_cursor: _page_from(
                self.list(drive_id, cursor=next_cursor, **kwargs), "items"
            ),
            cursor=cursor,
            max_pages=max_pages,
        )

    def iter_items(self, drive_id: str, **kwargs: Any) -> CursorItems[Any]:
        return self.client._items(self.iter_pages(drive_id, **kwargs))

    def get(self, drive_id: str, folder_id: str, *, if_none_match: str | None = None) -> Any:
        return self.client._invoke(
            "folders_read",
            {"drive_id": drive_id, "folder_id": folder_id, "if_none_match": if_none_match},
        ).data

    def create(
        self,
        drive_id: str,
        name: str,
        *,
        parent_id: str | None = None,
        parent_path: str | None = None,
        metadata: dict[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        parent = self._parent_id(drive_id, parent_id=parent_id, parent_path=parent_path)
        return self.client._invoke(
            "folders_create",
            {
                "drive_id": drive_id,
                "folder_create_in": FolderCreateIn(
                    parent_id=parent, name=name, metadata=metadata or {}
                ),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def create_path(
        self,
        drive_id: str,
        path: str,
        *,
        metadata: dict[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        parent_path, name = split_parent_path(path)
        return self.create(
            drive_id,
            name,
            parent_path=parent_path or None,
            metadata=metadata,
            idempotency_key=idempotency_key,
        )

    def update(
        self,
        drive_id: str,
        folder_id: str,
        *,
        revision: str,
        name: str | None = None,
        parent_id: str | None = None,
        parent_path: str | None = None,
        metadata: dict[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        parent = parent_id
        if parent_path is not None:
            parent = self._parent_id(drive_id, parent_id=None, parent_path=parent_path)
        if name is None and parent is None and metadata is None:
            raise ValueError("provide name, parent_id/parent_path, or metadata")
        return self.client._invoke(
            "folders_update",
            {
                "drive_id": drive_id,
                "folder_id": folder_id,
                "if_match": self._revision(revision),
                "folder_update_in": FolderUpdateIn(
                    name=name, parent_id=parent, metadata=metadata
                ),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def move(
        self,
        drive_id: str,
        folder_id: str,
        *,
        revision: str,
        parent_id: str | None = None,
        parent_path: str | None = None,
        name: str | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.update(
            drive_id,
            folder_id,
            revision=revision,
            parent_id=parent_id,
            parent_path=parent_path,
            name=name,
            idempotency_key=idempotency_key,
        )

    def delete(
        self,
        drive_id: str,
        folder_id: str,
        *,
        revision: str,
        recursive: bool = False,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "folders_delete",
            {
                "drive_id": drive_id,
                "folder_id": folder_id,
                "if_match": self._revision(revision),
                "recursive": recursive,
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def restore(
        self,
        drive_id: str,
        folder_id: str,
        *,
        revision: str,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "folders_restore",
            {
                "drive_id": drive_id,
                "folder_id": folder_id,
                "if_match": self._revision(revision),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def copy(
        self,
        drive_id: str,
        folder_id: str,
        *,
        destination_parent_id: str,
        destination_name: str,
        revision: str | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "folders_copy",
            {
                "drive_id": drive_id,
                "folder_id": folder_id,
                "if_match": strong_if_match(revision) if revision else None,
                "folder_copy_in": FolderCopyIn(
                    destination_parent_id=destination_parent_id,
                    destination_name=destination_name,
                ),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data


class ArtifactResource(_Resource):
    def list(
        self,
        drive_id: str,
        *,
        lifecycle: str = "active",
        limit: int | None = None,
        cursor: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
        content_type: str | None = None,
        label: str | None = None,
        updated_after: datetime | None = None,
        updated_before: datetime | None = None,
    ) -> Any:
        return self.client._invoke(
            "artifacts_list",
            {
                "drive_id": drive_id,
                "lifecycle": lifecycle,
                "limit": limit,
                "cursor": cursor,
                "parent_id": parent_id,
                "name": name,
                "content_type": content_type,
                "label": label,
                "updated_after": updated_after,
                "updated_before": updated_before,
            },
        ).data

    def iter_pages(self, drive_id: str, **kwargs: Any) -> CursorPages[Any]:
        cursor = kwargs.pop("cursor", None)
        max_pages = kwargs.pop("max_pages", None)
        return self.client._pages(
            lambda next_cursor: _page_from(
                self.list(drive_id, cursor=next_cursor, **kwargs), "items"
            ),
            cursor=cursor,
            max_pages=max_pages,
        )

    def iter_items(self, drive_id: str, **kwargs: Any) -> CursorItems[Any]:
        return self.client._items(self.iter_pages(drive_id, **kwargs))

    def get(self, drive_id: str, artifact_id: str, *, if_none_match: str | None = None) -> Any:
        return self.client._invoke(
            "artifacts_read",
            {"drive_id": drive_id, "artifact_id": artifact_id, "if_none_match": if_none_match},
        ).data

    def create(
        self,
        drive_id: str,
        name: str,
        *,
        parent_id: str | None = None,
        parent_path: str | None = None,
        content: bytes | str = b"",
        content_type: str | None = None,
        metadata: dict[str, Any] | None = None,
        sha256: str | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        parent = self._parent_id(drive_id, parent_id=parent_id, parent_path=parent_path)
        if isinstance(content, str):
            content = content.encode("utf-8")
        if sha256 is None:
            sha256 = hashlib.sha256(content).hexdigest()
        return self.client._invoke(
            "artifacts_create",
            {
                "drive_id": drive_id,
                "content": content,
                "name": name,
                "parent_id": parent,
                "content_type": content_type,
                "metadata": metadata,
                "sha256": sha256,
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def create_path(
        self,
        drive_id: str,
        path: str,
        *,
        content: bytes | str = b"",
        content_type: str | None = None,
        metadata: dict[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        parent_path, name = split_parent_path(path)
        return self.create(
            drive_id,
            name,
            parent_path=parent_path or None,
            content=content,
            content_type=content_type,
            metadata=metadata,
            idempotency_key=idempotency_key,
        )

    def update(
        self,
        drive_id: str,
        artifact_id: str,
        *,
        revision: str,
        name: str | None = None,
        parent_id: str | None = None,
        parent_path: str | None = None,
        metadata: dict[str, Any] | None = None,
        labels: list[str] | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        parent = parent_id
        if parent_path is not None:
            parent = self._parent_id(drive_id, parent_id=None, parent_path=parent_path)
        if name is None and parent is None and metadata is None and labels is None:
            raise ValueError("provide at least one artifact field")
        return self.client._invoke(
            "artifacts_update",
            {
                "drive_id": drive_id,
                "artifact_id": artifact_id,
                "if_match": self._revision(revision),
                "artifact_update_in": ArtifactUpdateIn(
                    name=name, parent_id=parent, metadata=metadata, labels=labels
                ),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def move(
        self,
        drive_id: str,
        artifact_id: str,
        *,
        revision: str,
        parent_id: str | None = None,
        parent_path: str | None = None,
        name: str | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.update(
            drive_id,
            artifact_id,
            revision=revision,
            parent_id=parent_id,
            parent_path=parent_path,
            name=name,
            idempotency_key=idempotency_key,
        )

    def delete(
        self,
        drive_id: str,
        artifact_id: str,
        *,
        revision: str,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "artifacts_delete",
            {
                "drive_id": drive_id,
                "artifact_id": artifact_id,
                "if_match": self._revision(revision),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def restore(
        self,
        drive_id: str,
        artifact_id: str,
        *,
        revision: str,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "artifacts_restore",
            {
                "drive_id": drive_id,
                "artifact_id": artifact_id,
                "if_match": self._revision(revision),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def copy(
        self,
        drive_id: str,
        artifact_id: str,
        *,
        destination_parent_id: str,
        destination_name: str,
        version_id: str | None = None,
        revision: str | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "artifacts_copy",
            {
                "drive_id": drive_id,
                "artifact_id": artifact_id,
                "if_match": strong_if_match(revision) if revision else None,
                "artifact_copy_in": ArtifactCopyIn(
                    destination_parent_id=destination_parent_id,
                    destination_name=destination_name,
                    version_id=version_id,
                ),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def content(self, drive_id: str, artifact_id: str) -> bytes:
        try:
            result = self.client._invoke(
                "artifacts_content", {"drive_id": drive_id, "artifact_id": artifact_id}
            )
            return bytes(result.data)
        except Exception as exc:
            location = getattr(exc, "headers", {}).get("location") if hasattr(exc, "headers") else None
            status = getattr(exc, "status_code", None)
            if status not in {301, 302, 303, 307, 308} or not location:
                raise
            return _fetch_redirect(location)

    def download_to(
        self,
        drive_id: str,
        artifact_id: str,
        destination: str | os.PathLike[str],
        *,
        overwrite: bool = False,
    ) -> Path:
        target = ensure_safe_destination(destination)
        if target.exists() and not overwrite:
            raise FileExistsError(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        payload = self.content(drive_id, artifact_id)
        fd, temporary = tempfile.mkstemp(prefix=f".{target.name}.", dir=target.parent)
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, target)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
        return target

    def upload_file(
        self,
        drive_id: str,
        source: str | os.PathLike[str],
        *,
        destination_path: str | None = None,
        parent_id: str | None = None,
        parent_path: str | None = None,
        content_type: str | None = None,
        metadata: dict[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        path = Path(source)
        if path.is_symlink():
            raise InvalidPathError("upload source must not be a symlink")
        if not path.is_file():
            raise FileNotFoundError(path)
        size = path.stat().st_size
        if size > self.client.inline_upload_limit:
            raise ValueError(
                f"file is {size} bytes, above the inline upload limit "
                f"of {self.client.inline_upload_limit} bytes"
            )
        content = path.read_bytes()
        if destination_path is not None:
            parent_path, name = split_parent_path(destination_path)
            parent_id = None
        else:
            name = path.name
        if content_type is None:
            import mimetypes

            content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        return self.create(
            drive_id,
            name,
            parent_id=parent_id,
            parent_path=parent_path,
            content=content,
            content_type=content_type,
            metadata=metadata,
            idempotency_key=idempotency_key,
        )

    def upload_directory(
        self,
        drive_id: str,
        source: str | os.PathLike[str],
        *,
        destination_path: str = "uploads",
        dry_run: bool = False,
        include_credentials: bool = False,
        follow_symlinks: bool = False,
    ) -> list[Any]:
        files = list(
            iter_safe_files(
                source,
                include_credentials=include_credentials,
                follow_symlinks=follow_symlinks,
            )
        )
        if dry_run:
            return [normalize_relative_path(f"{destination_path}/{relative}") for relative, _ in files]
        results: list[Any] = []
        for relative, path in files:
            results.append(
                self.upload_file(
                    drive_id,
                    path,
                    destination_path=f"{destination_path}/{relative}",
                )
            )
        return results


class VersionResource(_Resource):
    def list(self, drive_id: str, artifact_id: str, *, limit: int | None = None, cursor: str | None = None) -> Any:
        return self.client._invoke(
            "versions_list",
            {"drive_id": drive_id, "artifact_id": artifact_id, "limit": limit, "cursor": cursor},
        ).data

    def iter_pages(self, drive_id: str, artifact_id: str, **kwargs: Any) -> CursorPages[Any]:
        cursor = kwargs.pop("cursor", None)
        max_pages = kwargs.pop("max_pages", None)
        return self.client._pages(
            lambda next_cursor: _page_from(
                self.list(drive_id, artifact_id, cursor=next_cursor, **kwargs), "items"
            ),
            cursor=cursor,
            max_pages=max_pages,
        )

    def iter_items(self, drive_id: str, artifact_id: str, **kwargs: Any) -> CursorItems[Any]:
        return self.client._items(self.iter_pages(drive_id, artifact_id, **kwargs))

    def get(self, drive_id: str, artifact_id: str, version_id: str) -> Any:
        return self.client._invoke(
            "versions_read",
            {"drive_id": drive_id, "artifact_id": artifact_id, "version_id": version_id},
        ).data

    def append(
        self,
        drive_id: str,
        artifact_id: str,
        content: bytes | str,
        *,
        revision: str,
        content_type: str | None = None,
        sha256: str | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        if isinstance(content, str):
            content = content.encode("utf-8")
        return self.client._invoke(
            "versions_append",
            {
                "drive_id": drive_id,
                "artifact_id": artifact_id,
                "if_match": self._revision(revision),
                "content": content,
                "content_type": content_type,
                "sha256": sha256 or hashlib.sha256(content).hexdigest(),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def restore(
        self,
        drive_id: str,
        artifact_id: str,
        version_id: str,
        *,
        revision: str,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "versions_restore",
            {
                "drive_id": drive_id,
                "artifact_id": artifact_id,
                "version_id": version_id,
                "if_match": self._revision(revision),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def content(self, drive_id: str, artifact_id: str, version_id: str) -> bytes:
        try:
            result = self.client._invoke(
                "versions_content",
                {
                    "drive_id": drive_id,
                    "artifact_id": artifact_id,
                    "version_id": version_id,
                },
            )
            return bytes(result.data)
        except Exception as exc:
            location = getattr(exc, "headers", {}).get("location") if hasattr(exc, "headers") else None
            if getattr(exc, "status_code", None) in {301, 302, 303, 307, 308} and location:
                return _fetch_redirect(location)
            raise


class SearchResource(_Resource):
    def find(self, drive_id: str, query: str, **kwargs: Any) -> Any:
        return self.client._invoke(
            "drive_search", {"drive_id": drive_id, "q": query, **kwargs}
        ).data

    def iter_pages(self, drive_id: str, query: str, **kwargs: Any) -> CursorPages[Any]:
        cursor = kwargs.pop("cursor", None)
        max_pages = kwargs.pop("max_pages", None)
        return self.client._pages(
            lambda next_cursor: _page_from(
                self.find(drive_id, query, cursor=next_cursor, **kwargs), "items"
            ),
            cursor=cursor,
            max_pages=max_pages,
        )

    def iter_items(self, drive_id: str, query: str, **kwargs: Any) -> CursorItems[Any]:
        return self.client._items(self.iter_pages(drive_id, query, **kwargs))


class ChangeResource(_Resource):
    def list(
        self,
        drive_id: str,
        *,
        limit: int | None = None,
        start: str | None = None,
        cursor: str | None = None,
        type: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "changes_list",
            {"drive_id": drive_id, "limit": limit, "start": start, "cursor": cursor, "type": type},
        ).data

    def iter_pages(self, drive_id: str, **kwargs: Any) -> CursorPages[Any]:
        initial_cursor = kwargs.pop("cursor", None)
        max_pages = kwargs.pop("max_pages", None)
        start = kwargs.pop("start", None)
        first = True

        def load(cursor: str | None) -> Page[Any]:
            nonlocal first
            page = self.list(
                drive_id,
                cursor=cursor,
                start=start if first and cursor is None else None,
                **kwargs,
            )
            first = False
            return _page_from(page, "items", has_more=getattr(page, "has_more", None))

        return self.client._pages(load, cursor=initial_cursor, max_pages=max_pages)

    def iter_items(self, drive_id: str, **kwargs: Any) -> CursorItems[Any]:
        return self.client._items(self.iter_pages(drive_id, **kwargs))


class GrantResource(_Resource):
    def list(self, drive_id: str, **kwargs: Any) -> Any:
        return self.client._invoke("grants_list", {"drive_id": drive_id, **kwargs}).data

    def create(
        self,
        drive_id: str,
        *,
        resource_type: str,
        resource_id: str,
        principal_type: str,
        principal_id: str | None = None,
        role: str = "viewer",
        expires_at: datetime | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "grants_create",
            {
                "drive_id": drive_id,
                "grant_create_in": GrantCreateIn(
                    resource_type=resource_type,
                    resource_id=resource_id,
                    principal_type=principal_type,
                    principal_id=principal_id,
                    role=role,
                    expires_at=expires_at,
                ),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def get(self, drive_id: str, grant_id: str) -> Any:
        return self.client._invoke(
            "grants_read", {"drive_id": drive_id, "grant_id": grant_id}
        ).data

    def update(
        self,
        drive_id: str,
        grant_id: str,
        *,
        revision: str,
        role: str | None = None,
        expires_at: datetime | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        if role is None and expires_at is None:
            raise ValueError("provide role or expires_at")
        return self.client._invoke(
            "grants_update",
            {
                "drive_id": drive_id,
                "grant_id": grant_id,
                "if_match": self._revision(revision),
                "grant_update_in": GrantUpdateIn(role=role, expires_at=expires_at),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def revoke(
        self,
        drive_id: str,
        grant_id: str,
        *,
        revision: str,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "grants_revoke",
            {"drive_id": drive_id, "grant_id": grant_id, "if_match": self._revision(revision)},
            mutation=True,
            idempotency_key=idempotency_key,
        ).data


class ShareResource(_Resource):
    def list(self, drive_id: str, **kwargs: Any) -> Any:
        return self.client._invoke("shares_list", {"drive_id": drive_id, **kwargs}).data

    def create(
        self,
        drive_id: str,
        *,
        resource_type: str,
        resource_id: str,
        expires_at: datetime | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "shares_create",
            {
                "drive_id": drive_id,
                "share_create_in": ShareCreateIn(
                    resource_type=resource_type,
                    resource_id=resource_id,
                    expires_at=expires_at,
                ),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def get(self, drive_id: str, share_id: str) -> Any:
        return self.client._invoke(
            "shares_read", {"drive_id": drive_id, "share_id": share_id}
        ).data

    def revoke(
        self,
        drive_id: str,
        share_id: str,
        *,
        revision: str,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "shares_revoke",
            {"drive_id": drive_id, "share_id": share_id, "if_match": self._revision(revision)},
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def rotate(
        self,
        drive_id: str,
        share_id: str,
        *,
        revision: str,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "shares_rotate",
            {"drive_id": drive_id, "share_id": share_id, "if_match": self._revision(revision)},
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def url(self, share: Any) -> str:
        secret = getattr(share, "secret", None)
        if not secret:
            raise ValueError("share secret is only available from create or rotate")
        return f"{self.client.share_base_url}/s/{secret}/"


class UploadResource(_Resource):
    """Low-level direct-transfer session controls.

    The byte transfer itself is intentionally not hidden here: the server
    discloses an exact signed initiation target and its required headers.
    ``ArtifactResource.upload_file`` remains the safe inline helper for v0's
    bounded path.
    """

    def begin(
        self,
        drive_id: str,
        *,
        target: dict[str, Any],
        size_bytes: int,
        media_type: str,
        checksum_algorithm: str,
        checksum_value: str,
        revision: str | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        kind = target.get("kind")
        if kind == "artifact":
            target_model = UploadsCreateRequestTargetOneOf(
                kind="artifact",
                parent_folder_id=target["parent_folder_id"],
                name=target["name"],
            )
        elif kind == "version":
            target_model = UploadsCreateRequestTargetOneOf1(
                kind="version", artifact_id=target["artifact_id"]
            )
        else:
            raise ValueError("target.kind must be artifact or version")
        return self.client._invoke(
            "uploads_create",
            {
                "drive_id": drive_id,
                "if_match": strong_if_match(revision) if revision else None,
                "uploads_create_request": UploadsCreateRequest(
                    target=UploadsCreateRequestTarget(target_model),
                    content=UploadsCreateRequestContent(
                        size_bytes=size_bytes,
                        media_type=media_type,
                        checksum=UploadsCreateRequestContentChecksum(
                            algorithm=checksum_algorithm, value=checksum_value
                        ),
                    ),
                ),
            },
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def get(self, drive_id: str, upload_id: str) -> Any:
        return self.client._invoke(
            "uploads_read", {"drive_id": drive_id, "upload_id": upload_id}
        ).data

    def cancel(
        self,
        drive_id: str,
        upload_id: str,
        *,
        revision: str,
        idempotency_key: str | None = None,
    ) -> Any:
        return self.client._invoke(
            "uploads_delete",
            {"drive_id": drive_id, "upload_id": upload_id, "if_match": self._revision(revision)},
            mutation=True,
            idempotency_key=idempotency_key,
        ).data

    def complete(self, drive_id: str, upload_id: str, *, idempotency_key: str | None = None) -> Any:
        return self.client._invoke(
            "uploads_complete",
            {"drive_id": drive_id, "upload_id": upload_id},
            mutation=True,
            idempotency_key=idempotency_key,
        ).data


def _page_from(
    response: Any,
    item_field: str,
    *,
    has_more: bool | None = None,
) -> Page[Any]:
    return Page(
        items=tuple(getattr(response, item_field)),
        next_cursor=getattr(response, "next_cursor", None),
        has_more=has_more,
        raw=response,
    )


def _fetch_redirect(location: str) -> bytes:
    """Fetch a signed target without carrying the AgentDrive bearer header."""

    http = urllib3.PoolManager()
    current = location
    for _ in range(3):
        response = http.request(
            "GET",
            current,
            headers={"Accept": "*/*"},
            preload_content=True,
            redirect=False,
        )
        if 200 <= response.status < 300:
            return bytes(response.data)
        if response.status not in {301, 302, 303, 307, 308}:
            raise RuntimeError(f"signed download failed with HTTP {response.status}")
        current = response.headers.get("Location")
        if not current:
            raise RuntimeError("signed download redirect omitted Location")
    raise RuntimeError("signed download followed too many redirects")
