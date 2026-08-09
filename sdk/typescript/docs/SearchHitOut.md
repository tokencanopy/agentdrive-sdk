
# SearchHitOut


## Properties

Name | Type
------------ | -------------
`contentType` | string
`driveId` | string
`id` | string
`name` | string
`parentId` | string
`rank` | number
`snippet` | string
`updatedAt` | Date
`versionId` | string

## Example

```typescript
import type { SearchHitOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "contentType": null,
  "driveId": null,
  "id": null,
  "name": null,
  "parentId": null,
  "rank": null,
  "snippet": null,
  "updatedAt": null,
  "versionId": null,
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
