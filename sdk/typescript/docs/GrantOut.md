
# GrantOut

A live grant. Audit fields (`granted_by_*`, `on_behalf_of`) are surfaced so a manager can see who shared what.

## Properties

Name | Type
------------ | -------------
`artifactsAffected` | number
`createdAt` | Date
`expiresAt` | Date
`grantedById` | string
`grantedByType` | string
`id` | string
`onBehalfOf` | string
`principalEmail` | string
`principalId` | string
`principalType` | string
`resourceId` | string
`resourceType` | string
`role` | string

## Example

```typescript
import type { GrantOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "artifactsAffected": null,
  "createdAt": null,
  "expiresAt": null,
  "grantedById": null,
  "grantedByType": null,
  "id": null,
  "onBehalfOf": null,
  "principalEmail": null,
  "principalId": null,
  "principalType": null,
  "resourceId": null,
  "resourceType": null,
  "role": null,
} satisfies GrantOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as GrantOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
