
# UploadsCreateRequest


## Properties

Name | Type
------------ | -------------
`target` | [UploadsCreateRequestTarget](UploadsCreateRequestTarget.md)
`content` | [UploadsCreateRequestContent](UploadsCreateRequestContent.md)

## Example

```typescript
import type { UploadsCreateRequest } from '@tokencanopy/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "target": null,
  "content": null,
} satisfies UploadsCreateRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as UploadsCreateRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


