#!/usr/bin/env bash
# Generate the Python / TypeScript / Go SDKs from the AgentDrive OpenAPI spec.
#
# Usage: scripts/generate-sdks.sh [path-to-openapi.json]
# Requires: Docker. The generator image is pinned below and in provenance.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPEC_INPUT="${1:-sdk/openapi.json}"
if [[ "$SPEC_INPUT" = /* ]]; then
  SPEC="${SPEC_INPUT#"$ROOT/"}"
else
  SPEC="$SPEC_INPUT"
fi
if [[ "$SPEC" = /* || ! -f "$ROOT/$SPEC" ]]; then
  echo "spec must be a file inside the repository: $SPEC_INPUT" >&2
  exit 2
fi
VERSION="${SDK_VERSION:-0.0.1}"
GIT_HOST="github.com"
GIT_USER="Mnexa-AI"
GIT_REPO="agentdrive-sdk"
OAG_IMAGE="openapitools/openapi-generator-cli:v7.24.0"

echo "Generating SDKs from ${SPEC} with ${OAG_IMAGE} (version ${VERSION})"

# openapi-generator's Go templates emit invalid code for object/array `default`
# values (e.g. `var options CompileOptions = {wait=false}`). Strip those defaults
# into a sanitized spec used for generation; scalar defaults are left intact.
CLEAN_SPEC="$(dirname "$SPEC")/.openapi.codegen.json"
TYPESCRIPT_SPEC="$(dirname "$SPEC")/.openapi.codegen.typescript.json"
GO_SPEC="$(dirname "$SPEC")/.openapi.codegen.go.json"
LOCK_BACKUP="$(mktemp "${TMPDIR:-/tmp}/agentdrive-sdk-package-lock.XXXXXX")"
had_lock=false
if [[ -f "$ROOT/sdk/typescript/package-lock.json" ]]; then
  cp "$ROOT/sdk/typescript/package-lock.json" "$LOCK_BACKUP"
  had_lock=true
fi
cleanup() {
  rm -f \
    "$ROOT/$CLEAN_SPEC" \
    "$ROOT/$TYPESCRIPT_SPEC" \
    "$ROOT/$GO_SPEC" \
    "$LOCK_BACKUP"
}
trap cleanup EXIT

python3 "$ROOT/scripts/prepare_codegen_contract.py" \
  "$ROOT/$SPEC" "$ROOT/$CLEAN_SPEC"
python3 "$ROOT/scripts/prepare_codegen_contract.py" \
  "$ROOT/$SPEC" "$ROOT/$TYPESCRIPT_SPEC" --language typescript
python3 "$ROOT/scripts/prepare_codegen_contract.py" \
  "$ROOT/$SPEC" "$ROOT/$GO_SPEC" --language go
SPEC="$CLEAN_SPEC"
echo "Sanitized spec -> ${SPEC}"

# openapi-generator does not delete files for operations that no longer exist;
# wipe the generated dirs first so dropped endpoints (e.g. /internal/*) don't
# linger as stale clients.
rm -rf sdk/python sdk/typescript sdk/go

generate() {
  docker run --rm \
    --user "$(id -u):$(id -g)" \
    --volume "$ROOT:/local" \
    --workdir /local \
    "$OAG_IMAGE" generate "$@"
}

# --- Python -> package: agentdrive_sdk, PyPI dist: agentdrive-sdk ---
generate -i "/local/$SPEC" -g python -o /local/sdk/python \
  --additional-properties=packageName=agentdrive_sdk,projectName=agentdrive-sdk,packageVersion="${VERSION}",library=urllib3,hideGenerationTimestamp=true \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

# --- TypeScript (fetch-based: works in browser + Node, no axios dep) -> npm: @mnexa-ai/agentdrive-sdk ---
generate -i "/local/$TYPESCRIPT_SPEC" -g typescript-fetch -o /local/sdk/typescript \
  --additional-properties=npmName=@mnexa-ai/agentdrive-sdk,npmVersion="${VERSION}",supportsES6=true,typescriptThreePlus=true,hideGenerationTimestamp=true \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

# --- Go -> module: github.com/Mnexa-AI/agentdrive-sdk/sdk/go ---
generate -i "/local/$GO_SPEC" -g go -o /local/sdk/go \
  --additional-properties=packageName=agentdrive,isGoSubmodule=true,enumClassPrefix=true,hideGenerationTimestamp=true \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

# The generator's Go test stubs import `<repo>/<packageName>` even though this
# repository intentionally publishes the module at `sdk/go`. They contain
# only skipped placeholder calls and are not contract tests; remove them and
# compile/test the actual module with `go test ./...`.
rm -rf sdk/go/test

if [[ "$had_lock" = true ]]; then
  cp "$LOCK_BACKUP" "$ROOT/sdk/typescript/package-lock.json"
fi

# The module must be importable at its location in the monorepo so that
# `go get github.com/Mnexa-AI/agentdrive-sdk/sdk/go@<tag>` resolves. Version
# tags for this submodule are `sdk/go/vX.Y.Z` (see publish.yml).
GO_MODULE="${GIT_HOST}/${GIT_USER}/${GIT_REPO}/sdk/go"
sed -i.bak "1s|^module .*|module ${GO_MODULE}|" sdk/go/go.mod && rm -f sdk/go/go.mod.bak
python3 scripts/normalize_generated_text.py sdk/python sdk/typescript sdk/go

echo "Done. SDKs written to sdk/{python,typescript,go}."
