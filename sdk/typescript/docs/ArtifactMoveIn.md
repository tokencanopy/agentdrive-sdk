
# ArtifactMoveIn

POST /v0/artifacts/{art_id}/move body — rename / move to a new path on the same drive. Mirrors `FolderMoveIn`; its own schema (vs. reusing another body) keeps the move surface self-documenting in the OpenAPI spec.

## Properties

Name | Type
------------ | -------------
`path` | string

## Example

```typescript
import type { ArtifactMoveIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "path": null,
} satisfies ArtifactMoveIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ArtifactMoveIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


