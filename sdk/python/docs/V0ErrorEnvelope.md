# V0ErrorEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorResponseError**](ErrorResponseError.md) |  | 

## Example

```python
from agentdrive_sdk.models.v0_error_envelope import V0ErrorEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of V0ErrorEnvelope from a JSON string
v0_error_envelope_instance = V0ErrorEnvelope.from_json(json)
# print the JSON string representation of the object
print(V0ErrorEnvelope.to_json())

# convert the object into a dict
v0_error_envelope_dict = v0_error_envelope_instance.to_dict()
# create an instance of V0ErrorEnvelope from a dict
v0_error_envelope_from_dict = V0ErrorEnvelope.from_dict(v0_error_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


