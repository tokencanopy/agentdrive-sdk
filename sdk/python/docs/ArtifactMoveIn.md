# ArtifactMoveIn

POST /v0/artifacts/{art_id}/move body — rename / move to a new path on the same drive. Mirrors `FolderMoveIn`; its own schema (vs. reusing another body) keeps the move surface self-documenting in the OpenAPI spec.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  |

## Example

```python
from agentdrive_sdk.models.artifact_move_in import ArtifactMoveIn

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactMoveIn from a JSON string
artifact_move_in_instance = ArtifactMoveIn.from_json(json)
# print the JSON string representation of the object
print(ArtifactMoveIn.to_json())

# convert the object into a dict
artifact_move_in_dict = artifact_move_in_instance.to_dict()
# create an instance of ArtifactMoveIn from a dict
artifact_move_in_from_dict = ArtifactMoveIn.from_dict(artifact_move_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
