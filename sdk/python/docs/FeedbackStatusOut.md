# FeedbackStatusOut

GET /v0/feedback/{fbk_id} response — lifecycle status of feedback THIS drive filed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **bool** |  |
**created_at** | **datetime** |  |
**duplicate_of** | **str** |  | [optional]
**id** | **str** |  |
**kind** | **str** |  |
**status** | **str** |  |
**status_changed_at** | **datetime** |  |
**title** | **str** |  |

## Example

```python
from agentdrive_sdk.models.feedback_status_out import FeedbackStatusOut

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackStatusOut from a JSON string
feedback_status_out_instance = FeedbackStatusOut.from_json(json)
# print the JSON string representation of the object
print(FeedbackStatusOut.to_json())

# convert the object into a dict
feedback_status_out_dict = feedback_status_out_instance.to_dict()
# create an instance of FeedbackStatusOut from a dict
feedback_status_out_from_dict = FeedbackStatusOut.from_dict(feedback_status_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
