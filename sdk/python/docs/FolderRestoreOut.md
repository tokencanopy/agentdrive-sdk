# FolderRestoreOut

POST /v0/folders/{fld_id}/restore response — the restored (live) folder resource (same shape as `FolderOut`) plus the cascade counts from `core.folders.restore_cascade` (dashboard-file-operations-design §4.5), so the caller can confirm the scope of what came back with the root.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**drive_id** | **str** |  | 
**path** | **str** |  | 
**description** | **str** |  | [optional] 
**inherit_grants** | **bool** |  | [optional] [default to True]
**metageneration** | **int** |  | [optional] [default to 1]
**etag** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | [optional] 
**purge_at** | **datetime** |  | [optional] 
**n_subfolders_restored** | **int** |  | 
**n_artifacts_restored** | **int** |  | 

## Example

```python
from agentdrive_sdk.models.folder_restore_out import FolderRestoreOut

# TODO update the JSON string below
json = "{}"
# create an instance of FolderRestoreOut from a JSON string
folder_restore_out_instance = FolderRestoreOut.from_json(json)
# print the JSON string representation of the object
print(FolderRestoreOut.to_json())

# convert the object into a dict
folder_restore_out_dict = folder_restore_out_instance.to_dict()
# create an instance of FolderRestoreOut from a dict
folder_restore_out_from_dict = FolderRestoreOut.from_dict(folder_restore_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


