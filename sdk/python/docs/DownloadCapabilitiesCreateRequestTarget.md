# DownloadCapabilitiesCreateRequestTarget

Exactly one download-target union member.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_id** | **str** |  |
**kind** | **str** |  |
**version_id** | **str** |  |

## Example

```python
from agentdrive_sdk.models.download_capabilities_create_request_target import DownloadCapabilitiesCreateRequestTarget

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadCapabilitiesCreateRequestTarget from a JSON string
download_capabilities_create_request_target_instance = DownloadCapabilitiesCreateRequestTarget.from_json(json)
# print the JSON string representation of the object
print(DownloadCapabilitiesCreateRequestTarget.to_json())

# convert the object into a dict
download_capabilities_create_request_target_dict = download_capabilities_create_request_target_instance.to_dict()
# create an instance of DownloadCapabilitiesCreateRequestTarget from a dict
download_capabilities_create_request_target_from_dict = DownloadCapabilitiesCreateRequestTarget.from_dict(download_capabilities_create_request_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
