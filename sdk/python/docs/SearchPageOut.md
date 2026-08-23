# SearchPageOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SearchHitOut]**](SearchHitOut.md) |  |
**next_cursor** | **str** |  |

## Example

```python
from agentdrive_sdk.models.search_page_out import SearchPageOut

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPageOut from a JSON string
search_page_out_instance = SearchPageOut.from_json(json)
# print the JSON string representation of the object
print(SearchPageOut.to_json())

# convert the object into a dict
search_page_out_dict = search_page_out_instance.to_dict()
# create an instance of SearchPageOut from a dict
search_page_out_from_dict = SearchPageOut.from_dict(search_page_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
