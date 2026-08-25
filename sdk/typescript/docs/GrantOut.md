
# GrantOut


## Properties

Name | Type
------------ | -------------
`id` | string
`driveId` | string
`resourceType` | string
`resourceId` | string
`principalType` | string
`principalId` | string
`role` | string
`revision` | string
`state` | string
`expiresAt` | Date
`revokedAt` | Date
`createdAt` | Date

## Example

```typescript
import type { GrantOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "driveId": null,
  "resourceType": null,
  "resourceId": null,
  "principalType": null,
  "principalId": null,
  "role": null,
  "revision": null,
  "state": null,
  "expiresAt": null,
  "revokedAt": null,
  "createdAt": null,
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


