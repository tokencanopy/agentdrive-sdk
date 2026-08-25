# DriveUpdateIn

PATCH /v0/drives/{id} body — at least one field is required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from agentdrive_sdk.models.drive_update_in import DriveUpdateIn

# TODO update the JSON string below
json = "{}"
# create an instance of DriveUpdateIn from a JSON string
drive_update_in_instance = DriveUpdateIn.from_json(json)
# print the JSON string representation of the object
print(DriveUpdateIn.to_json())

# convert the object into a dict
drive_update_in_dict = drive_update_in_instance.to_dict()
# create an instance of DriveUpdateIn from a dict
drive_update_in_from_dict = DriveUpdateIn.from_dict(drive_update_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


