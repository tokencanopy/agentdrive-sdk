
# WorkspaceCreateIn

POST /v0/workspaces body. `name` is the user-facing workspace label; the creator becomes its admin and gets a starter drive.

## Properties

Name | Type
------------ | -------------
`name` | string

## Example

```typescript
import type { WorkspaceCreateIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "name": null,
} satisfies WorkspaceCreateIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WorkspaceCreateIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
