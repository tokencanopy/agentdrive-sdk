# ValidationIssue

One Pydantic/FastAPI validation issue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ctx** | **Dict[str, object]** |  | [optional]
**input** | [**AnyOf**](AnyOf.md) |  | [optional]
**loc** | [**List[LocInner]**](LocInner.md) |  |
**msg** | **str** |  |
**type** | **str** |  |

## Example

```python
from agentdrive_sdk.models.validation_issue import ValidationIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationIssue from a JSON string
validation_issue_instance = ValidationIssue.from_json(json)
# print the JSON string representation of the object
print(ValidationIssue.to_json())

# convert the object into a dict
validation_issue_dict = validation_issue_instance.to_dict()
# create an instance of ValidationIssue from a dict
validation_issue_from_dict = ValidationIssue.from_dict(validation_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
