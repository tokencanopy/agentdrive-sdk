
# MemberOut

One live member of a workspace — metadata for the members page / `GET /v0/members`.

## Properties

Name | Type
------------ | -------------
`createdAt` | Date
`email` | string
`firstName` | string
`lastName` | string
`role` | string
`userId` | string

## Example

```typescript
import type { MemberOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "createdAt": null,
  "email": null,
  "firstName": null,
  "lastName": null,
  "role": null,
  "userId": null,
} satisfies MemberOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MemberOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
