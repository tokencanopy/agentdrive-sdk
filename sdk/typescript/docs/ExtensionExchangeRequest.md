
# ExtensionExchangeRequest

Single-use ticket → JWT pair. Called by `auth-complete.html` inside the SnipIt extension. No `Authorization` header — the ticket itself is the credential.

## Properties

Name | Type
------------ | -------------
`extId` | string
`ticket` | string

## Example

```typescript
import type { ExtensionExchangeRequest } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "extId": null,
  "ticket": null,
} satisfies ExtensionExchangeRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ExtensionExchangeRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
