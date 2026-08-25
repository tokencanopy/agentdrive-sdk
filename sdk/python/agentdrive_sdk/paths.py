"""Safe root-relative AgentDrive path helpers."""

from __future__ import annotations

import os
from collections.abc import Iterator
from pathlib import Path


class InvalidPathError(ValueError):
    """The supplied path is not a safe AgentDrive relative path."""


def normalize_relative_path(path: str) -> str:
    """Return a canonical slash-separated path or raise ``InvalidPathError``.

    AgentDrive paths are root-relative and use `/` regardless of the host
    operating system. Dot segments, empty segments, backslashes, NUL bytes,
    and absolute paths are rejected instead of normalized away.
    """

    if not isinstance(path, str) or not path:
        raise InvalidPathError("path must be a non-empty relative string")
    if "\x00" in path:
        raise InvalidPathError("path must not contain NUL bytes")
    if "\\" in path or path.startswith("/") or path.endswith("/"):
        raise InvalidPathError("path must use non-empty relative POSIX segments")
    segments = path.split("/")
    if any(segment in {"", ".", ".."} for segment in segments):
        raise InvalidPathError("path contains an empty or dot segment")
    return "/".join(segments)


def split_parent_path(path: str) -> tuple[str, str]:
    """Split a safe path into ``(parent_path, name)``.

    The parent path is the empty string for a root child. Callers must resolve
    that empty parent to the drive's ``root_folder_id`` before sending it to
    the API.
    """

    normalized = normalize_relative_path(path)
    parent, _, name = normalized.rpartition("/")
    return parent, name


def join_relative_path(*parts: str) -> str:
    """Join path fragments after validating their resulting path."""

    return normalize_relative_path("/".join(part.strip("/") for part in parts if part))


def iter_safe_files(
    root: str | os.PathLike[str],
    *,
    include_credentials: bool = False,
    follow_symlinks: bool = False,
) -> Iterator[tuple[str, Path]]:
    """Yield safe ``(relative_path, absolute_path)`` directory entries.

    The default is deliberately conservative: symlinks and credential-like
    files are skipped by raising ``InvalidPathError``. A caller must opt into
    both behaviors independently.
    """

    base = Path(root)
    if not base.exists():
        raise FileNotFoundError(base)
    if base.is_symlink() and not follow_symlinks:
        raise InvalidPathError("upload root must not be a symlink")
    if not base.is_dir():
        raise NotADirectoryError(base)
    base = base.resolve()
    for candidate in sorted(base.rglob("*")):
        if candidate.is_symlink() and not follow_symlinks:
            raise InvalidPathError(f"symlink is not allowed: {candidate}")
        if not candidate.is_file():
            continue
        relative = normalize_relative_path(candidate.relative_to(base).as_posix())
        if not include_credentials and looks_like_credential_file(relative):
            raise InvalidPathError(f"credential-like file is not allowed: {relative}")
        resolved = candidate.resolve()
        try:
            resolved.relative_to(base)
        except ValueError as exc:
            raise InvalidPathError(f"file escapes upload root: {relative}") from exc
        yield relative, resolved


def looks_like_credential_file(path: str) -> bool:
    """Conservative filename check for common secrets and private keys."""

    name = path.rsplit("/", 1)[-1].lower()
    return (
        name in {".env", ".npmrc", ".pypirc", "id_rsa", "id_ed25519", "credentials.json"}
        or name.endswith((".pem", ".key", ".p12", ".pfx"))
        or name.startswith("service-account") and name.endswith(".json")
    )


def ensure_safe_destination(path: str | os.PathLike[str]) -> Path:
    """Reject a symlink destination and return its absolute path."""

    destination = Path(path)
    if destination.exists() and destination.is_symlink():
        raise InvalidPathError("download destination must not be a symlink")
    return destination
