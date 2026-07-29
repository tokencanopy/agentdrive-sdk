
# StorageBreakdownOut


## Properties

Name | Type
------------ | -------------
`asOf` | Date
`liveBytes` | number
`trashBytes` | number
`versionBytes` | number

## Example

```typescript
import type { StorageBreakdownOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "asOf": null,
  "liveBytes": null,
  "trashBytes": null,
  "versionBytes": null,
} satisfies StorageBreakdownOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StorageBreakdownOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
