# StorageBreakdownOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of** | **date** |  |
**live_bytes** | **int** |  |
**trash_bytes** | **int** |  |
**version_bytes** | **int** |  |

## Example

```python
from agentdrive_sdk.models.storage_breakdown_out import StorageBreakdownOut

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBreakdownOut from a JSON string
storage_breakdown_out_instance = StorageBreakdownOut.from_json(json)
# print the JSON string representation of the object
print(StorageBreakdownOut.to_json())

# convert the object into a dict
storage_breakdown_out_dict = storage_breakdown_out_instance.to_dict()
# create an instance of StorageBreakdownOut from a dict
storage_breakdown_out_from_dict = StorageBreakdownOut.from_dict(storage_breakdown_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
