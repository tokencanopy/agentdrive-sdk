from __future__ import annotations

import unittest

from scripts.prepare_codegen_contract import normalize_for_codegen


class PrepareCodegenContractTest(unittest.TestCase):
    def test_openapi_31_nullable_anyof_is_preserved(self):
        document = {
            "paths": {},
            "components": {
                "schemas": {
                    "Widget": {
                        "type": "object",
                        "properties": {
                            "label": {
                                "anyOf": [
                                    {"type": "string", "maxLength": 64},
                                    {"type": "null"},
                                ]
                            }
                        },
                    }
                }
            },
        }

        normalized = normalize_for_codegen(document)

        self.assertEqual(normalized, document)

    def test_openapi_31_nullable_type_array_is_preserved(self):
        document = {
            "paths": {},
            "components": {
                "schemas": {
                    "Widget": {
                        "type": "object",
                        "properties": {"label": {"type": ["string", "null"]}},
                    }
                }
            },
        }

        normalized = normalize_for_codegen(document)

        self.assertEqual(normalized, document)

    def test_object_and_array_defaults_are_removed_but_scalars_remain(self):
        document = {
            "paths": {},
            "components": {
                "schemas": {
                    "Options": {
                        "type": "object",
                        "properties": {
                            "mapping": {"type": "object", "default": {}},
                            "enabled": {"type": "boolean", "default": False},
                        },
                    }
                }
            },
        }

        normalized = normalize_for_codegen(document)
        properties = normalized["components"]["schemas"]["Options"]["properties"]

        self.assertNotIn("default", properties["mapping"])
        self.assertEqual(properties["enabled"]["default"], False)

    def test_openapi_31_const_is_preserved(self):
        document = {
            "paths": {},
            "components": {
                "schemas": {
                    "Health": {
                        "type": "object",
                        "properties": {
                            "status": {"type": "string", "const": "ok"}
                        },
                    }
                }
            },
        }

        normalized = normalize_for_codegen(document)

        self.assertEqual(normalized, document)

    def test_go_primitive_union_becomes_interface_value(self):
        document = {
            "paths": {},
            "components": {
                "schemas": {
                    "ValidationIssue": {
                        "type": "object",
                        "properties": {
                            "loc": {
                                "type": "array",
                                "items": {
                                    "anyOf": [
                                        {"type": "string"},
                                        {"type": "integer"},
                                    ]
                                },
                            }
                        },
                    }
                }
            },
        }

        normalized = normalize_for_codegen(document, language="go")

        self.assertEqual(
            normalized["components"]["schemas"]["ValidationIssue"]["properties"][
                "loc"
            ]["items"],
            {},
        )

    def test_go_free_form_nullable_union_becomes_interface_value(self):
        document = {
            "paths": {},
            "components": {
                "schemas": {
                    "ValidationIssue": {
                        "type": "object",
                        "properties": {
                            "input": {
                                "anyOf": [{}, {"type": "null"}]
                            }
                        },
                    }
                }
            },
        }

        normalized = normalize_for_codegen(document, language="go")

        self.assertEqual(
            normalized["components"]["schemas"]["ValidationIssue"]["properties"][
                "input"
            ],
            {},
        )

    def test_typescript_free_form_nullable_union_becomes_unknown_value(self):
        document = {
            "paths": {},
            "components": {
                "schemas": {
                    "ValidationIssue": {
                        "type": "object",
                        "properties": {
                            "input": {
                                "anyOf": [{}, {"type": "null"}]
                            }
                        },
                    }
                }
            },
        }

        normalized = normalize_for_codegen(document, language="typescript")

        self.assertEqual(
            normalized["components"]["schemas"]["ValidationIssue"]["properties"][
                "input"
            ],
            {},
        )


if __name__ == "__main__":
    unittest.main()
