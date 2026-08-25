# DownloadCapabilityOut

The §5.7 mint response — a capability computation, not a stored resource: 200 only, freshly signed on every call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download** | [**DownloadOut**](DownloadOut.md) |  | 

## Example

```python
from agentdrive_sdk.models.download_capability_out import DownloadCapabilityOut

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadCapabilityOut from a JSON string
download_capability_out_instance = DownloadCapabilityOut.from_json(json)
# print the JSON string representation of the object
print(DownloadCapabilityOut.to_json())

# convert the object into a dict
download_capability_out_dict = download_capability_out_instance.to_dict()
# create an instance of DownloadCapabilityOut from a dict
download_capability_out_from_dict = DownloadCapabilityOut.from_dict(download_capability_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


