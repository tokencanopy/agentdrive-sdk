# UploadStatusOut

Response of `GET /v0/uploads/{upload_id}` — the live state of a direct-to-GCS upload session (large-upload-design.md §5).  `state` is derived, not a stored column:   * `initiated` — session open; PUT the bytes to the `upload_url`, then                   `POST /v0/uploads/{upload_id}/commit`.   * `committed` — the bytes landed and the artifact was created                   (`committed_at` is set).   * `aborted`   — released via `DELETE /v0/uploads/{upload_id}`.   * `expired`   — past `expires_at` without a commit; the reservation is                   reclaimed by the GC sweep.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committed_at** | **datetime** |  | [optional]
**content_type** | **str** |  |
**created_at** | **datetime** |  |
**expires_at** | **datetime** |  |
**max_bytes** | **int** |  |
**path** | **str** |  |
**size_bytes** | **int** |  |
**state** | **str** |  |
**upload_id** | **str** |  |

## Example

```python
from agentdrive_sdk.models.upload_status_out import UploadStatusOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadStatusOut from a JSON string
upload_status_out_instance = UploadStatusOut.from_json(json)
# print the JSON string representation of the object
print(UploadStatusOut.to_json())

# convert the object into a dict
upload_status_out_dict = upload_status_out_instance.to_dict()
# create an instance of UploadStatusOut from a dict
upload_status_out_from_dict = UploadStatusOut.from_dict(upload_status_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
