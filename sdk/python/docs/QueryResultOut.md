# QueryResultOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_processed** | **int** |  |
**cache_hit** | **bool** |  |
**engine** | **str** |  |
**preview** | **List[Optional[Dict[str, object]]]** |  |
**result_art_id** | **str** |  |
**result_schema** | [**List[QueryColumnOut]**](QueryColumnOut.md) |  |
**row_count** | **int** |  |

## Example

```python
from agentdrive_sdk.models.query_result_out import QueryResultOut

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultOut from a JSON string
query_result_out_instance = QueryResultOut.from_json(json)
# print the JSON string representation of the object
print(QueryResultOut.to_json())

# convert the object into a dict
query_result_out_dict = query_result_out_instance.to_dict()
# create an instance of QueryResultOut from a dict
query_result_out_from_dict = QueryResultOut.from_dict(query_result_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
