# DriveListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DriveOut]**](DriveOut.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.drive_list_out import DriveListOut

# TODO update the JSON string below
json = "{}"
# create an instance of DriveListOut from a JSON string
drive_list_out_instance = DriveListOut.from_json(json)
# print the JSON string representation of the object
print(DriveListOut.to_json())

# convert the object into a dict
drive_list_out_dict = drive_list_out_instance.to_dict()
# create an instance of DriveListOut from a dict
drive_list_out_from_dict = DriveListOut.from_dict(drive_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


