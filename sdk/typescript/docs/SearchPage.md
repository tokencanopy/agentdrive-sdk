
# SearchPage

`/v0/search` response — single-shot top-N, deliberately unpaginated.  Ranked retrieval doesn\'t paginate meaningfully (the industry norm: vector/RAG APIs are pure top-K; Algolia/GitHub cap ranked results outright) — the correct \"next page\" of a relevance-ranked list is a narrower query. Raise `limit` (≤100) for more hits. A `next_cursor` field advertised here in the past was structurally always null and was dropped; if deep retrieval is ever needed, an ES-`search_after` style `(score, id)` keyset can be re-added additively.

## Properties

Name | Type
------------ | -------------
`items` | [Array&lt;SearchHitOut&gt;](SearchHitOut.md)

## Example

```typescript
import type { SearchPage } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "items": null,
} satisfies SearchPage

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SearchPage
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


