# WorkspaceCreateIn

POST /v0/workspaces body. `name` is the user-facing workspace label; the creator becomes its admin and gets a starter drive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |

## Example

```python
from agentdrive_sdk.models.workspace_create_in import WorkspaceCreateIn

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCreateIn from a JSON string
workspace_create_in_instance = WorkspaceCreateIn.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCreateIn.to_json())

# convert the object into a dict
workspace_create_in_dict = workspace_create_in_instance.to_dict()
# create an instance of WorkspaceCreateIn from a dict
workspace_create_in_from_dict = WorkspaceCreateIn.from_dict(workspace_create_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
