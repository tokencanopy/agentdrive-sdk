"""Normalize deterministic whitespace in OpenAPI Generator text output."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable


def normalize_generated_text(roots: Iterable[Path]) -> None:
    for root in roots:
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            raw = path.read_bytes()
            if b"\x00" in raw:
                continue
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                continue
            lines = [line.rstrip(" \t") for line in text.splitlines()]
            while lines and not lines[-1]:
                lines.pop()
            normalized = "\n".join(lines)
            if normalized:
                normalized += "\n"
            if normalized != text:
                path.write_text(normalized, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="+", type=Path)
    args = parser.parse_args()
    normalize_generated_text(args.roots)


if __name__ == "__main__":
    main()
