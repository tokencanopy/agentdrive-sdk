# QueryDryRunOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  |
**engine** | **str** |  |
**estimated_bytes_processed** | **int** |  |
**result_schema** | [**List[QueryColumnOut]**](QueryColumnOut.md) |  |
**valid** | **bool** |  |

## Example

```python
from agentdrive_sdk.models.query_dry_run_out import QueryDryRunOut

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDryRunOut from a JSON string
query_dry_run_out_instance = QueryDryRunOut.from_json(json)
# print the JSON string representation of the object
print(QueryDryRunOut.to_json())

# convert the object into a dict
query_dry_run_out_dict = query_dry_run_out_instance.to_dict()
# create an instance of QueryDryRunOut from a dict
query_dry_run_out_from_dict = QueryDryRunOut.from_dict(query_dry_run_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
