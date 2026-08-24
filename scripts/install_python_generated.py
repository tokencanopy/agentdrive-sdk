"""Install OpenAPI Generator's Python package into the isolated namespace.

The generator writes a complete package called ``agentdrive_sdk``.  The
handwritten facade must own the public package, so this installer relocates
only the generated package to ``agentdrive_sdk.generated`` and rewrites its
absolute intra-package imports.  It is intentionally deterministic and is
also used by the one-time migration of the v0.0.1 snapshot.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


def _rewrite_imports(root: Path) -> None:
    for path in sorted(root.rglob("*.py")):
        text = path.read_text(encoding="utf-8")
        rewritten = text.replace("agentdrive_sdk", "agentdrive_sdk.generated")
        if rewritten != text:
            path.write_text(rewritten, encoding="utf-8")


def install(source_root: Path, package_root: Path) -> None:
    source = source_root / "agentdrive_sdk"
    if not source.is_dir():
        raise SystemExit(f"generated Python package not found: {source}")

    target = package_root / "generated"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)
    _rewrite_imports(target)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: install_python_generated.py GENERATED_OUTPUT")
    repo = Path(__file__).resolve().parents[1]
    install(
        Path(sys.argv[1]).resolve(),
        repo / "sdk" / "python" / "agentdrive_sdk",
    )


if __name__ == "__main__":
    main()
