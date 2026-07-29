# ResponsePostQueryV0QueryPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  |
**engine** | **str** |  |
**estimated_bytes_processed** | **int** |  |
**result_schema** | [**List[QueryColumnOut]**](QueryColumnOut.md) |  |
**valid** | **bool** |  |
**bytes_processed** | **int** |  |
**cache_hit** | **bool** |  |
**preview** | **List[Dict[str, object]]** |  |
**result_art_id** | **str** |  |
**row_count** | **int** |  |

## Example

```python
from agentdrive_sdk.models.response_post_query_v0_query_post import ResponsePostQueryV0QueryPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponsePostQueryV0QueryPost from a JSON string
response_post_query_v0_query_post_instance = ResponsePostQueryV0QueryPost.from_json(json)
# print the JSON string representation of the object
print(ResponsePostQueryV0QueryPost.to_json())

# convert the object into a dict
response_post_query_v0_query_post_dict = response_post_query_v0_query_post_instance.to_dict()
# create an instance of ResponsePostQueryV0QueryPost from a dict
response_post_query_v0_query_post_from_dict = ResponsePostQueryV0QueryPost.from_dict(response_post_query_v0_query_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
