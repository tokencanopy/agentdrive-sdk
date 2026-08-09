
# GrantUpdateIn

PATCH /v0/drives/{id}/grants/{grant_id} body — at least one field is required. An explicit ``expires_at: null`` clears the expiry; omitting it leaves it unchanged.

## Properties

Name | Type
------------ | -------------
`expiresAt` | Date
`role` | string

## Example

```typescript
import type { GrantUpdateIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "expiresAt": null,
  "role": null,
} satisfies GrantUpdateIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GrantUpdateIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
