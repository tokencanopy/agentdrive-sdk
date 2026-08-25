
# ChangeOut


## Properties

Name | Type
------------ | -------------
`id` | string
`changeSetId` | string
`type` | string
`driveId` | string
`actor` | [ChangeActorOut](ChangeActorOut.md)
`resource` | [ChangeResourceOut](ChangeResourceOut.md)
`previousRevision` | string
`revision` | string
`occurredAt` | Date
`data` | { [key: string]: any; }

## Example

```typescript
import type { ChangeOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "changeSetId": null,
  "type": null,
  "driveId": null,
  "actor": null,
  "resource": null,
  "previousRevision": null,
  "revision": null,
  "occurredAt": null,
  "data": null,
} satisfies ChangeOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ChangeOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


