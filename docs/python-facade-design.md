# Python facade and generated-core boundary

- **Status:** Accepted for the v0.0.1 SDK line
- **Date:** 2026-08-23
- **Canonical API:** `https://drive.tokencanopy.com`

## Boundary

The OpenAPI Generator output is an implementation detail under
`agentdrive_sdk.generated`. It owns request serialization, wire models,
response parsing, and the operation names from `sdk/openapi.json`. It is
replaceable output: regeneration may delete and recreate that namespace, but
must never touch the handwritten modules beside it.

The public package is `agentdrive_sdk`. Its handwritten facade owns token
providers, retries, idempotency keys, conditional requests, cursor iteration,
path validation, and safe byte/file conveniences. Facade methods call exactly
one generated operation and return the generated model rather than copying
wire schemas.

The committed v0.0.1 generated Python client is synchronous and uses the
pinned OpenAPI Generator `urllib3` transport. The facade therefore has one
real transport implementation. Async callers receive an `asyncio.to_thread`
bridge over that same implementation; this is an explicit v0 compatibility
choice, not a second HTTP stack. A future generator-baseline change may move
the generated core to a native async library, but it must preserve the
namespace and facade mapping contract.

## Public construction

```python
from agentdrive_sdk import AgentDriveClient, StaticTokenProvider

client = AgentDriveClient(
    token_provider=StaticTokenProvider("synthetic-token"),
)
drive = client.drives.create("research")
folder = client.folders.create(drive.id, "notes", parent_id=drive.root_folder_id)
artifact = client.artifacts.create(
    drive.id, "readme.md", parent_id=folder.id, content=b"hello\n",
)
```

The facade returns stable resource IDs and revisions. Paths are accepted for
lookup and creation helpers, then resolved once; subsequent mutations use the
returned ID and revision. A caller must explicitly supply a revision for
existing-state mutations. The SDK never fetches a newer revision and silently
overwrites a concurrent change.

## Safety invariants

- OAuth client-credentials providers cache an access token until its expiry
  skew, renew under a lock, and never retain a refresh token.
- A mutation gets one idempotency key before its first attempt. Transient
  retries reuse that exact key and request body.
- `If-Match` accepts a bare revision for convenience and emits one strong
  quoted ETag. Missing revisions are rejected before the HTTP call.
- List helpers preserve opaque cursors and expose bounded iterators. Changes
  iteration yields pages/items without hiding the checkpoint cursor.
- Relative paths reject absolute paths, `..`, backslashes, NUL bytes, empty
  segments, and symlink escapes. Directory uploads reject symlinks and
  credential-like files unless explicitly opted in.
- Download helpers mint an AgentDrive download capability, then fetch the
  returned target without forwarding the AgentDrive bearer token.

## Non-goals

The facade does not expose Hub workspace, billing, identity, chat, query, wiki,
raw events, or legacy AgentDrive credential operations. Those boundaries stay
outside the AgentDrive SDK.
