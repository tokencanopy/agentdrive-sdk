#!/usr/bin/env bash
# Generate the Python / TypeScript / Go SDKs from the AgentDrive OpenAPI spec.
#
# Usage: scripts/generate-sdks.sh [path-to-openapi.json]
# Requires: Java (for openapi-generator) + Node (npx). CI provides both.
set -euo pipefail

SPEC="${1:-sdk/openapi.json}"
VERSION="${SDK_VERSION:-0.0.1}"
GIT_HOST="github.com"
GIT_USER="tokencanopy"
GIT_REPO="agentdrive-sdk"
GEN="npx --yes @openapitools/openapi-generator-cli@latest generate"

echo "Generating SDKs from ${SPEC} (version ${VERSION})"

# openapi-generator's Go templates emit invalid code for object/array `default`
# values (e.g. `var options CompileOptions = {wait=false}`). Strip those defaults
# into a sanitized spec used for generation; scalar defaults are left intact.
CLEAN_SPEC="$(dirname "$SPEC")/.openapi.clean.json"
python3 - "$SPEC" "$CLEAN_SPEC" <<'PY'
import json, sys
src, dst = sys.argv[1], sys.argv[2]
d = json.load(open(src))

# 1. Drop internal-only endpoints so the public SDKs never ship clients for them.
#    (Belt-and-suspenders: these are also being removed from the live public
#    OpenAPI schema upstream.)
paths = d.get("paths", {})
dropped = [p for p in paths if p.startswith("/internal/")]
for p in dropped:
    del paths[p]

# 2. openapi-generator's Go templates emit invalid code for object/array `default`
#    values (e.g. `var options CompileOptions = {wait=false}`). Strip those;
#    scalar defaults are left intact.
def walk(o):
    if isinstance(o, dict):
        if isinstance(o.get("default"), (dict, list)):
            del o["default"]
        for v in o.values():
            walk(v)
    elif isinstance(o, list):
        for v in o:
            walk(v)
walk(d)

json.dump(d, open(dst, "w"))
print(f"  dropped {len(dropped)} internal path(s): {dropped}", file=sys.stderr)
PY
SPEC="$CLEAN_SPEC"
echo "Sanitized spec -> ${SPEC}"

# openapi-generator does not delete files for operations that no longer exist;
# wipe the generated dirs first so dropped endpoints (e.g. /internal/*) don't
# linger as stale clients.
rm -rf sdk/python sdk/typescript sdk/go

# --- Python -> package: agentdrive_sdk, PyPI dist: agentdrive-sdk ---
$GEN -i "$SPEC" -g python -o sdk/python \
  --additional-properties=packageName=agentdrive_sdk,projectName=agentdrive-sdk,packageVersion="${VERSION}",library=urllib3 \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

# --- TypeScript (fetch-based: works in browser + Node, no axios dep) -> npm: @tokencanopy/agentdrive-sdk ---
$GEN -i "$SPEC" -g typescript-fetch -o sdk/typescript \
  --additional-properties=npmName=@tokencanopy/agentdrive-sdk,npmVersion="${VERSION}",supportsES6=true,typescriptThreePlus=true \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

# --- Go -> module: github.com/tokencanopy/agentdrive-sdk/sdk/go ---
$GEN -i "$SPEC" -g go -o sdk/go \
  --additional-properties=packageName=agentdrive,isGoSubmodule=true,enumClassPrefix=true \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

# The module must be importable at its location in the monorepo so that
# `go get github.com/tokencanopy/agentdrive-sdk/sdk/go@<tag>` resolves. Version
# tags for this submodule are `sdk/go/vX.Y.Z` (see publish.yml).
GO_MODULE="${GIT_HOST}/${GIT_USER}/${GIT_REPO}/sdk/go"
sed -i.bak "1s|^module .*|module ${GO_MODULE}|" sdk/go/go.mod && rm -f sdk/go/go.mod.bak

echo "Done. SDKs written to sdk/{python,typescript,go}."
