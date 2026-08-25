# DownloadOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_id** | **str** |  | 
**version_id** | **str** |  | 
**expires_at** | **datetime** |  | 
**target** | [**DownloadTargetOut**](DownloadTargetOut.md) |  | 

## Example

```python
from agentdrive_sdk.models.download_out import DownloadOut

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadOut from a JSON string
download_out_instance = DownloadOut.from_json(json)
# print the JSON string representation of the object
print(DownloadOut.to_json())

# convert the object into a dict
download_out_dict = download_out_instance.to_dict()
# create an instance of DownloadOut from a dict
download_out_from_dict = DownloadOut.from_dict(download_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


