from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.check_python_generated_contract import validate_generated_contract
from scripts.generate_python_api_reference import render_reference
from scripts.generate_python_contract_manifest import (
    _check_component_models,
    _headers_transport,
    _model_manifest,
)
from scripts.openapi_sdk_contract import ContractError, load_document, operation_map
from scripts.python_generated_surface import (
    check_surface_against_contract,
    parse_surface,
)


def _contract() -> dict:
    return {
        "openapi": "3.1.0",
        "paths": {
            "/v0/widgets/{widget_id}": {
                "get": {
                    "operationId": "widgets_read",
                    "security": [{"bearerAuth": []}],
                    "parameters": [
                        {
                            "name": "widget_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "authorization",
                            "in": "header",
                            "required": False,
                            "schema": {"anyOf": [{"type": "string"}, {"type": "null"}]},
                        },
                    ],
                    "responses": {
                        "200": {
                            "headers": {"ETag": {"schema": {"type": "string"}}},
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/WidgetOut"}
                                }
                            },
                        },
                        "404": {
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/ErrorOut"}
                                }
                            }
                        },
                    },
                }
            }
        },
        "components": {
            "schemas": {"WidgetOut": {"type": "object"}, "ErrorOut": {"type": "object"}},
            "securitySchemes": {"bearerAuth": {"type": "http", "scheme": "bearer"}},
        },
    }


def _api_source(
    *, asynchronous: bool, include_404: bool = True, include_bogus: bool = False
) -> str:
    prefix = "async " if asynchronous else ""
    responses = (
        "{'200': 'WidgetOut', '404': 'ErrorOut'}"
        if include_404
        else "{'200': 'WidgetOut'}"
    )
    bogus = ", bogus: Optional[StrictStr] = None" if include_bogus else ""
    variants = []
    for suffix in ("", "_with_http_info", "_without_preload_content"):
        variants.append(
            f'''    {prefix}def widgets_read{suffix}(
        self, widget_id: StrictStr, authorization: Optional[StrictStr] = None{bogus},
        _request_timeout: Any = None, _request_auth: Any = None,
        _content_type: Any = None, _headers: Any = None, _host_index: Any = 0
    ) -> WidgetOut:
        """Read one widget."""
        _response_types_map: Dict[str, Optional[str]] = {responses}
        return None
'''
        )
    return (
        "class WidgetsApi:\n"
        + "\n".join(variants)
        + '''
    def _widgets_read_serialize(self, widget_id, authorization):
        _path_params = {}
        _query_params = []
        _header_params = {}
        _form_params = []
        _files = {}
        _body_params = None
        _path_params['widget_id'] = widget_id
        _header_params['authorization'] = authorization
        _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        _auth_settings: List[str] = ['bearerAuth']
        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v0/widgets/{widget_id}',
            auth_settings=_auth_settings,
        )
'''
    )


