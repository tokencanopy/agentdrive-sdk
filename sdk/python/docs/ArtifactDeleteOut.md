# ArtifactDeleteOut

DELETE /v0/artifacts/{art_id} response — the soft-delete receipt. Reversible until the GC cron hard-deletes at `purge_at`; `restore_url` points at the by-id restore endpoint (deletion-design.md §5.3).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [optional] [default to True]
**id** | **str** |  | 
**path** | **str** |  | 
**deleted_at** | **datetime** |  | 
**purge_at** | **datetime** |  | 
**restore_url** | **str** |  | [optional] 

## Example

```python
from agentdrive_sdk.models.artifact_delete_out import ArtifactDeleteOut

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactDeleteOut from a JSON string
artifact_delete_out_instance = ArtifactDeleteOut.from_json(json)
# print the JSON string representation of the object
print(ArtifactDeleteOut.to_json())

# convert the object into a dict
artifact_delete_out_dict = artifact_delete_out_instance.to_dict()
# create an instance of ArtifactDeleteOut from a dict
artifact_delete_out_from_dict = ArtifactDeleteOut.from_dict(artifact_delete_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


