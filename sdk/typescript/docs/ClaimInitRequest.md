
# ClaimInitRequest

`POST /agent/identity/claim` body.

## Properties

Name | Type
------------ | -------------
`claimToken` | string
`email` | string

## Example

```typescript
import type { ClaimInitRequest } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "claimToken": null,
  "email": null,
} satisfies ClaimInitRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ClaimInitRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
