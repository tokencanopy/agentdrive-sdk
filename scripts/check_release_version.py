"""Validate a publish request against every SDK package version."""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
import tomllib
from pathlib import Path

SEMVER = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\Z")


def _python_assignment(path: Path, name: str) -> str:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    values: list[str] = []
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if isinstance(target, ast.Name) and target.id == name:
            value = ast.literal_eval(node.value)
            if isinstance(value, str):
                values.append(value)
    if len(values) != 1:
        raise ValueError(f"{path}: expected exactly one string assignment to {name}")
    return values[0]


def version_values(root: Path) -> dict[str, str]:
    python_project = tomllib.loads(
        (root / "sdk/python/pyproject.toml").read_text(encoding="utf-8")
    )
    typescript = json.loads(
        (root / "sdk/typescript/package.json").read_text(encoding="utf-8")
    )
    lock = json.loads(
        (root / "sdk/typescript/package-lock.json").read_text(encoding="utf-8")
    )
    return {
        "sdk/SDK_VERSION": (root / "sdk/SDK_VERSION").read_text(encoding="utf-8").strip(),
        "python project": str(python_project["project"]["version"]),
        "python package": _python_assignment(
            root / "sdk/python/src/agentdrive_sdk/__init__.py", "__version__"
        ),
        "python generated sync": _python_assignment(
            root / "sdk/python/src/agentdrive_sdk/generated/sync/__init__.py", "__version__"
        ),
        "python generated async": _python_assignment(
            root / "sdk/python/src/agentdrive_sdk/generated/async_client/__init__.py",
            "__version__",
        ),
        "typescript package": str(typescript["version"]),
        "typescript lock": str(lock["version"]),
        "typescript lock root": str(lock["packages"][""]["version"]),
    }


def check_release_version(root: Path, requested: str, *, event: str) -> str:
    canonical = requested[1:] if requested.startswith("v") else requested
    if event == "release" and requested != f"v{canonical}":
        raise ValueError("GitHub release tags must use the exact form vX.Y.Z")
    if not SEMVER.fullmatch(canonical):
        raise ValueError(f"publish version must be a stable X.Y.Z value, got {requested!r}")
    values = version_values(root)
    mismatches = {label: value for label, value in values.items() if value != canonical}
    if mismatches:
        detail = ", ".join(f"{label}={value!r}" for label, value in mismatches.items())
        raise ValueError(f"publish request {canonical!r} does not match metadata: {detail}")
    return canonical


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--requested", required=True, help="release tag or dispatch version")
    parser.add_argument(
        "--event", choices=("release", "workflow_dispatch"), required=True
    )
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    try:
        version = check_release_version(args.root, args.requested, event=args.event)
    except (KeyError, OSError, SyntaxError, ValueError, tomllib.TOMLDecodeError) as exc:
        print(f"Release version gate failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    print(version)


if __name__ == "__main__":
    main()
