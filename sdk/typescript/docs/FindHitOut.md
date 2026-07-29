
# FindHitOut

One passage-level hit from `/v0/find` (hybrid chunk RAG over `embed_chunks`). The unit is a passage, not a file — consecutive `ord` values from the same `art_id` are normal because chunks overlap by ~400 tokens. Span fields are modality-aware: only the pair matching `modality` is populated, the others stay None.

## Properties

Name | Type
------------ | -------------
`artId` | string
`charEnd` | number
`charStart` | number
`contentType` | string
`driveId` | string
`fileType` | string
`labels` | Array&lt;string&gt;
`modality` | string
`ord` | number
`pageEnd` | number
`pageStart` | number
`path` | string
`rankLexical` | number
`rankSemantic` | number
`score` | number
`snippet` | string
`text` | string
`timeEndMs` | number
`timeStartMs` | number
`updatedAt` | Date
`url` | string
`versionNumber` | number

## Example

```typescript
import type { FindHitOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "artId": null,
  "charEnd": null,
  "charStart": null,
  "contentType": null,
  "driveId": null,
  "fileType": null,
  "labels": null,
  "modality": null,
  "ord": null,
  "pageEnd": null,
  "pageStart": null,
  "path": null,
  "rankLexical": null,
  "rankSemantic": null,
  "score": null,
  "snippet": null,
  "text": null,
  "timeEndMs": null,
  "timeStartMs": null,
  "updatedAt": null,
  "url": null,
  "versionNumber": null,
} satisfies FindHitOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FindHitOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
