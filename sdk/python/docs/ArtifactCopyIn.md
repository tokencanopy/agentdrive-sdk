# ArtifactCopyIn

POST /v0/drives/{id}/artifacts/{artifact_id}/copy body.  ``destination_drive_id`` must equal the source drive (or be absent) — cross-drive copy is out of v0 scope and rejected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_drive_id** | **str** |  | [optional] 
**destination_parent_id** | **str** |  | 
**destination_name** | **str** |  | 
**version_id** | **str** |  | [optional] 

## Example

```python
from agentdrive_sdk.models.artifact_copy_in import ArtifactCopyIn

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactCopyIn from a JSON string
artifact_copy_in_instance = ArtifactCopyIn.from_json(json)
# print the JSON string representation of the object
print(ArtifactCopyIn.to_json())

# convert the object into a dict
artifact_copy_in_dict = artifact_copy_in_instance.to_dict()
# create an instance of ArtifactCopyIn from a dict
artifact_copy_in_from_dict = ArtifactCopyIn.from_dict(artifact_copy_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


