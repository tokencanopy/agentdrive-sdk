
# ResponsePostQueryV0QueryPost


## Properties

Name | Type
------------ | -------------
`dryRun` | boolean
`engine` | string
`estimatedBytesProcessed` | number
`resultSchema` | [Array&lt;QueryColumnOut&gt;](QueryColumnOut.md)
`valid` | boolean
`bytesProcessed` | number
`cacheHit` | boolean
`preview` | Array&lt;{ [key: string]: any; }&gt;
`resultArtId` | string
`rowCount` | number

## Example

```typescript
import type { ResponsePostQueryV0QueryPost } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "dryRun": null,
  "engine": null,
  "estimatedBytesProcessed": null,
  "resultSchema": null,
  "valid": null,
  "bytesProcessed": null,
  "cacheHit": null,
  "preview": null,
  "resultArtId": null,
  "rowCount": null,
} satisfies ResponsePostQueryV0QueryPost

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ResponsePostQueryV0QueryPost
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
