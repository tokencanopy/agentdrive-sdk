
# ShareOut


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
`state` | string

## Example

```typescript
import type { ShareOut } from '@mnexa-ai/agentdrive-sdk'

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
  "state": null,
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
