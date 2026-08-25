"""Install OpenAPI Generator's TypeScript source under the generated namespace."""

from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path


_REQUIRED_PATHS = (
    Path("index.ts"),
    Path("runtime.ts"),
    Path("apis/index.ts"),
    Path("models/index.ts"),
)


def install(source_root: Path, package_root: Path) -> None:
    source = source_root / "src"
    if not source.is_dir():
        raise SystemExit(f"generated TypeScript source not found: {source}")
    missing = [path for path in _REQUIRED_PATHS if not (source / path).is_file()]
    if missing:
        rendered = ", ".join(str(path) for path in missing)
        raise SystemExit(f"generated TypeScript source is incomplete ({rendered}): {source}")

    source_parent = package_root / "src"
    source_parent.mkdir(parents=True, exist_ok=True)
    target = source_parent / "generated"
    with tempfile.TemporaryDirectory(prefix=".generated-install-", dir=source_parent) as temporary:
        staged = Path(temporary) / "generated"
        shutil.copytree(source, staged)
        if target.exists():
            shutil.rmtree(target)
        staged.replace(target)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: install_typescript_generated.py GENERATED_OUTPUT")
    repo = Path(__file__).resolve().parents[1]
    install(
        Path(sys.argv[1]).resolve(),
        repo / "sdk" / "typescript",
    )


if __name__ == "__main__":
    main()
