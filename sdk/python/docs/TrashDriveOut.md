# TrashDriveOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_at** | **datetime** |  | [optional]
**id** | **str** |  |

## Example

```python
from agentdrive_sdk.models.trash_drive_out import TrashDriveOut

# TODO update the JSON string below
json = "{}"
# create an instance of TrashDriveOut from a JSON string
trash_drive_out_instance = TrashDriveOut.from_json(json)
# print the JSON string representation of the object
print(TrashDriveOut.to_json())

# convert the object into a dict
trash_drive_out_dict = trash_drive_out_instance.to_dict()
# create an instance of TrashDriveOut from a dict
trash_drive_out_from_dict = TrashDriveOut.from_dict(trash_drive_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
