# UploadWithTransferOut


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
**transfer** | [**UploadTransferOut**](UploadTransferOut.md) |  | 

## Example

```python
from agentdrive_sdk.models.upload_with_transfer_out import UploadWithTransferOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadWithTransferOut from a JSON string
upload_with_transfer_out_instance = UploadWithTransferOut.from_json(json)
# print the JSON string representation of the object
print(UploadWithTransferOut.to_json())

# convert the object into a dict
upload_with_transfer_out_dict = upload_with_transfer_out_instance.to_dict()
# create an instance of UploadWithTransferOut from a dict
upload_with_transfer_out_from_dict = UploadWithTransferOut.from_dict(upload_with_transfer_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


