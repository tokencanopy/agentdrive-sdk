
# FindPage

`/v0/find` response — single-shot top-N, deliberately unpaginated (same contract + rationale as `SearchPage`).

## Properties

Name | Type
------------ | -------------
`items` | [Array&lt;FindHitOut&gt;](FindHitOut.md)

## Example

```typescript
import type { FindPage } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "items": null,
} satisfies FindPage

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FindPage
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
