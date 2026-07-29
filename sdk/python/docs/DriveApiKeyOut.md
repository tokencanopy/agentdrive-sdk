# DriveApiKeyOut

One per-drive `ad_live_` key — metadata only (never the raw key or hash). Item shape for `GET /v0/drives/{id}/keys`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  |
**id** | **str** |  |
**label** | **str** |  | [optional]
**last_used_at** | **datetime** |  | [optional]
**prefix** | **str** |  |
**revoked_at** | **datetime** |  | [optional]

## Example

```python
from agentdrive_sdk.models.drive_api_key_out import DriveApiKeyOut

# TODO update the JSON string below
json = "{}"
# create an instance of DriveApiKeyOut from a JSON string
drive_api_key_out_instance = DriveApiKeyOut.from_json(json)
# print the JSON string representation of the object
print(DriveApiKeyOut.to_json())

# convert the object into a dict
drive_api_key_out_dict = drive_api_key_out_instance.to_dict()
# create an instance of DriveApiKeyOut from a dict
drive_api_key_out_from_dict = DriveApiKeyOut.from_dict(drive_api_key_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
