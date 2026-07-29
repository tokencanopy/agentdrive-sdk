
# DownloadUrlOut

A URL the caller can GET to fetch the artifact\'s bytes.  `direct=True` ⇒ a short-lived signed GCS URL on `storage.googleapis.com` (client downloads straight from GCS; `expires_at` is set). `direct=False` ⇒ the proxy `/download` endpoint on the API host (no expiry) — returned for sub-threshold artifacts or when signing is unavailable. The URL is opaque: callers should not parse it. See large-download-design.md §5.1.

## Properties

Name | Type
------------ | -------------
`contentType` | string
`direct` | boolean
`downloadUrl` | string
`expiresAt` | Date
`filename` | string
`sizeBytes` | number

## Example

```typescript
import type { DownloadUrlOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "contentType": null,
  "direct": null,
  "downloadUrl": null,
  "expiresAt": null,
  "filename": null,
  "sizeBytes": null,
} satisfies DownloadUrlOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DownloadUrlOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
