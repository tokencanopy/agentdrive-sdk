
# DownloadTargetOut

The one signed, generation-pinned direct GET target (B3 §5.7). Secret material: present only in the fresh mint response, never in any stored record, replay, or log. CLOSED schema on purpose: Packet 5 and generated clients must not learn a broader security-sensitive target contract than the wire actually carries.

## Properties

Name | Type
------------ | -------------
`url` | string
`method` | string
`requiredHeaders` | object
`contentDisposition` | string

## Example

```typescript
import type { DownloadTargetOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "url": null,
  "method": null,
  "requiredHeaders": null,
  "contentDisposition": null,
} satisfies DownloadTargetOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DownloadTargetOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


