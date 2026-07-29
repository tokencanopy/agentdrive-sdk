# TrashArtifactOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_at** | **datetime** |  | [optional]
**id** | **str** |  |
**path** | **str** |  |
**purge_at** | **datetime** |  | [optional]
**restore_url** | **str** |  |
**size_bytes** | **int** |  |

## Example

```python
from agentdrive_sdk.models.trash_artifact_out import TrashArtifactOut

# TODO update the JSON string below
json = "{}"
# create an instance of TrashArtifactOut from a JSON string
trash_artifact_out_instance = TrashArtifactOut.from_json(json)
# print the JSON string representation of the object
print(TrashArtifactOut.to_json())

# convert the object into a dict
trash_artifact_out_dict = trash_artifact_out_instance.to_dict()
# create an instance of TrashArtifactOut from a dict
trash_artifact_out_from_dict = TrashArtifactOut.from_dict(trash_artifact_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
