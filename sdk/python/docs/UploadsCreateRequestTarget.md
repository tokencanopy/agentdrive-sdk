# UploadsCreateRequestTarget

Exactly one destination union member.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**parent_folder_id** | **str** |  | 
**name** | **str** |  | 
**artifact_id** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.uploads_create_request_target import UploadsCreateRequestTarget

# TODO update the JSON string below
json = "{}"
# create an instance of UploadsCreateRequestTarget from a JSON string
uploads_create_request_target_instance = UploadsCreateRequestTarget.from_json(json)
# print the JSON string representation of the object
print(UploadsCreateRequestTarget.to_json())

# convert the object into a dict
uploads_create_request_target_dict = uploads_create_request_target_instance.to_dict()
# create an instance of UploadsCreateRequestTarget from a dict
uploads_create_request_target_from_dict = UploadsCreateRequestTarget.from_dict(uploads_create_request_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


