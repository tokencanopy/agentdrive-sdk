# AgentDrive REST API Reference

> Note: This document is authored in-repo and is no longer synced from an external website.

The AgentDrive REST API base URL is:

```
https://drive.tokencanopy.com
```

The current API contract is **v0**.

The authoritative, machine-readable specification is committed in this repository at [`sdk/openapi.json`](../sdk/openapi.json). Readers and client implementers should generate clients directly from `sdk/openapi.json` (see [`sdk-generation.md`](sdk-generation.md)) rather than hand-copying endpoint definitions or schemas.

## Endpoint Paths

The following operations are defined in `sdk/openapi.json`:

### System & Discovery
- `GET /.well-known/oauth-protected-resource` — Protected-resource metadata (RFC 9728)
- `GET /.well-known/oauth-protected-resource/mcp` — Protected-resource metadata for the MCP endpoint (RFC 9728)
- `GET /health` — Health check
- `GET /s/{share_key}` — Redeem share

### Drives
- `GET /v0/drives` — List drives
- `POST /v0/drives` — Create drive
- `GET /v0/drives/{drive_id}` — Read drive
- `DELETE /v0/drives/{drive_id}` — Delete drive
- `PATCH /v0/drives/{drive_id}` — Update drive
- `POST /v0/drives/{drive_id}/restore` — Restore drive
- `GET /v0/drives/{drive_id}/lookup` — Lookup entry by path
- `GET /v0/drives/{drive_id}/search` — Search drive
- `GET /v0/drives/{drive_id}/entries` — List entries
- `GET /v0/drives/{drive_id}/changes` — List changes
- `GET /v0/drives/{drive_id}/usage` — Drive usage stats
- `POST /v0/drives/{drive_id}/download-capabilities` — Create download capability

### Artifacts & Versions
- `GET /v0/drives/{drive_id}/artifacts` — List artifacts
- `POST /v0/drives/{drive_id}/artifacts` — Create artifact
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}` — Read artifact
- `DELETE /v0/drives/{drive_id}/artifacts/{artifact_id}` — Delete artifact
- `PATCH /v0/drives/{drive_id}/artifacts/{artifact_id}` — Update artifact
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}/content` — Read artifact content
- `POST /v0/drives/{drive_id}/artifacts/{artifact_id}/copy` — Copy artifact
- `POST /v0/drives/{drive_id}/artifacts/{artifact_id}/restore` — Restore artifact
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}/versions` — List versions
- `POST /v0/drives/{drive_id}/artifacts/{artifact_id}/versions` — Append version
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}` — Read version
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/content` — Read version content
- `POST /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/restore` — Restore version
- `POST /v0/drives/{drive_id}/artifacts/{artifact_id}/viewer-sessions` — Create viewer session

### Sheets & Sheet Sessions
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}/sheets` — List sheets
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}/cells` — Read sheet cells
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/sheets` — List version sheets
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/cells` — Read version cells
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions` — List sheet sessions
- `POST /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions` — Create sheet session
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions/{session_id}` — Read sheet session
- `DELETE /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions/{session_id}` — Delete sheet session
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions/{session_id}/cells` — Read sheet session cells
- `POST /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions/{session_id}/cells` — Write sheet session cells
- `POST /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions/{session_id}/complete` — Complete sheet session
- `GET /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions/{session_id}/edits` — List sheet session edits

### Folders
- `GET /v0/drives/{drive_id}/folders` — List folders
- `POST /v0/drives/{drive_id}/folders` — Create folder
- `GET /v0/drives/{drive_id}/folders/{folder_id}` — Read folder
- `DELETE /v0/drives/{drive_id}/folders/{folder_id}` — Delete folder
- `PATCH /v0/drives/{drive_id}/folders/{folder_id}` — Update folder
- `POST /v0/drives/{drive_id}/folders/{folder_id}/copy` — Copy folder
- `POST /v0/drives/{drive_id}/folders/{folder_id}/restore` — Restore folder

### Uploads
- `POST /v0/drives/{drive_id}/uploads` — Begin upload
- `GET /v0/drives/{drive_id}/uploads/{upload_id}` — Read upload
- `DELETE /v0/drives/{drive_id}/uploads/{upload_id}` — Cancel upload
- `POST /v0/drives/{drive_id}/uploads/{upload_id}/complete` — Complete upload

### Access Grants & Shares
- `GET /v0/drives/{drive_id}/grants` — List grants
- `POST /v0/drives/{drive_id}/grants` — Create grant
- `GET /v0/drives/{drive_id}/grants/{grant_id}` — Read grant
- `DELETE /v0/drives/{drive_id}/grants/{grant_id}` — Revoke grant
- `PATCH /v0/drives/{drive_id}/grants/{grant_id}` — Update grant
- `GET /v0/drives/{drive_id}/shares` — List shares
- `POST /v0/drives/{drive_id}/shares` — Create share
- `GET /v0/drives/{drive_id}/shares/{share_id}` — Read share
- `DELETE /v0/drives/{drive_id}/shares/{share_id}` — Revoke share
- `POST /v0/drives/{drive_id}/shares/{share_id}/rotate` — Rotate share
