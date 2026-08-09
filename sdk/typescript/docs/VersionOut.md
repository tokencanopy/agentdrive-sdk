
# VersionOut


## Properties

Name | Type
------------ | -------------
`artifactId` | string
`contentType` | string
`createdAt` | Date
`createdBy` | string
`hash` | string
`id` | string
`parentVersionId` | string
`sizeBytes` | number
`versionNumber` | number

## Example

```typescript
import type { VersionOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "artifactId": null,
  "contentType": null,
  "createdAt": null,
  "createdBy": null,
  "hash": null,
  "id": null,
  "parentVersionId": null,
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
