"""Parse and validate the generated sync/async Python callable wire surface."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from scripts.openapi_sdk_contract import (
        ContractError,
        media_schemas,
        merged_parameters,
        operation_map,
        python_name,
        ref_name,
        resolve_local_ref,
        schema_label,
    )
except ModuleNotFoundError:  # direct script execution through a sibling module
    from openapi_sdk_contract import (
        ContractError,
        media_schemas,
        merged_parameters,
        operation_map,
        python_name,
        ref_name,
        resolve_local_ref,
        schema_label,
    )

SPECIAL_PARAMETERS = frozenset(
    {"_request_timeout", "_request_auth", "_content_type", "_headers", "_host_index"}
)


@dataclass(frozen=True)
class ParsedFunction:
    name: str
    is_async: bool
    parameters: tuple[dict[str, Any], ...]
    returns: str
    docstring: str
    signature: str


def _literal(node: ast.AST | None) -> Any:
    if node is None:
        return None
    try:
        return ast.literal_eval(node)
    except (ValueError, TypeError):
        return None


def _annotation(node: ast.AST | None) -> str:
    return ast.unparse(node) if node is not None else "Any"


def _parameters(node: ast.FunctionDef | ast.AsyncFunctionDef) -> tuple[dict[str, Any], ...]:
    positional = [*node.args.posonlyargs, *node.args.args]
    positional_defaults: list[ast.AST | None] = [None] * (
        len(positional) - len(node.args.defaults)
    ) + list(node.args.defaults)
    result: list[dict[str, Any]] = []
    for argument, default in zip(positional, positional_defaults, strict=True):
        if argument.arg == "self":
            continue
        result.append(
            {
                "name": argument.arg,
                "annotation": _annotation(argument.annotation),
                "required": default is None,
                "default": None if default is None else ast.unparse(default),
                "kind": "positional",
            }
        )
    if node.args.vararg:
        result.append(
            {
                "name": f"*{node.args.vararg.arg}",
                "annotation": _annotation(node.args.vararg.annotation),
                "required": False,
                "default": None,
                "kind": "vararg",
            }
        )
    for argument, default in zip(
        node.args.kwonlyargs, node.args.kw_defaults, strict=True
    ):
        result.append(
            {
                "name": argument.arg,
                "annotation": _annotation(argument.annotation),
                "required": default is None,
                "default": None if default is None else ast.unparse(default),
                "kind": "keyword",
            }
        )
    return tuple(result)


def _signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    rendered = []
    for parameter in _parameters(node):
        text = f"{parameter['name']}: {parameter['annotation']}"
        if not parameter["required"] and parameter["kind"] != "vararg":
            text += f" = {parameter['default']}"
        rendered.append(text)
    prefix = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"
    return f"{prefix} {node.name}({', '.join(rendered)}) -> {_annotation(node.returns)}"


def _parse_function(node: ast.FunctionDef | ast.AsyncFunctionDef) -> ParsedFunction:
    return ParsedFunction(
        name=node.name,
        is_async=isinstance(node, ast.AsyncFunctionDef),
        parameters=_parameters(node),
        returns=_annotation(node.returns),
        docstring=ast.get_docstring(node, clean=True) or "",
        signature=_signature(node),
    )


def _mapping_location(name: str) -> str | None:
    return {
        "_path_params": "path",
        "_query_params": "query",
        "_header_params": "header",
        "_form_params": "form",
        "_files": "file",
    }.get(name)


def _subscript_key(node: ast.Subscript) -> str | None:
    value = _literal(node.slice)
    return value if isinstance(value, str) else None


def _extract_serialize(node: ast.FunctionDef) -> dict[str, Any]:
    wire: list[dict[str, str]] = []
    method: str | None = None
    path: str | None = None
    auth: list[str] = []
    accept: list[str] = []
    content_types: list[str] = []

    for child in ast.walk(node):
        if isinstance(child, ast.Assign) and len(child.targets) == 1:
            target = child.targets[0]
            if isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name):
                location = _mapping_location(target.value.id)
                key = _subscript_key(target)
                if (
                    location
                    and key
                    and key.lower() not in {"accept", "content-type"}
                    and isinstance(child.value, ast.Name)
                ):
                    wire.append(
                        {"location": location, "wire_name": key, "python_name": child.value.id}
                    )
            elif isinstance(target, ast.Name) and target.id == "_body_params" and isinstance(
                child.value, ast.Name
            ):
                wire.append(
                    {"location": "body", "wire_name": "body", "python_name": child.value.id}
                )
            elif isinstance(target, ast.Name) and target.id == "_auth_settings":
                value = _literal(child.value)
                if isinstance(value, list) and all(isinstance(item, str) for item in value):
                    auth = value
        elif (
            isinstance(child, ast.AnnAssign)
            and isinstance(child.target, ast.Name)
            and child.target.id == "_auth_settings"
        ):
            value = _literal(child.value)
            if isinstance(value, list) and all(isinstance(item, str) for item in value):
                auth = value
        if isinstance(child, ast.Expr) and isinstance(child.value, ast.Call):
            call = child.value
            if isinstance(call.func, ast.Attribute) and isinstance(call.func.value, ast.Name):
                location = _mapping_location(call.func.value.id)
                if location in {"query", "form"} and call.func.attr == "append" and call.args:
                    pair = call.args[0]
                    if isinstance(pair, ast.Tuple) and len(pair.elts) >= 2:
                        key = _literal(pair.elts[0])
                        value = pair.elts[1]
                        if isinstance(key, str) and isinstance(value, ast.Name):
                            wire.append(
                                {
                                    "location": location,
                                    "wire_name": key,
                                    "python_name": value.id,
                                }
                            )
        if not isinstance(child, ast.Call) or not isinstance(child.func, ast.Attribute):
            continue
        if child.func.attr == "param_serialize":
            values = {item.arg: _literal(item.value) for item in child.keywords if item.arg}
            method = values.get("method")
            path = values.get("resource_path")
        elif child.func.attr == "select_header_accept" and child.args:
            value = _literal(child.args[0])
            if isinstance(value, list):
                accept = [str(item) for item in value]
        elif child.func.attr == "select_header_content_type" and child.args:
            value = _literal(child.args[0])
            if isinstance(value, list):
                content_types = [str(item) for item in value]

    if method is None or path is None:
        raise ContractError(f"{node.name}: generated serializer lacks method/resource_path")
    unique_wire = {
        (item["location"], item["wire_name"], item["python_name"]): item for item in wire
    }
    return {
        "method": method,
        "path": path,
        "wire": sorted(
            unique_wire.values(),
            key=lambda item: (item["location"], item["wire_name"], item["python_name"]),
        ),
        "auth": sorted(auth),
        "accept": sorted(set(accept)),
        "content_types": sorted(set(content_types)),
    }


def _response_types(node: ast.FunctionDef | ast.AsyncFunctionDef) -> dict[str, str | None]:
    for child in ast.walk(node):
        if isinstance(child, ast.Assign) and len(child.targets) == 1:
            target = child.targets[0]
            assigned = child.value
        elif isinstance(child, ast.AnnAssign):
            target = child.target
            assigned = child.value
        else:
            continue
        if isinstance(target, ast.Name) and target.id == "_response_types_map":
            value = _literal(assigned)
            if isinstance(value, dict):
                return {
                    str(key): item if isinstance(item, str) else None
                    for key, item in value.items()
                }
    raise ContractError(f"{node.name}: generated operation lacks _response_types_map")


def _header_carrier(api_root: Path) -> bool:
    path = api_root.parent / "api_response.py"
    if not path.exists():
        return False
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return any(
        isinstance(node, ast.AnnAssign)
        and isinstance(node.target, ast.Name)
        and node.target.id == "headers"
        for node in ast.walk(tree)
    )


def parse_surface(
    api_root: Path, operation_ids: set[str], *, expected_async: bool
) -> dict[str, dict[str, Any]]:
    functions: dict[str, tuple[str, ast.FunctionDef | ast.AsyncFunctionDef]] = {}
    for path in sorted(api_root.glob("*_api.py")):
        if path.name == "__init__.py":
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
        for class_node in classes:
            for node in class_node.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    functions[node.name] = (class_node.name, node)

    result: dict[str, dict[str, Any]] = {}
    for operation_id in sorted(operation_ids):
        required_names = (
            operation_id,
            f"{operation_id}_with_http_info",
            f"{operation_id}_without_preload_content",
            f"_{operation_id}_serialize",
        )
        missing = [name for name in required_names if name not in functions]
        if missing:
            raise ContractError(f"{api_root}: {operation_id} missing generated callables {missing}")
        owner, primary_node = functions[operation_id]
        info_owner, info_node = functions[f"{operation_id}_with_http_info"]
        raw_owner, raw_node = functions[f"{operation_id}_without_preload_content"]
        serializer_owner, serializer_node = functions[f"_{operation_id}_serialize"]
        if len({owner, info_owner, raw_owner, serializer_owner}) != 1:
            raise ContractError(f"{operation_id}: generated variants are split across API classes")
        for public_node in (primary_node, info_node, raw_node):
            if isinstance(public_node, ast.AsyncFunctionDef) != expected_async:
                mode = "async" if expected_async else "sync"
                raise ContractError(f"{api_root}: {public_node.name} is not {mode}")
        if not isinstance(serializer_node, ast.FunctionDef):
            raise ContractError(f"{operation_id}: serializer must be synchronous setup code")

        primary = _parse_function(primary_node)
        with_info = _parse_function(info_node)
        without_preload = _parse_function(raw_node)
        parameter_shapes = [item.parameters for item in (primary, with_info, without_preload)]
        if not parameter_shapes[0] == parameter_shapes[1] == parameter_shapes[2]:
            raise ContractError(f"{operation_id}: generated variant parameter signatures drifted")
        result[operation_id] = {
            "api_class": owner,
            "primary": primary,
            "with_http_info": with_info,
            "without_preload_content": without_preload,
            "serialize": _extract_serialize(serializer_node),
            "response_types": _response_types(primary_node),
            "response_headers_available": _header_carrier(api_root),
        }
    return result


def _nonnull_schema(schema: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    alternatives = schema.get("anyOf")
    if isinstance(alternatives, list):
        nonnull = [item for item in alternatives if isinstance(item, dict) and item.get("type") != "null"]
        nullable = len(nonnull) != len(alternatives)
        if len(nonnull) == 1:
            return nonnull[0], nullable
    return schema, schema.get("nullable") is True


def _annotation_matches(schema: dict[str, Any], annotation: str) -> bool:
    schema, nullable = _nonnull_schema(schema)
    normalized = annotation.replace("Strict", "").lower()
    name = ref_name(schema)
    if name:
        matched = name.lower() in normalized
    else:
        schema_type = schema.get("type")
        if schema_type == "string" and schema.get("format") == "binary":
            matched = "bytes" in normalized
        elif schema_type == "string" and schema.get("format") == "date-time":
            matched = "datetime" in normalized
        elif schema_type == "string" and schema.get("format") == "date":
            matched = "date" in normalized
        elif schema_type == "string" and schema.get("format") == "uuid":
            matched = "uuid" in normalized or "str" in normalized
        elif schema_type == "string":
            matched = "str" in normalized
        elif schema_type == "integer":
            matched = "int" in normalized
        elif schema_type == "number":
            matched = "float" in normalized or "int" in normalized
        elif schema_type == "boolean":
            matched = "bool" in normalized
        elif schema_type == "array":
            matched = "list" in normalized or "sequence" in normalized
        elif schema_type == "object" or "properties" in schema:
            matched = any(item in normalized for item in ("dict", "mapping", "any"))
        else:
            matched = "any" in normalized
    if nullable and "optional" not in normalized and "none" not in normalized:
        return False
    return matched


def _expected_wire(document: dict[str, Any], entry: dict[str, Any]) -> list[dict[str, Any]]:
    operation = entry["operation"]
    result: list[dict[str, Any]] = []
    for parameter in merged_parameters(document, entry["path_item"], operation):
        result.append(
            {
                "location": parameter["in"],
                "wire_name": parameter["name"],
                "python_name": python_name(parameter["name"]),
                "required": bool(parameter.get("required")),
                "schema": parameter.get("schema", {}),
            }
        )
    request_body = resolve_local_ref(document, operation.get("requestBody", {}))
    if isinstance(request_body, dict) and request_body.get("content"):
        media = media_schemas(request_body["content"])
        if "multipart/form-data" in media:
            schema = resolve_local_ref(document, media["multipart/form-data"])
            required = set(schema.get("required", [])) if isinstance(schema, dict) else set()
            for name, field_schema in schema.get("properties", {}).items():
                nonnull, _nullable = _nonnull_schema(field_schema)
                location = "file" if nonnull.get("format") == "binary" else "form"
                result.append(
                    {
                        "location": location,
                        "wire_name": name,
                        "python_name": python_name(name),
                        "required": name in required,
                        "schema": field_schema,
                    }
                )
        else:
            first_schema = next(iter(media.values()))
            name = ref_name(first_schema)
            result.append(
                {
                    "location": "body",
                    "wire_name": "body",
                    "python_name": python_name(name) if name else "body",
                    "required": bool(request_body.get("required")),
                    "schema": first_schema,
                }
            )
    return result


def _expected_response_type(schema: dict[str, Any]) -> str | None:
    if not schema:
        return "object"
    name = ref_name(schema)
    if name:
        return name
    schema, _nullable = _nonnull_schema(schema)
    schema_type = schema.get("type")
    if schema_type == "string" and schema.get("format") == "binary":
        return "bytes"
    if schema_type == "string":
        return "str"
    if schema_type == "integer":
        return "int"
    if schema_type == "number":
        return "float"
    if schema_type == "boolean":
        return "bool"
    if schema_type == "array":
        child = _expected_response_type(schema.get("items", {})) or "object"
        return f"List[{child}]"
    if schema_type == "object" or "properties" in schema:
        return "<generated-object>"
    return None


def _parameters_by_name(surface: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["name"]: item for item in surface["primary"].parameters}


def check_surface_against_contract(
    document: dict[str, Any], surface: dict[str, dict[str, Any]], *, label: str
) -> list[str]:
    failures: list[str] = []
    expected = operation_map(document)
    if set(surface) != set(expected):
        failures.append(
            f"{label}: operation set differs; missing={sorted(set(expected) - set(surface))}, "
            f"extra={sorted(set(surface) - set(expected))}"
        )
        return failures
    for operation_id, entry in expected.items():
        actual = surface[operation_id]
        serialized = actual["serialize"]
        if serialized["method"] != entry["method"] or serialized["path"] != entry["path"]:
            failures.append(
                f"{label}:{operation_id}: expected {entry['method']} {entry['path']}, got "
                f"{serialized['method']} {serialized['path']}"
            )
        expected_auth = sorted(
            {name for requirement in entry["operation"].get("security", []) for name in requirement}
        )
        if serialized["auth"] != expected_auth:
            failures.append(
                f"{label}:{operation_id}: auth {serialized['auth']} != {expected_auth}"
            )

        expected_wire = _expected_wire(document, entry)
        actual_wire = {
            (item["location"], item["wire_name"], item["python_name"])
            for item in serialized["wire"]
        }
        expected_wire_keys = {
            (item["location"], item["wire_name"], item["python_name"])
            for item in expected_wire
        }
        if actual_wire != expected_wire_keys:
            failures.append(
                f"{label}:{operation_id}: wire params differ; missing="
                f"{sorted(expected_wire_keys - actual_wire)}, "
                f"extra={sorted(actual_wire - expected_wire_keys)}"
            )

        expected_public_parameters = {
            item["python_name"] for item in expected_wire
        } | SPECIAL_PARAMETERS
        for variant_name in (
            "primary",
            "with_http_info",
            "without_preload_content",
        ):
            actual_public_parameters = {
                item["name"] for item in actual[variant_name].parameters
            }
            if actual_public_parameters != expected_public_parameters:
                failures.append(
                    f"{label}:{operation_id}:{variant_name}: public parameters differ; "
                    f"missing={sorted(expected_public_parameters - actual_public_parameters)}, "
                    f"extra={sorted(actual_public_parameters - expected_public_parameters)}"
                )

        signature = _parameters_by_name(actual)
        for item in expected_wire:
            parameter = signature.get(item["python_name"])
            if not parameter:
                failures.append(
                    f"{label}:{operation_id}: signature missing {item['python_name']}"
                )
                continue
            if parameter["required"] != item["required"]:
                failures.append(
                    f"{label}:{operation_id}:{item['python_name']}: requiredness "
                    f"{parameter['required']} != {item['required']}"
                )
            if not _annotation_matches(item["schema"], parameter["annotation"]):
                failures.append(
                    f"{label}:{operation_id}:{item['python_name']}: annotation "
                    f"{parameter['annotation']} does not represent {schema_label(item['schema'])}"
                )

        operation = entry["operation"]
        request_body = resolve_local_ref(document, operation.get("requestBody", {}))
        expected_content_types = sorted(
            media_schemas(request_body.get("content", {}))
            if isinstance(request_body, dict)
            else []
        )
        if serialized["content_types"] != expected_content_types:
            failures.append(
                f"{label}:{operation_id}: request content types {serialized['content_types']} "
                f"!= {expected_content_types}"
            )
        expected_accept = sorted(
            {
                media_type
                for raw_response in operation.get("responses", {}).values()
                for media_type in media_schemas(
                    (
                        resolve_local_ref(document, raw_response)
                        if isinstance(resolve_local_ref(document, raw_response), dict)
                        else {}
                    ).get("content", {})
                )
            }
        )
        if serialized["accept"] != expected_accept:
            failures.append(
                f"{label}:{operation_id}: response content types {serialized['accept']} "
                f"!= {expected_accept}"
            )

        expected_responses: dict[str, str | None] = {}
        for status, raw_response in operation.get("responses", {}).items():
            response = resolve_local_ref(document, raw_response)
            media = media_schemas(response.get("content", {}) if isinstance(response, dict) else {})
            expected_responses[str(status)] = (
                _expected_response_type(next(iter(media.values()))) if media else None
            )
        actual_responses = actual["response_types"]
        if set(actual_responses) != set(expected_responses):
            failures.append(
                f"{label}:{operation_id}: response statuses {sorted(actual_responses)} "
                f"!= {sorted(expected_responses)}"
            )
        for status, expected_type in expected_responses.items():
            actual_type = actual_responses.get(status)
            if expected_type == "<generated-object>":
                if not actual_type:
                    failures.append(
                        f"{label}:{operation_id}:{status}: inline response has no generated model"
                    )
            elif actual_type != expected_type:
                failures.append(
                    f"{label}:{operation_id}:{status}: response type {actual_type!r} "
                    f"!= {expected_type!r}"
                )
        has_headers = any(
            isinstance(resolve_local_ref(document, raw), dict)
            and bool(resolve_local_ref(document, raw).get("headers"))
            for raw in operation.get("responses", {}).values()
        )
        if has_headers and not actual["response_headers_available"]:
            failures.append(
                f"{label}:{operation_id}: response headers exist but ApiResponse has no header carrier"
            )
    return failures


def _parity_value(value: dict[str, Any]) -> dict[str, Any]:
    def function(item: ParsedFunction) -> dict[str, Any]:
        return {
            "parameters": item.parameters,
            "returns": item.returns,
            "docstring": item.docstring,
        }

    return {
        "api_class": value["api_class"],
        "primary": function(value["primary"]),
        "with_http_info": function(value["with_http_info"]),
        "without_preload_content": function(value["without_preload_content"]),
        "serialize": value["serialize"],
        "response_types": value["response_types"],
        "response_headers_available": value["response_headers_available"],
    }


def check_sync_async_parity(
    sync: dict[str, dict[str, Any]], async_client: dict[str, dict[str, Any]]
) -> list[str]:
    failures: list[str] = []
    if set(sync) != set(async_client):
        return ["sync/async generated operation sets differ"]
    for operation_id in sorted(sync):
        if _parity_value(sync[operation_id]) != _parity_value(async_client[operation_id]):
            failures.append(f"{operation_id}: sync/async generated callable or wire shape differs")
    return failures


def public_operation_names(api_root: Path) -> set[str]:
    names: set[str] = set()
    for path in api_root.glob("*_api.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if node.name.startswith("_") or node.name.endswith(
                ("_with_http_info", "_without_preload_content")
            ):
                continue
            if node.name != "__init__":
                names.add(node.name)
    return names
