
# IdentityAssertionMetadataOut


## Properties

Name | Type
------------ | -------------
`alg` | string
`iss` | string
`version` | number

## Example

```typescript
import type { IdentityAssertionMetadataOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "alg": null,
  "iss": null,
  "version": null,
} satisfies IdentityAssertionMetadataOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as IdentityAssertionMetadataOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
