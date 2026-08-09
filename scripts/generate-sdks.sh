#!/usr/bin/env bash
# Generate the Python / TypeScript / Go SDKs from the AgentDrive OpenAPI spec.
#
# Usage: scripts/generate-sdks.sh [path-to-openapi.json]
# Requires: Docker and the immutable OpenAPI Generator image recorded in
# sdk/openapi-generator-image.txt.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPEC_INPUT="${1:-sdk/openapi.json}"
SPEC="$(python3 "$ROOT/scripts/resolve_repo_path.py" "$ROOT" "$SPEC_INPUT")"
SOURCE_SPEC="$ROOT/$SPEC"
VERSION_FILE="$ROOT/sdk/SDK_VERSION"
PYPROJECT="$ROOT/sdk/python/pyproject.toml"
GIT_HOST="github.com"
GIT_USER="Mnexa-AI"
GIT_REPO="agentdrive-sdk"
GO_MODULE="${GIT_HOST}/${GIT_USER}/${GIT_REPO}/sdk/go"

if [[ ! -f "$VERSION_FILE" ]]; then
  echo "sdk/SDK_VERSION is required" >&2
  exit 2
fi
VERSION="$(tr -d '\r\n' < "$VERSION_FILE")"
if [[ ! "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+([a-zA-Z0-9.-]+)?$ ]]; then
  echo "sdk/SDK_VERSION must contain one semantic version" >&2
  exit 2
fi

python3 - "$PYPROJECT" "$ROOT/sdk/python/src/agentdrive_sdk/__init__.py" "$VERSION" <<'PY'
import ast
import sys
import tomllib
from pathlib import Path

pyproject = Path(sys.argv[1])
package_init = Path(sys.argv[2])
expected = sys.argv[3]
actual = tomllib.loads(pyproject.read_text(encoding="utf-8"))["project"]["version"]
if actual != expected:
    raise SystemExit(
        f"{pyproject.relative_to(pyproject.parents[2])} version {actual!r} "
        f"does not match sdk/SDK_VERSION {expected!r}"
    )

tree = ast.parse(package_init.read_text(encoding="utf-8"), filename=str(package_init))
versions = [
    node.value.value
    for node in tree.body
    if isinstance(node, ast.Assign)
    and any(isinstance(target, ast.Name) and target.id == "__version__" for target in node.targets)
    and isinstance(node.value, ast.Constant)
    and isinstance(node.value.value, str)
]
if versions != [expected]:
    raise SystemExit(
        f"{package_init.relative_to(pyproject.parents[2])} must declare "
        f"__version__ = {expected!r}"
    )
PY

OAG_IMAGE="$(tr -d '\r\n' < "$ROOT/sdk/openapi-generator-image.txt")"
if [[ ! "$OAG_IMAGE" =~ ^openapitools/openapi-generator-cli:v7\.24\.0@sha256:[0-9a-f]{64}$ ]]; then
  echo "sdk/openapi-generator-image.txt must pin OpenAPI Generator 7.24.0 by digest" >&2
  exit 2
fi

GENERATION_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/agentdrive-sdk-generation.XXXXXX")"
cleanup() {
  rm -rf "$GENERATION_ROOT"
}
trap cleanup EXIT

COMMON_SPEC="$GENERATION_ROOT/openapi.common.json"
TYPESCRIPT_SPEC="$GENERATION_ROOT/openapi.typescript.json"
GO_SPEC="$GENERATION_ROOT/openapi.go.json"

python3 "$ROOT/scripts/prepare_codegen_contract.py" \
  "$SOURCE_SPEC" "$COMMON_SPEC"
python3 "$ROOT/scripts/prepare_codegen_contract.py" \
  "$SOURCE_SPEC" "$TYPESCRIPT_SPEC" --language typescript
python3 "$ROOT/scripts/prepare_codegen_contract.py" \
  "$SOURCE_SPEC" "$GO_SPEC" --language go

echo "Generating SDKs from ${SPEC} with ${OAG_IMAGE} (version ${VERSION})"

# Verify Docker and fetch the pinned image before touching committed output.
docker info >/dev/null
docker image inspect "$OAG_IMAGE" >/dev/null 2>&1 || docker pull "$OAG_IMAGE"

generate() {
  docker run --rm \
    --user "$(id -u):$(id -g)" \
    --volume "$ROOT:/local:ro" \
    --volume "$GENERATION_ROOT:/generated" \
    --workdir /local \
    "$OAG_IMAGE" generate "$@"
}

PYTHON_GLOBAL_PROPERTIES="apiTests=false,modelTests=false,apiDocs=false,modelDocs=false"

# Python's generated core has two deliberately separate implementations. The
# handwritten package lives outside these leaf directories and is never
# replaced by generation.
generate -i /generated/openapi.common.json -g python -o /generated/python-sync \
  --global-property="$PYTHON_GLOBAL_PROPERTIES" \
  --additional-properties=packageName=agentdrive_sdk.generated.sync,projectName=agentdrive-sdk,packageVersion="${VERSION}",library=urllib3,hideGenerationTimestamp=true \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

generate -i /generated/openapi.common.json -g python -o /generated/python-async \
  --global-property="$PYTHON_GLOBAL_PROPERTIES" \
  --additional-properties=packageName=agentdrive_sdk.generated.async_client,projectName=agentdrive-sdk,packageVersion="${VERSION}",library=httpx,supportHttpxSync=false,hideGenerationTimestamp=true \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

# TypeScript remains fetch-based for browser and Node compatibility.
generate -i /generated/openapi.typescript.json -g typescript-fetch \
  -o /generated/typescript \
  --additional-properties=npmName=@mnexa-ai/agentdrive-sdk,npmVersion="${VERSION}",supportsES6=true,typescriptThreePlus=true,hideGenerationTimestamp=true \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

# Go remains a submodule at sdk/go.
generate -i /generated/openapi.go.json -g go -o /generated/go \
  --additional-properties=packageName=agentdrive,isGoSubmodule=true,enumClassPrefix=true,hideGenerationTimestamp=true \
  --git-host="$GIT_HOST" --git-user-id="$GIT_USER" --git-repo-id="$GIT_REPO"

SYNC_SOURCE="$GENERATION_ROOT/python-sync/agentdrive_sdk/generated/sync"
ASYNC_SOURCE="$GENERATION_ROOT/python-async/agentdrive_sdk/generated/async_client"
for generated_python in "$SYNC_SOURCE" "$ASYNC_SOURCE"; do
  if [[ ! -f "$generated_python/api_client.py" ]]; then
    echo "OpenAPI Generator did not create expected Python source: $generated_python" >&2
    exit 2
  fi
done

# Redirects are credential-boundary events. Keep both generated transports from
# following them automatically; Phase 2 will follow signed storage URLs without
# forwarding AgentDrive authorization.
python3 "$ROOT/scripts/patch_python_transports.py" \
  "$SYNC_SOURCE/rest.py" "$ASYNC_SOURCE/rest.py"
python3 "$ROOT/scripts/postprocess_python_models.py" \
  --contract "$SOURCE_SPEC" \
  --models-dir "$SYNC_SOURCE/models" \
  --models-dir "$ASYNC_SOURCE/models"

# OpenAPI Generator's Go test stubs import the wrong module location and contain
# only skipped placeholder calls. Compile the actual generated module instead.
rm -rf "$GENERATION_ROOT/go/test"
sed -i.bak "1s|^module .*|module ${GO_MODULE}|" "$GENERATION_ROOT/go/go.mod"
rm -f "$GENERATION_ROOT/go/go.mod.bak"

# OpenAPI Generator does not create a lockfile. Preserve the reviewed npm lock
# while replacing the rest of the TypeScript output.
if [[ -f "$ROOT/sdk/typescript/package-lock.json" ]]; then
  cp "$ROOT/sdk/typescript/package-lock.json" \
    "$GENERATION_ROOT/typescript/package-lock.json"
  python3 - "$GENERATION_ROOT/typescript/package-lock.json" "$VERSION" <<'PY'
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
version = sys.argv[2]
document = json.loads(path.read_text(encoding="utf-8"))
document["version"] = version
document["packages"][""]["version"] = version
path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
PY
fi

python3 - \
  "$VERSION" \
  "$SYNC_SOURCE/__init__.py" \
  "$ASYNC_SOURCE/__init__.py" \
  "$GENERATION_ROOT/typescript/package.json" \
  "$GENERATION_ROOT/typescript/package-lock.json" <<'PY'
import ast
import json
import sys
from pathlib import Path

expected = sys.argv[1]
for raw in sys.argv[2:4]:
    path = Path(raw)
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    versions = [
        node.value.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "__version__"
            for target in node.targets
        )
        and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    ]
    if versions != [expected]:
        raise SystemExit(f"generated package version drift in {path}")

package = json.loads(Path(sys.argv[4]).read_text(encoding="utf-8"))
lock = json.loads(Path(sys.argv[5]).read_text(encoding="utf-8"))
actual = {
    package["version"],
    lock["version"],
    lock["packages"][""]["version"],
}
if actual != {expected}:
    raise SystemExit(f"TypeScript package version drift: {sorted(actual)}")
PY

python3 "$ROOT/scripts/normalize_generated_text.py" \
  "$SYNC_SOURCE" \
  "$ASYNC_SOURCE" \
  "$GENERATION_ROOT/typescript" \
  "$GENERATION_ROOT/go"

# Generation succeeded completely. Replace only generated output from here on.
PYTHON_PACKAGE="$ROOT/sdk/python/src/agentdrive_sdk"
PYTHON_GENERATED="$PYTHON_PACKAGE/generated"
mkdir -p "$PYTHON_GENERATED"
rm -rf "$PYTHON_GENERATED/sync" "$PYTHON_GENERATED/async_client"
cp -a "$SYNC_SOURCE" "$PYTHON_GENERATED/sync"
cp -a "$ASYNC_SOURCE" "$PYTHON_GENERATED/async_client"

# Remove the legacy all-generated Python package layout. These exact paths are
# intentionally narrower than sdk/python so README, packaging, and tests remain.
rm -rf \
  "$ROOT/sdk/python/agentdrive_sdk" \
  "$ROOT/sdk/python/docs" \
  "$ROOT/sdk/python/test" \
  "$ROOT/sdk/python/.github" \
  "$ROOT/sdk/python/.openapi-generator"
rm -f \
  "$ROOT/sdk/python/.gitignore" \
  "$ROOT/sdk/python/.gitlab-ci.yml" \
  "$ROOT/sdk/python/.openapi-generator-ignore" \
  "$ROOT/sdk/python/.travis.yml" \
  "$ROOT/sdk/python/git_push.sh" \
  "$ROOT/sdk/python/requirements.txt" \
  "$ROOT/sdk/python/setup.cfg" \
  "$ROOT/sdk/python/setup.py" \
  "$ROOT/sdk/python/test-requirements.txt" \
  "$ROOT/sdk/python/tox.ini"

rm -rf "$ROOT/sdk/typescript" "$ROOT/sdk/go"
cp -a "$GENERATION_ROOT/typescript" "$ROOT/sdk/typescript"
cp -a "$GENERATION_ROOT/go" "$ROOT/sdk/go"

# The exact Python reference and review manifest are generated artifacts too.
# Keep them in the same one-command pipeline as the clients so an API change
# cannot regenerate code while leaving either representation stale.
python3 "$ROOT/scripts/generate_python_contract_manifest.py" \
  --contract "$SOURCE_SPEC" \
  --sync-root "$PYTHON_GENERATED/sync" \
  --async-root "$PYTHON_GENERATED/async_client" \
  --output "$ROOT/sdk/python/generated-contract-shape.json"
python3 "$ROOT/scripts/generate_python_api_reference.py" \
  --contract "$SOURCE_SPEC" \
  --provenance "$ROOT/sdk/openapi.provenance.json" \
  --sync-api "$PYTHON_GENERATED/sync/api" \
  --async-api "$PYTHON_GENERATED/async_client/api" \
  --output "$ROOT/docs/python-sdk-api-reference.md"

echo "Done. Generated Python core -> sdk/python/src/agentdrive_sdk/generated/{sync,async_client}."
echo "TypeScript and Go -> sdk/{typescript,go}."
echo "Python contract manifest/reference -> sdk/python/generated-contract-shape.json and docs/python-sdk-api-reference.md."
