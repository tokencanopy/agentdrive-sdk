
# QueryResultOut


## Properties

Name | Type
------------ | -------------
`bytesProcessed` | number
`cacheHit` | boolean
`engine` | string
`preview` | Array&lt;{ [key: string]: any; } | null&gt;
`resultArtId` | string
`resultSchema` | [Array&lt;QueryColumnOut&gt;](QueryColumnOut.md)
`rowCount` | number

## Example

```typescript
import type { QueryResultOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "bytesProcessed": null,
  "cacheHit": null,
  "engine": null,
  "preview": null,
  "resultArtId": null,
  "resultSchema": null,
  "rowCount": null,
} satisfies QueryResultOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as QueryResultOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
