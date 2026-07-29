#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

status="$(git status --porcelain=v1 --untracked-files=all)"
if [[ -n "$status" ]]; then
  echo "Generated SDKs are stale or contain untracked output:" >&2
  echo "$status" >&2
  exit 1
fi

echo "Generated SDK worktree is clean, including untracked files."
