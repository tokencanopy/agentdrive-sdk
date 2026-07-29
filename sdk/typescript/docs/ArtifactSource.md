
# ArtifactSource

Caller-supplied provenance metadata, attached to an artifact.  v0.6 model: a list of typed refs. The legacy v0.5 fields (`agent_id`, `run_id`, `prompt_hash`) were never validated and are superseded by the `refs` shape (an agent-id ref would be `{\"type\": \"agent\", \"id\": \"...\"}` in v0.6 vocabulary).

## Properties

Name | Type
------------ | -------------
`refs` | [Array&lt;SourceRef&gt;](SourceRef.md)

## Example

```typescript
import type { ArtifactSource } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "refs": null,
} satisfies ArtifactSource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ArtifactSource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
