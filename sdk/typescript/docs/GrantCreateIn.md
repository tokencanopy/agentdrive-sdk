
# GrantCreateIn

POST /v0/drives/{id}/grants body.

## Properties

Name | Type
------------ | -------------
`principalType` | string
`principalId` | string
`resourceType` | string
`resourceId` | string
`role` | string
`expiresAt` | Date

## Example

```typescript
import type { GrantCreateIn } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "principalType": null,
  "principalId": null,
  "resourceType": null,
  "resourceId": null,
  "role": null,
  "expiresAt": null,
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


