# SDK contract migration — July 2026

This regeneration switches the SDK source from the live production
`/openapi.json` endpoint to AgentDrive's reviewed, committed PR 3 contract.
No package is published by this change.

## Generated surface

| | Before | After |
|---|---:|---:|
| OpenAPI paths | 159 | 86 |
| Operations | 185 | 110 |
| Component schemas | 123 | 128 |

The removed generated methods were browser pages, `/web/*` forms, and other UI
or internal operations that never belonged in a machine SDK. Their runtime
routes are unchanged.

The corrected generated surface adds:

- the HTTP Bearer authentication scheme used by `ad_live_`, `ad_user_`, and
  supported JWT credentials;
- canonical structured error and validation models;
- typed JSON success payloads plus correct binary/text response types;
- PR 2 cursor inputs and `next_cursor` outputs for trash and compile-job
  listings, while retaining their deprecated response aliases.

Generated method and model changes should be reviewed as a client-surface
correction. Before publishing, choose an SDK version appropriate to the
packages' current stability promise and include these notes in the release.

## Workflow change

- Input is the committed `sdk/openapi.json` with exact AgentDrive commit and
  SHA-256 provenance.
- OpenAPI Generator is pinned to 7.24.0.
- CI regenerates and fails on drift.
- Python, TypeScript, and Go must expose exactly the contract's operation IDs.
- All language builds/tests run before merge.
- Scheduled production fetches, bot auto-commits, and implicit publishing are
  removed.
