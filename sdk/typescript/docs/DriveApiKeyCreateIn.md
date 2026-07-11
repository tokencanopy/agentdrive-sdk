
# DriveApiKeyCreateIn

`POST /v0/drives/{id}/keys` body — a required human label (a name for the key, e.g. the agent/integration it\'s for).

## Properties

Name | Type
------------ | -------------
`label` | string

## Example

```typescript
import type { DriveApiKeyCreateIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "label": null,
} satisfies DriveApiKeyCreateIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DriveApiKeyCreateIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


