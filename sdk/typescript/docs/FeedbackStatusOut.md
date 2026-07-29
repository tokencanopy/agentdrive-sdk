
# FeedbackStatusOut

GET /v0/feedback/{fbk_id} response — lifecycle status of feedback THIS drive filed.

## Properties

Name | Type
------------ | -------------
`contact` | boolean
`createdAt` | Date
`duplicateOf` | string
`id` | string
`kind` | string
`status` | string
`statusChangedAt` | Date
`title` | string

## Example

```typescript
import type { FeedbackStatusOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "contact": null,
  "createdAt": null,
  "duplicateOf": null,
  "id": null,
  "kind": null,
  "status": null,
  "statusChangedAt": null,
  "title": null,
} satisfies FeedbackStatusOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FeedbackStatusOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
