
# GrantOut


## Properties

Name | Type
------------ | -------------
`createdAt` | Date
`driveId` | string
`expiresAt` | Date
`id` | string
`principalId` | string
`principalType` | string
`resourceId` | string
`resourceType` | string
`revision` | string
`revokedAt` | Date
`role` | string
`state` | string

## Example

```typescript
import type { GrantOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "createdAt": null,
  "driveId": null,
  "expiresAt": null,
  "id": null,
  "principalId": null,
  "principalType": null,
  "resourceId": null,
  "resourceType": null,
  "revision": null,
  "revokedAt": null,
  "role": null,
  "state": null,
} satisfies GrantOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GrantOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
