"""Resolve a repository-owned input file without allowing path escape."""

from __future__ import annotations

import argparse
from pathlib import Path


class RepoPathError(ValueError):
    pass


def resolve_repo_file(repo_root: Path, requested: Path) -> str:
    root = repo_root.resolve(strict=True)
    candidate = requested if requested.is_absolute() else root / requested
    try:
        resolved = candidate.resolve(strict=True)
    except (FileNotFoundError, OSError) as exc:
        raise RepoPathError(f"file does not exist: {requested}") from exc
    if not resolved.is_file():
        raise RepoPathError(f"path is not a file: {requested}")
    try:
        relative = resolved.relative_to(root)
    except ValueError as exc:
        raise RepoPathError(
            f"file must be inside the repository: {requested}"
        ) from exc
    return relative.as_posix()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo_root", type=Path)
    parser.add_argument("requested", type=Path)
    args = parser.parse_args()
    try:
        print(resolve_repo_file(args.repo_root, args.requested))
    except RepoPathError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
