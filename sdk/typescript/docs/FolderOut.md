
# FolderOut


## Properties

Name | Type
------------ | -------------
`id` | string
`driveId` | string
`parentId` | string
`name` | string
`metadata` | { [key: string]: any; }
`revision` | string
`state` | string
`createdAt` | Date
`updatedAt` | Date
`deletedAt` | Date

## Example

```typescript
import type { FolderOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "driveId": null,
  "parentId": null,
  "name": null,
  "metadata": null,
  "revision": null,
  "state": null,
  "createdAt": null,
  "updatedAt": null,
  "deletedAt": null,
} satisfies FolderOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FolderOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


