from __future__ import annotations

import unittest
from types import SimpleNamespace

from scripts.generate_python_api_reference import _inline_anchor, render_reference
from scripts.openapi_sdk_contract import schema_label


class PythonApiReferenceTest(unittest.TestCase):
    def test_inline_error_schema_is_linked_and_rendered_with_generated_type(self):
        nested_error = {
            "type": "object",
            "required": ["code", "message"],
            "properties": {
                "code": {"type": "string"},
                "message": {"type": "string"},
            },
        }
        error_envelope = {
            "type": "object",
            "required": ["error"],
            "properties": {"error": nested_error},
        }
        contract = {
            "openapi": "3.1.0",
            "paths": {
                "/v0/things/{thing_id}": {
                    "get": {
                        "operationId": "things_read",
                        "parameters": [
                            {
                                "name": "thing_id",
                                "in": "path",
                                "required": True,
                                "schema": {"type": "string"},
                            }
                        ],
                        "responses": {
                            "400": {
                                "content": {
                                    "application/json": {"schema": error_envelope}
                                }
                            }
                        },
                    }
                }
            },
            "components": {"schemas": {}},
        }
        call = SimpleNamespace(
            signature="def things_read(thing_id: StrictStr) -> ThingsRead400Response",
            docstring="Read one thing.",
        )
        surface = {
            "things_read": {
                "api_class": "ThingsApi",
                "primary": call,
                "with_http_info": call,
                "without_preload_content": call,
                "response_types": {"400": "ThingsRead400Response"},
            }
        }

        rendered = render_reference(contract, surface, surface)
        envelope_label = schema_label(error_envelope)
        nested_label = schema_label(nested_error)

        self.assertIn(
            f"[`{envelope_label}`](#{_inline_anchor(error_envelope)})",
            rendered,
        )
        self.assertIn("`ThingsRead400Response`", rendered)
        self.assertIn(f"### `{nested_label}`", rendered)
        self.assertIn("| `code` | yes | `string` |", rendered)
        self.assertIn("| `message` | yes | `string` |", rendered)


if __name__ == "__main__":
    unittest.main()
