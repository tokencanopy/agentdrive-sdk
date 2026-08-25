
# SearchHitOut


## Properties

Name | Type
------------ | -------------
`id` | string
`driveId` | string
`parentId` | string
`name` | string
`versionId` | string
`rank` | number
`snippet` | string
`contentType` | string
`updatedAt` | Date

## Example

```typescript
import type { SearchHitOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "driveId": null,
  "parentId": null,
  "name": null,
  "versionId": null,
  "rank": null,
  "snippet": null,
  "contentType": null,
  "updatedAt": null,
} satisfies SearchHitOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SearchHitOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


