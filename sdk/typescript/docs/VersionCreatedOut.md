
# VersionCreatedOut

The append/restore response — a version plus the artifact\'s new revision, which the version-creating 201 rotates.

## Properties

Name | Type
------------ | -------------
`artifactId` | string
`artifactRevision` | string
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
import type { VersionCreatedOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "artifactId": null,
  "artifactRevision": null,
  "contentType": null,
  "createdAt": null,
  "createdBy": null,
  "hash": null,
  "id": null,
  "parentVersionId": null,
  "sizeBytes": null,
  "versionNumber": null,
} satisfies VersionCreatedOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as VersionCreatedOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
