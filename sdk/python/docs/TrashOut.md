# TrashOut

Trash collection with a compatibility-preserving pagination opt-in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts** | [**List[TrashArtifactOut]**](TrashArtifactOut.md) | Deprecated alias of items. |
**drive** | [**TrashDriveOut**](TrashDriveOut.md) |  |
**items** | [**List[TrashArtifactOut]**](TrashArtifactOut.md) |  |
**next_cursor** | **str** |  | [optional]

## Example

```python
from agentdrive_sdk.models.trash_out import TrashOut

# TODO update the JSON string below
json = "{}"
# create an instance of TrashOut from a JSON string
trash_out_instance = TrashOut.from_json(json)
# print the JSON string representation of the object
print(TrashOut.to_json())

# convert the object into a dict
trash_out_dict = trash_out_instance.to_dict()
# create an instance of TrashOut from a dict
trash_out_from_dict = TrashOut.from_dict(trash_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
