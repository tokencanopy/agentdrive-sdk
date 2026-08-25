
# DriveOut


## Properties

Name | Type
------------ | -------------
`id` | string
`workspaceId` | string
`createdBy` | string
`name` | string
`metadata` | { [key: string]: any; }
`revision` | string
`rootFolderId` | string
`storageBytes` | number
`retrievalBytes` | number
`createdAt` | Date
`updatedAt` | Date
`deletedAt` | Date
`state` | string

## Example

```typescript
import type { DriveOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "workspaceId": null,
  "createdBy": null,
  "name": null,
  "metadata": null,
  "revision": null,
  "rootFolderId": null,
  "storageBytes": null,
  "retrievalBytes": null,
  "createdAt": null,
  "updatedAt": null,
  "deletedAt": null,
  "state": null,
} satisfies DriveOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DriveOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


