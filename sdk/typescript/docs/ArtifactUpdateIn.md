
# ArtifactUpdateIn

PATCH /v0/drives/{id}/artifacts/{artifact_id} body — at least one field is required.

## Properties

Name | Type
------------ | -------------
`name` | string
`parentId` | string
`metadata` | { [key: string]: any; }
`labels` | Array&lt;string&gt;

## Example

```typescript
import type { ArtifactUpdateIn } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "parentId": null,
  "metadata": null,
  "labels": null,
} satisfies ArtifactUpdateIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ArtifactUpdateIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


