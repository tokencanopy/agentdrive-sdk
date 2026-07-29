# FolderCopyIn

POST /v0/folders/{fld_id}/copy body — duplicate the subtree to a new path. `path` is the target folder path (canonical, trailing slash). Its own schema (vs. reusing `FolderMoveIn`) keeps the copy surface self-documenting in the OpenAPI spec.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_metageneration** | **int** |  | [optional]
**path** | **str** |  |

## Example

```python
from agentdrive_sdk.models.folder_copy_in import FolderCopyIn

# TODO update the JSON string below
json = "{}"
# create an instance of FolderCopyIn from a JSON string
folder_copy_in_instance = FolderCopyIn.from_json(json)
# print the JSON string representation of the object
print(FolderCopyIn.to_json())

# convert the object into a dict
folder_copy_in_dict = folder_copy_in_instance.to_dict()
# create an instance of FolderCopyIn from a dict
folder_copy_in_from_dict = FolderCopyIn.from_dict(folder_copy_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
