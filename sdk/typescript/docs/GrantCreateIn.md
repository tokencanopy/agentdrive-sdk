
# GrantCreateIn

POST /v0/drives/{id}/grants body.

## Properties

Name | Type
------------ | -------------
`expiresAt` | Date
`principalId` | string
`principalType` | string
`resourceId` | string
`resourceType` | string
`role` | string

## Example

```typescript
import type { GrantCreateIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "expiresAt": null,
  "principalId": null,
  "principalType": null,
  "resourceId": null,
  "resourceType": null,
  "role": null,
} satisfies GrantCreateIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GrantCreateIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
