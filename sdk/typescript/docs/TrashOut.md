
# TrashOut

Trash collection with a compatibility-preserving pagination opt-in.

## Properties

Name | Type
------------ | -------------
`artifacts` | [Array&lt;TrashArtifactOut&gt;](TrashArtifactOut.md)
`drive` | [TrashDriveOut](TrashDriveOut.md)
`items` | [Array&lt;TrashArtifactOut&gt;](TrashArtifactOut.md)
`nextCursor` | string

## Example

```typescript
import type { TrashOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "artifacts": null,
  "drive": null,
  "items": null,
  "nextCursor": null,
} satisfies TrashOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TrashOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
