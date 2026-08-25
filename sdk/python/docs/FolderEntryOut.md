# FolderEntryOut

Compact D13 folder member returned by the unified namespace list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**revision** | **str** |  | 
**updated_at** | **datetime** |  | 
**state** | **str** |  | 
**deleted_at** | **datetime** |  | 

## Example

```python
from agentdrive_sdk.models.folder_entry_out import FolderEntryOut

# TODO update the JSON string below
json = "{}"
# create an instance of FolderEntryOut from a JSON string
folder_entry_out_instance = FolderEntryOut.from_json(json)
# print the JSON string representation of the object
print(FolderEntryOut.to_json())

# convert the object into a dict
folder_entry_out_dict = folder_entry_out_instance.to_dict()
# create an instance of FolderEntryOut from a dict
folder_entry_out_from_dict = FolderEntryOut.from_dict(folder_entry_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


