# WorkspaceOut

One workspace in a listing — metadata only. `role` is the CALLER's role in it (admin/member), so a client can render management affordances without a second round-trip.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  |
**id** | **str** |  |
**name** | **str** |  |
**role** | **str** |  |
**tier_id** | **str** |  |

## Example

```python
from agentdrive_sdk.models.workspace_out import WorkspaceOut

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceOut from a JSON string
workspace_out_instance = WorkspaceOut.from_json(json)
# print the JSON string representation of the object
print(WorkspaceOut.to_json())

# convert the object into a dict
workspace_out_dict = workspace_out_instance.to_dict()
# create an instance of WorkspaceOut from a dict
workspace_out_from_dict = WorkspaceOut.from_dict(workspace_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
