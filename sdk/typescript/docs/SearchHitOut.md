
# SearchHitOut


## Properties

Name | Type
------------ | -------------
`artId` | string
`contentType` | string
`driveId` | string
`fileType` | string
`labels` | Array&lt;string&gt;
`path` | string
`score` | number
`snippet` | string
`updatedAt` | Date
`url` | string
`versionNumber` | number

## Example

```typescript
import type { SearchHitOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "artId": null,
  "contentType": null,
  "driveId": null,
  "fileType": null,
  "labels": null,
  "path": null,
  "score": null,
  "snippet": null,
  "updatedAt": null,
  "url": null,
  "versionNumber": null,
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
