# FindPage

`/v0/find` response — single-shot top-N, deliberately unpaginated (same contract + rationale as `SearchPage`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FindHitOut]**](FindHitOut.md) |  |

## Example

```python
from agentdrive_sdk.models.find_page import FindPage

# TODO update the JSON string below
json = "{}"
# create an instance of FindPage from a JSON string
find_page_instance = FindPage.from_json(json)
# print the JSON string representation of the object
print(FindPage.to_json())

# convert the object into a dict
find_page_dict = find_page_instance.to_dict()
# create an instance of FindPage from a dict
find_page_from_dict = FindPage.from_dict(find_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
