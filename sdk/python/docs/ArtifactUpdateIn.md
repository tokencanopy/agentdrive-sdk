# ArtifactUpdateIn

PATCH /v0/drives/{id}/artifacts/{artifact_id} body — at least one field is required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**labels** | **List[str]** |  | [optional] 

## Example

```python
from agentdrive_sdk.models.artifact_update_in import ArtifactUpdateIn

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactUpdateIn from a JSON string
artifact_update_in_instance = ArtifactUpdateIn.from_json(json)
# print the JSON string representation of the object
print(ArtifactUpdateIn.to_json())

# convert the object into a dict
artifact_update_in_dict = artifact_update_in_instance.to_dict()
# create an instance of ArtifactUpdateIn from a dict
artifact_update_in_from_dict = ArtifactUpdateIn.from_dict(artifact_update_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


