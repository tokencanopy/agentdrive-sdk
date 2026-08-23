# AgentDrive SDKs

REST clients for the AgentDrive API, generated from the reviewed contract
committed at [`openapi.json`](openapi.json) using pinned OpenAPI Generator
7.16.0. The v0 contract contains 50 operations: 47 authenticated `/v0`
operations plus three public operations. [`openapi.provenance.json`](openapi.provenance.json) records the exact
AgentDrive source commit and snapshot digest.

| Language | Directory | Package | Generator |
|---|---|---|---|
| Python | [`python/`](python/) | `agentdrive-sdk` (PyPI) | `python` (urllib3) |
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

## Authentication

All three clients talk to `https://drive.tokencanopy.com`. Authenticate with an API
key (`ad_live_...`) or an OAuth access token as a bearer credential — see
[`../docs/auth.md`](../docs/auth.md) and [`../docs/api.md`](../docs/api.md).

> **Generated code.** Don't hand-edit files under `python/`, `typescript/`, or
> `go/` — changes are overwritten on the next generation. Adjust
> `scripts/generate-sdks.sh` instead.
