# FolderCopyOut

POST /v0/folders/{fld_id}/copy response — the newly-created folder resource (same shape as `FolderOut`) plus copy-provenance fields: `from_fld_id` is the source folder and `n_artifacts_copied` is the number of descendant artifacts cloned into the new subtree. Mirrors the MCP `copy` folder route's conceptual shape.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  |
**deleted_at** | **datetime** |  | [optional]
**description** | **str** |  | [optional]
**drive_id** | **str** |  |
**etag** | **str** |  |
**from_fld_id** | **str** |  |
**id** | **str** |  |
**inherit_grants** | **bool** |  | [optional] [default to True]
**metageneration** | **int** |  | [optional] [default to 1]
**n_artifacts_copied** | **int** |  |
**path** | **str** |  |
**purge_at** | **datetime** |  | [optional]
**updated_at** | **datetime** |  |

## Example

```python
from agentdrive_sdk.models.folder_copy_out import FolderCopyOut

# TODO update the JSON string below
json = "{}"
# create an instance of FolderCopyOut from a JSON string
folder_copy_out_instance = FolderCopyOut.from_json(json)
# print the JSON string representation of the object
print(FolderCopyOut.to_json())

# convert the object into a dict
folder_copy_out_dict = folder_copy_out_instance.to_dict()
# create an instance of FolderCopyOut from a dict
folder_copy_out_from_dict = FolderCopyOut.from_dict(folder_copy_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
