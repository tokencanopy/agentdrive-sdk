
# ShareMintOut

The create/rotate response — the ONLY place the `share_key` and its redemption `url` are exposed.

## Properties

Name | Type
------------ | -------------
`accessCount` | number
`audience` | string
`createdAt` | Date
`expiresAt` | Date
`hasPassword` | boolean
`id` | string
`lastAccessedAt` | Date
`resourceId` | string
`resourceType` | string
`role` | string
`shareKey` | string
`url` | string

## Example

```typescript
import type { ShareMintOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "accessCount": null,
  "audience": null,
  "createdAt": null,
  "expiresAt": null,
  "hasPassword": null,
  "id": null,
  "lastAccessedAt": null,
  "resourceId": null,
  "resourceType": null,
  "role": null,
  "shareKey": null,
  "url": null,
} satisfies ShareMintOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ShareMintOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
