
# FolderRestoreOut

POST /v0/folders/{fld_id}/restore response — the restored (live) folder resource (same shape as `FolderOut`) plus the cascade counts from `core.folders.restore_cascade` (dashboard-file-operations-design §4.5), so the caller can confirm the scope of what came back with the root.

## Properties

Name | Type
------------ | -------------
`createdAt` | Date
`deletedAt` | Date
`description` | string
`driveId` | string
`etag` | string
`id` | string
`inheritGrants` | boolean
`metageneration` | number
`nArtifactsRestored` | number
`nSubfoldersRestored` | number
`path` | string
`purgeAt` | Date
`updatedAt` | Date

## Example

```typescript
import type { FolderRestoreOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "createdAt": null,
  "deletedAt": null,
  "description": null,
  "driveId": null,
  "etag": null,
  "id": null,
  "inheritGrants": null,
  "metageneration": null,
  "nArtifactsRestored": null,
  "nSubfoldersRestored": null,
  "path": null,
  "purgeAt": null,
  "updatedAt": null,
} satisfies FolderRestoreOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FolderRestoreOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
