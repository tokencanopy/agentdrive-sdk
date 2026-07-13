
# SearchHitOut


## Properties

Name | Type
------------ | -------------
`artId` | string
`driveId` | string
`path` | string
`url` | string
`contentType` | string
`fileType` | string
`labels` | Array&lt;string&gt;
`snippet` | string
`score` | number
`updatedAt` | Date
`versionNumber` | number

## Example

```typescript
import type { SearchHitOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "artId": null,
  "driveId": null,
  "path": null,
  "url": null,
  "contentType": null,
  "fileType": null,
  "labels": null,
  "snippet": null,
  "score": null,
  "updatedAt": null,
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


