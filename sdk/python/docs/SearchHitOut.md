# SearchHitOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**drive_id** | **str** |  | 
**parent_id** | **str** |  | 
**name** | **str** |  | 
**version_id** | **str** |  | 
**rank** | **float** |  | 
**snippet** | **str** | HTML-safe highlighted excerpt. The ONLY markup it may contain is the server&#39;s own &lt;mark&gt;...&lt;/mark&gt; highlight pair; artifact content is entity-escaped, so this may be rendered as HTML. | 
**content_type** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from agentdrive_sdk.models.search_hit_out import SearchHitOut

# TODO update the JSON string below
json = "{}"
# create an instance of SearchHitOut from a JSON string
search_hit_out_instance = SearchHitOut.from_json(json)
# print the JSON string representation of the object
print(SearchHitOut.to_json())

# convert the object into a dict
search_hit_out_dict = search_hit_out_instance.to_dict()
# create an instance of SearchHitOut from a dict
search_hit_out_from_dict = SearchHitOut.from_dict(search_hit_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


