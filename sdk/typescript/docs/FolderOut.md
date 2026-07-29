
# FolderOut

Folder resource (folders+permalinks design §13). `path` is the canonical leading+trailing-slash form. Access is expressed through grants (permission-sharing-design §4.4), not a folder-level flag.

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
`path` | string
`purgeAt` | Date
`updatedAt` | Date

## Example

```typescript
import type { FolderOut } from '@mnexa-ai/agentdrive-sdk'

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
  "path": null,
  "purgeAt": null,
  "updatedAt": null,
} satisfies FolderOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FolderOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
