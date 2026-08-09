
# FolderCopyIn

POST /v0/drives/{id}/folders/{folder_id}/copy body.  ``destination_drive_id`` must equal the source drive (or be absent) — cross-drive copy is out of v0 scope and rejected.

## Properties

Name | Type
------------ | -------------
`destinationDriveId` | string
`destinationName` | string
`destinationParentId` | string

## Example

```typescript
import type { FolderCopyIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "destinationDriveId": null,
  "destinationName": null,
  "destinationParentId": null,
} satisfies FolderCopyIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FolderCopyIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
