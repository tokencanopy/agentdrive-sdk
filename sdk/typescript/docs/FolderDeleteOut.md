
# FolderDeleteOut

DELETE response — surfaces cascade counts so the caller can confirm scope of an rmdir before the client retries with `?recursive=true`.

## Properties

Name | Type
------------ | -------------
`deletedAt` | Date
`id` | string
`nArtifactsDeleted` | number
`nSubfoldersDeleted` | number
`ok` | boolean
`path` | string
`purgeAt` | Date
`retentionDays` | number

## Example

```typescript
import type { FolderDeleteOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "deletedAt": null,
  "id": null,
  "nArtifactsDeleted": null,
  "nSubfoldersDeleted": null,
  "ok": null,
  "path": null,
  "purgeAt": null,
  "retentionDays": null,
} satisfies FolderDeleteOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FolderDeleteOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
