
# UploadOut


## Properties

Name | Type
------------ | -------------
`id` | string
`driveId` | string
`state` | string
`target` | [Target](Target.md)
`content` | [UploadContentOut](UploadContentOut.md)
`expiresAt` | Date
`targetDisclosed` | boolean
`restartRequired` | boolean
`result` | [UploadResultOut](UploadResultOut.md)
`failure` | [UploadFailureOut](UploadFailureOut.md)
`cleanup` | [UploadCleanupOut](UploadCleanupOut.md)

## Example

```typescript
import type { UploadOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "driveId": null,
  "state": null,
  "target": null,
  "content": null,
  "expiresAt": null,
  "targetDisclosed": null,
  "restartRequired": null,
  "result": null,
  "failure": null,
  "cleanup": null,
} satisfies UploadOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UploadOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


