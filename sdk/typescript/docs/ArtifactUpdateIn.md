
# ArtifactUpdateIn

PATCH /v0/drives/{id}/artifacts/{artifact_id} body — at least one field is required.

## Properties

Name | Type
------------ | -------------
`labels` | Array&lt;string&gt;
`metadata` | { [key: string]: any; }
`name` | string
`parentId` | string

## Example

```typescript
import type { ArtifactUpdateIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "labels": null,
  "metadata": null,
  "name": null,
  "parentId": null,
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
