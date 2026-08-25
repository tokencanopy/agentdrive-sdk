# UploadOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**drive_id** | **str** |  | 
**state** | **str** |  | 
**target** | [**Target**](Target.md) |  | 
**content** | [**UploadContentOut**](UploadContentOut.md) |  | 
**expires_at** | **datetime** |  | 
**target_disclosed** | **bool** |  | 
**restart_required** | **bool** |  | 
**result** | [**UploadResultOut**](UploadResultOut.md) |  | 
**failure** | [**UploadFailureOut**](UploadFailureOut.md) |  | 
**cleanup** | [**UploadCleanupOut**](UploadCleanupOut.md) |  | 

## Example

```python
from agentdrive_sdk.models.upload_out import UploadOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadOut from a JSON string
upload_out_instance = UploadOut.from_json(json)
# print the JSON string representation of the object
print(UploadOut.to_json())

# convert the object into a dict
upload_out_dict = upload_out_instance.to_dict()
# create an instance of UploadOut from a dict
upload_out_from_dict = UploadOut.from_dict(upload_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


