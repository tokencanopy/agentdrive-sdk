# ExtensionExchangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | 15-minute access_token (scope&#x3D;extension). |
**drive_id** | **str** | The drive these credentials are scoped to. |
**expires_in** | **int** | Seconds until access_token expiry. |
**identity_assertion** | **str** | 90-day identity_assertion. Refresh via POST /oauth2/token. |
**scope** | **str** |  | [optional] [default to 'extension']
**token_type** | **str** |  | [optional] [default to 'Bearer']

## Example

```python
from agentdrive_sdk.models.extension_exchange_response import ExtensionExchangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionExchangeResponse from a JSON string
extension_exchange_response_instance = ExtensionExchangeResponse.from_json(json)
# print the JSON string representation of the object
print(ExtensionExchangeResponse.to_json())

# convert the object into a dict
extension_exchange_response_dict = extension_exchange_response_instance.to_dict()
# create an instance of ExtensionExchangeResponse from a dict
extension_exchange_response_from_dict = ExtensionExchangeResponse.from_dict(extension_exchange_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
