"""Prepare the canonical OpenAPI contract for deterministic SDK generation."""

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
    # The checked-in contract remains OpenAPI 3.1.  The pinned generator is
    # intentionally fed a deterministic 3.0.3 representation because it does
    # not support the 3.1 nullable/const forms used by the server contract.
    normalized["openapi"] = "3.0.3"
    invalid = sorted(
        path
        for path in normalized.get("paths", {})
        if path.startswith(("/internal/", "/web/", "/v1/agenttag"))
    )
    if invalid:
        raise CodegenContractError(f"non-SDK paths in committed contract: {invalid}")

    def normalize_nullable_anyof(value: Dict[str, Any]) -> None:
        alternatives = value.get("anyOf")
        if not isinstance(alternatives, list) or len(alternatives) != 2:
            return
        null_branches = [
            alternative
            for alternative in alternatives
            if isinstance(alternative, dict) and alternative == {"type": "null"}
        ]
        if len(null_branches) != 1:
            return
        non_null = next(
            alternative
            for alternative in alternatives
            if alternative is not null_branches[0]
        )
        if not isinstance(non_null, dict):
            return

        metadata = {key: child for key, child in value.items() if key != "anyOf"}
        value.clear()
        value.update(metadata)
        if set(non_null) == {"$ref"}:
            # A 3.0 Reference Object cannot carry nullable as a sibling.  An
            # allOf wrapper keeps the reference valid while preserving the
            # nullable meaning for the generator.
            value["allOf"] = [non_null]
        else:
            value.update(non_null)
        value["nullable"] = True

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            if isinstance(value.get("default"), (dict, list)):
                value.pop("default")

            schema_types = value.get("type")
            if isinstance(schema_types, list):
                non_null_types = [item for item in schema_types if item != "null"]
                if len(schema_types) == 2 and len(non_null_types) == 1:
                    value["type"] = non_null_types[0]
                    value["nullable"] = True
                else:
                    raise CodegenContractError(
                        "unsupported OpenAPI 3.1 type union: "
                        f"{schema_types!r}"
                    )

            if "const" in value:
                constant = value.pop("const")
                existing_enum = value.get("enum")
                if existing_enum is None:
                    value["enum"] = [constant]
                elif constant not in existing_enum:
                    raise CodegenContractError(
                        "OpenAPI const conflicts with enum: "
                        f"{constant!r} not in {existing_enum!r}"
                    )

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
                    # The pinned generator emits references to undefined AnyOf
                    # helpers for primitive unions. Go has no native union;
                    # interface{} faithfully accepts every declared branch.
                    value.pop("anyOf")
            normalize_nullable_anyof(value)
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
