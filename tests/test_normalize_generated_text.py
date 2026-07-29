from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.normalize_generated_text import normalize_generated_text


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


if __name__ == "__main__":
    unittest.main()
