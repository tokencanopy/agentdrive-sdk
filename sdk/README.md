# AgentDrive SDKs

REST clients for the AgentDrive API, generated from the reviewed contract
committed at [`openapi.json`](openapi.json) using pinned OpenAPI Generator
7.24.0. [`openapi.provenance.json`](openapi.provenance.json) records the exact
AgentDrive source commit and snapshot digest.

| Language | Directory | Package | Generator |
|---|---|---|---|
| Python | [`python/`](python/) | `agentdrive-sdk` (PyPI) | `python` (`urllib3` sync + `httpx` async) |
| TypeScript | [`typescript/`](typescript/) | `@mnexa-ai/agentdrive-sdk` (npm) | `typescript-fetch` |
| Go | [`go/`](go/) | `github.com/Mnexa-AI/agentdrive-sdk/sdk/go` | `go` |

## Regenerating

An AgentDrive API change first updates the handler-generated
`tests/openapi.golden.json` in the private server repository. A coordinated SDK
PR imports that reviewed snapshot with its exact source commit:

```bash
python3 scripts/import_agentdrive_contract.py \
  /path/to/agentdrive/tests/openapi.golden.json \
  --source-commit <agentdrive-commit>
bash scripts/generate-sdks.sh sdk/openapi.json
```

Generation requires Docker. CI first verifies the source digest and generator
pin recorded in `openapi.provenance.json`, regenerates from the committed
contract, and requires a clean worktree including untracked files. It then
checks that Python, TypeScript, and Go expose every contract `operationId`
without language-specific name collisions or stale operations. It never
fetches the live production endpoint and never auto-commits or publishes
generated changes.

Python has two generated cores under
`python/src/agentdrive_sdk/generated/{sync,async_client}`. Everything else in
the Python package—metadata, README, type marker, tests, and the future
ergonomic facade—is hand-owned and survives regeneration. The Python gates
also verify exact callable/wire parity, component fields and
required/nullable shape, model constraint hashes, raw response-header
preservation, request strictness, response forward compatibility, and the
generated [API reference](../docs/python-sdk-api-reference.md).

## Authentication

All three clients talk to `https://api.agentdrive.run`. Authenticate with an API
key (`ad_live_...`) or an OAuth access token as a bearer credential — see
[`../docs/auth.md`](../docs/auth.md) and [`../docs/api.md`](../docs/api.md).

> **Generated code.** In Python, only
> `python/src/agentdrive_sdk/generated/sync` and
> `python/src/agentdrive_sdk/generated/async_client` are generated. TypeScript
> and Go remain generator-owned package trees. Change the contract or
> deterministic generation/postprocessing scripts instead of editing those
> generated files.
