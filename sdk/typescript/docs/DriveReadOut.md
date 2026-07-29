
# DriveReadOut

Drive singleton shape returned by both data-plane read routes.

## Properties

Name | Type
------------ | -------------
`createdAt` | Date
`email` | string
`etag` | string
`id` | string
`metageneration` | number
`organizationId` | string
`storageBytes` | number
`storageLimit` | number

## Example

```typescript
import type { DriveReadOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "createdAt": null,
  "email": null,
  "etag": null,
  "id": null,
  "metageneration": null,
  "organizationId": null,
  "storageBytes": null,
  "storageLimit": null,
} satisfies DriveReadOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DriveReadOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
