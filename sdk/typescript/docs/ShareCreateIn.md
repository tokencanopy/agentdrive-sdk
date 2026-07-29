
# ShareCreateIn

POST /v0/shares body. `resource` is an `art_*`/`fld_*` id or a path. `expires_in` is seconds from now (omit for the default: none for a human creator, a short TTL for an agent). `password` (optional) gates redemption.

## Properties

Name | Type
------------ | -------------
`expiresIn` | number
`password` | string
`resource` | string
`role` | string

## Example

```typescript
import type { ShareCreateIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "expiresIn": null,
  "password": null,
  "resource": null,
  "role": null,
} satisfies ShareCreateIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ShareCreateIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
