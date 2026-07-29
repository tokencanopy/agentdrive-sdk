# DriveRestoreOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  |
**rebased_artifact_count** | **int** |  |
**restored_at** | **datetime** |  |

## Example

```python
from agentdrive_sdk.models.drive_restore_out import DriveRestoreOut

# TODO update the JSON string below
json = "{}"
# create an instance of DriveRestoreOut from a JSON string
drive_restore_out_instance = DriveRestoreOut.from_json(json)
# print the JSON string representation of the object
print(DriveRestoreOut.to_json())

# convert the object into a dict
drive_restore_out_dict = drive_restore_out_instance.to_dict()
# create an instance of DriveRestoreOut from a dict
drive_restore_out_from_dict = DriveRestoreOut.from_dict(drive_restore_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
