# ExtensionExchangeRequest

Single-use ticket → JWT pair. Called by `auth-complete.html` inside the SnipIt extension. No `Authorization` header — the ticket itself is the credential.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ext_id** | **str** | The extension&#39;s ID (Chrome Web Store ID or unpacked dev ID). |
**ticket** | **str** | The opaque ticket from the /auth/callback handoff. |

## Example

```python
from agentdrive_sdk.models.extension_exchange_request import ExtensionExchangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionExchangeRequest from a JSON string
extension_exchange_request_instance = ExtensionExchangeRequest.from_json(json)
# print the JSON string representation of the object
print(ExtensionExchangeRequest.to_json())

# convert the object into a dict
extension_exchange_request_dict = extension_exchange_request_instance.to_dict()
# create an instance of ExtensionExchangeRequest from a dict
extension_exchange_request_from_dict = ExtensionExchangeRequest.from_dict(extension_exchange_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
