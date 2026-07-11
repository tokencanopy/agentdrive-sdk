# DriveApiKeyCreateIn

`POST /v0/drives/{id}/keys` body — a required human label (a name for the key, e.g. the agent/integration it's for).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.drive_api_key_create_in import DriveApiKeyCreateIn

# TODO update the JSON string below
json = "{}"
# create an instance of DriveApiKeyCreateIn from a JSON string
drive_api_key_create_in_instance = DriveApiKeyCreateIn.from_json(json)
# print the JSON string representation of the object
print(DriveApiKeyCreateIn.to_json())

# convert the object into a dict
drive_api_key_create_in_dict = drive_api_key_create_in_instance.to_dict()
# create an instance of DriveApiKeyCreateIn from a dict
drive_api_key_create_in_from_dict = DriveApiKeyCreateIn.from_dict(drive_api_key_create_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


