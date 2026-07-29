
# CompileJobListOut


## Properties

Name | Type
------------ | -------------
`items` | [Array&lt;CompileJobOut&gt;](CompileJobOut.md)
`jobs` | [Array&lt;CompileJobOut&gt;](CompileJobOut.md)
`nextCursor` | string

## Example

```typescript
import type { CompileJobListOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "items": null,
  "jobs": null,
  "nextCursor": null,
} satisfies CompileJobListOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CompileJobListOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
