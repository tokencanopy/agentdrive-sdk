# UploadContentOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size_bytes** | **int** |  | 
**media_type** | **str** |  | 
**checksum** | [**UploadChecksumOut**](UploadChecksumOut.md) |  | 

## Example

```python
from agentdrive_sdk.models.upload_content_out import UploadContentOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadContentOut from a JSON string
upload_content_out_instance = UploadContentOut.from_json(json)
# print the JSON string representation of the object
print(UploadContentOut.to_json())

# convert the object into a dict
upload_content_out_dict = upload_content_out_instance.to_dict()
# create an instance of UploadContentOut from a dict
upload_content_out_from_dict = UploadContentOut.from_dict(upload_content_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


