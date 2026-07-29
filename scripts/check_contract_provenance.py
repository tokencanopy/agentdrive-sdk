"""Verify the committed SDK contract against its source and generator provenance."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Dict

from scripts.import_agentdrive_contract import (
    SDK_SERVER,
    SOURCE_PATH,
    SOURCE_REPOSITORY,
)

EXPECTED_PROVENANCE_KEYS = frozenset(
    {
        "generator_image",
        "source_commit",
        "source_path",
        "source_repository",
        "source_sha256",
    }
)


class ProvenanceError(ValueError):
    pass


def _canonical_bytes(document: Dict[str, Any]) -> bytes:
    return (json.dumps(document, indent=2, sort_keys=True) + "\n").encode()


def check_contract_provenance(
    contract_path: Path,
    provenance_path: Path,
    generator_pin_path: Path,
) -> None:
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    generator_image = generator_pin_path.read_text(encoding="utf-8").strip()

    if set(provenance) != EXPECTED_PROVENANCE_KEYS:
        raise ProvenanceError(
            "provenance keys must be exactly "
            f"{sorted(EXPECTED_PROVENANCE_KEYS)}"
        )
    if provenance["source_repository"] != SOURCE_REPOSITORY:
        raise ProvenanceError("source_repository is not canonical")
    if provenance["source_path"] != SOURCE_PATH:
        raise ProvenanceError("source_path is not canonical")
    if not re.fullmatch(r"[0-9a-f]{40}", provenance["source_commit"]):
        raise ProvenanceError("source_commit must be a full lowercase Git SHA")
    if not generator_image or provenance["generator_image"] != generator_image:
        raise ProvenanceError(
            "generator_image does not match sdk/openapi-generator-image.txt"
        )
    if contract.get("servers") != [SDK_SERVER]:
        raise ProvenanceError("SDK contract does not contain the canonical server")

    reconstructed_source = copy.deepcopy(contract)
    reconstructed_source["servers"] = ["<DEPLOYMENT-DERIVED>"]
    actual_digest = hashlib.sha256(
        _canonical_bytes(reconstructed_source)
    ).hexdigest()
    if provenance["source_sha256"] != actual_digest:
        raise ProvenanceError(
            "source_sha256 does not match the committed SDK contract"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--contract", type=Path, default=Path("sdk/openapi.json")
    )
    parser.add_argument(
        "--provenance",
        type=Path,
        default=Path("sdk/openapi.provenance.json"),
    )
    parser.add_argument(
        "--generator-pin",
        type=Path,
        default=Path("sdk/openapi-generator-image.txt"),
    )
    args = parser.parse_args()
    check_contract_provenance(
        args.contract, args.provenance, args.generator_pin
    )
    print("SDK contract provenance and generator pin are consistent.")


if __name__ == "__main__":
    main()
