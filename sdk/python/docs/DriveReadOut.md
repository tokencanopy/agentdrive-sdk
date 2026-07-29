# DriveReadOut

Drive singleton shape returned by both data-plane read routes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  |
**email** | **str** |  | [optional]
**etag** | **str** |  |
**id** | **str** |  |
**metageneration** | **int** |  |
**organization_id** | **str** |  |
**storage_bytes** | **int** |  |
**storage_limit** | **int** |  |

## Example

```python
from agentdrive_sdk.models.drive_read_out import DriveReadOut

# TODO update the JSON string below
json = "{}"
# create an instance of DriveReadOut from a JSON string
drive_read_out_instance = DriveReadOut.from_json(json)
# print the JSON string representation of the object
print(DriveReadOut.to_json())

# convert the object into a dict
drive_read_out_dict = drive_read_out_instance.to_dict()
# create an instance of DriveReadOut from a dict
drive_read_out_from_dict = DriveReadOut.from_dict(drive_read_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
