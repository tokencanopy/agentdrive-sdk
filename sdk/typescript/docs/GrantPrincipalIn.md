
# GrantPrincipalIn

Who a grant is for. `anyone` carries no id/email; `org`/`agent` require `id`; `user` requires exactly one of `id` / `email` (an email with no account becomes a pending-email invite resolved on sign-in).

## Properties

Name | Type
------------ | -------------
`email` | string
`id` | string
`type` | string

## Example

```typescript
import type { GrantPrincipalIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "email": null,
  "id": null,
  "type": null,
} satisfies GrantPrincipalIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GrantPrincipalIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
