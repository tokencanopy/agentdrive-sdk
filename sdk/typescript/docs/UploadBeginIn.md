
# UploadBeginIn

Body of `POST /v0/uploads` — the large-upload begin call (large-upload- design.md §5.1). All artifact decisions are frozen here; the subsequent GCS PUT carries only bytes, and `commit` carries only the `upload_id`.  `labels`/`metadata`/`source` omitted (null) ⇒ preserve the existing artifact\'s value at commit; present (incl. empty) ⇒ replace.

## Properties

Name | Type
------------ | -------------
`actorName` | string
`changeSummary` | string
`contentType` | string
`corsOrigin` | string
`crc32c` | string
`ifMatch` | number
`ifNoneMatch` | boolean
`labels` | Array&lt;string&gt;
`metadata` | { [key: string]: any; }
`path` | string
`sizeBytes` | number
`source` | [ArtifactSource](ArtifactSource.md)

## Example

```typescript
import type { UploadBeginIn } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "actorName": null,
  "changeSummary": null,
  "contentType": null,
  "corsOrigin": null,
  "crc32c": null,
  "ifMatch": null,
  "ifNoneMatch": null,
  "labels": null,
  "metadata": null,
  "path": null,
  "sizeBytes": null,
  "source": null,
} satisfies UploadBeginIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UploadBeginIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
