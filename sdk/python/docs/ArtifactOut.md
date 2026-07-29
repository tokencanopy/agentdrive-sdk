# ArtifactOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  |
**created_at** | **datetime** |  |
**drive_id** | **str** |  |
**embedded_at** | **datetime** |  | [optional]
**etag** | **str** |  |
**file_type** | **str** |  |
**hash** | **str** |  |
**id** | **str** |  |
**indexed_at** | **datetime** |  | [optional]
**labels** | **List[str]** |  | [optional]
**llm_index** | **Dict[str, object]** |  | [optional]
**metadata** | **Dict[str, object]** |  | [optional]
**metageneration** | **int** |  | [optional] [default to 1]
**path** | **str** |  |
**permalink** | **str** |  |
**size_bytes** | **int** |  |
**source** | [**ArtifactSource**](ArtifactSource.md) |  | [optional]
**updated_at** | **datetime** |  |
**url** | **str** |  |
**version_number** | **int** |  | [optional] [default to 1]

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
