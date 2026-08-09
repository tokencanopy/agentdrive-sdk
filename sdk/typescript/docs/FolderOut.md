
# FolderOut


## Properties

Name | Type
------------ | -------------
`createdAt` | Date
`deletedAt` | Date
`driveId` | string
`grantInheritance` | string
`id` | string
`metadata` | { [key: string]: any; }
`name` | string
`parentId` | string
`revision` | string
`state` | string
`updatedAt` | Date

## Example

```typescript
import type { FolderOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "createdAt": null,
  "deletedAt": null,
  "driveId": null,
  "grantInheritance": null,
  "id": null,
  "metadata": null,
  "name": null,
  "parentId": null,
  "revision": null,
  "state": null,
  "updatedAt": null,
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
