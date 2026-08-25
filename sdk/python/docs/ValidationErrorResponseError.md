# ValidationErrorResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**details** | [**ValidationErrorResponseErrorDetails**](ValidationErrorResponseErrorDetails.md) |  | [optional] 

## Example

```python
from agentdrive_sdk.models.validation_error_response_error import ValidationErrorResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorResponseError from a JSON string
validation_error_response_error_instance = ValidationErrorResponseError.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorResponseError.to_json())

# convert the object into a dict
validation_error_response_error_dict = validation_error_response_error_instance.to_dict()
# create an instance of ValidationErrorResponseError from a dict
validation_error_response_error_from_dict = ValidationErrorResponseError.from_dict(validation_error_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


