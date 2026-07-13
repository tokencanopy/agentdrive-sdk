# ArtifactPatchIn

PATCH /v0/artifacts/{art_id} body — metadata-only partial (JSON-merge-patch) update.  Every field is optional. Presence is what matters, not the value: a field left out of the body (per Pydantic `model_fields_set`) is left unchanged; a field that IS present is applied — with an explicit `null` / `[]` / `{}` meaning \"clear it\". This mirrors the MCP `set_metadata` tool and the core `patch_artifact_metadata` sentinel semantics (omitted = preserve, present = replace/clear).    * `labels`   — replace the label set; `[]` or `null` clears it.   * `metadata` — replace the free-form metadata object; `{}` or `null`                  clears it.   * `source`   — replace provenance refs; `null` (or `{\"refs\": []}`)                  clears them.  PATCH is metadata-only: to move/rename an artifact, use `POST /v0/artifacts/{art_id}/move`. `extra=\"forbid\"` makes a stray field (notably a legacy `path`) a hard 422 rather than a silent no-op — a clean-break signal to migrate to the move verb.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**source** | [**ArtifactSource**](ArtifactSource.md) |  | [optional] 

## Example

```python
from agentdrive_sdk.models.artifact_patch_in import ArtifactPatchIn

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactPatchIn from a JSON string
artifact_patch_in_instance = ArtifactPatchIn.from_json(json)
# print the JSON string representation of the object
print(ArtifactPatchIn.to_json())

# convert the object into a dict
artifact_patch_in_dict = artifact_patch_in_instance.to_dict()
# create an instance of ArtifactPatchIn from a dict
artifact_patch_in_from_dict = ArtifactPatchIn.from_dict(artifact_patch_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


