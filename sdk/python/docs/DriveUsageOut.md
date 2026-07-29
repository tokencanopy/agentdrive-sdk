# DriveUsageOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_footprint** | [**StorageFootprintOut**](StorageFootprintOut.md) |  |
**egress_bytes** | [**UsageCounterOut**](UsageCounterOut.md) |  |
**footprint** | [**StorageFootprintOut**](StorageFootprintOut.md) |  |
**indexed_bytes** | [**UsageCounterOut**](UsageCounterOut.md) |  |
**indexing_ops** | [**UsageCounterOut**](UsageCounterOut.md) |  |
**ops_this_month** | [**OperationUsageOut**](OperationUsageOut.md) |  |
**period** | [**UsagePeriodOut**](UsagePeriodOut.md) |  |
**retrieval_queries** | [**UsageCounterOut**](UsageCounterOut.md) |  |
**storage** | [**UsageCounterOut**](UsageCounterOut.md) |  |
**storage_breakdown** | [**StorageBreakdownOut**](StorageBreakdownOut.md) |  | [optional]
**tokens_this_month** | [**TokenUsageOut**](TokenUsageOut.md) |  |
**version_retention** | [**VersionRetentionOut**](VersionRetentionOut.md) |  |
**writes_this_hour** | [**HourlyUsageCounterOut**](HourlyUsageCounterOut.md) |  |

## Example

```python
from agentdrive_sdk.models.drive_usage_out import DriveUsageOut

# TODO update the JSON string below
json = "{}"
# create an instance of DriveUsageOut from a JSON string
drive_usage_out_instance = DriveUsageOut.from_json(json)
# print the JSON string representation of the object
print(DriveUsageOut.to_json())

# convert the object into a dict
drive_usage_out_dict = drive_usage_out_instance.to_dict()
# create an instance of DriveUsageOut from a dict
drive_usage_out_from_dict = DriveUsageOut.from_dict(drive_usage_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
