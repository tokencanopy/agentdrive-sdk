# StorageFootprintOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of** | **date** |  | [optional]
**live_bytes** | **int** |  |
**total_bytes** | **int** |  |
**trash_bytes** | **int** |  |
**version_bytes** | **int** |  |

## Example

```python
from agentdrive_sdk.models.storage_footprint_out import StorageFootprintOut

# TODO update the JSON string below
json = "{}"
# create an instance of StorageFootprintOut from a JSON string
storage_footprint_out_instance = StorageFootprintOut.from_json(json)
# print the JSON string representation of the object
print(StorageFootprintOut.to_json())

# convert the object into a dict
storage_footprint_out_dict = storage_footprint_out_instance.to_dict()
# create an instance of StorageFootprintOut from a dict
storage_footprint_out_from_dict = StorageFootprintOut.from_dict(storage_footprint_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
