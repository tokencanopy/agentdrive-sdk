
# MemberRemoveOut

DELETE /v0/members/{user_id} response — the member-removal receipt. `id` is the removed user\'s id (replaces the ad-hoc `removed` key).

## Properties

Name | Type
------------ | -------------
`id` | string
`ok` | boolean
`organizationId` | string

## Example

```typescript
import type { MemberRemoveOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "ok": null,
  "organizationId": null,
} satisfies MemberRemoveOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MemberRemoveOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
