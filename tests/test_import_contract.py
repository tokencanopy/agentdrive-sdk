from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.import_agentdrive_contract import ContractImportError, import_contract


class ImportContractTest(unittest.TestCase):
    def _source(self, root: Path) -> Path:
        path = root / "golden.json"
        path.write_text(
            json.dumps(
                {
                    "openapi": "3.1.0",
                    "info": {"title": "AgentDrive", "version": "<PINNED>"},
                    "servers": ["<DEPLOYMENT-DERIVED>"],
                    "x-agentdrive-compatibility-policy": 1,
                    "components": {
                        "securitySchemes": {
                            "BearerAuth": {
                                "type": "http",
                                "scheme": "bearer",
                                "bearerFormat": "AgentDrive API key or JWT",
                            }
                        }
                    },
                    "paths": {
                        "/v0/widgets": {
                            "get": {"operationId": "list_widgets_v0_widgets_get"}
                        }
                    },
                }
            )
            + "\n",
            encoding="utf-8",
        )
        return path

    def test_import_replaces_only_deployment_server_and_records_provenance(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            source = self._source(root)
            output = root / "openapi.json"
            provenance = root / "openapi.provenance.json"

            import_contract(
                source,
                output,
                provenance,
                source_commit="abc123",
            )

            contract = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(
                contract["servers"],
                [
                    {
                        "url": "https://api.agentdrive.run",
                        "description": "AgentDrive public API",
                    }
                ],
            )
            metadata = json.loads(provenance.read_text(encoding="utf-8"))
            self.assertEqual(metadata["source_commit"], "abc123")
            self.assertEqual(
                metadata["source_path"], "tests/openapi.golden.json"
            )
            self.assertIn("source_sha256", metadata)

    def test_import_rejects_a_pre_freeze_contract(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            source = self._source(root)
            document = json.loads(source.read_text(encoding="utf-8"))
            document.pop("x-agentdrive-compatibility-policy")
            source.write_text(json.dumps(document), encoding="utf-8")

            with self.assertRaisesRegex(ContractImportError, "policy"):
                import_contract(
                    source,
                    root / "openapi.json",
                    root / "openapi.provenance.json",
                    source_commit="abc123",
                )


if __name__ == "__main__":
    unittest.main()
