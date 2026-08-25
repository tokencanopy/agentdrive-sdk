# DownloadCapabilitiesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**DownloadCapabilitiesCreateRequestTarget**](DownloadCapabilitiesCreateRequestTarget.md) |  | 

## Example

```python
from agentdrive_sdk.models.download_capabilities_create_request import DownloadCapabilitiesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadCapabilitiesCreateRequest from a JSON string
download_capabilities_create_request_instance = DownloadCapabilitiesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DownloadCapabilitiesCreateRequest.to_json())

# convert the object into a dict
download_capabilities_create_request_dict = download_capabilities_create_request_instance.to_dict()
# create an instance of DownloadCapabilitiesCreateRequest from a dict
download_capabilities_create_request_from_dict = DownloadCapabilitiesCreateRequest.from_dict(download_capabilities_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


