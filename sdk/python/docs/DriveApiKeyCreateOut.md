# DriveApiKeyCreateOut

`POST /v0/drives/{id}/keys` response — the new key's metadata PLUS the raw `ad_live_` value, returned **once**. Store `api_key` now; only its hash is persisted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**api_key** | **str** |  | 
**prefix** | **str** |  | 
**label** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from agentdrive_sdk.models.drive_api_key_create_out import DriveApiKeyCreateOut

# TODO update the JSON string below
json = "{}"
# create an instance of DriveApiKeyCreateOut from a JSON string
drive_api_key_create_out_instance = DriveApiKeyCreateOut.from_json(json)
# print the JSON string representation of the object
print(DriveApiKeyCreateOut.to_json())

# convert the object into a dict
drive_api_key_create_out_dict = drive_api_key_create_out_instance.to_dict()
# create an instance of DriveApiKeyCreateOut from a dict
drive_api_key_create_out_from_dict = DriveApiKeyCreateOut.from_dict(drive_api_key_create_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


