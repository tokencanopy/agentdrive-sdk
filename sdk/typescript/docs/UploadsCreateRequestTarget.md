
# UploadsCreateRequestTarget

Exactly one destination union member.

## Properties

Name | Type
------------ | -------------
`kind` | string
`parentFolderId` | string
`name` | string
`artifactId` | string

## Example

```typescript
import type { UploadsCreateRequestTarget } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "kind": null,
  "parentFolderId": null,
  "name": null,
  "artifactId": null,
} satisfies UploadsCreateRequestTarget

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UploadsCreateRequestTarget
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


