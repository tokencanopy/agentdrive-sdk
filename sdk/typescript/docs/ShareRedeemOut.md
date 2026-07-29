
# ShareRedeemOut


## Properties

Name | Type
------------ | -------------
`expiresAt` | Date
`role` | string
`token` | string
`url` | string

## Example

```typescript
import type { ShareRedeemOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "expiresAt": null,
  "role": null,
  "token": null,
  "url": null,
} satisfies ShareRedeemOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ShareRedeemOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
