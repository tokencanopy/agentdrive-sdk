
# UploadBeginOut

The one 201 begin response — the only shape carrying ``transfer``.

## Properties

Name | Type
------------ | -------------
`upload` | [UploadWithTransferOut](UploadWithTransferOut.md)

## Example

```typescript
import type { UploadBeginOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "upload": null,
} satisfies UploadBeginOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UploadBeginOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


