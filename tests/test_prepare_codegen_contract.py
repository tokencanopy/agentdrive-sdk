from __future__ import annotations

import unittest

from scripts.prepare_codegen_contract import normalize_for_codegen


class PrepareCodegenContractTest(unittest.TestCase):
    def test_openapi_31_is_downgraded_for_pinned_generator(self):
        document = {
            "openapi": "3.1.0",
            "paths": {},
        }

        normalized = normalize_for_codegen(document)

        self.assertEqual(normalized["openapi"], "3.0.3")

    def test_openapi_31_nullable_anyof_becomes_nullable_schema(self):
        document = {
            "openapi": "3.1.0",
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

        self.assertEqual(
            normalized["components"]["schemas"]["Widget"]["properties"]["label"],
            {"type": "string", "maxLength": 64, "nullable": True},
        )

    def test_openapi_31_nullable_type_array_becomes_nullable_schema(self):
        document = {
            "openapi": "3.1.0",
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

        self.assertEqual(
            normalized["components"]["schemas"]["Widget"]["properties"]["label"],
            {"type": "string", "nullable": True},
        )

    def test_object_and_array_defaults_are_removed_but_scalars_remain(self):
        document = {
            "openapi": "3.1.0",
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

    def test_openapi_31_const_becomes_single_value_enum(self):
        document = {
            "openapi": "3.1.0",
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

        self.assertEqual(
            normalized["components"]["schemas"]["Health"]["properties"]["status"],
            {"type": "string", "enum": ["ok"]},
        )

    def test_nullable_reference_is_wrapped_for_openapi_30(self):
        document = {
            "openapi": "3.1.0",
            "paths": {},
            "components": {
                "schemas": {
                    "Widget": {
                        "type": "object",
                        "properties": {
                            "owner": {
                                "anyOf": [
                                    {"$ref": "#/components/schemas/Owner"},
                                    {"type": "null"},
                                ]
                            }
                        },
                    }
                }
            },
        }

        normalized = normalize_for_codegen(document)

        self.assertEqual(
            normalized["components"]["schemas"]["Widget"]["properties"]["owner"],
            {
                "allOf": [{"$ref": "#/components/schemas/Owner"}],
                "nullable": True,
            },
        )

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
