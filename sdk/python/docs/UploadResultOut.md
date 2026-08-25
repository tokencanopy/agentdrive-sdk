# UploadResultOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**artifact_id** | **str** |  | 
**version_id** | **str** |  | 
**revision** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.upload_result_out import UploadResultOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadResultOut from a JSON string
upload_result_out_instance = UploadResultOut.from_json(json)
# print the JSON string representation of the object
print(UploadResultOut.to_json())

# convert the object into a dict
upload_result_out_dict = upload_result_out_instance.to_dict()
# create an instance of UploadResultOut from a dict
upload_result_out_from_dict = UploadResultOut.from_dict(upload_result_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


