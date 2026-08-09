
# ShareCreateOut

The create/rotate response — the ONLY response carrying the plaintext secret.

## Properties

Name | Type
------------ | -------------
`createdAt` | Date
`createdBy` | string
`driveId` | string
`expiresAt` | Date
`id` | string
`resourceId` | string
`resourceType` | string
`revision` | string
`revokedAt` | Date
`rotatedAt` | Date
`secret` | string
`state` | string

## Example

```typescript
import type { ShareCreateOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "createdAt": null,
  "createdBy": null,
  "driveId": null,
  "expiresAt": null,
  "id": null,
  "resourceId": null,
  "resourceType": null,
  "revision": null,
  "revokedAt": null,
  "rotatedAt": null,
  "secret": null,
  "state": null,
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
