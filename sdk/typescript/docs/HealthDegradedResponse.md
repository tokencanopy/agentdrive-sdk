
# HealthDegradedResponse

Legacy health-probe failure shape.  Health predates the `/v0` error envelope and is consumed by load balancers. PR 1 documents the wire shape without changing it; convergence on the canonical API envelope is a separately reviewed compatibility decision.

## Properties

Name | Type
------------ | -------------
`detail` | [HealthDegradedDetail](HealthDegradedDetail.md)

## Example

```typescript
import type { HealthDegradedResponse } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "detail": null,
} satisfies HealthDegradedResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as HealthDegradedResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
