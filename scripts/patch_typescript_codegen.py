"""Apply deterministic compatibility fixes for the pinned TypeScript generator."""

from __future__ import annotations

import re
from pathlib import Path


_UNQUALIFIED_OBJECT_TO_JSON = re.compile(r"(?<![.\w])objectToJSON\(")
_RUNTIME_IMPORT = "import * as runtime from '../runtime';"
_RUNTIME_HELPER = """

/**
 * OpenAPI Generator 7.16 emits this call for free-form multipart objects but
 * does not emit the corresponding helper. Free-form values are already JSON
 * compatible, so the deterministic compatibility implementation is identity.
 */
export function objectToJSON(value: any): any {
    return value;
}
"""


def patch_typescript_codegen(directory: Path) -> None:
    """Make the pinned generator's free-form multipart serializer compile."""

    changed = False
    for path in sorted((directory / "src" / "apis").glob("*.ts")):
        text = path.read_text(encoding="utf-8")
        if not _UNQUALIFIED_OBJECT_TO_JSON.search(text):
            continue
        if _RUNTIME_IMPORT not in text:
            raise ValueError(f"cannot qualify objectToJSON without runtime import: {path}")
        patched = _UNQUALIFIED_OBJECT_TO_JSON.sub("runtime.objectToJSON(", text)
        if patched != text:
            path.write_text(patched, encoding="utf-8")
            changed = True

    if not changed:
        return

    runtime_path = directory / "src" / "runtime.ts"
    runtime = runtime_path.read_text(encoding="utf-8")
    if "export function objectToJSON(" not in runtime:
        runtime_path.write_text(runtime.rstrip() + _RUNTIME_HELPER, encoding="utf-8")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    patch_typescript_codegen(parser.parse_args().directory)
