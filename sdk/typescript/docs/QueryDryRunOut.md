
# QueryDryRunOut


## Properties

Name | Type
------------ | -------------
`dryRun` | boolean
`engine` | string
`estimatedBytesProcessed` | number
`resultSchema` | [Array&lt;QueryColumnOut&gt;](QueryColumnOut.md)
`valid` | boolean

## Example

```typescript
import type { QueryDryRunOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "dryRun": null,
  "engine": null,
  "estimatedBytesProcessed": null,
  "resultSchema": null,
  "valid": null,
} satisfies QueryDryRunOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as QueryDryRunOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
