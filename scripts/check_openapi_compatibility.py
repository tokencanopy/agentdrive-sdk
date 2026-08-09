"""Reject backward-incompatible SDK contract changes.

The comparator is direction-aware: a new request schema must continue to
accept every previously valid request, while a new response schema must remain
readable by an older client. AgentDrive response models intentionally ignore
additive fields and accept unknown enum strings, so those two response changes
are explicitly compatible.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Literal

try:
    from scripts.openapi_sdk_contract import (
        ContractError,
        load_document,
        media_schemas,
        merged_parameters,
        operation_map,
        resolve_local_ref,
        sha256_json,
        shape_schema,
    )
except ModuleNotFoundError:  # direct `python scripts/...py` execution
    from openapi_sdk_contract import (
        ContractError,
        load_document,
        media_schemas,
        merged_parameters,
        operation_map,
        resolve_local_ref,
        sha256_json,
        shape_schema,
    )

Direction = Literal["request", "response"]
DEFAULT_CURRENT = Path("sdk/openapi.json")
DEFAULT_RESET = Path("sdk/openapi.compatibility-reset.json")
DEFAULT_PROVENANCE = Path("sdk/openapi.provenance.json")


def load_source(source: str) -> dict[str, Any]:
    """Load a filesystem JSON document or a ``git show`` object expression."""

    path = Path(source)
    if path.is_file():
        return load_document(path)
    result = subprocess.run(
        ["git", "show", source],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        detail = result.stderr.strip() or "git show failed"
        raise ContractError(f"cannot load compatibility base {source!r}: {detail}")
    try:
        document = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise ContractError(f"compatibility base {source!r} is not JSON: {exc}") from exc
    if not isinstance(document, dict):
        raise ContractError(f"compatibility base {source!r} must contain a JSON object")
    return document


def _effective_security(document: dict[str, Any], operation: dict[str, Any]) -> list[Any]:
    value = operation.get("security", document.get("security", []))
    return value if isinstance(value, list) else []


def _security_covers(old: list[Any], new: list[Any]) -> bool:
    """Return whether each old authentication alternative still works."""

    if not old:
        old = [{}]
    if not new:
        new = [{}]
    for old_requirement in old:
        if not isinstance(old_requirement, dict):
            return False
        accepted = False
        for new_requirement in new:
            if not isinstance(new_requirement, dict):
                continue
            if not set(new_requirement).issubset(old_requirement):
                continue
            if all(
                set(new_requirement[name] or []).issubset(old_requirement[name] or [])
                for name in new_requirement
            ):
                accepted = True
                break
        if not accepted:
            return False
    return True


def _type_set(schema: dict[str, Any]) -> set[str] | None:
    raw = schema.get("type")
    if isinstance(raw, str):
        result = {raw}
    elif isinstance(raw, list) and all(isinstance(item, str) for item in raw):
        result = set(raw)
    elif not schema or set(schema).issubset({"description", "title", "examples", "example"}):
        return None
    elif "properties" in schema or "additionalProperties" in schema:
        result = {"object"}
    elif "items" in schema:
        result = {"array"}
    else:
        return None
    if schema.get("nullable") is True:
        result.add("null")
    return result


def _bound_breaks(
    old: dict[str, Any], new: dict[str, Any], direction: Direction
) -> list[str]:
    failures: list[str] = []
    lower = ("minimum", "exclusiveMinimum", "minLength", "minItems", "minProperties")
    upper = ("maximum", "exclusiveMaximum", "maxLength", "maxItems", "maxProperties")
    for name in lower:
        old_value = old.get(name)
        new_value = new.get(name)
        if direction == "request":
            if new_value is not None and (old_value is None or new_value > old_value):
                failures.append(f"tightened {name} from {old_value!r} to {new_value!r}")
        elif old_value is not None and (new_value is None or new_value < old_value):
            failures.append(f"response loosened {name} from {old_value!r} to {new_value!r}")
    for name in upper:
        old_value = old.get(name)
        new_value = new.get(name)
        if direction == "request":
            if new_value is not None and (old_value is None or new_value < old_value):
                failures.append(f"tightened {name} from {old_value!r} to {new_value!r}")
        elif old_value is not None and (new_value is None or new_value > old_value):
            failures.append(f"response loosened {name} from {old_value!r} to {new_value!r}")
    old_pattern = old.get("pattern")
    new_pattern = new.get("pattern")
    if direction == "request" and new_pattern and new_pattern != old_pattern:
        failures.append(f"introduced/changed pattern from {old_pattern!r} to {new_pattern!r}")
    if direction == "response" and old_pattern and new_pattern != old_pattern:
        failures.append(f"response changed/removed pattern from {old_pattern!r} to {new_pattern!r}")
    return failures


def _additional_policy(schema: dict[str, Any]) -> Any:
    return schema.get("additionalProperties", True)


def _schema_breaks(
    old_document: dict[str, Any],
    new_document: dict[str, Any],
    old_schema: Any,
    new_schema: Any,
    *,
    direction: Direction,
    location: str,
    seen: set[tuple[int, int, Direction]] | None = None,
) -> list[str]:
    old_schema = resolve_local_ref(old_document, old_schema)
    new_schema = resolve_local_ref(new_document, new_schema)
    if not isinstance(old_schema, dict) or not isinstance(new_schema, dict):
        if shape_schema(old_schema) != shape_schema(new_schema):
            return [f"{location}: schema changed"]
        return []

    seen = seen or set()
    pair = (id(old_schema), id(new_schema), direction)
    if pair in seen:
        return []
    seen.add(pair)

    old_alternatives = old_schema.get("anyOf") or old_schema.get("oneOf")
    new_alternatives = new_schema.get("anyOf") or new_schema.get("oneOf")
    if isinstance(old_alternatives, list) or isinstance(new_alternatives, list):
        old_values = old_alternatives if isinstance(old_alternatives, list) else [old_schema]
        new_values = new_alternatives if isinstance(new_alternatives, list) else [new_schema]
        source, targets = (
            (old_values, new_values) if direction == "request" else (new_values, old_values)
        )
        for index, candidate in enumerate(source):
            if not any(
                not _schema_breaks(
                    old_document,
                    new_document,
                    candidate if direction == "request" else target,
                    target if direction == "request" else candidate,
                    direction=direction,
                    location=location,
                    seen=set(seen),
                )
                for target in targets
            ):
                return [f"{location}: union alternative {index} is no longer compatible"]
        return []

    failures: list[str] = []
    old_types = _type_set(old_schema)
    new_types = _type_set(new_schema)
    if direction == "request":
        if old_types is None and new_types is not None:
            failures.append(f"{location}: unconstrained request type became {sorted(new_types)}")
        elif old_types is not None and new_types is not None and not old_types <= new_types:
            failures.append(
                f"{location}: request types {sorted(old_types)} are not a subset of "
                f"{sorted(new_types)}"
            )
    elif old_types is not None:
        if new_types is None or not new_types <= old_types:
            failures.append(
                f"{location}: response types {sorted(new_types) if new_types else 'any'} "
                f"are not a subset of {sorted(old_types)}"
            )

    old_format = old_schema.get("format")
    new_format = new_schema.get("format")
    if old_format != new_format:
        if direction == "request" and new_format is not None:
            failures.append(f"{location}: request format changed {old_format!r} -> {new_format!r}")
        elif direction == "response" and old_format is not None:
            failures.append(f"{location}: response format changed {old_format!r} -> {new_format!r}")

    old_enum = old_schema.get("enum")
    new_enum = new_schema.get("enum")
    if direction == "request":
        if isinstance(new_enum, list) and (
            not isinstance(old_enum, list) or not set(old_enum).issubset(new_enum)
        ):
            failures.append(f"{location}: request enum removed or newly restricts values")
    # Response enums are deliberately open in both generated Python clients.
    # Expansion and contraction therefore do not make wire deserialization fail.

    failures.extend(
        f"{location}: {message}" for message in _bound_breaks(old_schema, new_schema, direction)
    )

    old_properties = old_schema.get("properties", {})
    new_properties = new_schema.get("properties", {})
    if isinstance(old_properties, dict) and isinstance(new_properties, dict):
        old_required = set(old_schema.get("required", []))
        new_required = set(new_schema.get("required", []))
        if direction == "request":
            added_required = new_required - old_required
            if added_required:
                failures.append(
                    f"{location}: new required request properties {sorted(added_required)}"
                )
            old_additional = _additional_policy(old_schema)
            new_additional = _additional_policy(new_schema)
            if old_additional is not False and new_additional is False:
                failures.append(f"{location}: request additionalProperties became false")
            for name, old_property in old_properties.items():
                if name in new_properties:
                    failures.extend(
                        _schema_breaks(
                            old_document,
                            new_document,
                            old_property,
                            new_properties[name],
                            direction=direction,
                            location=f"{location}.{name}",
                            seen=set(seen),
                        )
                    )
                elif new_additional is False:
                    failures.append(f"{location}: request property {name!r} is no longer accepted")
                elif isinstance(new_additional, dict):
                    failures.extend(
                        _schema_breaks(
                            old_document,
                            new_document,
                            old_property,
                            new_additional,
                            direction=direction,
                            location=f"{location}.{name}",
                            seen=set(seen),
                        )
                    )
        else:
            no_longer_required = old_required - new_required
            if no_longer_required:
                failures.append(
                    f"{location}: required response properties became optional "
                    f"{sorted(no_longer_required)}"
                )
            for name, old_property in old_properties.items():
                if name not in new_properties:
                    failures.append(f"{location}: response property {name!r} was removed")
                    continue
                failures.extend(
                    _schema_breaks(
                        old_document,
                        new_document,
                        old_property,
                        new_properties[name],
                        direction=direction,
                        location=f"{location}.{name}",
                        seen=set(seen),
                    )
                )
            # Additive response properties are safe because generated response
            # models are postprocessed with Pydantic ``extra='ignore'``.

    old_items = old_schema.get("items")
    new_items = new_schema.get("items")
    if isinstance(old_items, dict) and isinstance(new_items, dict):
        failures.extend(
            _schema_breaks(
                old_document,
                new_document,
                old_items,
                new_items,
                direction=direction,
                location=f"{location}[]",
                seen=set(seen),
            )
        )
    elif isinstance(old_items, dict) != isinstance(new_items, dict):
        failures.append(f"{location}: array item schema was added or removed")
    return failures


def _parameter_map(
    document: dict[str, Any], entry: dict[str, Any]
) -> dict[tuple[str, str], dict[str, Any]]:
    return {
        (str(item.get("in")), str(item.get("name"))): item
        for item in merged_parameters(document, entry["path_item"], entry["operation"])
    }


def _request_body_breaks(
    old_document: dict[str, Any],
    new_document: dict[str, Any],
    operation_id: str,
    old_operation: dict[str, Any],
    new_operation: dict[str, Any],
) -> list[str]:
    old_body = resolve_local_ref(old_document, old_operation.get("requestBody", {}))
    new_body = resolve_local_ref(new_document, new_operation.get("requestBody", {}))
    old_body = old_body if isinstance(old_body, dict) else {}
    new_body = new_body if isinstance(new_body, dict) else {}
    failures: list[str] = []
    if not old_body.get("content"):
        if new_body.get("required"):
            failures.append(f"{operation_id}: added a required request body")
        return failures
    if not new_body.get("content"):
        return [f"{operation_id}: request body was removed"]
    if not old_body.get("required") and new_body.get("required"):
        failures.append(f"{operation_id}: request body became required")
    old_media = media_schemas(old_body.get("content"))
    new_media = media_schemas(new_body.get("content"))
    for media_type, old_schema in old_media.items():
        if media_type not in new_media:
            failures.append(f"{operation_id}: removed request media type {media_type}")
            continue
        failures.extend(
            _schema_breaks(
                old_document,
                new_document,
                old_schema,
                new_media[media_type],
                direction="request",
                location=f"{operation_id}:request[{media_type}]",
            )
        )
    return failures


def _response_breaks(
    old_document: dict[str, Any],
    new_document: dict[str, Any],
    operation_id: str,
    old_operation: dict[str, Any],
    new_operation: dict[str, Any],
) -> list[str]:
    failures: list[str] = []
    old_responses = old_operation.get("responses", {})
    new_responses = new_operation.get("responses", {})
    for status, old_raw in old_responses.items():
        if status not in new_responses:
            failures.append(f"{operation_id}: removed response status {status}")
            continue
        old_response = resolve_local_ref(old_document, old_raw)
        new_response = resolve_local_ref(new_document, new_responses[status])
        old_response = old_response if isinstance(old_response, dict) else {}
        new_response = new_response if isinstance(new_response, dict) else {}
        old_media = media_schemas(old_response.get("content"))
        new_media = media_schemas(new_response.get("content"))
        for media_type, old_schema in old_media.items():
            if media_type not in new_media:
                failures.append(
                    f"{operation_id}:{status}: removed response media type {media_type}"
                )
                continue
            failures.extend(
                _schema_breaks(
                    old_document,
                    new_document,
                    old_schema,
                    new_media[media_type],
                    direction="response",
                    location=f"{operation_id}:response[{status},{media_type}]",
                )
            )
        old_headers = old_response.get("headers", {})
        new_headers = new_response.get("headers", {})
        for name, old_header in old_headers.items():
            if name not in new_headers:
                failures.append(f"{operation_id}:{status}: removed response header {name}")
                continue
            old_header = resolve_local_ref(old_document, old_header)
            new_header = resolve_local_ref(new_document, new_headers[name])
            if isinstance(old_header, dict) and isinstance(new_header, dict):
                failures.extend(
                    _schema_breaks(
                        old_document,
                        new_document,
                        old_header.get("schema", {}),
                        new_header.get("schema", {}),
                        direction="response",
                        location=f"{operation_id}:response[{status}].header[{name}]",
                    )
                )
    return failures


def compare_contracts(
    old_document: dict[str, Any], new_document: dict[str, Any]
) -> list[str]:
    """Return deterministic backward-compatibility failures."""

    failures: list[str] = []
    old_servers = [item.get("url") for item in old_document.get("servers", []) if isinstance(item, dict)]
    new_servers = [item.get("url") for item in new_document.get("servers", []) if isinstance(item, dict)]
    if old_servers and old_servers != new_servers:
        failures.append(f"API server URLs changed: {old_servers!r} -> {new_servers!r}")

    old_operations = operation_map(old_document)
    new_operations = operation_map(new_document)
    for operation_id in sorted(old_operations):
        if operation_id not in new_operations:
            failures.append(f"removed operationId {operation_id}")
            continue
        old_entry = old_operations[operation_id]
        new_entry = new_operations[operation_id]
        if (old_entry["method"], old_entry["path"]) != (
            new_entry["method"],
            new_entry["path"],
        ):
            failures.append(
                f"{operation_id}: route changed from {old_entry['method']} {old_entry['path']} "
                f"to {new_entry['method']} {new_entry['path']}"
            )
        old_operation = old_entry["operation"]
        new_operation = new_entry["operation"]
        if not _security_covers(
            _effective_security(old_document, old_operation),
            _effective_security(new_document, new_operation),
        ):
            failures.append(f"{operation_id}: authentication requirements became stricter")

        old_parameters = _parameter_map(old_document, old_entry)
        new_parameters = _parameter_map(new_document, new_entry)
        for key, old_parameter in old_parameters.items():
            if key not in new_parameters:
                failures.append(f"{operation_id}: removed {key[0]} parameter {key[1]}")
                continue
            new_parameter = new_parameters[key]
            if not old_parameter.get("required") and new_parameter.get("required"):
                failures.append(f"{operation_id}: parameter {key[1]} became required")
            failures.extend(
                _schema_breaks(
                    old_document,
                    new_document,
                    old_parameter.get("schema", {}),
                    new_parameter.get("schema", {}),
                    direction="request",
                    location=f"{operation_id}:parameter[{key[0]},{key[1]}]",
                )
            )
        for key, new_parameter in new_parameters.items():
            if key not in old_parameters and new_parameter.get("required"):
                failures.append(f"{operation_id}: added required {key[0]} parameter {key[1]}")

        failures.extend(
            _request_body_breaks(
                old_document, new_document, operation_id, old_operation, new_operation
            )
        )
        failures.extend(
            _response_breaks(
                old_document, new_document, operation_id, old_operation, new_operation
            )
        )
    return sorted(set(failures))


def _reset_matches(
    reset_path: Path,
    old_document: dict[str, Any],
    new_document: dict[str, Any],
    *,
    source_commit: str,
) -> tuple[bool, str]:
    if not reset_path.is_file():
        return False, ""
    reset = load_document(reset_path)
    required = {"format", "from_sha256", "to_sha256", "reason", "source_commit"}
    if set(reset) != required:
        raise ContractError(
            f"{reset_path}: reset metadata keys must be exactly {sorted(required)}"
        )
    if reset["format"] != 1:
        raise ContractError(f"{reset_path}: unsupported reset metadata format")
    string_fields = required - {"format"}
    if not all(isinstance(reset[name], str) and reset[name] for name in string_fields):
        raise ContractError(f"{reset_path}: reset metadata values must be non-empty strings")
    matches = (
        reset["from_sha256"] == sha256_json(old_document)
        and reset["to_sha256"] == sha256_json(new_document)
        and reset["source_commit"] == source_commit
    )
    return matches, str(reset["reason"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--base",
        required=True,
        help="base contract path or git object expression (for example BASE:sdk/openapi.json)",
    )
    parser.add_argument("--current", type=Path, default=DEFAULT_CURRENT)
    parser.add_argument("--allow-reset", type=Path, default=DEFAULT_RESET)
    parser.add_argument("--provenance", type=Path, default=DEFAULT_PROVENANCE)
    args = parser.parse_args()

    try:
        old_document = load_source(args.base)
        new_document = load_document(args.current)
        provenance = load_document(args.provenance)
        source_commit = provenance.get("source_commit")
        if not isinstance(source_commit, str) or not source_commit:
            raise ContractError(f"{args.provenance}: source_commit must be a non-empty string")
        failures = compare_contracts(old_document, new_document)
        if not failures:
            print(
                "OpenAPI compatibility gate passed: "
                f"{len(operation_map(old_document))} -> {len(operation_map(new_document))} operations."
            )
            return
        reset_matches, reason = _reset_matches(
            args.allow_reset,
            old_document,
            new_document,
            source_commit=source_commit,
        )
        if reset_matches:
            print(
                "OpenAPI compatibility reset matched exact reviewed contract digests: "
                f"{len(operation_map(old_document))} -> {len(operation_map(new_document))} "
                f"operations ({len(failures)} otherwise-breaking changes). Reason: {reason}"
            )
            return
        print("OpenAPI compatibility gate failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        if args.allow_reset.is_file():
            print(
                f"Reset metadata {args.allow_reset} does not exactly match the base/current digests.",
                file=sys.stderr,
            )
        raise SystemExit(1)
    except (ContractError, OSError) as exc:
        print(f"OpenAPI compatibility gate failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
