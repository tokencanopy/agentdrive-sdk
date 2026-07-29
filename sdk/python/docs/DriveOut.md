# DriveOut

One drive in a listing — metadata only (workspaces-design §4.2). Carries NO capability and NEVER a raw key. An admin's inventory and a member's owned list both serialize to this shape; `owner_email` is the only owner-identifying field surfaced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  |
**id** | **str** |  |
**name** | **str** |  |
**organization_id** | **str** |  |
**owner_email** | **str** |  | [optional]
**owner_user_id** | **str** |  | [optional]
**storage_bytes** | **int** |  |

## Example

```python
from agentdrive_sdk.models.drive_out import DriveOut

# TODO update the JSON string below
json = "{}"
# create an instance of DriveOut from a JSON string
drive_out_instance = DriveOut.from_json(json)
# print the JSON string representation of the object
print(DriveOut.to_json())

# convert the object into a dict
drive_out_dict = drive_out_instance.to_dict()
# create an instance of DriveOut from a dict
drive_out_from_dict = DriveOut.from_dict(drive_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
