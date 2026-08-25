# HealthDegradedResponse

Legacy health-probe failure shape.  Health predates the `/v0` error envelope and is consumed by load balancers. PR 1 documents the wire shape without changing it; convergence on the canonical API envelope is a separately reviewed compatibility decision.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**HealthDegradedDetail**](HealthDegradedDetail.md) |  | 

## Example

```python
from agentdrive_sdk.models.health_degraded_response import HealthDegradedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HealthDegradedResponse from a JSON string
health_degraded_response_instance = HealthDegradedResponse.from_json(json)
# print the JSON string representation of the object
print(HealthDegradedResponse.to_json())

# convert the object into a dict
health_degraded_response_dict = health_degraded_response_instance.to_dict()
# create an instance of HealthDegradedResponse from a dict
health_degraded_response_from_dict = HealthDegradedResponse.from_dict(health_degraded_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


