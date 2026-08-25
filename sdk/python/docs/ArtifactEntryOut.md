# ArtifactEntryOut

Compact D13 artifact member; content and rich metadata stay excluded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**revision** | **str** |  | 
**updated_at** | **datetime** |  | 
**state** | **str** |  | 
**deleted_at** | **datetime** |  | 
**size_bytes** | **int** |  | 
**content_type** | **str** |  | 
**head_version_id** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.artifact_entry_out import ArtifactEntryOut

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactEntryOut from a JSON string
artifact_entry_out_instance = ArtifactEntryOut.from_json(json)
# print the JSON string representation of the object
print(ArtifactEntryOut.to_json())

# convert the object into a dict
artifact_entry_out_dict = artifact_entry_out_instance.to_dict()
# create an instance of ArtifactEntryOut from a dict
artifact_entry_out_from_dict = ArtifactEntryOut.from_dict(artifact_entry_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


