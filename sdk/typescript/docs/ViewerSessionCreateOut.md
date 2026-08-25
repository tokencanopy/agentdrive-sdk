
# ViewerSessionCreateOut

The mint response — the ONLY response carrying the plaintext viewer credential. The credential authorizes the isolated viewer host\'s `/view/doc` and `/view/content` for this one pinned version, via an Authorization header only — it must never be placed in a URL, cookie, or persistent storage.

## Properties

Name | Type
------------ | -------------
`id` | string
`driveId` | string
`artifactId` | string
`versionId` | string
`expiresAt` | Date
`createdAt` | Date
`expiresIn` | number
`credential` | string

## Example

```typescript
import type { ViewerSessionCreateOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "driveId": null,
  "artifactId": null,
  "versionId": null,
  "expiresAt": null,
  "createdAt": null,
  "expiresIn": null,
  "credential": null,
} satisfies ViewerSessionCreateOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ViewerSessionCreateOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