class PythonGeneratedContractTest(unittest.TestCase):
    def _fixture(self, root: Path) -> tuple[Path, Path, Path]:
        contract_path = root / "openapi.json"
        contract_path.write_text(json.dumps(_contract()), encoding="utf-8")
        sync = root / "sync" / "api"
        async_client = root / "async" / "api"
        sync.mkdir(parents=True)
        async_client.mkdir(parents=True)
        (sync / "widgets_api.py").write_text(
            _api_source(asynchronous=False), encoding="utf-8"
        )
        (async_client / "widgets_api.py").write_text(
            _api_source(asynchronous=True), encoding="utf-8"
        )
        api_response = '''\
from pydantic import BaseModel
class ApiResponse(BaseModel):
    headers: dict[str, str]
'''
        (sync.parent / "api_response.py").write_text(api_response, encoding="utf-8")
        (async_client.parent / "api_response.py").write_text(api_response, encoding="utf-8")
        return contract_path, sync, async_client

    def test_exact_sync_and_async_surfaces_pass(self):
        with tempfile.TemporaryDirectory() as raw:
            sync, async_client = validate_generated_contract(
                *self._fixture(Path(raw))
            )
            self.assertEqual(set(sync), {"widgets_read"})
            self.assertTrue(async_client["widgets_read"]["primary"].is_async)

    def test_missing_response_status_is_detected(self):
        with tempfile.TemporaryDirectory() as raw:
            contract_path, sync, _async_client = self._fixture(Path(raw))
            (sync / "widgets_api.py").write_text(
                _api_source(asynchronous=False, include_404=False), encoding="utf-8"
            )
            document = load_document(contract_path)
            surface = parse_surface(sync, set(operation_map(document)), expected_async=False)
            failures = check_surface_against_contract(document, surface, label="sync")
            self.assertTrue(any("response statuses" in item for item in failures))

    def test_reference_contains_exact_dual_signatures_and_generated_docstring(self):
        with tempfile.TemporaryDirectory() as raw:
            contract_path, sync_path, async_path = self._fixture(Path(raw))
            sync, async_client = validate_generated_contract(
                contract_path, sync_path, async_path
            )
            rendered = render_reference(
                load_document(contract_path), sync, async_client
            )
            self.assertIn(
                "def widgets_read(widget_id: StrictStr, "
                "authorization: Optional[StrictStr] = None, "
                "_request_timeout: Any = None",
                rendered,
            )
            self.assertIn("async def widgets_read_with_http_info", rendered)
            self.assertIn("Generated docstring:\n\n```text\nRead one widget.", rendered)
            self.assertEqual(rendered, render_reference(load_document(contract_path), sync, async_client))

    def test_missing_callable_is_detected(self):
        with tempfile.TemporaryDirectory() as raw:
            contract_path, sync, async_client = self._fixture(Path(raw))
            source = (sync / "widgets_api.py").read_text(encoding="utf-8")
            source = source.replace("def widgets_read_with_http_info", "def _missing_with_http_info")
            (sync / "widgets_api.py").write_text(source, encoding="utf-8")
            with self.assertRaisesRegex(ContractError, "missing generated callables"):
                validate_generated_contract(contract_path, sync, async_client)

    def test_extra_public_parameter_is_detected_in_every_client_variant(self):
        with tempfile.TemporaryDirectory() as raw:
            contract_path, sync, async_client = self._fixture(Path(raw))
            (sync / "widgets_api.py").write_text(
                _api_source(asynchronous=False, include_bogus=True), encoding="utf-8"
            )
            (async_client / "widgets_api.py").write_text(
                _api_source(asynchronous=True, include_bogus=True), encoding="utf-8"
            )
            with self.assertRaisesRegex(ContractError, "public parameters differ"):
                validate_generated_contract(contract_path, sync, async_client)

    def test_model_manifest_hash_captures_requiredness_nullability_and_constraints(self):
        with tempfile.TemporaryDirectory() as raw:
            models = Path(raw)
            path = models / "widget_in.py"
            path.write_text(
                "class WidgetIn:\n"
                "    name: Annotated[str, Field(min_length=1)]\n"
                "    note: Optional[str] = None\n",
                encoding="utf-8",
            )
            before = _model_manifest(models)["WidgetIn"]
            path.write_text(
                "class WidgetIn:\n"
                "    name: Annotated[str, Field(min_length=2)]\n"
                "    note: str\n",
                encoding="utf-8",
            )
            after = _model_manifest(models)["WidgetIn"]
            self.assertNotEqual(before["class_ast_sha256"], after["class_ast_sha256"])
            self.assertTrue(before["fields"]["name"]["required"])
            self.assertFalse(before["fields"]["note"]["required"])
            self.assertTrue(after["fields"]["note"]["required"])

    def test_component_model_check_compares_fields_requiredness_and_nullability(self):
        document = {
            "components": {
                "schemas": {
                    "WidgetIn": {
                        "type": "object",
                        "required": ["name"],
                        "properties": {
                            "name": {"type": "string"},
                            "note": {
                                "anyOf": [{"type": "string"}, {"type": "null"}]
                            },
                        },
                    }
                }
            }
        }
        model = {
            "WidgetIn": {
                "fields": {
                    "name": {"annotation": "str", "required": True},
                    "note": {"annotation": "Optional[str]", "required": False},
                }
            }
        }
        _check_component_models(document, model, label="test")
        model["WidgetIn"]["fields"]["note"]["annotation"] = "str"
        with self.assertRaisesRegex(ValueError, "nullable annotation"):
            _check_component_models(document, model, label="test")

    def test_header_transport_requires_generic_carrier_and_raw_forwarding(self):
        with tempfile.TemporaryDirectory() as raw:
            package = Path(raw)
            (package / "api_response.py").write_text(
                "class ApiResponse:\n    headers: Mapping[str, str]\n",
                encoding="utf-8",
            )
            (package / "api_client.py").write_text(
                "def response_deserialize(response_data):\n"
                "    return ApiResponse(headers=response_data.headers)\n",
                encoding="utf-8",
            )
            shape = _headers_transport(package)
            self.assertEqual(shape["api_response_headers_annotation"], ["Mapping[str, str]"])
            self.assertTrue(shape["response_deserialize_forwards_all_headers"])


if __name__ == "__main__":
    unittest.main()
