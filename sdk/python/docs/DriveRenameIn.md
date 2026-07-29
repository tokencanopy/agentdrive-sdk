# DriveRenameIn

PATCH /v0/drives/{id} body — rename a drive the caller owns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |

## Example

```python
from agentdrive_sdk.models.drive_rename_in import DriveRenameIn

# TODO update the JSON string below
json = "{}"
# create an instance of DriveRenameIn from a JSON string
drive_rename_in_instance = DriveRenameIn.from_json(json)
# print the JSON string representation of the object
print(DriveRenameIn.to_json())

# convert the object into a dict
drive_rename_in_dict = drive_rename_in_instance.to_dict()
# create an instance of DriveRenameIn from a dict
drive_rename_in_from_dict = DriveRenameIn.from_dict(drive_rename_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
