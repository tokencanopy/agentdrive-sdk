
# ClaimInitResponse


## Properties

Name | Type
------------ | -------------
`claimAttemptToken` | string
`expiresAt` | Date
`userCode` | string
`verificationUri` | string
`verificationUriComplete` | string

## Example

```typescript
import type { ClaimInitResponse } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "claimAttemptToken": null,
  "expiresAt": null,
  "userCode": null,
  "verificationUri": null,
  "verificationUriComplete": null,
} satisfies ClaimInitResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ClaimInitResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
