
# DriveDeleteOut

DELETE /v0/drives/{drive_id} response — the drive soft-delete receipt. Reversible until the GC cron hard-deletes at `purge_at`; `restore_url` points at the drive restore endpoint (deletion-design.md §5.2).

## Properties

Name | Type
------------ | -------------
`ok` | boolean
`id` | string
`deletedAt` | Date
`purgeAt` | Date
`restoreUrl` | string

## Example

```typescript
import type { DriveDeleteOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "ok": null,
  "id": null,
  "deletedAt": null,
  "purgeAt": null,
  "restoreUrl": null,
} satisfies DriveDeleteOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DriveDeleteOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


