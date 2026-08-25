# VersionCreatedOut

The append/restore response — a version plus the artifact's new revision, which the version-creating 201 rotates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**artifact_id** | **str** |  | 
**version_number** | **int** |  | 
**parent_version_id** | **str** |  | 
**content_type** | **str** |  | 
**size_bytes** | **int** |  | 
**hash** | **str** |  | 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | 
**artifact_revision** | **str** | The artifact&#39;s revision after this version became head — the If-Match value for the next mutation. | 

## Example

```python
from agentdrive_sdk.models.version_created_out import VersionCreatedOut

# TODO update the JSON string below
json = "{}"
# create an instance of VersionCreatedOut from a JSON string
version_created_out_instance = VersionCreatedOut.from_json(json)
# print the JSON string representation of the object
print(VersionCreatedOut.to_json())

# convert the object into a dict
version_created_out_dict = version_created_out_instance.to_dict()
# create an instance of VersionCreatedOut from a dict
version_created_out_from_dict = VersionCreatedOut.from_dict(version_created_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


