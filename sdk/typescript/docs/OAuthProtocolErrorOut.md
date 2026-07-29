
# OAuthProtocolErrorOut

RFC OAuth error shape used by public protocol endpoints.

## Properties

Name | Type
------------ | -------------
`error` | string
`errorDescription` | string

## Example

```typescript
import type { OAuthProtocolErrorOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "error": null,
  "errorDescription": null,
} satisfies OAuthProtocolErrorOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OAuthProtocolErrorOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
