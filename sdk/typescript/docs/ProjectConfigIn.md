
# ProjectConfigIn


## Properties

Name | Type
------------ | -------------
`autoCompile` | boolean
`engine` | string
`entrypoint` | string

## Example

```typescript
import type { ProjectConfigIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "autoCompile": null,
  "engine": null,
  "entrypoint": null,
} satisfies ProjectConfigIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProjectConfigIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
