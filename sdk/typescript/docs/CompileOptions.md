
# CompileOptions


## Properties

Name | Type
------------ | -------------
`engine` | string
`entrypoint` | string
`wait` | boolean

## Example

```typescript
import type { CompileOptions } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "engine": null,
  "entrypoint": null,
  "wait": null,
} satisfies CompileOptions

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CompileOptions
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
