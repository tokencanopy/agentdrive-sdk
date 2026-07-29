# FolderOut

Folder resource (folders+permalinks design §13). `path` is the canonical leading+trailing-slash form. Access is expressed through grants (permission-sharing-design §4.4), not a folder-level flag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  |
**deleted_at** | **datetime** |  | [optional]
**description** | **str** |  | [optional]
**drive_id** | **str** |  |
**etag** | **str** |  |
**id** | **str** |  |
**inherit_grants** | **bool** |  | [optional] [default to True]
**metageneration** | **int** |  | [optional] [default to 1]
**path** | **str** |  |
**purge_at** | **datetime** |  | [optional]
**updated_at** | **datetime** |  |

## Example

```python
from agentdrive_sdk.models.folder_out import FolderOut

# TODO update the JSON string below
json = "{}"
# create an instance of FolderOut from a JSON string
folder_out_instance = FolderOut.from_json(json)
# print the JSON string representation of the object
print(FolderOut.to_json())

# convert the object into a dict
folder_out_dict = folder_out_instance.to_dict()
# create an instance of FolderOut from a dict
folder_out_from_dict = FolderOut.from_dict(folder_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
