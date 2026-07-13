
# FolderRestoreOut

POST /v0/folders/{fld_id}/restore response — the restored (live) folder resource (same shape as `FolderOut`) plus the cascade counts from `core.folders.restore_cascade` (dashboard-file-operations-design §4.5), so the caller can confirm the scope of what came back with the root.

## Properties

Name | Type
------------ | -------------
`id` | string
`driveId` | string
`path` | string
`description` | string
`inheritGrants` | boolean
`metageneration` | number
`etag` | string
`createdAt` | Date
`updatedAt` | Date
`deletedAt` | Date
`purgeAt` | Date
`nSubfoldersRestored` | number
`nArtifactsRestored` | number

## Example

```typescript
import type { FolderRestoreOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "driveId": null,
  "path": null,
  "description": null,
  "inheritGrants": null,
  "metageneration": null,
  "etag": null,
  "createdAt": null,
  "updatedAt": null,
  "deletedAt": null,
  "purgeAt": null,
  "nSubfoldersRestored": null,
  "nArtifactsRestored": null,
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


