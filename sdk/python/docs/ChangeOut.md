# ChangeOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**ChangeActorOut**](ChangeActorOut.md) |  |
**change_set_id** | **str** |  |
**data** | **Dict[str, object]** |  |
**drive_id** | **str** |  |
**id** | **str** |  |
**occurred_at** | **datetime** |  |
**previous_revision** | **str** |  |
**resource** | [**ChangeResourceOut**](ChangeResourceOut.md) |  |
**revision** | **str** |  |
**type** | **str** |  |

## Example

```python
from agentdrive_sdk.models.change_out import ChangeOut

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeOut from a JSON string
change_out_instance = ChangeOut.from_json(json)
# print the JSON string representation of the object
print(ChangeOut.to_json())

# convert the object into a dict
change_out_dict = change_out_instance.to_dict()
# create an instance of ChangeOut from a dict
change_out_from_dict = ChangeOut.from_dict(change_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
