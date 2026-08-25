
# FolderCreateIn

POST /v0/drives/{id}/folders body.

## Properties

Name | Type
------------ | -------------
`parentId` | string
`name` | string
`metadata` | { [key: string]: any; }

## Example

```typescript
import type { FolderCreateIn } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "parentId": null,
  "name": null,
  "metadata": null,
} satisfies FolderCreateIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FolderCreateIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


