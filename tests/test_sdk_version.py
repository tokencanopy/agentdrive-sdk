from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


EXPECTED_VERSION = "0.0.3"
ROOT = Path(__file__).resolve().parents[1]


class SdkVersionTest(unittest.TestCase):
    def test_all_published_sdk_metadata_share_one_version(self):
        python_init = (ROOT / "sdk/python/agentdrive_sdk/__init__.py").read_text()
        python_project = (ROOT / "sdk/python/pyproject.toml").read_text()
        typescript_package = json.loads(
            (ROOT / "sdk/typescript/package.json").read_text()
        )
        typescript_lock = json.loads(
            (ROOT / "sdk/typescript/package-lock.json").read_text()
        )
        go_readme = (ROOT / "sdk/go/README.md").read_text()
        generate_script = (ROOT / "scripts/generate-sdks.sh").read_text()

        self.assertRegex(python_init, rf'__version__ = "{re.escape(EXPECTED_VERSION)}"')
        self.assertRegex(
            python_project,
            re.compile(rf'^version = "{re.escape(EXPECTED_VERSION)}"$', re.MULTILINE),
        )
        self.assertEqual(typescript_package["version"], EXPECTED_VERSION)
        self.assertEqual(typescript_lock["packages"][""]["version"], EXPECTED_VERSION)
        self.assertRegex(
            go_readme,
            re.compile(
                rf'^- Package version: {re.escape(EXPECTED_VERSION)}$',
                re.MULTILINE,
            ),
        )
        # The generator's own default, which CI regenerates with because it
        # sets no SDK_VERSION. Left behind, every committed metadata file says
        # the new version and regeneration rewrites them to the old one -- so
        # the freshness check fails and names generated files rather than the
        # one stale default that caused it.
        self.assertRegex(
            generate_script,
            re.compile(
                rf'^VERSION="\$\{{SDK_VERSION:-{re.escape(EXPECTED_VERSION)}\}}"$',
                re.MULTILINE,
            ),
        )


if __name__ == "__main__":
    unittest.main()
