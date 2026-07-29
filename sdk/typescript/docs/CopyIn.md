
# CopyIn

POST /v0/artifacts/{art_id}/copy body — duplicate to new path.

## Properties

Name | Type
------------ | -------------
`fromGeneration` | number
`path` | string
`source` | [ArtifactSource](ArtifactSource.md)

## Example

```typescript
import type { CopyIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "fromGeneration": null,
  "path": null,
  "source": null,
} satisfies CopyIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CopyIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
