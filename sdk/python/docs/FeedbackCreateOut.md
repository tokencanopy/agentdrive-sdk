# FeedbackCreateOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **bool** |  |
**id** | **str** |  |
**note** | **str** |  | [optional]
**status** | **str** |  |

## Example

```python
from agentdrive_sdk.models.feedback_create_out import FeedbackCreateOut

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackCreateOut from a JSON string
feedback_create_out_instance = FeedbackCreateOut.from_json(json)
# print the JSON string representation of the object
print(FeedbackCreateOut.to_json())

# convert the object into a dict
feedback_create_out_dict = feedback_create_out_instance.to_dict()
# create an instance of FeedbackCreateOut from a dict
feedback_create_out_from_dict = FeedbackCreateOut.from_dict(feedback_create_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
