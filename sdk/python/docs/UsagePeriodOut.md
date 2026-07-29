# UsagePeriodOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ends** | **datetime** |  |
**starts** | **datetime** |  |
**year_month** | **str** |  |

## Example

```python
from agentdrive_sdk.models.usage_period_out import UsagePeriodOut

# TODO update the JSON string below
json = "{}"
# create an instance of UsagePeriodOut from a JSON string
usage_period_out_instance = UsagePeriodOut.from_json(json)
# print the JSON string representation of the object
print(UsagePeriodOut.to_json())

# convert the object into a dict
usage_period_out_dict = usage_period_out_instance.to_dict()
# create an instance of UsagePeriodOut from a dict
usage_period_out_from_dict = UsagePeriodOut.from_dict(usage_period_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
