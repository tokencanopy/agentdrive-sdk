
# ArtifactOut


## Properties

Name | Type
------------ | -------------
`id` | string
`driveId` | string
`path` | string
`url` | string
`permalink` | string
`contentType` | string
`fileType` | string
`sizeBytes` | number
`hash` | string
`versionNumber` | number
`metageneration` | number
`etag` | string
`labels` | Array&lt;string&gt;
`metadata` | { [key: string]: any; }
`source` | [ArtifactSource](ArtifactSource.md)
`indexedAt` | Date
`embeddedAt` | Date
`createdAt` | Date
`updatedAt` | Date
`llmIndex` | { [key: string]: any; }

## Example

```typescript
import type { ArtifactOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "driveId": null,
  "path": null,
  "url": null,
  "permalink": null,
  "contentType": null,
  "fileType": null,
  "sizeBytes": null,
  "hash": null,
  "versionNumber": null,
  "metageneration": null,
  "etag": null,
  "labels": null,
  "metadata": null,
  "source": null,
  "indexedAt": null,
  "embeddedAt": null,
  "createdAt": null,
  "updatedAt": null,
  "llmIndex": null,
} satisfies ArtifactOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ArtifactOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


