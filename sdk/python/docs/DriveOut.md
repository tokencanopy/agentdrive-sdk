# DriveOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**workspace_id** | **str** |  | 
**created_by** | **str** |  | 
**name** | **str** |  | 
**metadata** | **Dict[str, object]** |  | 
**revision** | **str** |  | 
**root_folder_id** | **str** |  | 
**storage_bytes** | **int** |  | 
**retrieval_bytes** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | 
**state** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.drive_out import DriveOut

# TODO update the JSON string below
json = "{}"
# create an instance of DriveOut from a JSON string
drive_out_instance = DriveOut.from_json(json)
# print the JSON string representation of the object
print(DriveOut.to_json())

# convert the object into a dict
drive_out_dict = drive_out_instance.to_dict()
# create an instance of DriveOut from a dict
drive_out_from_dict = DriveOut.from_dict(drive_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


