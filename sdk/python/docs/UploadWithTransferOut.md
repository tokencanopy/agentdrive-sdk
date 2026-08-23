# UploadWithTransferOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cleanup** | [**UploadCleanupOut**](UploadCleanupOut.md) |  |
**content** | [**UploadContentOut**](UploadContentOut.md) |  |
**drive_id** | **str** |  |
**expires_at** | **datetime** |  |
**failure** | [**UploadFailureOut**](UploadFailureOut.md) |  |
**id** | **str** |  |
**restart_required** | **bool** |  |
**result** | [**UploadResultOut**](UploadResultOut.md) |  |
**state** | **str** |  |
**target** | [**Target**](Target.md) |  |
**target_disclosed** | **bool** |  |
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
