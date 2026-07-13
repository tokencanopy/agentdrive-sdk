
# FolderCreateIn

PUT /v0/folders/{path} body for the optional metadata params. Empty body is fine — `mkdir` with no description just creates the folder row.

## Properties

Name | Type
------------ | -------------
`description` | string

## Example

```typescript
import type { FolderCreateIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "description": null,
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


