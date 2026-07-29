# FindHitOut

One passage-level hit from `/v0/find` (hybrid chunk RAG over `embed_chunks`). The unit is a passage, not a file — consecutive `ord` values from the same `art_id` are normal because chunks overlap by ~400 tokens. Span fields are modality-aware: only the pair matching `modality` is populated, the others stay None.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**art_id** | **str** |  |
**char_end** | **int** |  | [optional]
**char_start** | **int** |  | [optional]
**content_type** | **str** |  |
**drive_id** | **str** |  |
**file_type** | **str** |  |
**labels** | **List[str]** |  | [optional]
**modality** | **str** |  |
**ord** | **int** |  |
**page_end** | **int** |  | [optional]
**page_start** | **int** |  | [optional]
**path** | **str** |  |
**rank_lexical** | **int** |  | [optional]
**rank_semantic** | **int** |  | [optional]
**score** | **float** |  |
**snippet** | **str** |  |
**text** | **str** |  |
**time_end_ms** | **int** |  | [optional]
**time_start_ms** | **int** |  | [optional]
**updated_at** | **datetime** |  |
**url** | **str** |  |
**version_number** | **int** |  |

## Example

```python
from agentdrive_sdk.models.find_hit_out import FindHitOut

# TODO update the JSON string below
json = "{}"
# create an instance of FindHitOut from a JSON string
find_hit_out_instance = FindHitOut.from_json(json)
# print the JSON string representation of the object
print(FindHitOut.to_json())

# convert the object into a dict
find_hit_out_dict = find_hit_out_instance.to_dict()
# create an instance of FindHitOut from a dict
find_hit_out_from_dict = FindHitOut.from_dict(find_hit_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
