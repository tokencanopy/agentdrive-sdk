# DriveCreateOut

The create response — the ONLY place (besides key-rotate) a raw `ad_live_` key is returned, reveal-once.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**owner_user_id** | **str** |  | [optional] 
**owner_email** | **str** |  | [optional] 
**storage_bytes** | **int** |  | 
**created_at** | **datetime** |  | 
**api_key** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.drive_create_out import DriveCreateOut

# TODO update the JSON string below
json = "{}"
# create an instance of DriveCreateOut from a JSON string
drive_create_out_instance = DriveCreateOut.from_json(json)
# print the JSON string representation of the object
print(DriveCreateOut.to_json())

# convert the object into a dict
drive_create_out_dict = drive_create_out_instance.to_dict()
# create an instance of DriveCreateOut from a dict
drive_create_out_from_dict = DriveCreateOut.from_dict(drive_create_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


