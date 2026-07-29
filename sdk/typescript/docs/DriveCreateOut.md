
# DriveCreateOut

The create response — the ONLY place (besides key-rotate) a raw `ad_live_` key is returned, reveal-once.

## Properties

Name | Type
------------ | -------------
`apiKey` | string
`createdAt` | Date
`id` | string
`name` | string
`organizationId` | string
`ownerEmail` | string
`ownerUserId` | string
`storageBytes` | number

## Example

```typescript
import type { DriveCreateOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "apiKey": null,
  "createdAt": null,
  "id": null,
  "name": null,
  "organizationId": null,
  "ownerEmail": null,
  "ownerUserId": null,
  "storageBytes": null,
} satisfies DriveCreateOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DriveCreateOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
