
# ShareCreateIn

POST /v0/drives/{id}/shares body.

## Properties

Name | Type
------------ | -------------
`resourceType` | string
`resourceId` | string
`expiresAt` | Date

## Example

```typescript
import type { ShareCreateIn } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "resourceType": null,
  "resourceId": null,
  "expiresAt": null,
} satisfies ShareCreateIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ShareCreateIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


