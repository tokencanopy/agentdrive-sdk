# UploadTargetArtifactOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  |
**name** | **str** |  |
**parent_folder_id** | **str** |  |

## Example

```python
from agentdrive_sdk.models.upload_target_artifact_out import UploadTargetArtifactOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadTargetArtifactOut from a JSON string
upload_target_artifact_out_instance = UploadTargetArtifactOut.from_json(json)
# print the JSON string representation of the object
print(UploadTargetArtifactOut.to_json())

# convert the object into a dict
upload_target_artifact_out_dict = upload_target_artifact_out_instance.to_dict()
# create an instance of UploadTargetArtifactOut from a dict
upload_target_artifact_out_from_dict = UploadTargetArtifactOut.from_dict(upload_target_artifact_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
