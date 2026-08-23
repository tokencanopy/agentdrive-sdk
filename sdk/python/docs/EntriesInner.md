# EntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_at** | **datetime** |  |
**id** | **str** |  |
**name** | **str** |  |
**revision** | **str** |  |
**state** | **str** |  |
**type** | **str** |  |
**updated_at** | **datetime** |  |
**content_type** | **str** |  |
**head_version_id** | **str** |  |
**size_bytes** | **int** |  |

## Example

```python
from agentdrive_sdk.models.entries_inner import EntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of EntriesInner from a JSON string
entries_inner_instance = EntriesInner.from_json(json)
# print the JSON string representation of the object
print(EntriesInner.to_json())

# convert the object into a dict
entries_inner_dict = entries_inner_instance.to_dict()
# create an instance of EntriesInner from a dict
entries_inner_from_dict = EntriesInner.from_dict(entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
