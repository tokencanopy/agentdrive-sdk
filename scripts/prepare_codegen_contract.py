"""Prepare the canonical OpenAPI 3.1 contract for deterministic generation."""

from __future__ import annotations

import argparse
import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict


class CodegenContractError(ValueError):
    pass


def normalize_for_codegen(
    document: Dict[str, Any], *, language: str = "common"
) -> Dict[str, Any]:
    normalized = deepcopy(document)
    invalid = sorted(
        path
        for path in normalized.get("paths", {})
        if path.startswith(("/internal/", "/web/", "/v1/agenttag"))
    )
    if invalid:
        raise CodegenContractError(f"non-SDK paths in committed contract: {invalid}")

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            if isinstance(value.get("default"), (dict, list)):
                value.pop("default")
            alternatives = value.get("anyOf")
            if language in {"go", "typescript"} and isinstance(alternatives, list):
                has_free_form_branch = any(
                    isinstance(alternative, dict) and not alternative
                    for alternative in alternatives
                )
                primitive_types = [
                    alternative.get("type")
                    for alternative in alternatives
                    if isinstance(alternative, dict)
                    and set(alternative) == {"type"}
                ]
                non_null = {item for item in primitive_types if item != "null"}
                if has_free_form_branch or (
                    language == "go"
                    and
                    len(primitive_types) == len(alternatives)
                    and len(non_null) > 1
                ):
                    # Generator 7.24 emits references to undefined AnyOf
                    # helpers for primitive unions. Go has no native union;
                    # interface{} faithfully accepts every declared branch.
                    value.pop("anyOf")
            for child in list(value.values()):
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(normalized)
    return normalized


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--language",
        choices=("common", "go", "typescript"),
        default="common",
    )
    args = parser.parse_args()
    document = json.loads(args.source.read_text(encoding="utf-8"))
    normalized = normalize_for_codegen(document, language=args.language)
    args.output.write_text(
        json.dumps(normalized, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
