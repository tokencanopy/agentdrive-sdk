# ArtifactSource

Caller-supplied provenance metadata, attached to an artifact.  v0.6 model: a list of typed refs. The legacy v0.5 fields (`agent_id`, `run_id`, `prompt_hash`) were never validated and are superseded by the `refs` shape (an agent-id ref would be `{\"type\": \"agent\", \"id\": \"...\"}` in v0.6 vocabulary).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refs** | [**List[SourceRef]**](SourceRef.md) |  | [optional]

## Example

```python
from agentdrive_sdk.models.artifact_source import ArtifactSource

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactSource from a JSON string
artifact_source_instance = ArtifactSource.from_json(json)
# print the JSON string representation of the object
print(ArtifactSource.to_json())

# convert the object into a dict
artifact_source_dict = artifact_source_instance.to_dict()
# create an instance of ArtifactSource from a dict
artifact_source_from_dict = ArtifactSource.from_dict(artifact_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
