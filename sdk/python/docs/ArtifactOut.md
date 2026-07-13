# ArtifactOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**drive_id** | **str** |  | 
**path** | **str** |  | 
**url** | **str** |  | 
**permalink** | **str** |  | 
**content_type** | **str** |  | 
**file_type** | **str** |  | 
**size_bytes** | **int** |  | 
**hash** | **str** |  | 
**version_number** | **int** |  | [optional] [default to 1]
**metageneration** | **int** |  | [optional] [default to 1]
**etag** | **str** |  | 
**labels** | **List[str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**source** | [**ArtifactSource**](ArtifactSource.md) |  | [optional] 
**indexed_at** | **datetime** |  | [optional] 
**embedded_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**llm_index** | **Dict[str, object]** |  | [optional] 

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


