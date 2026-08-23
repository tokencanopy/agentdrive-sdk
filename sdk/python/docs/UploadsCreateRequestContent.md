# UploadsCreateRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | [**UploadsCreateRequestContentChecksum**](UploadsCreateRequestContentChecksum.md) |  |
**media_type** | **str** | Bare IANA type/subtype, no parameters. |
**size_bytes** | **int** | Declared object size in bytes, within the enabled B8-configured window. |

## Example

```python
from agentdrive_sdk.models.uploads_create_request_content import UploadsCreateRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of UploadsCreateRequestContent from a JSON string
uploads_create_request_content_instance = UploadsCreateRequestContent.from_json(json)
# print the JSON string representation of the object
print(UploadsCreateRequestContent.to_json())

# convert the object into a dict
uploads_create_request_content_dict = uploads_create_request_content_instance.to_dict()
# create an instance of UploadsCreateRequestContent from a dict
uploads_create_request_content_from_dict = UploadsCreateRequestContent.from_dict(uploads_create_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
