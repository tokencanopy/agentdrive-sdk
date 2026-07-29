
# FolderCopyIn

POST /v0/folders/{fld_id}/copy body — duplicate the subtree to a new path. `path` is the target folder path (canonical, trailing slash). Its own schema (vs. reusing `FolderMoveIn`) keeps the copy surface self-documenting in the OpenAPI spec.

## Properties

Name | Type
------------ | -------------
`fromMetageneration` | number
`path` | string

## Example

```typescript
import type { FolderCopyIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "fromMetageneration": null,
  "path": null,
} satisfies FolderCopyIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FolderCopyIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
