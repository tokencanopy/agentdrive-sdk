
# FolderEntryOut

Compact D13 folder member returned by the unified namespace list.

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

## Example

```typescript
import type { FolderEntryOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "type": null,
  "id": null,
  "name": null,
  "revision": null,
  "updatedAt": null,
  "state": null,
  "deletedAt": null,
} satisfies FolderEntryOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FolderEntryOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


