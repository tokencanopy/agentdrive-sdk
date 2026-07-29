# AuthorizationServerMetadataOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_auth** | [**AgentAuthMetadataOut**](AgentAuthMetadataOut.md) |  |
**authorization_endpoint** | **str** |  |
**authorization_response_iss_parameter_supported** | **bool** |  |
**code_challenge_methods_supported** | **List[str]** |  |
**grant_types_supported** | **List[str]** |  |
**issuer** | **str** |  |
**jwks_uri** | **str** |  |
**registration_endpoint** | **str** |  |
**response_modes_supported** | **List[str]** |  |
**response_types_supported** | **List[str]** |  |
**revocation_endpoint** | **str** |  |
**revocation_endpoint_auth_methods_supported** | **List[str]** |  |
**scopes_supported** | **List[str]** |  |
**token_endpoint** | **str** |  |
**token_endpoint_auth_methods_supported** | **List[str]** |  |

## Example

```python
from agentdrive_sdk.models.authorization_server_metadata_out import AuthorizationServerMetadataOut

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerMetadataOut from a JSON string
authorization_server_metadata_out_instance = AuthorizationServerMetadataOut.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerMetadataOut.to_json())

# convert the object into a dict
authorization_server_metadata_out_dict = authorization_server_metadata_out_instance.to_dict()
# create an instance of AuthorizationServerMetadataOut from a dict
authorization_server_metadata_out_from_dict = AuthorizationServerMetadataOut.from_dict(authorization_server_metadata_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
