"""Render/check the deterministic Python generated-core API reference."""

from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path
from typing import Any

try:
    from scripts.check_python_generated_contract import validate_generated_contract
    from scripts.openapi_sdk_contract import (
        iter_operations,
        load_document,
        media_schemas,
        merged_parameters,
        ref_name,
        resolve_local_ref,
        schema_label,
        sha256_json,
    )
except ModuleNotFoundError:  # direct `python scripts/...py` execution
    from check_python_generated_contract import validate_generated_contract
    from openapi_sdk_contract import (
        iter_operations,
        load_document,
        media_schemas,
        merged_parameters,
        ref_name,
        resolve_local_ref,
        schema_label,
        sha256_json,
    )

DEFAULT_CONTRACT = Path("sdk/openapi.json")
DEFAULT_PROVENANCE = Path("sdk/openapi.provenance.json")
DEFAULT_OUTPUT = Path("docs/python-sdk-api-reference.md")
DEFAULT_SYNC_API = Path("sdk/python/src/agentdrive_sdk/generated/sync/api")
DEFAULT_ASYNC_API = Path("sdk/python/src/agentdrive_sdk/generated/async_client/api")


def _text(value: Any) -> str:
    return " ".join(str(value or "").split())


def _cell(value: Any) -> str:
    return _text(value).replace("|", "\\|").replace("`", "\\`") or "—"


def _anchor(name: str) -> str:
    return "model-" + "".join(char.lower() if char.isalnum() else "-" for char in name).strip("-")


def _inline_anchor(schema: Any) -> str:
    label = schema_label(schema)
    slug = "".join(char.lower() if char.isalnum() else "-" for char in label).strip("-")
    return f"inline-schema-{slug}"


def _schema(schema: Any, *, link_inline: bool = True) -> str:
    name = ref_name(schema)
    if name:
        return f"[`{name}`](#{_anchor(name)})"
    if not isinstance(schema, dict):
        return "`none`"
    if isinstance(schema.get("anyOf"), list):
        return " or ".join(_schema(item, link_inline=link_inline) for item in schema["anyOf"])
    if isinstance(schema.get("oneOf"), list):
        return "one of: " + ", ".join(
            _schema(item, link_inline=link_inline) for item in schema["oneOf"]
        )
    if isinstance(schema.get("allOf"), list):
        return "all of: " + ", ".join(
            _schema(item, link_inline=link_inline) for item in schema["allOf"]
        )
    if schema.get("type") == "array":
        return f"`array` of {_schema(schema.get('items', {}), link_inline=link_inline)}"
    label = schema_label(schema)
    if link_inline and (schema.get("type") == "object" or "properties" in schema):
        return f"[`{_cell(label)}`](#{_inline_anchor(schema)})"
    return f"`{_cell(label)}`"


def _schema_children(schema: Any) -> list[dict[str, Any]]:
    if not isinstance(schema, dict):
        return []
    children: list[dict[str, Any]] = []
    properties = schema.get("properties", {})
    if isinstance(properties, dict):
        children.extend(item for item in properties.values() if isinstance(item, dict))
    items = schema.get("items")
    if isinstance(items, dict):
        children.append(items)
    additional = schema.get("additionalProperties")
    if isinstance(additional, dict):
        children.append(additional)
    for keyword in ("allOf", "anyOf", "oneOf", "prefixItems"):
        alternatives = schema.get(keyword, [])
        if isinstance(alternatives, list):
            children.extend(item for item in alternatives if isinstance(item, dict))
    return children


