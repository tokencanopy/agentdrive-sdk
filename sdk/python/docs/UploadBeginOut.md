# UploadBeginOut

The one 201 begin response — the only shape carrying ``transfer``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload** | [**UploadWithTransferOut**](UploadWithTransferOut.md) |  |

## Example

```python
from agentdrive_sdk.models.upload_begin_out import UploadBeginOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadBeginOut from a JSON string
upload_begin_out_instance = UploadBeginOut.from_json(json)
# print the JSON string representation of the object
print(UploadBeginOut.to_json())

# convert the object into a dict
upload_begin_out_dict = upload_begin_out_instance.to_dict()
# create an instance of UploadBeginOut from a dict
upload_begin_out_from_dict = UploadBeginOut.from_dict(upload_begin_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
