
# UploadAbortOut

Response of `DELETE /v0/uploads/{upload_id}` — the session is released. `released_bytes` is the reservation returned to the drive\'s quota (the session\'s `size_bytes` for a live `initiated` session; `0` when the session was already aborted or already expired — the GC sweep owns an expired session\'s release).

## Properties

Name | Type
------------ | -------------
`releasedBytes` | number
`state` | string
`uploadId` | string

## Example

```typescript
import type { UploadAbortOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "releasedBytes": null,
  "state": null,
  "uploadId": null,
} satisfies UploadAbortOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UploadAbortOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
