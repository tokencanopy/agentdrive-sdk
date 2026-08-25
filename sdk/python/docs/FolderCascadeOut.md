# FolderCascadeOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | [**FolderOut**](FolderOut.md) |  | 
**cascade** | **Dict[str, int]** |  | 

## Example

```python
from agentdrive_sdk.models.folder_cascade_out import FolderCascadeOut

# TODO update the JSON string below
json = "{}"
# create an instance of FolderCascadeOut from a JSON string
folder_cascade_out_instance = FolderCascadeOut.from_json(json)
# print the JSON string representation of the object
print(FolderCascadeOut.to_json())

# convert the object into a dict
folder_cascade_out_dict = folder_cascade_out_instance.to_dict()
# create an instance of FolderCascadeOut from a dict
folder_cascade_out_from_dict = FolderCascadeOut.from_dict(folder_cascade_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


