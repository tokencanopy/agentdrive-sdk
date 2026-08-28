#!/usr/bin/env bash
# Generate the Python / TypeScript / Go SDKs from the AgentDrive OpenAPI spec.
#
# Usage: scripts/generate-sdks.sh [path-to-openapi.json]
# Requires: Docker. The generator image is pinned below and in provenance.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPEC_INPUT="${1:-sdk/openapi.json}"
SPEC="$(python3 "$ROOT/scripts/resolve_repo_path.py" "$ROOT" "$SPEC_INPUT")"
cd "$ROOT"
VERSION="${SDK_VERSION:-0.0.3}"
GIT_HOST="github.com"
GIT_USER="tokencanopy"
GIT_REPO="agentdrive-sdk"
OAG_IMAGE="$(tr -d '\r\n' < "$ROOT/sdk/openapi-generator-image.txt")"
if [[ -z "$OAG_IMAGE" ]]; then
  echo "sdk/openapi-generator-image.txt must not be empty" >&2
  exit 2
fi

echo "Generating SDKs from ${SPEC} with ${OAG_IMAGE} (version ${VERSION})"

# openapi-generator's Go templates emit invalid code for object/array `default`
# values (e.g. `var options CompileOptions = {wait=false}`). Strip those defaults
# into a sanitized spec used for generation; scalar defaults are left intact.
CLEAN_SPEC="$(dirname "$SPEC")/.openapi.codegen.json"
TYPESCRIPT_SPEC="$(dirname "$SPEC")/.openapi.codegen.typescript.json"
GO_SPEC="$(dirname "$SPEC")/.openapi.codegen.go.json"
PYTHON_OUTPUT="$ROOT/.openapi-python-generated"
TYPESCRIPT_OUTPUT="$ROOT/.openapi-typescript-generated"
LOCK_BACKUP="$(mktemp "${TMPDIR:-/tmp}/agentdrive-sdk-package-lock.XXXXXX")"
had_lock=false
if [[ -f "$ROOT/sdk/typescript/package-lock.json" ]]; then
  cp "$ROOT/sdk/typescript/package-lock.json" "$LOCK_BACKUP"
  had_lock=true
fi
cleanup() {
  if [[ "$had_lock" = true && -f "$LOCK_BACKUP" ]]; then
    mkdir -p "$ROOT/sdk/typescript"
    cp "$LOCK_BACKUP" "$ROOT/sdk/typescript/package-lock.json"
  fi
  rm -f \
    "$ROOT/$CLEAN_SPEC" \
    "$ROOT/$TYPESCRIPT_SPEC" \
    "$ROOT/$GO_SPEC" \
    "$LOCK_BACKUP"
  rm -rf "$PYTHON_OUTPUT" "$TYPESCRIPT_OUTPUT"
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
# Verify Docker and the pinned image before deleting the recoverable generated
# tree, so a missing daemon or failed image pull leaves the worktree untouched.
docker info >/dev/null
docker image inspect "$OAG_IMAGE" >/dev/null 2>&1 || docker pull "$OAG_IMAGE"
rm -rf "$ROOT/sdk/go" "$PYTHON_OUTPUT" "$TYPESCRIPT_OUTPUT"

generate() {
  docker run --rm \
    --user "$(id -u):$(id -g)" \
    --volume "$ROOT:/local" \
    --workdir /local \
    "$OAG_IMAGE" generate "$@"
}

# --- Python -> generated package: agentdrive_sdk.generated ---
# Generate into a disposable root. The installer below relocates only the
# generated package, preserving the handwritten public facade and its tests.
generate -i "/local/$SPEC" -g python -o /local/.openapi-python-generated \
  --additional-properties=packageName=agentdrive_sdk,projectName=agentdrive-sdk,packageVersion="${VERSION}",library=urllib3,hideGenerationTimestamp=true \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

# --- TypeScript (fetch-based: works in browser + Node, no axios dep) -> generated core ---
# Generate into a disposable root. The installer relocates only src/ into the
# generated namespace, preserving the handwritten facade and package metadata.
generate -i "/local/$TYPESCRIPT_SPEC" -g typescript-fetch -o /local/.openapi-typescript-generated \
  --additional-properties=npmName=@tokencanopy/agentdrive-sdk,npmVersion="${VERSION}",supportsES6=true,typescriptThreePlus=true,hideGenerationTimestamp=true \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

# --- Go -> module: github.com/tokencanopy/agentdrive-sdk/sdk/go ---
generate -i "/local/$GO_SPEC" -g go -o /local/sdk/go \
  --additional-properties=packageName=agentdrive,packageVersion="${VERSION}",isGoSubmodule=true,enumClassPrefix=true,hideGenerationTimestamp=true \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

# The generator's Go test stubs import `<repo>/<packageName>` even though this
# repository intentionally publishes the module at `sdk/go`. They contain
# only skipped placeholder calls and are not contract tests; remove them and
# compile/test the actual module with `go test ./...`.
rm -rf "$ROOT/sdk/go/test"

python3 "$ROOT/scripts/install_python_generated.py" "$PYTHON_OUTPUT"
python3 "$ROOT/scripts/patch_typescript_codegen.py" "$TYPESCRIPT_OUTPUT"
python3 "$ROOT/scripts/install_typescript_generated.py" "$TYPESCRIPT_OUTPUT"

# The module must be importable at its location in the monorepo so that
# `go get github.com/tokencanopy/agentdrive-sdk/sdk/go@<tag>` resolves. Version
# tags for this submodule are `sdk/go/vX.Y.Z` (see publish.yml).
GO_MODULE="${GIT_HOST}/${GIT_USER}/${GIT_REPO}/sdk/go"
sed -i.bak "1s|^module .*|module ${GO_MODULE}|" "$ROOT/sdk/go/go.mod"
rm -f "$ROOT/sdk/go/go.mod.bak"
python3 "$ROOT/scripts/normalize_generated_text.py" \
  "$ROOT/sdk/python" "$ROOT/sdk/typescript/src/generated" "$ROOT/sdk/go"

echo "Done. SDKs written to sdk/{python,typescript,go}."
