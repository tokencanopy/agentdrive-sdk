
# FolderCascadeOut


## Properties

Name | Type
------------ | -------------
`cascade` | { [key: string]: number; }
`folder` | [FolderOut](FolderOut.md)

## Example

```typescript
import type { FolderCascadeOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "cascade": null,
  "folder": null,
} satisfies FolderCascadeOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FolderCascadeOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
