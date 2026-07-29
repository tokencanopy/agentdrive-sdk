
# DriveApiKeyOut

One per-drive `ad_live_` key — metadata only (never the raw key or hash). Item shape for `GET /v0/drives/{id}/keys`.

## Properties

Name | Type
------------ | -------------
`createdAt` | Date
`id` | string
`label` | string
`lastUsedAt` | Date
`prefix` | string
`revokedAt` | Date

## Example

```typescript
import type { DriveApiKeyOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "createdAt": null,
  "id": null,
  "label": null,
  "lastUsedAt": null,
  "prefix": null,
  "revokedAt": null,
} satisfies DriveApiKeyOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DriveApiKeyOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
