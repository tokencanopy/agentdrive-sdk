
# CompileDiagnosticOut


## Properties

Name | Type
------------ | -------------
`category` | string
`file` | string
`line` | number
`message` | string
`severity` | string
`suggestion` | string

## Example

```typescript
import type { CompileDiagnosticOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "category": null,
  "file": null,
  "line": null,
  "message": null,
  "severity": null,
  "suggestion": null,
} satisfies CompileDiagnosticOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CompileDiagnosticOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
