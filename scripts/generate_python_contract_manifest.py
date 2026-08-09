"""Render/check the exact OpenAPI-to-generated-Python shape manifest."""

from __future__ import annotations

import argparse
import ast
import difflib
import json
import sys
from pathlib import Path
from typing import Any

try:
    from scripts.check_python_generated_contract import validate_generated_contract
    from scripts.openapi_sdk_contract import (
        iter_operations,
        load_document,
        merged_parameters,
        python_name,
        resolve_local_ref,
        sha256_json,
        shape_schema,
    )
except ModuleNotFoundError:  # direct `python scripts/...py` execution
    from check_python_generated_contract import validate_generated_contract
    from openapi_sdk_contract import (
        iter_operations,
        load_document,
        merged_parameters,
        python_name,
        resolve_local_ref,
        sha256_json,
        shape_schema,
    )

DEFAULT_CONTRACT = Path("sdk/openapi.json")
DEFAULT_SYNC_ROOT = Path("sdk/python/src/agentdrive_sdk/generated/sync")
DEFAULT_ASYNC_ROOT = Path("sdk/python/src/agentdrive_sdk/generated/async_client")
DEFAULT_OUTPUT = Path("sdk/python/generated-contract-shape.json")


def _field_shape(node: ast.AnnAssign) -> dict[str, Any]:
    required = node.value is None
    if isinstance(node.value, ast.Call):
        function = node.value.func
        is_field = (isinstance(function, ast.Name) and function.id == "Field") or (
            isinstance(function, ast.Attribute) and function.attr == "Field"
        )
        has_default = bool(node.value.args) or any(
            item.arg in {"default", "default_factory"} for item in node.value.keywords
        )
        if is_field and not has_default:
            required = True
    return {
        "annotation": ast.unparse(node.annotation),
        "default": ast.unparse(node.value) if node.value is not None else None,
        "required": required,
    }


def _annotation_nullable(annotation: str) -> bool:
    tree = ast.parse(annotation, mode="eval")
    return any(
        (isinstance(node, ast.Name) and node.id in {"Optional", "None"})
        or (isinstance(node, ast.Constant) and node.value is None)
        for node in ast.walk(tree)
    )


def _schema_nullable(schema: Any) -> bool:
    if not isinstance(schema, dict):
        return False
    if schema.get("nullable") is True:
        return True
    schema_type = schema.get("type")
    if isinstance(schema_type, list) and "null" in schema_type:
        return True
    return any(
        isinstance(item, dict) and item.get("type") == "null"
        for keyword in ("anyOf", "oneOf")
        for item in schema.get(keyword, [])
    )


def _check_component_models(
    document: dict[str, Any], models: dict[str, Any], *, label: str
) -> None:
    failures: list[str] = []
    schemas = document.get("components", {}).get("schemas", {})
    for model_name, schema in sorted(schemas.items()):
        if not isinstance(schema, dict) or not isinstance(schema.get("properties"), dict):
            continue
        model = models.get(model_name)
        if model is None:
            failures.append(f"{label}: missing component model {model_name}")
            continue
        properties = schema["properties"]
        expected_fields = {python_name(name) for name in properties}
        actual_fields = set(model["fields"])
        if actual_fields != expected_fields:
            failures.append(
                f"{label}:{model_name}: property set differs; "
                f"missing={sorted(expected_fields - actual_fields)}, "
                f"extra={sorted(actual_fields - expected_fields)}"
            )
        required = set(schema.get("required", []))
        for wire_name, property_schema in properties.items():
            field_name = python_name(wire_name)
            field = model["fields"].get(field_name)
            if field is None:
                continue
            expected_required = wire_name in required
            if field["required"] != expected_required:
                failures.append(
                    f"{label}:{model_name}.{wire_name}: requiredness "
                    f"{field['required']} != {expected_required}"
                )
            expected_nullable = _schema_nullable(property_schema)
            actual_nullable = _annotation_nullable(field["annotation"])
            if actual_nullable != expected_nullable:
                failures.append(
                    f"{label}:{model_name}.{wire_name}: nullable annotation "
                    f"{actual_nullable} != {expected_nullable}"
                )
    if failures:
        raise ValueError("\n".join(failures))


