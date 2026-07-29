# ValidationErrorBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  |
**fields** | [**List[ValidationIssue]**](ValidationIssue.md) |  |
**message** | **str** |  |

## Example

```python
from agentdrive_sdk.models.validation_error_body import ValidationErrorBody

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorBody from a JSON string
validation_error_body_instance = ValidationErrorBody.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorBody.to_json())

# convert the object into a dict
validation_error_body_dict = validation_error_body_instance.to_dict()
# create an instance of ValidationErrorBody from a dict
validation_error_body_from_dict = ValidationErrorBody.from_dict(validation_error_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
