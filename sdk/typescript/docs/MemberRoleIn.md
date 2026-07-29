
# MemberRoleIn

PATCH /v0/members/{user} body — promote/demote a member.

## Properties

Name | Type
------------ | -------------
`role` | string

## Example

```typescript
import type { MemberRoleIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "role": null,
} satisfies MemberRoleIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MemberRoleIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
