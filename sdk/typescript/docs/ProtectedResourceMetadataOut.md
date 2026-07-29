
# ProtectedResourceMetadataOut


## Properties

Name | Type
------------ | -------------
`authorizationServers` | Array&lt;string&gt;
`bearerMethodsSupported` | Array&lt;string&gt;
`resource` | string
`scopesSupported` | Array&lt;string&gt;

## Example

```typescript
import type { ProtectedResourceMetadataOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "authorizationServers": null,
  "bearerMethodsSupported": null,
  "resource": null,
  "scopesSupported": null,
} satisfies ProtectedResourceMetadataOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProtectedResourceMetadataOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
