
# WorkspaceOut

One workspace in a listing — metadata only. `role` is the CALLER\'s role in it (admin/member), so a client can render management affordances without a second round-trip.

## Properties

Name | Type
------------ | -------------
`createdAt` | Date
`id` | string
`name` | string
`role` | string
`tierId` | string

## Example

```typescript
import type { WorkspaceOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "createdAt": null,
  "id": null,
  "name": null,
  "role": null,
  "tierId": null,
} satisfies WorkspaceOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WorkspaceOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
