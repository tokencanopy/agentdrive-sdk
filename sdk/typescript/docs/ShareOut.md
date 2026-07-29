
# ShareOut

A live share link as seen on list/management — NEVER carries the `share_key` (that is the credential, returned only at mint/rotate).

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

## Example

```typescript
import type { ShareOut } from '@mnexa-ai/agentdrive-sdk'

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
} satisfies ShareOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ShareOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
