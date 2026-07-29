
# AgentAuthMetadataOut


## Properties

Name | Type
------------ | -------------
`claimEndpoint` | string
`eventsEndpoint` | string
`identityAssertion` | [IdentityAssertionMetadataOut](IdentityAssertionMetadataOut.md)
`identityEndpoint` | string
`identityTypesSupported` | Array&lt;string&gt;
`skill` | string
`specVersion` | string

## Example

```typescript
import type { AgentAuthMetadataOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "claimEndpoint": null,
  "eventsEndpoint": null,
  "identityAssertion": null,
  "identityEndpoint": null,
  "identityTypesSupported": null,
  "skill": null,
  "specVersion": null,
} satisfies AgentAuthMetadataOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AgentAuthMetadataOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
