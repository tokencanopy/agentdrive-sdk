
# RevokeOut

DELETE /v0/grants/{grn_id}, DELETE /v0/shares/{shr_id}, DELETE /v0/invitations/{invitation_id} response — the unified revoke receipt. `revoked` is a COUNT: 1 when a live row was revoked, 0 when it was already gone (DELETE is idempotent).

## Properties

Name | Type
------------ | -------------
`ok` | boolean
`id` | string
`revoked` | number

## Example

```typescript
import type { RevokeOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "ok": null,
  "id": null,
  "revoked": null,
} satisfies RevokeOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RevokeOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


