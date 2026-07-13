
# DriveApiKeyListOut

`GET /v0/drives/{id}/keys` response — the drive\'s keys, oldest first (keyset order, design §3), including recently-revoked rows (filter on `revoked_at` for live only).  `items` is the canonical list field (B-3: one envelope key everywhere); `keys` is a deprecated same-value alias kept for one release — the REST twin of the grep `matches` / compile `jobs` aliases.

## Properties

Name | Type
------------ | -------------
`items` | [Array&lt;DriveApiKeyOut&gt;](DriveApiKeyOut.md)
`keys` | [Array&lt;DriveApiKeyOut&gt;](DriveApiKeyOut.md)
`nextCursor` | string

## Example

```typescript
import type { DriveApiKeyListOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "items": null,
  "keys": null,
  "nextCursor": null,
} satisfies DriveApiKeyListOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DriveApiKeyListOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


