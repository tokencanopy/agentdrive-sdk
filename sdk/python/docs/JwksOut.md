# JwksOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[JwkOut]**](JwkOut.md) |  |

## Example

```python
from agentdrive_sdk.models.jwks_out import JwksOut

# TODO update the JSON string below
json = "{}"
# create an instance of JwksOut from a JSON string
jwks_out_instance = JwksOut.from_json(json)
# print the JSON string representation of the object
print(JwksOut.to_json())

# convert the object into a dict
jwks_out_dict = jwks_out_instance.to_dict()
# create an instance of JwksOut from a dict
jwks_out_from_dict = JwksOut.from_dict(jwks_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
