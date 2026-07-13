
# UploadStatusOut

Response of `GET /v0/uploads/{upload_id}` — the live state of a direct-to-GCS upload session (large-upload-design.md §5).  `state` is derived, not a stored column:   * `initiated` — session open; PUT the bytes to the `upload_url`, then                   `POST /v0/uploads/{upload_id}/commit`.   * `committed` — the bytes landed and the artifact was created                   (`committed_at` is set).   * `aborted`   — released via `DELETE /v0/uploads/{upload_id}`.   * `expired`   — past `expires_at` without a commit; the reservation is                   reclaimed by the GC sweep.

## Properties

Name | Type
------------ | -------------
`uploadId` | string
`path` | string
`contentType` | string
`sizeBytes` | number
`state` | string
`maxBytes` | number
`expiresAt` | Date
`createdAt` | Date
`committedAt` | Date

## Example

```typescript
import type { UploadStatusOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "uploadId": null,
  "path": null,
  "contentType": null,
  "sizeBytes": null,
  "state": null,
  "maxBytes": null,
  "expiresAt": null,
  "createdAt": null,
  "committedAt": null,
} satisfies UploadStatusOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UploadStatusOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


