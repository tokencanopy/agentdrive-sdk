
# V0ErrorEnvelope


## Properties

Name | Type
------------ | -------------
`error` | [ErrorResponseError](ErrorResponseError.md)

## Example

```typescript
import type { V0ErrorEnvelope } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "error": null,
} satisfies V0ErrorEnvelope

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as V0ErrorEnvelope
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


