
# TokenResponse

`POST /oauth2/token` success response. Mirrors RFC 6749 with an optional `identity_assertion` field for the claim grant path (where a fresh post-claim assertion supersedes the pre-claim one).

## Properties

Name | Type
------------ | -------------
`accessToken` | string
`expiresIn` | number
`identityAssertion` | string
`scope` | string
`tokenType` | string

## Example

```typescript
import type { TokenResponse } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "accessToken": null,
  "expiresIn": null,
  "identityAssertion": null,
  "scope": null,
  "tokenType": null,
} satisfies TokenResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as TokenResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
