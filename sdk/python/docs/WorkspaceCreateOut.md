# WorkspaceCreateOut

POST /v0/workspaces response. Carries the new workspace + its starter drive's `ad_live_` key **once** (`starter_drive_api_key`) — reveal-once, store it now (mint more keys via `POST /v0/drives/{id}/keys`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starter_drive_api_key** | **str** |  |
**starter_drive_id** | **str** |  |
**workspace** | [**WorkspaceOut**](WorkspaceOut.md) |  |

## Example

```python
from agentdrive_sdk.models.workspace_create_out import WorkspaceCreateOut

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCreateOut from a JSON string
workspace_create_out_instance = WorkspaceCreateOut.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCreateOut.to_json())

# convert the object into a dict
workspace_create_out_dict = workspace_create_out_instance.to_dict()
# create an instance of WorkspaceCreateOut from a dict
workspace_create_out_from_dict = WorkspaceCreateOut.from_dict(workspace_create_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
