"""Enforce request strictness and response forward compatibility in OAG models.

OpenAPI Generator 7.24 does not faithfully preserve ``additionalProperties:
false`` in generated Pydantic request models, and it emits closed enum
validators for response vocabularies. This deterministic postprocessor applies
the AgentDrive policy without hand-editing generated files:

* request-reachable component models reject unknown fields and retain enums;
* all other generated models ignore additive response fields;
* response enum validators are removed so additive wire values deserialize.
"""

from __future__ import annotations

import argparse
import ast
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    from scripts.openapi_sdk_contract import (
        ContractError,
        load_document,
        model_contexts,
        python_name,
    )
except ModuleNotFoundError:  # direct `python scripts/...py` execution
    from openapi_sdk_contract import ContractError, load_document, model_contexts, python_name

DEFAULT_MODEL_DIRS = (
    Path("sdk/python/src/agentdrive_sdk/generated/sync/models"),
    Path("sdk/python/src/agentdrive_sdk/generated/async_client/models"),
)


@dataclass(frozen=True)
class Replacement:
    start: int
    end: int
    lines: tuple[str, ...]


def _class_node(tree: ast.Module) -> ast.ClassDef:
    classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    if len(classes) != 1:
        raise ContractError(f"expected exactly one generated model class, found {len(classes)}")
    return classes[0]


def _decorated_start(node: ast.FunctionDef | ast.AsyncFunctionDef) -> int:
    return min([node.lineno, *(item.lineno for item in node.decorator_list)])


def _field_validator_name(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str | None:
    for decorator in node.decorator_list:
        if not isinstance(decorator, ast.Call):
            continue
        function = decorator.func
        if not (
            isinstance(function, ast.Name) and function.id == "field_validator"
        ) and not (
            isinstance(function, ast.Attribute) and function.attr == "field_validator"
        ):
            continue
        if decorator.args and isinstance(decorator.args[0], ast.Constant):
            value = decorator.args[0].value
            return value if isinstance(value, str) else None
    return None


def _config_replacement(
    source_lines: list[str], class_node: ast.ClassDef, policy: str
) -> Replacement:
    assignments = [
        node
        for node in class_node.body
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "model_config" for target in node.targets)
    ]
    if len(assignments) != 1:
        raise ContractError(f"{class_node.name}: expected one model_config assignment")
    node = assignments[0]
    if not isinstance(node.value, (ast.Call, ast.Dict)):
        raise ContractError(f"{class_node.name}: unsupported model_config shape")
    block = source_lines[node.lineno - 1 : node.end_lineno]
    joined = "\n".join(block)
    if re.search(r"\bextra\s*=", joined):
        joined = re.sub(r"\bextra\s*=\s*(['\"])(?:forbid|ignore|allow)\1", f'extra="{policy}"', joined)
        return Replacement(node.lineno, node.end_lineno or node.lineno, tuple(joined.splitlines()))
    if isinstance(node.value, ast.Call):
        if node.lineno == node.end_lineno:
            joined = joined.rsplit(")", 1)[0] + f', extra="{policy}")'
            return Replacement(node.lineno, node.end_lineno, (joined,))
        indent = re.match(r"\s*", source_lines[node.lineno - 1]).group(0) + "    "
        block.insert(1, f'{indent}extra="{policy}",')
        return Replacement(node.lineno, node.end_lineno or node.lineno, tuple(block))
    # Dict-form ConfigDict is uncommon in generated models, but preserving it is
    # straightforward and keeps the checker future-proof.
    if node.lineno == node.end_lineno:
        joined = joined.rsplit("}", 1)[0] + f', "extra": "{policy}"}}'
        return Replacement(node.lineno, node.end_lineno, (joined,))
    indent = re.match(r"\s*", source_lines[node.lineno - 1]).group(0) + "    "
    block.insert(1, f'{indent}"extra": "{policy}",')
    return Replacement(node.lineno, node.end_lineno or node.lineno, tuple(block))


def _request_method_replacement(node: ast.FunctionDef) -> Replacement | None:
    if node.name == "to_dict":
        return Replacement(
            node.lineno,
            node.end_lineno or node.lineno,
            (
                "    def to_dict(self) -> Dict[str, Any]:",
                '        """Return the request body using wire aliases."""',
                "        return to_jsonable_python(",
                "            self.model_dump(",
                "                by_alias=True,",
                "                exclude_unset=True,",
                '                exclude={"additional_properties"},',
                "            )",
                "        )",
            ),
        )
    if node.name == "from_dict":
        return Replacement(
            _decorated_start(node),
            node.end_lineno or node.lineno,
            (
                "    @classmethod",
                "    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:",
                '        """Validate a request dictionary without discarding unknown fields."""',
                "        if obj is None:",
                "            return None",
                "        return cls.model_validate(obj)",
            ),
        )
    return None


def _is_nullable(schema: object) -> bool:
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


def _strip_outer_optional(node: ast.AST) -> ast.AST:
    if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name):
        if node.value.id == "Optional":
            return node.slice
        if node.value.id == "Annotated" and isinstance(node.slice, ast.Tuple):
            first, *rest = node.slice.elts
            stripped = _strip_outer_optional(first)
            if ast.dump(stripped) != ast.dump(first):
                return ast.Subscript(
                    value=node.value,
                    slice=ast.Tuple(elts=[stripped, *rest], ctx=ast.Load()),
                    ctx=ast.Load(),
                )
    return node


