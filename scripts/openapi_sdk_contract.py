"""Shared, dependency-free helpers for AgentDrive SDK contract gates."""

from __future__ import annotations

import hashlib
import json
import re
from copy import deepcopy
from pathlib import Path
from typing import Any, Iterator

HTTP_METHODS = frozenset(
    {"get", "put", "post", "delete", "patch", "head", "options", "trace"}
)
SCHEMA_DOC_KEYS = frozenset(
    {"$comment", "description", "example", "examples", "externalDocs", "title"}
)


class ContractError(ValueError):
    """Raised when an SDK contract invariant is violated."""


def load_document(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError(f"{path} must contain a JSON object")
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode()).hexdigest()


def resolve_local_ref(document: dict[str, Any], value: Any) -> Any:
    """Resolve one local JSON pointer, leaving non-reference values unchanged."""

    if not isinstance(value, dict) or set(value) != {"$ref"}:
        return value
    ref = value["$ref"]
    if not isinstance(ref, str) or not ref.startswith("#/"):
        raise ContractError(f"only local OpenAPI references are supported: {ref!r}")
    current: Any = document
    for raw_part in ref[2:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        try:
            current = current[part]
        except (KeyError, TypeError) as exc:
            raise ContractError(f"unresolvable local reference: {ref}") from exc
    return current


def ref_name(value: Any) -> str | None:
    if not isinstance(value, dict):
        return None
    ref = value.get("$ref")
    if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
        return ref.rsplit("/", 1)[1]
    return None


def iter_operations(
    document: dict[str, Any],
) -> Iterator[tuple[str, str, dict[str, Any], dict[str, Any]]]:
    """Yield ``(path, method, path_item, operation)`` in wire order."""

    for path, path_item in document.get("paths", {}).items():
        if not isinstance(path_item, dict):
            continue
        for method, operation in path_item.items():
            if method in HTTP_METHODS and isinstance(operation, dict):
                yield path, method, path_item, operation


def operation_map(document: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for path, method, path_item, operation in iter_operations(document):
        operation_id = operation.get("operationId")
        if not isinstance(operation_id, str) or not operation_id:
            raise ContractError(f"{method.upper()} {path} is missing operationId")
        if operation_id in result:
            raise ContractError(f"duplicate operationId: {operation_id}")
        result[operation_id] = {
            "path": path,
            "method": method.upper(),
            "path_item": path_item,
            "operation": operation,
        }
    return result


def python_name(value: str) -> str:
    """Match OpenAPI Generator's ordinary Python parameter/model spelling."""

    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    if value and value[0].isdigit():
        value = f"var_{value}"
    return value


def shape_schema(value: Any) -> Any:
    """Remove prose-only keys while retaining every wire/validation constraint."""

    if isinstance(value, dict):
        return {
            key: shape_schema(child)
            for key, child in sorted(value.items())
            if key not in SCHEMA_DOC_KEYS
        }
    if isinstance(value, list):
        return [shape_schema(child) for child in value]
    return value


def schema_label(schema: Any) -> str:
    """Return a concise, deterministic schema label for docs and diagnostics."""

    if not isinstance(schema, dict):
        return "none"
    name = ref_name(schema)
    if name:
        return name
    if "anyOf" in schema:
        return " | ".join(schema_label(item) for item in schema["anyOf"])
    if "oneOf" in schema:
        return "oneOf(" + ", ".join(schema_label(item) for item in schema["oneOf"]) + ")"
    if "allOf" in schema:
        return "allOf(" + ", ".join(schema_label(item) for item in schema["allOf"]) + ")"
    schema_type = schema.get("type")
    if schema_type == "array":
        return f"array[{schema_label(schema.get('items', {}))}]"
    if schema_type == "object" or "properties" in schema:
        return f"object#{sha256_json(shape_schema(schema))[:12]}"
    if isinstance(schema.get("enum"), list):
        return "enum[" + ", ".join(map(str, schema["enum"])) + "]"
    if schema_type == "string" and schema.get("format"):
        return f"string({schema['format']})"
    if isinstance(schema_type, list):
        return " | ".join(map(str, schema_type))
    return str(schema_type or "any")


def merged_parameters(
    document: dict[str, Any], path_item: dict[str, Any], operation: dict[str, Any]
) -> list[dict[str, Any]]:
    """Return dereferenced path-level + operation-level parameters."""

    by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for raw in [*path_item.get("parameters", []), *operation.get("parameters", [])]:
        parameter = resolve_local_ref(document, raw)
        if not isinstance(parameter, dict):
            raise ContractError("parameter must resolve to an object")
        key = (str(parameter.get("name")), str(parameter.get("in")))
        by_key[key] = parameter
    return list(by_key.values())


def media_schemas(content: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(content, dict):
        return {}
    result: dict[str, dict[str, Any]] = {}
    for media_type, media in content.items():
        if isinstance(media, dict):
            schema = media.get("schema", {})
            result[str(media_type)] = schema if isinstance(schema, dict) else {}
    return result


def schema_references(value: Any) -> set[str]:
    result: set[str] = set()
    if isinstance(value, dict):
        name = ref_name(value)
        if name:
            result.add(name)
        for child in value.values():
            result.update(schema_references(child))
    elif isinstance(value, list):
        for child in value:
            result.update(schema_references(child))
    return result


def schema_closure(document: dict[str, Any], seeds: set[str]) -> set[str]:
    schemas = document.get("components", {}).get("schemas", {})
    result = set(seeds)
    pending = list(seeds)
    while pending:
        name = pending.pop()
        schema = schemas.get(name)
        if not isinstance(schema, dict):
            raise ContractError(f"unknown component schema: {name}")
        for child in schema_references(schema):
            if child not in result:
                result.add(child)
                pending.append(child)
    return result


def model_contexts(document: dict[str, Any]) -> tuple[set[str], set[str]]:
    """Return transitive request and response component schema sets."""

    request_seeds: set[str] = set()
    response_seeds: set[str] = set()
    for _path, _method, _path_item, operation in iter_operations(document):
        request_body = resolve_local_ref(document, operation.get("requestBody", {}))
        if isinstance(request_body, dict):
            request_seeds.update(schema_references(request_body.get("content", {})))
        for raw_response in operation.get("responses", {}).values():
            response = resolve_local_ref(document, raw_response)
            if isinstance(response, dict):
                response_seeds.update(schema_references(response.get("content", {})))
    return (
        schema_closure(document, request_seeds),
        schema_closure(document, response_seeds),
    )


def enum_properties(schema: dict[str, Any]) -> set[str]:
    result: set[str] = set()
    for name, value in schema.get("properties", {}).items():
        if isinstance(value, dict) and (
            isinstance(value.get("enum"), list)
            or any(
                isinstance(item, dict) and isinstance(item.get("enum"), list)
                for item in value.get("anyOf", [])
            )
        ):
            result.add(name)
    return result


def clone(value: Any) -> Any:
    """Typed alias used by compatibility checks before local mutation."""

    return deepcopy(value)
