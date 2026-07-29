# DriveDeleteOut

DELETE /v0/drives/{drive_id} response — the drive soft-delete receipt. Reversible until the GC cron hard-deletes at `purge_at`; `restore_url` points at the drive restore endpoint (deletion-design.md §5.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_at** | **datetime** |  |
**id** | **str** |  |
**ok** | **bool** |  | [optional] [default to True]
**purge_at** | **datetime** |  |
**restore_url** | **str** |  | [optional]

## Example

```python
from agentdrive_sdk.models.drive_delete_out import DriveDeleteOut

# TODO update the JSON string below
json = "{}"
# create an instance of DriveDeleteOut from a JSON string
drive_delete_out_instance = DriveDeleteOut.from_json(json)
# print the JSON string representation of the object
print(DriveDeleteOut.to_json())

# convert the object into a dict
drive_delete_out_dict = drive_delete_out_instance.to_dict()
# create an instance of DriveDeleteOut from a dict
drive_delete_out_from_dict = DriveDeleteOut.from_dict(drive_delete_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
