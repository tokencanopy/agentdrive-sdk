# OAuthProtocolErrorOut

RFC OAuth error shape used by public protocol endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  |
**error_description** | **str** |  | [optional]

## Example

```python
from agentdrive_sdk.models.o_auth_protocol_error_out import OAuthProtocolErrorOut

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthProtocolErrorOut from a JSON string
o_auth_protocol_error_out_instance = OAuthProtocolErrorOut.from_json(json)
# print the JSON string representation of the object
print(OAuthProtocolErrorOut.to_json())

# convert the object into a dict
o_auth_protocol_error_out_dict = o_auth_protocol_error_out_instance.to_dict()
# create an instance of OAuthProtocolErrorOut from a dict
o_auth_protocol_error_out_from_dict = OAuthProtocolErrorOut.from_dict(o_auth_protocol_error_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
