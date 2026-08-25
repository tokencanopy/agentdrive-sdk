# ArtifactOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**drive_id** | **str** |  | 
**parent_id** | **str** |  | 
**name** | **str** |  | 
**content_type** | **str** |  | 
**content_preview** | **str** |  | 
**labels** | **List[str]** |  | 
**metadata** | **Dict[str, object]** |  | 
**head_version_id** | **str** |  | 
**revision** | **str** |  | 
**state** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | 
**effective_visibility** | **str** | Server-computed exposure summary, resolved over the artifact&#39;s live grants, its whole folder ancestry, and the drive. &#39;public&#39; when any live grant has principal_type &#39;public&#39;; otherwise &#39;shared&#39; when a live grant names a principal other than the drive&#39;s creator; otherwise &#39;private&#39;. Describes exposure, NOT the caller&#39;s own access. | 

## Example

```python
from agentdrive_sdk.models.artifact_out import ArtifactOut

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactOut from a JSON string
artifact_out_instance = ArtifactOut.from_json(json)
# print the JSON string representation of the object
print(ArtifactOut.to_json())

# convert the object into a dict
artifact_out_dict = artifact_out_instance.to_dict()
# create an instance of ArtifactOut from a dict
artifact_out_from_dict = ArtifactOut.from_dict(artifact_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