def _nonnull_field_replacement(node: ast.AnnAssign) -> Replacement | None:
    parsed = ast.parse(ast.unparse(node.annotation), mode="eval").body
    rewritten = ast.fix_missing_locations(_strip_outer_optional(parsed))
    annotation = ast.unparse(rewritten)
    if annotation == ast.unparse(node.annotation):
        return None
    if not isinstance(node.target, ast.Name):
        return None
    line = f"    {node.target.id}: {annotation}"
    if node.value is not None:
        line += f" = {ast.unparse(node.value)}"
    return Replacement(node.lineno, node.end_lineno or node.lineno, (line,))


def _apply_replacements(source_lines: list[str], replacements: list[Replacement]) -> str:
    result = list(source_lines)
    previous_start = len(result) + 1
    for replacement in sorted(replacements, key=lambda item: item.start, reverse=True):
        if replacement.end >= previous_start:
            raise ContractError("overlapping generated-model source replacements")
        result[replacement.start - 1 : replacement.end] = list(replacement.lines)
        previous_start = replacement.start
    return "\n".join(result).rstrip() + "\n"


def transform_model(
    source: str,
    *,
    request_model: bool,
    nonnullable_fields: set[str] | None = None,
) -> str:
    tree = ast.parse(source)
    class_node = _class_node(tree)
    lines = source.splitlines()
    replacements = [
        _config_replacement(lines, class_node, "forbid" if request_model else "ignore")
    ]

    for node in class_node.body:
        if (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id in (nonnullable_fields or set())
        ):
            replacement = _nonnull_field_replacement(node)
            if replacement:
                replacements.append(replacement)
        if request_model:
            if (
                isinstance(node, ast.AnnAssign)
                and isinstance(node.target, ast.Name)
                and node.target.id == "additional_properties"
            ):
                replacements.append(
                    Replacement(node.lineno, node.end_lineno or node.lineno, ())
                )
            if isinstance(node, ast.FunctionDef):
                replacement = _request_method_replacement(node)
                if replacement:
                    replacements.append(replacement)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Every field-validator emitted for a response enum is closed over
            # the contract's current value set. Response vocabularies are open;
            # request models take the opposite policy and never enter this arm.
            if _field_validator_name(node) is not None and node.name.endswith("_validate_enum"):
                replacements.append(
                    Replacement(
                        _decorated_start(node), node.end_lineno or node.lineno, ()
                    )
                )

    return _apply_replacements(lines, replacements)


def _model_files(directory: Path) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in sorted(directory.glob("*.py")):
        if path.name == "__init__.py":
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
        if len(classes) == 1:
            result[classes[0].name] = path
    return result


def process_directory(
    directory: Path,
    *,
    request_models: set[str],
    nonnullable_fields: dict[str, set[str]],
    check: bool,
) -> list[str]:
    files = _model_files(directory)
    missing = sorted(request_models - set(files))
    if missing:
        raise ContractError(f"{directory}: missing request models: {missing}")
    changed: list[str] = []
    for name, path in sorted(files.items()):
        source = path.read_text(encoding="utf-8")
        transformed = transform_model(
            source,
            request_model=name in request_models,
            nonnullable_fields=nonnullable_fields.get(name, set()),
        )
        if transformed == source:
            continue
        changed.append(str(path))
        if check:
            diff = difflib.unified_diff(
                source.splitlines(),
                transformed.splitlines(),
                fromfile=str(path),
                tofile=f"{path} (postprocessed)",
                lineterm="",
            )
            print("\n".join(diff), file=sys.stderr)
        else:
            path.write_text(transformed, encoding="utf-8")
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, default=Path("sdk/openapi.json"))
    parser.add_argument(
        "--models-dir",
        action="append",
        type=Path,
        dest="model_dirs",
        help="generated models directory (repeatable)",
    )
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    document = load_document(args.contract)
    request_models, response_models = model_contexts(document)
    overlap = request_models & response_models
    if overlap:
        raise ContractError(
            "request and response schemas must be split to apply opposite compatibility "
            f"policies: {sorted(overlap)}"
        )

    schemas = document.get("components", {}).get("schemas", {})
    nonnullable_fields = {
        name: {
            python_name(field_name)
            for field_name, field_schema in schema.get("properties", {}).items()
            if not _is_nullable(field_schema)
        }
        for name, schema in schemas.items()
        if isinstance(schema, dict)
    }

    changed: list[str] = []
    for directory in args.model_dirs or DEFAULT_MODEL_DIRS:
        if not directory.is_dir():
            raise ContractError(f"generated model directory is missing: {directory}")
        changed.extend(
            process_directory(
                directory,
                request_models=request_models,
                nonnullable_fields=nonnullable_fields,
                check=args.check,
            )
        )
    if args.check and changed:
        print(
            "Generated Python model policy drifted. Regenerate through the pinned pipeline.",
            file=sys.stderr,
        )
        raise SystemExit(1)
    action = "checked" if args.check else "postprocessed"
    print(
        f"Python generated models {action}: {len(request_models)} strict request schemas; "
        f"{len(response_models)} referenced response schemas."
    )


if __name__ == "__main__":
    main()
