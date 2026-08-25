
# EntriesInner


## Properties

Name | Type
------------ | -------------
`type` | string
`id` | string
`name` | string
`revision` | string
`updatedAt` | Date
`state` | string
`deletedAt` | Date
`sizeBytes` | number
`contentType` | string
`headVersionId` | string

## Example

```typescript
import type { EntriesInner } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "type": null,
  "id": null,
  "name": null,
  "revision": null,
  "updatedAt": null,
  "state": null,
  "deletedAt": null,
  "sizeBytes": null,
  "contentType": null,
  "headVersionId": null,
} satisfies EntriesInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EntriesInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


