
# InvitationOut

One workspace invitation — metadata only; the raw token is never surfaced over the API (it lives only in the invite email).

## Properties

Name | Type
------------ | -------------
`createdAt` | Date
`email` | string
`expiresAt` | Date
`id` | string
`invitedBy` | string
`organizationId` | string
`role` | string
`status` | string

## Example

```typescript
import type { InvitationOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "createdAt": null,
  "email": null,
  "expiresAt": null,
  "id": null,
  "invitedBy": null,
  "organizationId": null,
  "role": null,
  "status": null,
} satisfies InvitationOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as InvitationOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
