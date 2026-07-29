
# DriveRestoreOut


## Properties

Name | Type
------------ | -------------
`id` | string
`rebasedArtifactCount` | number
`restoredAt` | Date

## Example

```typescript
import type { DriveRestoreOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "rebasedArtifactCount": null,
  "restoredAt": null,
} satisfies DriveRestoreOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DriveRestoreOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
