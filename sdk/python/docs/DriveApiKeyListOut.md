# DriveApiKeyListOut

`GET /v0/drives/{id}/keys` response — the drive's keys, newest first, including recently-revoked rows (filter on `revoked_at` for live only).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[DriveApiKeyOut]**](DriveApiKeyOut.md) |  | 

## Example

```python
from agentdrive_sdk.models.drive_api_key_list_out import DriveApiKeyListOut

# TODO update the JSON string below
json = "{}"
# create an instance of DriveApiKeyListOut from a JSON string
drive_api_key_list_out_instance = DriveApiKeyListOut.from_json(json)
# print the JSON string representation of the object
print(DriveApiKeyListOut.to_json())

# convert the object into a dict
drive_api_key_list_out_dict = drive_api_key_list_out_instance.to_dict()
# create an instance of DriveApiKeyListOut from a dict
drive_api_key_list_out_from_dict = DriveApiKeyListOut.from_dict(drive_api_key_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


