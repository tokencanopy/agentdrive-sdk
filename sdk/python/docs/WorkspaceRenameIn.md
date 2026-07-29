# WorkspaceRenameIn

PATCH /v0/workspaces/{org} body — rename a workspace the caller administers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |

## Example

```python
from agentdrive_sdk.models.workspace_rename_in import WorkspaceRenameIn

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceRenameIn from a JSON string
workspace_rename_in_instance = WorkspaceRenameIn.from_json(json)
# print the JSON string representation of the object
print(WorkspaceRenameIn.to_json())

# convert the object into a dict
workspace_rename_in_dict = workspace_rename_in_instance.to_dict()
# create an instance of WorkspaceRenameIn from a dict
workspace_rename_in_from_dict = WorkspaceRenameIn.from_dict(workspace_rename_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
