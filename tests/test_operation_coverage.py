from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.check_operation_coverage import (
    CoverageError,
    check_operation_coverage,
    generated_names,
)


class OperationCoverageTest(unittest.TestCase):
    def test_generator_name_conventions_collapse_fastapi_placeholders(self):
        self.assertEqual(
            generated_names("put_artifact_v0_artifacts__path__put"),
            {
                "python": "put_artifact_v0_artifacts_path_put",
                "typescript": "putArtifactV0ArtifactsPathPut",
                "go": "PutArtifactV0ArtifactsPathPut",
            },
        )

    def test_all_three_generated_languages_must_cover_exact_operations(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            spec_path = root / "openapi.json"
            spec_path.write_text(
                json.dumps(
                    {
                        "paths": {
                            "/v0/widgets": {
                                "get": {"operationId": "list_widgets_v0_widgets_get"}
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )
            python_sync_dir = root / "python-sync"
            python_async_dir = root / "python-async"
            typescript_dir = root / "typescript"
            go_dir = root / "go"
            python_sync_dir.mkdir()
            python_async_dir.mkdir()
            typescript_dir.mkdir()
            go_dir.mkdir()
            (python_sync_dir / "widgets_api.py").write_text(
                "class WidgetsApi:\n"
                "    def list_widgets_v0_widgets_get(self):\n"
                "        pass\n",
                encoding="utf-8",
            )
            (python_async_dir / "widgets_api.py").write_text(
                "class WidgetsApi:\n"
                "    async def list_widgets_v0_widgets_get(self):\n"
                "        pass\n",
                encoding="utf-8",
            )
            (typescript_dir / "WidgetsApi.ts").write_text(
                "export class WidgetsApi {\n"
                "  async listWidgetsV0WidgetsGet(): Promise<void> {}\n"
                "}\n",
                encoding="utf-8",
            )
            (go_dir / "api_widgets.go").write_text(
                "func (a *WidgetsAPIService) "
                "ListWidgetsV0WidgetsGet(ctx context.Context) Request {}\n",
                encoding="utf-8",
            )

            check_operation_coverage(
                spec_path,
                python_sync_dir=python_sync_dir,
                python_async_dir=python_async_dir,
                typescript_dir=typescript_dir,
                go_dir=go_dir,
            )

    def test_missing_generated_operation_fails_with_language_and_name(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            spec_path = root / "openapi.json"
            spec_path.write_text(
                json.dumps(
                    {
                        "paths": {
                            "/v0/widgets": {
                                "get": {"operationId": "list_widgets_v0_widgets_get"}
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )
            for name in ("python-sync", "python-async", "typescript", "go"):
                (root / name).mkdir()

            with self.assertRaisesRegex(
                CoverageError,
                "python sync missing.*list_widgets_v0_widgets_get",
            ):
                check_operation_coverage(
                    spec_path,
                    python_sync_dir=root / "python-sync",
                    python_async_dir=root / "python-async",
                    typescript_dir=root / "typescript",
                    go_dir=root / "go",
                )

    def test_language_specific_name_collisions_are_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            spec_path = root / "openapi.json"
            spec_path.write_text(
                json.dumps(
                    {
                        "paths": {
                            "/v0/first": {
                                "get": {"operationId": "get_widget"}
                            },
                            "/v0/second": {
                                "get": {"operationId": "get__widget"}
                            },
                        }
                    }
                ),
                encoding="utf-8",
            )
            for name in ("python-sync", "python-async", "typescript", "go"):
                (root / name).mkdir()

            with self.assertRaisesRegex(
                CoverageError,
                "python sync generated-name collision.*get_widget.*get__widget",
            ):
                check_operation_coverage(
                    spec_path,
                    python_sync_dir=root / "python-sync",
                    python_async_dir=root / "python-async",
                    typescript_dir=root / "typescript",
                    go_dir=root / "go",
                )


if __name__ == "__main__":
    unittest.main()
