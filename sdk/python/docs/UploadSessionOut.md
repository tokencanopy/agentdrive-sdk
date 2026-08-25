# UploadSessionOut

The non-secret session representation (status, replay, cancel, complete). Deliberately has NO transfer field — it is structurally incapable of carrying the bearer target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload** | [**UploadOut**](UploadOut.md) |  | 

## Example

```python
from agentdrive_sdk.models.upload_session_out import UploadSessionOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSessionOut from a JSON string
upload_session_out_instance = UploadSessionOut.from_json(json)
# print the JSON string representation of the object
print(UploadSessionOut.to_json())

# convert the object into a dict
upload_session_out_dict = upload_session_out_instance.to_dict()
# create an instance of UploadSessionOut from a dict
upload_session_out_from_dict = UploadSessionOut.from_dict(upload_session_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


