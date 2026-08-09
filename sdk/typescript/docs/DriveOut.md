
# DriveOut


## Properties

Name | Type
------------ | -------------
`createdAt` | Date
`createdBy` | string
`deletedAt` | Date
`id` | string
`metadata` | { [key: string]: any; }
`name` | string
`retrievalBytes` | number
`revision` | string
`rootFolderId` | string
`state` | string
`storageBytes` | number
`updatedAt` | Date
`workspaceId` | string

## Example

```typescript
import type { DriveOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "createdAt": null,
  "createdBy": null,
  "deletedAt": null,
  "id": null,
  "metadata": null,
  "name": null,
  "retrievalBytes": null,
  "revision": null,
  "rootFolderId": null,
  "state": null,
  "storageBytes": null,
  "updatedAt": null,
  "workspaceId": null,
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