def _model_manifest(models_root: Path) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for path in sorted(models_root.glob("*.py")):
        if path.name == "__init__.py":
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
        if len(classes) != 1:
            continue
        class_node = classes[0]
        fields = {
            node.target.id: _field_shape(node)
            for node in class_node.body
            if isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and not node.target.id.startswith("__")
        }
        validators = {
            node.name: sha256_json(ast.dump(node, include_attributes=False))
            for node in class_node.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.decorator_list
        }
        result[class_node.name] = {
            "class_ast_sha256": sha256_json(ast.dump(class_node, include_attributes=False)),
            "fields": fields,
            "validators": validators,
        }
    return result


def _headers_transport(package_root: Path) -> dict[str, Any]:
    response_path = package_root / "api_response.py"
    client_path = package_root / "api_client.py"
    response_tree = ast.parse(
        response_path.read_text(encoding="utf-8"), filename=str(response_path)
    )
    headers_annotations = [
        ast.unparse(node.annotation)
        for node in ast.walk(response_tree)
        if isinstance(node, ast.AnnAssign)
        and isinstance(node.target, ast.Name)
        and node.target.id == "headers"
    ]
    client_tree = ast.parse(client_path.read_text(encoding="utf-8"), filename=str(client_path))
    forwarded = False
    for node in ast.walk(client_tree):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Name) or node.func.id != "ApiResponse":
            continue
        for keyword in node.keywords:
            if keyword.arg == "headers" and ast.unparse(keyword.value) == "response_data.headers":
                forwarded = True
    return {
        "api_response_headers_annotation": headers_annotations,
        "response_deserialize_forwards_all_headers": forwarded,
    }


def _function_manifest(item: Any) -> dict[str, Any]:
    return {
        "docstring_sha256": sha256_json(item.docstring),
        "parameters": list(item.parameters),
        "return": item.returns,
        "signature": item.signature,
    }


