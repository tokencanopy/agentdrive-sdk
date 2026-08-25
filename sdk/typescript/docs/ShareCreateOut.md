
# ShareCreateOut

The create/rotate response — the ONLY response carrying the plaintext secret.

## Properties

Name | Type
------------ | -------------
`id` | string
`driveId` | string
`resourceType` | string
`resourceId` | string
`createdBy` | string
`revision` | string
`state` | string
`expiresAt` | Date
`revokedAt` | Date
`createdAt` | Date
`rotatedAt` | Date
`secret` | string

## Example

```typescript
import type { ShareCreateOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "driveId": null,
  "resourceType": null,
  "resourceId": null,
  "createdBy": null,
  "revision": null,
  "state": null,
  "expiresAt": null,
  "revokedAt": null,
  "createdAt": null,
  "rotatedAt": null,
  "secret": null,
} satisfies ShareCreateOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ShareCreateOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


