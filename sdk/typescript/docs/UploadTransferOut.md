
# UploadTransferOut

The one-time external transfer disclosure (B3 §5.2, amended 2026-08-20 to the two-step browser-initiated shape). Secret material: present ONLY in the initial successful begin response, never in status, replay, or any stored record.

## Properties

Name | Type
------------ | -------------
`chunkProtocol` | string
`initiation` | [UploadInitiationOut](UploadInitiationOut.md)
`chunks` | [UploadChunksOut](UploadChunksOut.md)

## Example

```typescript
import type { UploadTransferOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "chunkProtocol": null,
  "initiation": null,
  "chunks": null,
} satisfies UploadTransferOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UploadTransferOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


