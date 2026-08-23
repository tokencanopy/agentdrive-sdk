# VersionOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_id** | **str** |  |
**content_type** | **str** |  |
**created_at** | **datetime** |  |
**created_by** | **str** |  |
**hash** | **str** |  |
**id** | **str** |  |
**parent_version_id** | **str** |  |
**size_bytes** | **int** |  |
**version_number** | **int** |  |

## Example

```python
from agentdrive_sdk.models.version_out import VersionOut

# TODO update the JSON string below
json = "{}"
# create an instance of VersionOut from a JSON string
version_out_instance = VersionOut.from_json(json)
# print the JSON string representation of the object
print(VersionOut.to_json())

# convert the object into a dict
version_out_dict = version_out_instance.to_dict()
# create an instance of VersionOut from a dict
version_out_from_dict = VersionOut.from_dict(version_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
