
# GrantPatchIn

PATCH /v0/grants/{grn_id} body. Field absence = unchanged; explicit `expires_in: null` clears the expiry (makes the grant permanent).

## Properties

Name | Type
------------ | -------------
`expiresIn` | number
`role` | string

## Example

```typescript
import type { GrantPatchIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "expiresIn": null,
  "role": null,
} satisfies GrantPatchIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GrantPatchIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
