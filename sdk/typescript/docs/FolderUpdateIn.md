
# FolderUpdateIn

PATCH /v0/drives/{id}/folders/{folder_id} body — at least one field is required.

## Properties

Name | Type
------------ | -------------
`grantInheritance` | string
`metadata` | { [key: string]: any; }
`name` | string
`parentId` | string

## Example

```typescript
import type { FolderUpdateIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "grantInheritance": null,
  "metadata": null,
  "name": null,
  "parentId": null,
} satisfies FolderUpdateIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FolderUpdateIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
