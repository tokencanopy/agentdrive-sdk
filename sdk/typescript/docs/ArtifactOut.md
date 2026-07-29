
# ArtifactOut


## Properties

Name | Type
------------ | -------------
`contentType` | string
`createdAt` | Date
`driveId` | string
`embeddedAt` | Date
`etag` | string
`fileType` | string
`hash` | string
`id` | string
`indexedAt` | Date
`labels` | Array&lt;string&gt;
`llmIndex` | { [key: string]: any; }
`metadata` | { [key: string]: any; }
`metageneration` | number
`path` | string
`permalink` | string
`sizeBytes` | number
`source` | [ArtifactSource](ArtifactSource.md)
`updatedAt` | Date
`url` | string
`versionNumber` | number

## Example

```typescript
import type { ArtifactOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "contentType": null,
  "createdAt": null,
  "driveId": null,
  "embeddedAt": null,
  "etag": null,
  "fileType": null,
  "hash": null,
  "id": null,
  "indexedAt": null,
  "labels": null,
  "llmIndex": null,
  "metadata": null,
  "metageneration": null,
  "path": null,
  "permalink": null,
  "sizeBytes": null,
  "source": null,
  "updatedAt": null,
  "url": null,
  "versionNumber": null,
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
