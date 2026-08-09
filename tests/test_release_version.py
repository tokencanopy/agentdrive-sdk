from __future__ import annotations

import unittest
from pathlib import Path

from scripts.check_release_version import check_release_version


class ReleaseVersionTest(unittest.TestCase):
    def test_repository_metadata_matches_dispatch_and_release_inputs(self):
        version = Path("sdk/SDK_VERSION").read_text(encoding="utf-8").strip()
        self.assertEqual(
            check_release_version(Path("."), version, event="workflow_dispatch"),
            version,
        )
        self.assertEqual(check_release_version(Path("."), f"v{version}", event="release"), version)

    def test_release_tag_requires_v_prefix(self):
        version = Path("sdk/SDK_VERSION").read_text(encoding="utf-8").strip()
        with self.assertRaisesRegex(ValueError, "exact form vX.Y.Z"):
            check_release_version(Path("."), version, event="release")

    def test_requested_version_must_match_every_package(self):
        with self.assertRaisesRegex(ValueError, "does not match metadata"):
            check_release_version(Path("."), "9.9.9", event="workflow_dispatch")


if __name__ == "__main__":
    unittest.main()
