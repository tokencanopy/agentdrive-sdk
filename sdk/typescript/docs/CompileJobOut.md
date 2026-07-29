
# CompileJobOut


## Properties

Name | Type
------------ | -------------
`cacheHit` | boolean
`diagnostics` | [Array&lt;CompileDiagnosticOut&gt;](CompileDiagnosticOut.md)
`durationMs` | number
`engine` | string
`jobId` | string
`logsUrl` | string
`output` | { [key: string]: any; }
`status` | string
`task` | string

## Example

```typescript
import type { CompileJobOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "cacheHit": null,
  "diagnostics": null,
  "durationMs": null,
  "engine": null,
  "jobId": null,
  "logsUrl": null,
  "output": null,
  "status": null,
  "task": null,
} satisfies CompileJobOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CompileJobOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
