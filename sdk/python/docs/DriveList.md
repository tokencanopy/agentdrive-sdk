# DriveList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DriveOut]**](DriveOut.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from agentdrive_sdk.models.drive_list import DriveList

# TODO update the JSON string below
json = "{}"
# create an instance of DriveList from a JSON string
drive_list_instance = DriveList.from_json(json)
# print the JSON string representation of the object
print(DriveList.to_json())

# convert the object into a dict
drive_list_dict = drive_list_instance.to_dict()
# create an instance of DriveList from a dict
drive_list_from_dict = DriveList.from_dict(drive_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


