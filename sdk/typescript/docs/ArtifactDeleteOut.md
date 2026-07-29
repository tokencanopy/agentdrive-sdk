
# ArtifactDeleteOut

DELETE /v0/artifacts/{art_id} response — the soft-delete receipt. Reversible until the GC cron hard-deletes at `purge_at`; `restore_url` points at the by-id restore endpoint (deletion-design.md §5.3).

## Properties

Name | Type
------------ | -------------
`deletedAt` | Date
`id` | string
`ok` | boolean
`path` | string
`purgeAt` | Date
`restoreUrl` | string

## Example

```typescript
import type { ArtifactDeleteOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "deletedAt": null,
  "id": null,
  "ok": null,
  "path": null,
  "purgeAt": null,
  "restoreUrl": null,
} satisfies ArtifactDeleteOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ArtifactDeleteOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
