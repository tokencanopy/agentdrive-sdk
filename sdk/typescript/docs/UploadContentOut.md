
# UploadContentOut


## Properties

Name | Type
------------ | -------------
`sizeBytes` | number
`mediaType` | string
`checksum` | [UploadChecksumOut](UploadChecksumOut.md)

## Example

```typescript
import type { UploadContentOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "sizeBytes": null,
  "mediaType": null,
  "checksum": null,
} satisfies UploadContentOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UploadContentOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


