"""Import AgentDrive's reviewed OpenAPI snapshot with explicit provenance."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Dict

SDK_SERVER = {
    "url": "https://api.agentdrive.run",
    "description": "AgentDrive public API",
}
SOURCE_REPOSITORY = "https://github.com/tokencanopy/agentdrive"
SOURCE_PATH = "tests/openapi.golden.json"
GENERATOR_IMAGE = "openapitools/openapi-generator-cli:v7.24.0"
HTTP_METHODS = frozenset(
    {"get", "put", "post", "delete", "patch", "head", "options", "trace"}
)


class ContractImportError(ValueError):
    pass


def _validate(document: Dict[str, Any]) -> None:
    if document.get("x-agentdrive-compatibility-policy") != 1:
        raise ContractImportError("source contract lacks compatibility policy version 1")
    if document.get("servers") != ["<DEPLOYMENT-DERIVED>"]:
        raise ContractImportError("source contract lacks the deployment-derived server sentinel")

    leaked = sorted(
        path
        for path in document.get("paths", {})
        if path.startswith(("/web/", "/internal/", "/v1/agenttag"))
    )
    if leaked:
        raise ContractImportError(f"non-SDK paths entered source contract: {leaked}")

    scheme = (
        document.get("components", {})
        .get("securitySchemes", {})
        .get("BearerAuth")
    )
    if (
        not isinstance(scheme, dict)
        or scheme.get("type") != "http"
        or scheme.get("scheme") != "bearer"
        or not scheme.get("bearerFormat")
    ):
        raise ContractImportError("source contract lacks canonical BearerAuth")

    operation_ids = []
    for path_item in document.get("paths", {}).values():
        for method, operation in path_item.items():
            if method in HTTP_METHODS:
                operation_id = operation.get("operationId")
                if not operation_id:
                    raise ContractImportError("source operation lacks operationId")
                operation_ids.append(operation_id)
    if len(operation_ids) != len(set(operation_ids)):
        raise ContractImportError("source contract has duplicate operationIds")


def import_contract(
    source: Path,
    output: Path,
    provenance: Path,
    *,
    source_commit: str,
) -> None:
    source_bytes = source.read_bytes()
    document = json.loads(source_bytes)
    _validate(document)
    document["servers"] = [SDK_SERVER]
    output.write_text(
        json.dumps(document, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    provenance.write_text(
        json.dumps(
            {
                "generator_image": GENERATOR_IMAGE,
                "source_commit": source_commit,
                "source_path": SOURCE_PATH,
                "source_repository": SOURCE_REPOSITORY,
                "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--output", type=Path, default=Path("sdk/openapi.json"))
    parser.add_argument(
        "--provenance",
        type=Path,
        default=Path("sdk/openapi.provenance.json"),
    )
    args = parser.parse_args()
    import_contract(
        args.source,
        args.output,
        args.provenance,
        source_commit=args.source_commit,
    )
    print(
        f"Imported {SOURCE_REPOSITORY}@{args.source_commit}:{SOURCE_PATH} "
        f"to {args.output}."
    )


if __name__ == "__main__":
    main()
