# DriveUsageOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_bytes** | **int** |  | 
**retrieval_bytes** | **int** |  | 

## Example

```python
from agentdrive_sdk.models.drive_usage_out import DriveUsageOut

# TODO update the JSON string below
json = "{}"
# create an instance of DriveUsageOut from a JSON string
drive_usage_out_instance = DriveUsageOut.from_json(json)
# print the JSON string representation of the object
print(DriveUsageOut.to_json())

# convert the object into a dict
drive_usage_out_dict = drive_usage_out_instance.to_dict()
# create an instance of DriveUsageOut from a dict
drive_usage_out_from_dict = DriveUsageOut.from_dict(drive_usage_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


