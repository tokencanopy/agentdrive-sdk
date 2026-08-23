# DriveCreateIn

POST /v0/drives body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, object]** |  | [optional]
**name** | **str** |  |

## Example

```python
from agentdrive_sdk.models.drive_create_in import DriveCreateIn

# TODO update the JSON string below
json = "{}"
# create an instance of DriveCreateIn from a JSON string
drive_create_in_instance = DriveCreateIn.from_json(json)
# print the JSON string representation of the object
print(DriveCreateIn.to_json())

# convert the object into a dict
drive_create_in_dict = drive_create_in_instance.to_dict()
# create an instance of DriveCreateIn from a dict
drive_create_in_from_dict = DriveCreateIn.from_dict(drive_create_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
