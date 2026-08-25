# ValidationErrorResponseErrorDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[ValidationErrorResponseErrorDetailsFieldsInner]**](ValidationErrorResponseErrorDetailsFieldsInner.md) |  | [optional] 

## Example

```python
from agentdrive_sdk.models.validation_error_response_error_details import ValidationErrorResponseErrorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorResponseErrorDetails from a JSON string
validation_error_response_error_details_instance = ValidationErrorResponseErrorDetails.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorResponseErrorDetails.to_json())

# convert the object into a dict
validation_error_response_error_details_dict = validation_error_response_error_details_instance.to_dict()
# create an instance of ValidationErrorResponseErrorDetails from a dict
validation_error_response_error_details_from_dict = ValidationErrorResponseErrorDetails.from_dict(validation_error_response_error_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


