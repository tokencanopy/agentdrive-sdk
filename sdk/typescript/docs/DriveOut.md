
# DriveOut

One drive in a listing — metadata only (workspaces-design §4.2). Carries NO capability and NEVER a raw key. An admin\'s inventory and a member\'s owned list both serialize to this shape; `owner_email` is the only owner-identifying field surfaced.

## Properties

Name | Type
------------ | -------------
`createdAt` | Date
`id` | string
`name` | string
`organizationId` | string
`ownerEmail` | string
`ownerUserId` | string
`storageBytes` | number

## Example

```typescript
import type { DriveOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "createdAt": null,
  "id": null,
  "name": null,
  "organizationId": null,
  "ownerEmail": null,
  "ownerUserId": null,
  "storageBytes": null,
} satisfies DriveOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DriveOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
