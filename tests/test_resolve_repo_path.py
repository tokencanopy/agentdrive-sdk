from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.resolve_repo_path import RepoPathError, resolve_repo_file


class ResolveRepoPathTest(unittest.TestCase):
    def test_repo_relative_file_is_canonicalized(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            spec = root / "sdk" / "openapi.json"
            spec.parent.mkdir()
            spec.write_text("{}\n", encoding="utf-8")

            self.assertEqual(
                resolve_repo_file(root, Path("sdk/../sdk/openapi.json")),
                "sdk/openapi.json",
            )

    def test_parent_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw) / "repo"
            root.mkdir()
            outside = root.parent / "outside.json"
            outside.write_text("{}\n", encoding="utf-8")

            with self.assertRaisesRegex(RepoPathError, "inside the repository"):
                resolve_repo_file(root, Path("../outside.json"))

    def test_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw) / "repo"
            root.mkdir()
            outside = root.parent / "outside.json"
            outside.write_text("{}\n", encoding="utf-8")
            (root / "linked.json").symlink_to(outside)

            with self.assertRaisesRegex(RepoPathError, "inside the repository"):
                resolve_repo_file(root, Path("linked.json"))


if __name__ == "__main__":
    unittest.main()
