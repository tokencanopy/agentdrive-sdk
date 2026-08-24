"""Verify every committed OpenAPI operation exists in every generated SDK."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, Iterable, Set

HTTP_METHODS = frozenset(
    {"get", "put", "post", "delete", "patch", "head", "options", "trace"}
)


class CoverageError(ValueError):
    pass


def generated_names(operation_id: str) -> Dict[str, str]:
    collapsed = re.sub(r"_+", "_", operation_id).strip("_").lower()
    words = collapsed.split("_")
    pascal = "".join(word[:1].upper() + word[1:] for word in words)
    camel = words[0] + "".join(word[:1].upper() + word[1:] for word in words[1:])
    return {"python": collapsed, "typescript": camel, "go": pascal}


def _operation_ids(spec_path: Path) -> Set[str]:
    document = json.loads(spec_path.read_text(encoding="utf-8"))
    operation_ids = []
    for path_item in document.get("paths", {}).values():
        for method, operation in path_item.items():
            if method in HTTP_METHODS:
                operation_id = operation.get("operationId")
                if not operation_id:
                    raise CoverageError("contract operation is missing operationId")
                operation_ids.append(operation_id)
    duplicates = sorted(
        operation_id
        for operation_id in set(operation_ids)
        if operation_ids.count(operation_id) > 1
    )
    if duplicates:
        raise CoverageError(f"duplicate contract operationIds: {duplicates}")
    return set(operation_ids)


def _contents(paths: Iterable[Path]) -> str:
    return "\n".join(path.read_text(encoding="utf-8") for path in paths)


def _python_operations(directory: Path) -> Set[str]:
    content = _contents(directory.glob("*_api.py"))
    names = set(re.findall(r"^    def ([A-Za-z0-9_]+)\(", content, re.MULTILINE))
    return {
        name
        for name in names
        if not name.startswith("_")
        and not name.endswith(
            ("_with_http_info", "_without_preload_content", "_serialize")
        )
    }


def _typescript_operations(directory: Path) -> Set[str]:
    content = _contents(directory.glob("*Api.ts"))
    names = set(re.findall(r"^\s+async ([A-Za-z0-9]+)\(", content, re.MULTILINE))
    return {
        name
        for name in names
        if not name.endswith(("Raw", "RequestOpts"))
    }


def _go_operations(directory: Path) -> Set[str]:
    content = _contents(directory.glob("api_*.go"))
    names = set(
        re.findall(
            r"^func \(a \*[^)]*APIService\) ([A-Za-z0-9]+)\(",
            content,
            re.MULTILINE,
        )
    )
    return {name for name in names if not name.endswith("Execute")}


def check_operation_coverage(
    spec_path: Path,
    *,
    python_dir: Path,
    typescript_dir: Path,
    go_dir: Path,
) -> None:
    operation_ids = _operation_ids(spec_path)
    expected = {}
    for language in ("python", "typescript", "go"):
        owners: Dict[str, list[str]] = {}
        for operation_id in operation_ids:
            generated = generated_names(operation_id)[language]
            owners.setdefault(generated, []).append(operation_id)
        collisions = {
            name: sorted(ids)
            for name, ids in owners.items()
            if len(ids) > 1
        }
        if collisions:
            raise CoverageError(
                f"{language} generated-name collision: {collisions}"
            )
        expected[language] = set(owners)
    actual = {
        "python": _python_operations(python_dir),
        "typescript": _typescript_operations(typescript_dir),
        "go": _go_operations(go_dir),
    }

    failures = []
    for language in ("python", "typescript", "go"):
        missing = sorted(expected[language] - actual[language])
        extra = sorted(actual[language] - expected[language])
        if missing:
            failures.append(f"{language} missing generated operations: {missing}")
        if extra:
            failures.append(f"{language} has operations absent from contract: {extra}")
    if failures:
        raise CoverageError("\n".join(failures))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path, nargs="?", default=Path("sdk/openapi.json"))
    args = parser.parse_args()
    check_operation_coverage(
        args.spec,
        python_dir=Path("sdk/python/agentdrive_sdk/generated/api"),
        typescript_dir=Path("sdk/typescript/src/generated/apis"),
        go_dir=Path("sdk/go"),
    )
    print("Generated SDK operation coverage matches the committed contract.")


if __name__ == "__main__":
    main()
