# JwkOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  |
**e** | **str** |  |
**kid** | **str** |  |
**kty** | **str** |  |
**n** | **str** |  |
**use** | **str** |  |

## Example

```python
from agentdrive_sdk.models.jwk_out import JwkOut

# TODO update the JSON string below
json = "{}"
# create an instance of JwkOut from a JSON string
jwk_out_instance = JwkOut.from_json(json)
# print the JSON string representation of the object
print(JwkOut.to_json())

# convert the object into a dict
jwk_out_dict = jwk_out_instance.to_dict()
# create an instance of JwkOut from a dict
jwk_out_from_dict = JwkOut.from_dict(jwk_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
