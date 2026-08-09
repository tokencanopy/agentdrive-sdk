from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.check_openapi_compatibility import _reset_matches, compare_contracts
from scripts.openapi_sdk_contract import sha256_json


def contract() -> dict:
    return {
        "openapi": "3.1.0",
        "servers": [{"url": "https://api.agentdrive.run"}],
        "components": {
            "schemas": {
                "CreateIn": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["name"],
                    "properties": {
                        "name": {"type": "string"},
                        "role": {"type": "string", "enum": ["reader", "writer"]},
                    },
                },
                "WidgetOut": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["id", "state"],
                    "properties": {
                        "id": {"type": "string"},
                        "state": {"type": "string", "enum": ["ready"]},
                    },
                },
            },
            "securitySchemes": {"bearerAuth": {"type": "http", "scheme": "bearer"}},
        },
        "paths": {
            "/v0/widgets": {
                "post": {
                    "operationId": "widgets_create",
                    "security": [{"bearerAuth": []}],
                    "parameters": [
                        {
                            "name": "Idempotency-Key",
                            "in": "header",
                            "required": False,
                            "schema": {"type": "string"},
                        }
                    ],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/CreateIn"}
                            }
                        },
                    },
                    "responses": {
                        "201": {
                            "headers": {
                                "ETag": {"schema": {"type": "string"}}
                            },
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/WidgetOut"}
                                }
                            },
                        }
                    },
                }
            }
        },
    }


class OpenApiCompatibilityTest(unittest.TestCase):
    def test_additive_response_fields_and_enum_values_are_compatible(self):
        old = contract()
        new = copy.deepcopy(old)
        output = new["components"]["schemas"]["WidgetOut"]
        output["properties"]["future"] = {"type": "integer"}
        output["properties"]["state"]["enum"].append("future-state")

        self.assertEqual(compare_contracts(old, new), [])

    def test_removed_operation_is_breaking(self):
        old = contract()
        new = copy.deepcopy(old)
        new["paths"] = {}

        self.assertIn("removed operationId widgets_create", compare_contracts(old, new))

    def test_new_required_request_field_and_removed_enum_value_are_breaking(self):
        old = contract()
        new = copy.deepcopy(old)
        request = new["components"]["schemas"]["CreateIn"]
        request["properties"]["tenant"] = {"type": "string"}
        request["required"].append("tenant")
        request["properties"]["role"]["enum"].remove("writer")

        failures = "\n".join(compare_contracts(old, new))
        self.assertIn("new required request properties ['tenant']", failures)
        self.assertIn("request enum removed", failures)

    def test_removed_response_field_status_header_and_media_are_breaking(self):
        old = contract()
        variants = []
        for mutation in ("field", "status", "header", "media"):
            new = copy.deepcopy(old)
            response = new["paths"]["/v0/widgets"]["post"]["responses"]["201"]
            if mutation == "field":
                del new["components"]["schemas"]["WidgetOut"]["properties"]["id"]
            elif mutation == "status":
                del new["paths"]["/v0/widgets"]["post"]["responses"]["201"]
            elif mutation == "header":
                del response["headers"]["ETag"]
            else:
                del response["content"]["application/json"]
            variants.append("\n".join(compare_contracts(old, new)))

        self.assertIn("response property 'id' was removed", variants[0])
        self.assertIn("removed response status 201", variants[1])
        self.assertIn("removed response header ETag", variants[2])
        self.assertIn("removed response media type application/json", variants[3])

    def test_reset_only_matches_one_exact_reviewed_digest_pair(self):
        old = contract()
        new = copy.deepcopy(old)
        new["paths"] = {}
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "reset.json"
            path.write_text(
                json.dumps(
                    {
                        "format": 1,
                        "from_sha256": sha256_json(old),
                        "to_sha256": sha256_json(new),
                        "reason": "one reviewed reset",
                        "source_commit": "a" * 40,
                    }
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                _reset_matches(path, old, new, source_commit="a" * 40),
                (True, "one reviewed reset"),
            )
            changed_again = copy.deepcopy(new)
            changed_again["info"] = {"title": "unreviewed"}
            self.assertEqual(
                _reset_matches(path, old, changed_again, source_commit="a" * 40)[0],
                False,
            )
            self.assertEqual(
                _reset_matches(path, old, new, source_commit="b" * 40)[0], False
            )


if __name__ == "__main__":
    unittest.main()
