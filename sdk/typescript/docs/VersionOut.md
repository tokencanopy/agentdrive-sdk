
# VersionOut


## Properties

Name | Type
------------ | -------------
`actorName` | string
`artId` | string
`changeSummary` | string
`contentType` | string
`createdAt` | Date
`hash` | string
`sizeBytes` | number
`versionNumber` | number

## Example

```typescript
import type { VersionOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "actorName": null,
  "artId": null,
  "changeSummary": null,
  "contentType": null,
  "createdAt": null,
  "hash": null,
  "sizeBytes": null,
  "versionNumber": null,
} satisfies VersionOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as VersionOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
