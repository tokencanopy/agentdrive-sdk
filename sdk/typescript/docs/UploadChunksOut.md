
# UploadChunksOut

How to stream chunks against the session URI the initiation\'s ``Location`` disclosed: the unchanged ``gcs-xml-resumable`` protocol (PUT + ``Content-Range``, 308/``Range`` resume).

## Properties

Name | Type
------------ | -------------
`method` | string
`requiredHeaders` | { [key: string]: string; }

## Example

```typescript
import type { UploadChunksOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "method": null,
  "requiredHeaders": null,
} satisfies UploadChunksOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UploadChunksOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


