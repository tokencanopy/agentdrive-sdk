# ValidationErrorResponseErrorDetailsFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | [optional]
**reason** | **str** |  | [optional]

## Example

```python
from agentdrive_sdk.models.validation_error_response_error_details_fields_inner import ValidationErrorResponseErrorDetailsFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorResponseErrorDetailsFieldsInner from a JSON string
validation_error_response_error_details_fields_inner_instance = ValidationErrorResponseErrorDetailsFieldsInner.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorResponseErrorDetailsFieldsInner.to_json())

# convert the object into a dict
validation_error_response_error_details_fields_inner_dict = validation_error_response_error_details_fields_inner_instance.to_dict()
# create an instance of ValidationErrorResponseErrorDetailsFieldsInner from a dict
validation_error_response_error_details_fields_inner_from_dict = ValidationErrorResponseErrorDetailsFieldsInner.from_dict(validation_error_response_error_details_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
