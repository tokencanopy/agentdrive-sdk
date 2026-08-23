# UploadsCreateRequestTargetOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  |
**name** | **str** |  |
**parent_folder_id** | **str** |  |

## Example

```python
from agentdrive_sdk.models.uploads_create_request_target_one_of import UploadsCreateRequestTargetOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of UploadsCreateRequestTargetOneOf from a JSON string
uploads_create_request_target_one_of_instance = UploadsCreateRequestTargetOneOf.from_json(json)
# print the JSON string representation of the object
print(UploadsCreateRequestTargetOneOf.to_json())

# convert the object into a dict
uploads_create_request_target_one_of_dict = uploads_create_request_target_one_of_instance.to_dict()
# create an instance of UploadsCreateRequestTargetOneOf from a dict
uploads_create_request_target_one_of_from_dict = UploadsCreateRequestTargetOneOf.from_dict(uploads_create_request_target_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
