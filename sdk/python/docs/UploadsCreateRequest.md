# UploadsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**UploadsCreateRequestContent**](UploadsCreateRequestContent.md) |  |
**target** | [**UploadsCreateRequestTarget**](UploadsCreateRequestTarget.md) |  |

## Example

```python
from agentdrive_sdk.models.uploads_create_request import UploadsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadsCreateRequest from a JSON string
uploads_create_request_instance = UploadsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(UploadsCreateRequest.to_json())

# convert the object into a dict
uploads_create_request_dict = uploads_create_request_instance.to_dict()
# create an instance of UploadsCreateRequest from a dict
uploads_create_request_from_dict = UploadsCreateRequest.from_dict(uploads_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
