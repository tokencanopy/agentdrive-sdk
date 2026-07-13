
# FolderCopyOut

POST /v0/folders/{fld_id}/copy response — the newly-created folder resource (same shape as `FolderOut`) plus copy-provenance fields: `from_fld_id` is the source folder and `n_artifacts_copied` is the number of descendant artifacts cloned into the new subtree. Mirrors the MCP `copy` folder route\'s conceptual shape.

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
`fromFldId` | string
`nArtifactsCopied` | number

## Example

```typescript
import type { FolderCopyOut } from '@mnexa-ai/agentdrive-sdk'

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
  "fromFldId": null,
  "nArtifactsCopied": null,
} satisfies FolderCopyOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FolderCopyOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


