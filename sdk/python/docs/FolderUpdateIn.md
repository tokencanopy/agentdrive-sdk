# FolderUpdateIn

PATCH /v0/drives/{id}/folders/{folder_id} body — at least one field is required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from agentdrive_sdk.models.folder_update_in import FolderUpdateIn

# TODO update the JSON string below
json = "{}"
# create an instance of FolderUpdateIn from a JSON string
folder_update_in_instance = FolderUpdateIn.from_json(json)
# print the JSON string representation of the object
print(FolderUpdateIn.to_json())

# convert the object into a dict
folder_update_in_dict = folder_update_in_instance.to_dict()
# create an instance of FolderUpdateIn from a dict
folder_update_in_from_dict = FolderUpdateIn.from_dict(folder_update_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