def _inline_schemas(contract: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Collect every anonymous object schema reachable from the public contract."""

    result: dict[str, dict[str, Any]] = {}

    def visit(schema: Any) -> None:
        if not isinstance(schema, dict) or ref_name(schema):
            return
        if schema.get("type") == "object" or "properties" in schema:
            result.setdefault(schema_label(schema), schema)
        for child in _schema_children(schema):
            visit(child)

    schemas = contract.get("components", {}).get("schemas", {})
    if isinstance(schemas, dict):
        for schema in schemas.values():
            # The named component itself is rendered under Models. Its anonymous
            # nested objects still need their own linkable definition.
            for child in _schema_children(schema):
                visit(child)

    for _path, _method, path_item, operation in iter_operations(contract):
        for parameter in merged_parameters(contract, path_item, operation):
            visit(parameter.get("schema", {}))
        request_body = resolve_local_ref(contract, operation.get("requestBody", {}))
        if isinstance(request_body, dict):
            for schema in media_schemas(request_body.get("content", {})).values():
                visit(schema)
        for raw_response in operation.get("responses", {}).values():
            response = resolve_local_ref(contract, raw_response)
            if isinstance(response, dict):
                for schema in media_schemas(response.get("content", {})).values():
                    visit(schema)
    return result


def _append_object_fields(lines: list[str], schema: dict[str, Any]) -> None:
    properties = schema.get("properties", {})
    required = set(schema.get("required", []))
    if isinstance(properties, dict) and properties:
        lines.extend(
            [
                "| Field | Required | Schema | Description |",
                "|---|:---:|---|---|",
            ]
        )
        for property_name, property_schema in sorted(properties.items()):
            lines.append(
                "| `{}` | {} | {} | {} |".format(
                    _cell(property_name),
                    "yes" if property_name in required else "no",
                    _schema(property_schema),
                    _cell(
                        property_schema.get("description")
                        if isinstance(property_schema, dict)
                        else ""
                    ),
                )
            )
        lines.append("")
    else:
        lines.extend([f"Schema type: {_schema(schema, link_inline=False)}", ""])

    if "additionalProperties" in schema:
        additional = schema["additionalProperties"]
        if additional is True:
            detail = "allowed (any JSON value)"
        elif additional is False:
            detail = "not allowed"
        else:
            detail = f"allowed values matching {_schema(additional)}"
        lines.extend([f"Additional properties: {detail}.", ""])


def _response_sort_key(value: str) -> tuple[int, str]:
    return (int(value), value) if value.isdigit() else (10_000, value)


def render_reference(
    contract: dict[str, Any],
    sync_surface: dict[str, dict[str, Any]],
    async_surface: dict[str, dict[str, Any]],
    provenance: dict[str, Any] | None = None,
) -> str:
    operations = list(iter_operations(contract))
    authenticated = sum(bool(operation.get("security")) for *_, operation in operations)
    lines = [
        "<!-- Generated by scripts/generate_python_api_reference.py; do not edit. -->",
        "# AgentDrive Python generated-core API reference",
        "",
        "This reference describes the exact OpenAPI wire surface wrapped by both the",
        "synchronous and asynchronous generated Python cores. The ergonomic SDK facade",
        "is documented separately. Callable signatures and docstrings below are parsed",
        "from the committed generated source; the reference check fails if either client",
        "is absent or drifts from the contract.",
        "",
        f"- Contract SHA-256: `{sha256_json(contract)}`",
        f"- Operations: **{len(operations)}** ({authenticated} bearer-authenticated, "
        f"{len(operations) - authenticated} anonymous)",
    ]
    if provenance:
        lines.extend(
            [
                f"- AgentDrive source commit: `{_text(provenance.get('source_commit'))}`",
                f"- Generator image: `{_text(provenance.get('generator_image'))}`",
            ]
        )
    lines.extend(["", "## Operations", ""])

    grouped: dict[str, list[tuple[str, str, dict[str, Any], dict[str, Any]]]] = {}
    for item in operations:
        operation = item[3]
        tag = str((operation.get("tags") or ["default"])[0])
        grouped.setdefault(tag, []).append(item)

    for tag in sorted(grouped):
        lines.extend([f"### {tag}", ""])
        for path, method, path_item, operation in sorted(
            grouped[tag], key=lambda item: (item[0], item[1], item[3]["operationId"])
        ):
            operation_id = operation["operationId"]
            lines.extend(
                [
                    f"#### `{operation_id}`",
                    "",
                    f"`{method.upper()} {path}` — {_text(operation.get('summary')) or operation_id}",
                    "",
                    f"Authentication: **{'bearer token' if operation.get('security') else 'anonymous'}**.",
                    "",
                ]
            )
            description = _text(operation.get("description"))
            if description:
                lines.extend([description, ""])

            sync = sync_surface[operation_id]
            async_client = async_surface[operation_id]
            lines.extend(
                [
                    f"Generated API class: `{sync['api_class']}`",
                    "",
                    "Synchronous callables:",
                    "",
                    "```python",
                    sync["primary"].signature,
                    sync["with_http_info"].signature,
                    sync["without_preload_content"].signature,
                    "```",
                    "",
                    "Asynchronous callables:",
                    "",
                    "```python",
                    async_client["primary"].signature,
                    async_client["with_http_info"].signature,
                    async_client["without_preload_content"].signature,
                    "```",
                    "",
                    "Generated docstring:",
                    "",
                    "```text",
                    sync["primary"].docstring or "(empty)",
                    "```",
                    "",
                ]
            )

            parameters = merged_parameters(contract, path_item, operation)
            if parameters:
                lines.extend(
                    [
                        "Request parameters:",
                        "",
                        "| Wire name | In | Required | Schema | Description |",
                        "|---|---|:---:|---|---|",
                    ]
                )
                for parameter in parameters:
                    lines.append(
                        "| `{}` | `{}` | {} | {} | {} |".format(
                            _cell(parameter.get("name")),
                            _cell(parameter.get("in")),
                            "yes" if parameter.get("required") else "no",
                            _schema(parameter.get("schema", {})),
                            _cell(parameter.get("description")),
                        )
                    )
                lines.append("")

            raw_body = resolve_local_ref(contract, operation.get("requestBody", {}))
            if isinstance(raw_body, dict) and raw_body.get("content"):
                lines.extend(
                    [
                        f"Request body ({'required' if raw_body.get('required') else 'optional'}):",
                        "",
                        "| Content type | Schema |",
                        "|---|---|",
                    ]
                )
                for media_type, schema in sorted(media_schemas(raw_body["content"]).items()):
                    lines.append(f"| `{_cell(media_type)}` | {_schema(schema)} |")
                lines.append("")

            lines.extend(
                [
                    "Responses:",
                    "",
                    "| Status | Content | OpenAPI schema | Generated Python type | Headers |",
                    "|---:|---|---|---|---|",
                ]
            )
            for status, raw_response in sorted(
                operation.get("responses", {}).items(), key=lambda item: _response_sort_key(item[0])
            ):
                response = resolve_local_ref(contract, raw_response)
                if not isinstance(response, dict):
                    response = {}
                media = media_schemas(response.get("content", {}))
                content_types = ", ".join(f"`{_cell(item)}`" for item in sorted(media)) or "—"
                schemas = ", ".join(_schema(media[item]) for item in sorted(media)) or "—"
                generated_type = sync["response_types"].get(str(status))
                generated = f"`{_cell(generated_type)}`" if generated_type else "—"
                headers = ", ".join(f"`{_cell(item)}`" for item in sorted(response.get("headers", {}))) or "—"
                lines.append(
                    f"| `{_cell(status)}` | {content_types} | {schemas} | {generated} | {headers} |"
                )
            lines.append("")

    lines.extend(["## Models", ""])
    schemas = contract.get("components", {}).get("schemas", {})
    for name in sorted(schemas):
        schema = schemas[name]
        if not isinstance(schema, dict):
            continue
        lines.extend([f"### {name}", f"<a id=\"{_anchor(name)}\"></a>", ""])
        description = _text(schema.get("description"))
        if description:
            lines.extend([description, ""])
        _append_object_fields(lines, schema)

    inline_schemas = _inline_schemas(contract)
    lines.extend(
        [
            "## Anonymous and inline schemas",
            "",
            "OpenAPI permits request and response objects without a component name.",
            "The generated clients assign Python class names to some of these objects;",
            "the response tables show those generated names, while this section records",
            "their exact wire fields directly from the authoritative contract.",
            "",
        ]
    )
    for label, schema in sorted(inline_schemas.items()):
        lines.extend(
            [
                f"### `{label}`",
                f'<a id="{_inline_anchor(schema)}"></a>',
                "",
            ]
        )
        description = _text(schema.get("description"))
        if description:
            lines.extend([description, ""])
        _append_object_fields(lines, schema)
    return "\n".join(lines).rstrip() + "\n"


def check_output(path: Path, expected: str) -> bool:
    try:
        actual = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"generated API reference is missing: {path}", file=sys.stderr)
        return False
    if actual == expected:
        print(f"Generated Python API reference is current: {path}")
        return True
    diff = difflib.unified_diff(
        actual.splitlines(),
        expected.splitlines(),
        fromfile=str(path),
        tofile=f"{path} (regenerated)",
        lineterm="",
    )
    print("\n".join(diff), file=sys.stderr)
    print(
        "Run `python3 scripts/generate_python_api_reference.py` and commit the result.",
        file=sys.stderr,
    )
    return False


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--provenance", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--sync-api", type=Path, default=DEFAULT_SYNC_API)
    parser.add_argument("--async-api", type=Path, default=DEFAULT_ASYNC_API)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    contract = load_document(args.contract)
    provenance = load_document(args.provenance) if args.provenance.exists() else None
    sync_surface, async_surface = validate_generated_contract(
        args.contract, args.sync_api, args.async_api
    )
    rendered = render_reference(contract, sync_surface, async_surface, provenance)
    if args.check:
        raise SystemExit(0 if check_output(args.output, rendered) else 1)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(
        f"Rendered {args.output} from {args.contract} "
        f"({len(list(iter_operations(contract)))} operations)."
    )


if __name__ == "__main__":
    main()
