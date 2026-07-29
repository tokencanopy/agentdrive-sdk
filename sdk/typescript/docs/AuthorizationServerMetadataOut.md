
# AuthorizationServerMetadataOut


## Properties

Name | Type
------------ | -------------
`agentAuth` | [AgentAuthMetadataOut](AgentAuthMetadataOut.md)
`authorizationEndpoint` | string
`authorizationResponseIssParameterSupported` | boolean
`codeChallengeMethodsSupported` | Array&lt;string&gt;
`grantTypesSupported` | Array&lt;string&gt;
`issuer` | string
`jwksUri` | string
`registrationEndpoint` | string
`responseModesSupported` | Array&lt;string&gt;
`responseTypesSupported` | Array&lt;string&gt;
`revocationEndpoint` | string
`revocationEndpointAuthMethodsSupported` | Array&lt;string&gt;
`scopesSupported` | Array&lt;string&gt;
`tokenEndpoint` | string
`tokenEndpointAuthMethodsSupported` | Array&lt;string&gt;

## Example

```typescript
import type { AuthorizationServerMetadataOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "agentAuth": null,
  "authorizationEndpoint": null,
  "authorizationResponseIssParameterSupported": null,
  "codeChallengeMethodsSupported": null,
  "grantTypesSupported": null,
  "issuer": null,
  "jwksUri": null,
  "registrationEndpoint": null,
  "responseModesSupported": null,
  "responseTypesSupported": null,
  "revocationEndpoint": null,
  "revocationEndpointAuthMethodsSupported": null,
  "scopesSupported": null,
  "tokenEndpoint": null,
  "tokenEndpointAuthMethodsSupported": null,
} satisfies AuthorizationServerMetadataOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AuthorizationServerMetadataOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
