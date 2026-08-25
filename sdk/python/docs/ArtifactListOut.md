# ArtifactListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ArtifactOut]**](ArtifactOut.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.artifact_list_out import ArtifactListOut

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactListOut from a JSON string
artifact_list_out_instance = ArtifactListOut.from_json(json)
# print the JSON string representation of the object
print(ArtifactListOut.to_json())

# convert the object into a dict
artifact_list_out_dict = artifact_list_out_instance.to_dict()
# create an instance of ArtifactListOut from a dict
artifact_list_out_from_dict = ArtifactListOut.from_dict(artifact_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


