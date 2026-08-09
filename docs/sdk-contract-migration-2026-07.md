# SDK Phase 1 contract migration — July–August 2026

This PR replaces the pre-Phase 1 generated surface with AgentDrive's reviewed,
committed SDK contract and introduces the Python `0.1.0` generated core. No
package is published by this repository change.

## Generated surface

| | Pre-Phase 1 (`0.0.1`) | Phase 1 (`0.1.0`) |
|---|---:|---:|
| OpenAPI paths | 86 | 27 |
| Operations | 110 | 42 |
| Component schemas | 128 | 38 |

The 68 removed operations were browser pages, internal/admin services, and
other routes outside the supported machine SDK. Their removal from this client
contract does not claim that their server routes disappeared. The Phase 1
surface contains 39 bearer-authenticated operations and three anonymous
discovery/health/share-redemption operations.

The old `agentdrive-sdk` `0.0.1` distribution is pre-Phase 1 and superseded by
this reviewed contract. Separately, the bare `agentdrive` PyPI name is only a
parked `0.0.1` placeholder; the retired stdio MCP companion is not part of the
new SDK architecture.

## Python architecture

The Python package is now hand-owned except for two isolated generated trees:

- synchronous `urllib3` client at
  `src/agentdrive_sdk/generated/sync`;
- asynchronous `httpx` client at
  `src/agentdrive_sdk/generated/async_client`.

Both cores cover all 42 operations and expose the primary,
`*_with_http_info`, and `*_without_preload_content` variants. The ergonomic
resource facade is a later phase; `0.1.0` intentionally exposes the complete
generated cores first. Exact callable signatures and generated docstrings are
in `docs/python-sdk-api-reference.md`.

Generated request models reject unknown fields, keep request enums closed, and
distinguish omitted PATCH fields from explicit null. Optional but non-nullable
wire fields reject explicit null. Generated response models ignore additive
fields and accept future enum strings. Both transports disable automatic
redirect following so credentials are not forwarded across hosts, while
`ApiResponse.headers` preserves the complete raw response-header mapping.

## Compatibility and review gates

The 110-to-42 transition is an intentional one-time reset. It is authorized by
`sdk/openapi.compatibility-reset.json`, bound to the exact old/new canonical
contract digests and AgentDrive source commit
`31cd35c8e12aef1cbee228e965289107cb51092c`. Any different candidate fails the
reset match. After this contract reaches the base branch, CI performs normal
directional compatibility checks and rejects breaking request or response
changes.

CI additionally requires:

- exact provenance and pinned-generator verification;
- byte-identical regeneration and exact operation coverage in all languages;
- exact sync/async Python callable and wire parity;
- direct component property/requiredness/nullability comparison plus reviewed
  constraint, response status/media/header, and generated AST hashes;
- generated model evolution and transport conformance tests on Python 3.10,
  3.12, and 3.14;
- a current generated API reference and contract-shape manifest;
- release input/tag equality with every package version before any publish job.

Publishing remains a separate human-approved action. Before publishing
`0.1.0`, verify PyPI and npm trusted-publisher ownership after the GitHub
repository transfer; immutable existing versions are hard failures, not
silently skipped.
