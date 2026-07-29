# FolderMoveIn

POST /v0/folders/{fld_id}/move body — rename / move.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  |

## Example

```python
from agentdrive_sdk.models.folder_move_in import FolderMoveIn

# TODO update the JSON string below
json = "{}"
# create an instance of FolderMoveIn from a JSON string
folder_move_in_instance = FolderMoveIn.from_json(json)
# print the JSON string representation of the object
print(FolderMoveIn.to_json())

# convert the object into a dict
folder_move_in_dict = folder_move_in_instance.to_dict()
# create an instance of FolderMoveIn from a dict
folder_move_in_from_dict = FolderMoveIn.from_dict(folder_move_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
