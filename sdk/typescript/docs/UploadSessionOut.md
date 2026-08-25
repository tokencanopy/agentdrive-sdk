
# UploadSessionOut

The non-secret session representation (status, replay, cancel, complete). Deliberately has NO transfer field — it is structurally incapable of carrying the bearer target.

## Properties

Name | Type
------------ | -------------
`upload` | [UploadOut](UploadOut.md)

## Example

```typescript
import type { UploadSessionOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "upload": null,
} satisfies UploadSessionOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UploadSessionOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


