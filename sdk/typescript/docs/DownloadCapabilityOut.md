
# DownloadCapabilityOut

The §5.7 mint response — a capability computation, not a stored resource: 200 only, freshly signed on every call.

## Properties

Name | Type
------------ | -------------
`download` | [DownloadOut](DownloadOut.md)

## Example

```typescript
import type { DownloadCapabilityOut } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "download": null,
} satisfies DownloadCapabilityOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DownloadCapabilityOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


