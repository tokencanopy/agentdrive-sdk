# ClientRegistrationOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  |
**client_id_issued_at** | **int** |  |
**client_name** | **str** |  |
**grant_types** | **List[str]** |  |
**redirect_uris** | **List[str]** |  |
**response_types** | **List[str]** |  |
**scope** | **str** |  |
**token_endpoint_auth_method** | **str** |  |

## Example

```python
from agentdrive_sdk.models.client_registration_out import ClientRegistrationOut

# TODO update the JSON string below
json = "{}"
# create an instance of ClientRegistrationOut from a JSON string
client_registration_out_instance = ClientRegistrationOut.from_json(json)
# print the JSON string representation of the object
print(ClientRegistrationOut.to_json())

# convert the object into a dict
client_registration_out_dict = client_registration_out_instance.to_dict()
# create an instance of ClientRegistrationOut from a dict
client_registration_out_from_dict = ClientRegistrationOut.from_dict(client_registration_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
