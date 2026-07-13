# CopyIn

POST /v0/artifacts/{art_id}/copy body — duplicate to new path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**source** | [**ArtifactSource**](ArtifactSource.md) |  | [optional] 
**from_generation** | **int** |  | [optional] 

## Example

```python
from agentdrive_sdk.models.copy_in import CopyIn

# TODO update the JSON string below
json = "{}"
# create an instance of CopyIn from a JSON string
copy_in_instance = CopyIn.from_json(json)
# print the JSON string representation of the object
print(CopyIn.to_json())

# convert the object into a dict
copy_in_dict = copy_in_instance.to_dict()
# create an instance of CopyIn from a dict
copy_in_from_dict = CopyIn.from_dict(copy_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