def _surface_manifest(surface: dict[str, dict[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for operation_id, value in sorted(surface.items()):
        full_shape = {
            "api_class": value["api_class"],
            "primary": _function_manifest(value["primary"]),
            "with_http_info": _function_manifest(value["with_http_info"]),
            "without_preload_content": _function_manifest(value["without_preload_content"]),
            "serializer": value["serialize"],
            "response_types": value["response_types"],
        }
        result[operation_id] = {
            "api_class": value["api_class"],
            "primary_signature": value["primary"].signature,
            "surface_sha256": sha256_json(full_shape),
        }
    return result


def _contract_operation_shape(
    document: dict[str, Any],
    path: str,
    method: str,
    path_item: dict[str, Any],
    operation: dict[str, Any],
) -> dict[str, Any]:
    parameter_shapes = []
    for parameter in merged_parameters(document, path_item, operation):
        full_parameter = shape_schema(
            {
                key: value
                for key, value in parameter.items()
                if key
                in {
                    "name",
                    "in",
                    "required",
                    "deprecated",
                    "style",
                    "explode",
                    "allowEmptyValue",
                    "allowReserved",
                    "schema",
                    "content",
                }
            }
        )
        parameter_shapes.append(
            {
                "in": parameter.get("in"),
                "name": parameter.get("name"),
                "required": bool(parameter.get("required")),
                "shape_sha256": sha256_json(full_parameter),
            }
        )
    request_body = resolve_local_ref(document, operation.get("requestBody", {}))
    request_shape = shape_schema(request_body)
    responses: dict[str, Any] = {}
    for status, raw_response in sorted(operation.get("responses", {}).items()):
        response = resolve_local_ref(document, raw_response)
        response = response if isinstance(response, dict) else {}
        responses[str(status)] = {
            "content": {
                media_type: sha256_json(shape_schema(media.get("schema", {})))
                for media_type, media in sorted(response.get("content", {}).items())
                if isinstance(media, dict)
            },
            "headers": {
                name: sha256_json(shape_schema(resolve_local_ref(document, header)))
                for name, header in sorted(response.get("headers", {}).items())
            },
            "shape_sha256": sha256_json(shape_schema(response)),
        }
    full_operation = shape_schema(operation)
    return {
        "method": method.upper(),
        "path": path,
        "operation_shape_sha256": sha256_json(full_operation),
        "parameters": parameter_shapes,
        "request_body": {
            "required": bool(request_body.get("required"))
            if isinstance(request_body, dict)
            else False,
            "shape_sha256": sha256_json(request_shape),
        },
        # Each response entry retains its exact status, media schemas, and
        # header names/schemas. Generated clients preserve those headers via
        # the generic ApiResponse.headers carrier recorded alongside this map.
        "responses": responses,
    }


def build_manifest(
    contract_path: Path,
    sync_root: Path,
    async_root: Path,
) -> dict[str, Any]:
    document = load_document(contract_path)
    sync, async_client = validate_generated_contract(
        contract_path, sync_root / "api", async_root / "api"
    )
    sync_models = _model_manifest(sync_root / "models")
    async_models = _model_manifest(async_root / "models")
    if sync_models != async_models:
        raise ValueError("sync/async generated model AST shapes differ")
    _check_component_models(document, sync_models, label="sync")
    _check_component_models(document, async_models, label="async")
    header_transport = {
        "sync": _headers_transport(sync_root),
        "async": _headers_transport(async_root),
    }
    if not all(
        value["api_response_headers_annotation"]
        and value["response_deserialize_forwards_all_headers"]
        for value in header_transport.values()
    ):
        raise ValueError("generated response transport does not preserve raw response headers")
    operations = {
        operation["operationId"]: _contract_operation_shape(
            document, path, method, path_item, operation
        )
        for path, method, path_item, operation in iter_operations(document)
    }
    raw_schemas = document.get("components", {}).get("schemas", {})
    schemas = {
        name: sha256_json(shape_schema(schema)) for name, schema in sorted(raw_schemas.items())
    }
    full_contract_shape = {"operations": operations, "schemas": shape_schema(raw_schemas)}
    return {
        "format": 1,
        "contract_sha256": sha256_json(document),
        "contract": {
            "operations": dict(sorted(operations.items())),
            "schemas": schemas,
            "shape_sha256": sha256_json(full_contract_shape),
        },
        "generated": {
            "models": sync_models,
            "sync_operations": _surface_manifest(sync),
            "async_operations": _surface_manifest(async_client),
            "response_header_transport": header_transport,
        },
    }


def render_manifest(manifest: dict[str, Any]) -> str:
    return json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--sync-root", type=Path, default=DEFAULT_SYNC_ROOT)
    parser.add_argument("--async-root", type=Path, default=DEFAULT_ASYNC_ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    try:
        expected = render_manifest(
            build_manifest(args.contract, args.sync_root, args.async_root)
        )
    except (OSError, SyntaxError, ValueError) as exc:
        print(f"Python contract-shape manifest failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    if args.check:
        try:
            actual = args.output.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"Python contract-shape manifest is missing: {args.output}", file=sys.stderr)
            raise SystemExit(1) from None
        if actual != expected:
            print(
                "\n".join(
                    difflib.unified_diff(
                        actual.splitlines(),
                        expected.splitlines(),
                        fromfile=str(args.output),
                        tofile=f"{args.output} (regenerated)",
                        lineterm="",
                    )
                ),
                file=sys.stderr,
            )
            print(
                "Run `python3 scripts/generate_python_contract_manifest.py` and review the "
                "schema/signature delta.",
                file=sys.stderr,
            )
            raise SystemExit(1)
        print(f"Generated Python contract-shape manifest is current: {args.output}")
        return
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(expected, encoding="utf-8")
    print(f"Rendered exact Python contract-shape manifest: {args.output}")


if __name__ == "__main__":
    main()
