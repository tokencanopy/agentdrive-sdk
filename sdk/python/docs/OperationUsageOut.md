# OperationUsageOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reads** | **int** |  |
**writes** | **int** |  |

## Example

```python
from agentdrive_sdk.models.operation_usage_out import OperationUsageOut

# TODO update the JSON string below
json = "{}"
# create an instance of OperationUsageOut from a JSON string
operation_usage_out_instance = OperationUsageOut.from_json(json)
# print the JSON string representation of the object
print(OperationUsageOut.to_json())

# convert the object into a dict
operation_usage_out_dict = operation_usage_out_instance.to_dict()
# create an instance of OperationUsageOut from a dict
operation_usage_out_from_dict = OperationUsageOut.from_dict(operation_usage_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
