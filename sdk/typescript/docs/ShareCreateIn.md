
# ShareCreateIn

POST /v0/drives/{id}/shares body.

## Properties

Name | Type
------------ | -------------
`expiresAt` | Date
`resourceId` | string
`resourceType` | string

## Example

```typescript
import type { ShareCreateIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "expiresAt": null,
  "resourceId": null,
  "resourceType": null,
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
