
# DriveUsageOut


## Properties

Name | Type
------------ | -------------
`accountFootprint` | [StorageFootprintOut](StorageFootprintOut.md)
`egressBytes` | [UsageCounterOut](UsageCounterOut.md)
`footprint` | [StorageFootprintOut](StorageFootprintOut.md)
`indexedBytes` | [UsageCounterOut](UsageCounterOut.md)
`indexingOps` | [UsageCounterOut](UsageCounterOut.md)
`opsThisMonth` | [OperationUsageOut](OperationUsageOut.md)
`period` | [UsagePeriodOut](UsagePeriodOut.md)
`retrievalQueries` | [UsageCounterOut](UsageCounterOut.md)
`storage` | [UsageCounterOut](UsageCounterOut.md)
`storageBreakdown` | [StorageBreakdownOut](StorageBreakdownOut.md)
`tokensThisMonth` | [TokenUsageOut](TokenUsageOut.md)
`versionRetention` | [VersionRetentionOut](VersionRetentionOut.md)
`writesThisHour` | [HourlyUsageCounterOut](HourlyUsageCounterOut.md)

## Example

```typescript
import type { DriveUsageOut } from '@mnexa-ai/agentdrive-sdk'

// TODO: Update the object below with actual values
const example = {
  "accountFootprint": null,
  "egressBytes": null,
  "footprint": null,
  "indexedBytes": null,
  "indexingOps": null,
  "opsThisMonth": null,
  "period": null,
  "retrievalQueries": null,
  "storage": null,
  "storageBreakdown": null,
  "tokensThisMonth": null,
  "versionRetention": null,
  "writesThisHour": null,
} satisfies DriveUsageOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DriveUsageOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
