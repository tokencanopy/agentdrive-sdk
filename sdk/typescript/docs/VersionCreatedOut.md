
# VersionCreatedOut

The append/restore response — a version plus the artifact\'s new revision, which the version-creating 201 rotates.

## Properties

Name | Type
------------ | -------------
`id` | string
`artifactId` | string
`versionNumber` | number
`parentVersionId` | string
`contentType` | string
`sizeBytes` | number
`hash` | string
`createdBy` | string
`createdAt` | Date
`artifactRevision` | string

## Example

```typescript
import type { VersionCreatedOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "artifactId": null,
  "versionNumber": null,
  "parentVersionId": null,
  "contentType": null,
  "sizeBytes": null,
  "hash": null,
  "createdBy": null,
  "createdAt": null,
  "artifactRevision": null,
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


