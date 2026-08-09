"""Apply deterministic security policy to generated Python transports."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


class TransportPatchError(ValueError):
    pass


def patch_sync_redirects(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if text.count("redirect=False") == 6:
        return
    if "redirect=False" in text:
        raise TransportPatchError("sync redirect patch is only partially applied")

    pattern = re.compile(
        r"^(?P<indent>[ \t]*)preload_content=False,?[ \t]*$",
        re.MULTILINE,
    )
    patched, count = pattern.subn(
        lambda match: (
            f'{match.group("indent")}preload_content=False,\n'
            f'{match.group("indent")}redirect=False,'
        ),
        text,
    )
    if count != 6:
        raise TransportPatchError(
            f"expected six urllib3 request sites, found {count}"
        )
    path.write_text(patched, encoding="utf-8")


def patch_async_redirects(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if text.count("follow_redirects=False") == 1:
        return
    if "follow_redirects=" in text:
        raise TransportPatchError("async redirect policy is unexpected")

    marker = "            trust_env=True\n        )"
    replacement = (
        "            trust_env=True,\n"
        "            follow_redirects=False\n"
        "        )"
    )
    if text.count(marker) != 1:
        raise TransportPatchError("expected one generated httpx client constructor")
    path.write_text(text.replace(marker, replacement), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sync_rest", type=Path)
    parser.add_argument("async_rest", type=Path)
    args = parser.parse_args()
    patch_sync_redirects(args.sync_rest)
    patch_async_redirects(args.async_rest)


if __name__ == "__main__":
    main()
