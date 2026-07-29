
# EventOut


## Properties

Name | Type
------------ | -------------
`action` | string
`actorName` | string
`artId` | string
`createdAt` | Date
`driveId` | string
`id` | string
`metadata` | { [key: string]: any; }

## Example

```typescript
import type { EventOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "action": null,
  "actorName": null,
  "artId": null,
  "createdAt": null,
  "driveId": null,
  "id": null,
  "metadata": null,
} satisfies EventOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EventOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
