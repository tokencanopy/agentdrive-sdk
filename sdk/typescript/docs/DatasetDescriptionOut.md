
# DatasetDescriptionOut


## Properties

Name | Type
------------ | -------------
`columns` | [Array&lt;QueryColumnOut&gt;](QueryColumnOut.md)
`dataset` | string

## Example

```typescript
import type { DatasetDescriptionOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "columns": null,
  "dataset": null,
} satisfies DatasetDescriptionOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DatasetDescriptionOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
