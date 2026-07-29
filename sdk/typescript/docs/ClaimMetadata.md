
# ClaimMetadata

Hints the agent\'s UI/CLI can use when initiating the claim ceremony. Decoupled from the `claim_token` itself so future additions don\'t change the token\'s shape.

## Properties

Name | Type
------------ | -------------
`claimEndpoint` | string
`supportedEmailHints` | boolean

## Example

```typescript
import type { ClaimMetadata } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "claimEndpoint": null,
  "supportedEmailHints": null,
} satisfies ClaimMetadata

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ClaimMetadata
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
