# FolderListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FolderOut]**](FolderOut.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.folder_list_out import FolderListOut

# TODO update the JSON string below
json = "{}"
# create an instance of FolderListOut from a JSON string
folder_list_out_instance = FolderListOut.from_json(json)
# print the JSON string representation of the object
print(FolderListOut.to_json())

# convert the object into a dict
folder_list_out_dict = folder_list_out_instance.to_dict()
# create an instance of FolderListOut from a dict
folder_list_out_from_dict = FolderListOut.from_dict(folder_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


