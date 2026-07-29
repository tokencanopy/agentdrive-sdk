
# JwkOut


## Properties

Name | Type
------------ | -------------
`alg` | string
`e` | string
`kid` | string
`kty` | string
`n` | string
`use` | string

## Example

```typescript
import type { JwkOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "alg": null,
  "e": null,
  "kid": null,
  "kty": null,
  "n": null,
  "use": null,
} satisfies JwkOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as JwkOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
