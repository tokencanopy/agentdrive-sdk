# UploadTransferOut

The one-time external transfer disclosure (B3 §5.2, amended 2026-08-20 to the two-step browser-initiated shape). Secret material: present ONLY in the initial successful begin response, never in status, replay, or any stored record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_protocol** | **str** |  |
**chunks** | [**UploadChunksOut**](UploadChunksOut.md) |  |
**initiation** | [**UploadInitiationOut**](UploadInitiationOut.md) |  |

## Example

```python
from agentdrive_sdk.models.upload_transfer_out import UploadTransferOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadTransferOut from a JSON string
upload_transfer_out_instance = UploadTransferOut.from_json(json)
# print the JSON string representation of the object
print(UploadTransferOut.to_json())

# convert the object into a dict
upload_transfer_out_dict = upload_transfer_out_instance.to_dict()
# create an instance of UploadTransferOut from a dict
upload_transfer_out_from_dict = UploadTransferOut.from_dict(upload_transfer_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
