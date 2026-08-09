
# DriveUpdateIn

PATCH /v0/drives/{id} body — at least one field is required.

## Properties

Name | Type
------------ | -------------
`metadata` | { [key: string]: any; }
`name` | string

## Example

```typescript
import type { DriveUpdateIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "metadata": null,
  "name": null,
} satisfies DriveUpdateIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DriveUpdateIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
