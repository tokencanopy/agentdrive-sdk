
# UploadBeginOut

Response of `POST /v0/uploads`. PUT the bytes to `upload_url` (no auth header — the URL is the credential), then `POST .../commit`.

## Properties

Name | Type
------------ | -------------
`expiresAt` | Date
`headers` | { [key: string]: string; }
`maxBytes` | number
`method` | string
`uploadId` | string
`uploadUrl` | string

## Example

```typescript
import type { UploadBeginOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "expiresAt": null,
  "headers": null,
  "maxBytes": null,
  "method": null,
  "uploadId": null,
  "uploadUrl": null,
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
