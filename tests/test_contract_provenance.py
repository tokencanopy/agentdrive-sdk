from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.check_contract_provenance import (
    ProvenanceError,
    check_contract_provenance,
)
from scripts.import_agentdrive_contract import (
    GENERATOR_IMAGE,
    SDK_SERVER,
    SOURCE_PATH,
    SOURCE_REPOSITORY,
)


class ContractProvenanceTest(unittest.TestCase):
    def _fixture(self, root: Path) -> tuple[Path, Path, Path]:
        source = {
            "openapi": "3.1.0",
            "servers": ["<DEPLOYMENT-DERIVED>"],
            "paths": {"/v0/widgets": {"get": {"operationId": "list_widgets"}}},
        }
        source_bytes = (
            json.dumps(source, indent=2, sort_keys=True) + "\n"
        ).encode()
        contract = copy.deepcopy(source)
        contract["servers"] = [SDK_SERVER]

        contract_path = root / "openapi.json"
        contract_path.write_text(
            json.dumps(contract, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        provenance_path = root / "openapi.provenance.json"
        provenance_path.write_text(
            json.dumps(
                {
                    "generator_image": GENERATOR_IMAGE,
                    "source_commit": "a" * 40,
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
        pin_path = root / "generator-image.txt"
        pin_path.write_text(GENERATOR_IMAGE + "\n", encoding="utf-8")
        return contract_path, provenance_path, pin_path

    def test_exact_contract_and_generator_provenance_pass(self):
        with tempfile.TemporaryDirectory() as raw:
            paths = self._fixture(Path(raw))
            check_contract_provenance(*paths)

    def test_contract_edit_with_stale_source_digest_fails(self):
        with tempfile.TemporaryDirectory() as raw:
            contract_path, provenance_path, pin_path = self._fixture(Path(raw))
            contract = json.loads(contract_path.read_text(encoding="utf-8"))
            contract["info"] = {"title": "hand edited"}
            contract_path.write_text(json.dumps(contract), encoding="utf-8")

            with self.assertRaisesRegex(ProvenanceError, "source_sha256"):
                check_contract_provenance(
                    contract_path, provenance_path, pin_path
                )

    def test_generator_pin_drift_fails(self):
        with tempfile.TemporaryDirectory() as raw:
            contract_path, provenance_path, pin_path = self._fixture(Path(raw))
            pin_path.write_text("openapitools/openapi-generator-cli:v0.0.0\n")

            with self.assertRaisesRegex(ProvenanceError, "generator_image"):
                check_contract_provenance(
                    contract_path, provenance_path, pin_path
                )


if __name__ == "__main__":
    unittest.main()
