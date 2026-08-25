
# UploadInitiationOut

The V4-signed XML resumable initiation target (§5.6 as amended 2026-08-20). Secret material: the URL plus the exact signed header values. The client POSTs it with EXACTLY ``required_headers`` and an empty body; the 201 response\'s ``Location`` header is the resumable session URI. CLOSED schema on purpose — a generated client must not learn a broader security-sensitive target contract than the wire carries.

## Properties

Name | Type
------------ | -------------
`url` | string
`method` | string
`requiredHeaders` | { [key: string]: string; }
`expiresAt` | Date

## Example

```typescript
import type { UploadInitiationOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "url": null,
  "method": null,
  "requiredHeaders": null,
  "expiresAt": null,
} satisfies UploadInitiationOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UploadInitiationOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


