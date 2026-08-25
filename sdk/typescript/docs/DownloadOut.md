
# DownloadOut


## Properties

Name | Type
------------ | -------------
`artifactId` | string
`versionId` | string
`expiresAt` | Date
`target` | [DownloadTargetOut](DownloadTargetOut.md)

## Example

```typescript
import type { DownloadOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "artifactId": null,
  "versionId": null,
  "expiresAt": null,
  "target": null,
} satisfies DownloadOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DownloadOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


