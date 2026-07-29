
# UserTokenOut

One `ad_user_` token — metadata only. The raw token is NEVER exposed over the API (minting is web-only, reveal-once); this shape omits both the raw value and the stored hash by construction.

## Properties

Name | Type
------------ | -------------
`createdAt` | Date
`defaultDriveId` | string
`expiresAt` | Date
`id` | string
`label` | string
`lastUsedAt` | Date
`prefix` | string
`revokedAt` | Date
`scope` | string

## Example

```typescript
import type { UserTokenOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "createdAt": null,
  "defaultDriveId": null,
  "expiresAt": null,
  "id": null,
  "label": null,
  "lastUsedAt": null,
  "prefix": null,
  "revokedAt": null,
  "scope": null,
} satisfies UserTokenOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UserTokenOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
