
# ArtifactOut


## Properties

Name | Type
------------ | -------------
`id` | string
`driveId` | string
`parentId` | string
`name` | string
`contentType` | string
`contentPreview` | string
`labels` | Array&lt;string&gt;
`metadata` | { [key: string]: any; }
`headVersionId` | string
`revision` | string
`state` | string
`createdAt` | Date
`updatedAt` | Date
`deletedAt` | Date
`effectiveVisibility` | string

## Example

```typescript
import type { ArtifactOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "driveId": null,
  "parentId": null,
  "name": null,
  "contentType": null,
  "contentPreview": null,
  "labels": null,
  "metadata": null,
  "headVersionId": null,
  "revision": null,
  "state": null,
  "createdAt": null,
  "updatedAt": null,
  "deletedAt": null,
  "effectiveVisibility": null,
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


