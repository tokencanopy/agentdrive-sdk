
# WorkspaceCreateOut

POST /v0/workspaces response. Carries the new workspace + its starter drive\'s `ad_live_` key **once** (`starter_drive_api_key`) — reveal-once, store it now (mint more keys via `POST /v0/drives/{id}/keys`).

## Properties

Name | Type
------------ | -------------
`starterDriveApiKey` | string
`starterDriveId` | string
`workspace` | [WorkspaceOut](WorkspaceOut.md)

## Example

```typescript
import type { WorkspaceCreateOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "starterDriveApiKey": null,
  "starterDriveId": null,
  "workspace": null,
} satisfies WorkspaceCreateOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WorkspaceCreateOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
