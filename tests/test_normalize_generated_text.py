from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.normalize_generated_text import normalize_generated_text
from scripts.patch_typescript_codegen import patch_typescript_codegen


class NormalizeGeneratedTextTest(unittest.TestCase):
    def test_strips_trailing_whitespace_and_extra_eof_blanks(self):
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "generated.ts"
            path.write_text("export const value = 1;  \n\t\n\n", encoding="utf-8")

            normalize_generated_text([path.parent])

            self.assertEqual(
                path.read_text(encoding="utf-8"),
                "export const value = 1;\n",
            )

    def test_binary_files_are_left_unchanged(self):
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "fixture.bin"
            original = b"\x00binary  \n"
            path.write_bytes(original)

            normalize_generated_text([path.parent])

            self.assertEqual(path.read_bytes(), original)

    def test_typescript_free_form_multipart_serializer_is_qualified(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            api_dir = root / "src" / "apis"
            api_dir.mkdir(parents=True)
            (api_dir / "ArtifactsApi.ts").write_text(
                "import * as runtime from '../runtime';\n"
                "const encoded = objectToJSON(value);\n",
                encoding="utf-8",
            )
            runtime = root / "src" / "runtime.ts"
            runtime.write_text("export const BASE_PATH = '';\n", encoding="utf-8")

            patch_typescript_codegen(root)
            patch_typescript_codegen(root)

            self.assertIn("runtime.objectToJSON(value)", (api_dir / "ArtifactsApi.ts").read_text())
            self.assertEqual(
                (runtime.read_text()).count("export function objectToJSON("),
                1,
            )


if __name__ == "__main__":
    unittest.main()
