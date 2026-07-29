# FolderDeleteOut

DELETE response — surfaces cascade counts so the caller can confirm scope of an rmdir before the client retries with `?recursive=true`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_at** | **datetime** |  |
**id** | **str** |  |
**n_artifacts_deleted** | **int** |  |
**n_subfolders_deleted** | **int** |  |
**ok** | **bool** |  | [optional] [default to True]
**path** | **str** |  |
**purge_at** | **datetime** |  |
**retention_days** | **int** |  |

## Example

```python
from agentdrive_sdk.models.folder_delete_out import FolderDeleteOut

# TODO update the JSON string below
json = "{}"
# create an instance of FolderDeleteOut from a JSON string
folder_delete_out_instance = FolderDeleteOut.from_json(json)
# print the JSON string representation of the object
print(FolderDeleteOut.to_json())

# convert the object into a dict
folder_delete_out_dict = folder_delete_out_instance.to_dict()
# create an instance of FolderDeleteOut from a dict
folder_delete_out_from_dict = FolderDeleteOut.from_dict(folder_delete_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
