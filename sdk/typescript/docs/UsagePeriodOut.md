
# UsagePeriodOut


## Properties

Name | Type
------------ | -------------
`ends` | Date
`starts` | Date
`yearMonth` | string

## Example

```typescript
import type { UsagePeriodOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "ends": null,
  "starts": null,
  "yearMonth": null,
} satisfies UsagePeriodOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UsagePeriodOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
