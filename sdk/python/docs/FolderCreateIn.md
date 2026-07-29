# FolderCreateIn

PUT /v0/folders/{path} body for the optional metadata params. Empty body is fine — `mkdir` with no description just creates the folder row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional]

## Example

```python
from agentdrive_sdk.models.folder_create_in import FolderCreateIn

# TODO update the JSON string below
json = "{}"
# create an instance of FolderCreateIn from a JSON string
folder_create_in_instance = FolderCreateIn.from_json(json)
# print the JSON string representation of the object
print(FolderCreateIn.to_json())

# convert the object into a dict
folder_create_in_dict = folder_create_in_instance.to_dict()
# create an instance of FolderCreateIn from a dict
folder_create_in_from_dict = FolderCreateIn.from_dict(folder_create_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
