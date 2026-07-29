# HealthDegradedDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  |
**status** | **str** |  |

## Example

```python
from agentdrive_sdk.models.health_degraded_detail import HealthDegradedDetail

# TODO update the JSON string below
json = "{}"
# create an instance of HealthDegradedDetail from a JSON string
health_degraded_detail_instance = HealthDegradedDetail.from_json(json)
# print the JSON string representation of the object
print(HealthDegradedDetail.to_json())

# convert the object into a dict
health_degraded_detail_dict = health_degraded_detail_instance.to_dict()
# create an instance of HealthDegradedDetail from a dict
health_degraded_detail_from_dict = HealthDegradedDetail.from_dict(health_degraded_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
