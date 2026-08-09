
# ArtifactOut


## Properties

Name | Type
------------ | -------------
`contentPreview` | string
`contentType` | string
`createdAt` | Date
`deletedAt` | Date
`driveId` | string
`effectiveVisibility` | string
`headVersionId` | string
`id` | string
`labels` | Array&lt;string&gt;
`metadata` | { [key: string]: any; }
`name` | string
`parentId` | string
`revision` | string
`state` | string
`updatedAt` | Date

## Example

```typescript
import type { ArtifactOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "contentPreview": null,
  "contentType": null,
  "createdAt": null,
  "deletedAt": null,
  "driveId": null,
  "effectiveVisibility": null,
  "headVersionId": null,
  "id": null,
  "labels": null,
  "metadata": null,
  "name": null,
  "parentId": null,
  "revision": null,
  "state": null,
  "updatedAt": null,
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
