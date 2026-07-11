
# DriveApiKeyOut

One per-drive `ad_live_` key — metadata only (never the raw key or hash). Item shape for `GET /v0/drives/{id}/keys`.

## Properties

Name | Type
------------ | -------------
`id` | string
`prefix` | string
`label` | string
`lastUsedAt` | Date
`createdAt` | Date
`revokedAt` | Date

## Example

```typescript
import type { DriveApiKeyOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "prefix": null,
  "label": null,
  "lastUsedAt": null,
  "createdAt": null,
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


