
# DriveApiKeyCreateOut

`POST /v0/drives/{id}/keys` response — the new key\'s metadata PLUS the raw `ad_live_` value, returned **once**. Store `api_key` now; only its hash is persisted.

## Properties

Name | Type
------------ | -------------
`id` | string
`apiKey` | string
`prefix` | string
`label` | string
`createdAt` | Date

## Example

```typescript
import type { DriveApiKeyCreateOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "apiKey": null,
  "prefix": null,
  "label": null,
  "createdAt": null,
} satisfies DriveApiKeyCreateOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DriveApiKeyCreateOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


