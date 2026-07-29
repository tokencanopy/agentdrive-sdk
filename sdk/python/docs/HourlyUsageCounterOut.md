# HourlyUsageCounterOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  |
**reset_at** | **datetime** |  |
**used** | **int** |  |

## Example

```python
from agentdrive_sdk.models.hourly_usage_counter_out import HourlyUsageCounterOut

# TODO update the JSON string below
json = "{}"
# create an instance of HourlyUsageCounterOut from a JSON string
hourly_usage_counter_out_instance = HourlyUsageCounterOut.from_json(json)
# print the JSON string representation of the object
print(HourlyUsageCounterOut.to_json())

# convert the object into a dict
hourly_usage_counter_out_dict = hourly_usage_counter_out_instance.to_dict()
# create an instance of HourlyUsageCounterOut from a dict
hourly_usage_counter_out_from_dict = HourlyUsageCounterOut.from_dict(hourly_usage_counter_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
