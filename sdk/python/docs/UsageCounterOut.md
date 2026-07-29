# UsageCounterOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  |
**used** | **int** |  |

## Example

```python
from agentdrive_sdk.models.usage_counter_out import UsageCounterOut

# TODO update the JSON string below
json = "{}"
# create an instance of UsageCounterOut from a JSON string
usage_counter_out_instance = UsageCounterOut.from_json(json)
# print the JSON string representation of the object
print(UsageCounterOut.to_json())

# convert the object into a dict
usage_counter_out_dict = usage_counter_out_instance.to_dict()
# create an instance of UsageCounterOut from a dict
usage_counter_out_from_dict = UsageCounterOut.from_dict(usage_counter_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
