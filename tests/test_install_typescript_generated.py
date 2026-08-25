from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.install_typescript_generated import install


class InstallTypeScriptGeneratedTests(unittest.TestCase):
    def test_replaces_only_generated_namespace(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generated = root / "openapi"
            package = root / "package"
            source = generated / "src"
            (source / "apis").mkdir(parents=True)
            (source / "models").mkdir()
            (source / "index.ts").write_text("export * from './runtime';\n", encoding="utf-8")
            (source / "runtime.ts").write_text("export const generated = true;\n", encoding="utf-8")
            (source / "apis" / "index.ts").write_text("export {};\n", encoding="utf-8")
            (source / "models" / "index.ts").write_text("export {};\n", encoding="utf-8")
            (package / "src" / "facade").mkdir(parents=True)
            (package / "src" / "facade" / "marker.ts").write_text("handwritten\n", encoding="utf-8")
            (package / "src" / "generated").mkdir()
            (package / "src" / "generated" / "stale.ts").write_text("stale\n", encoding="utf-8")

            install(generated, package)

            self.assertEqual(
                (package / "src" / "facade" / "marker.ts").read_text(encoding="utf-8"),
                "handwritten\n",
            )
            self.assertFalse((package / "src" / "generated" / "stale.ts").exists())
            self.assertEqual(
                (package / "src" / "generated" / "runtime.ts").read_text(encoding="utf-8"),
                "export const generated = true;\n",
            )

    def test_rejects_incomplete_output_before_replacing_current_core(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generated = root / "openapi"
            package = root / "package"
            (generated / "src").mkdir(parents=True)
            current = package / "src" / "generated" / "runtime.ts"
            current.parent.mkdir(parents=True)
            current.write_text("current\n", encoding="utf-8")

            with self.assertRaises(SystemExit):
                install(generated, package)

            self.assertEqual(current.read_text(encoding="utf-8"), "current\n")


if __name__ == "__main__":
    unittest.main()
