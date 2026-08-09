from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.patch_python_transports import (
    patch_async_redirects,
    patch_sync_redirects,
)


class PatchPythonTransportsTest(unittest.TestCase):
    def test_sync_requests_disable_redirects_at_all_generated_sites(self):
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "rest.py"
            site = """\
        response = pool.request(
            preload_content=False
        )
"""
            path.write_text(site * 6, encoding="utf-8")

            patch_sync_redirects(path)
            patch_sync_redirects(path)

            text = path.read_text(encoding="utf-8")
            self.assertEqual(text.count("redirect=False"), 6)
            self.assertEqual(text.count("preload_content=False"), 6)

    def test_async_client_disables_redirects_explicitly(self):
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "rest.py"
            path.write_text(
                "return httpx.AsyncClient(\n"
                "            trust_env=True\n"
                "        )\n",
                encoding="utf-8",
            )

            patch_async_redirects(path)
            patch_async_redirects(path)

            text = path.read_text(encoding="utf-8")
            self.assertEqual(text.count("follow_redirects=False"), 1)


if __name__ == "__main__":
    unittest.main()
