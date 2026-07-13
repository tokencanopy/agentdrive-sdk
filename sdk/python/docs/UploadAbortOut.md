# UploadAbortOut

Response of `DELETE /v0/uploads/{upload_id}` — the session is released. `released_bytes` is the reservation returned to the drive's quota (the session's `size_bytes` for a live `initiated` session; `0` when the session was already aborted or already expired — the GC sweep owns an expired session's release).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** |  | 
**state** | **str** |  | [optional] [default to 'aborted']
**released_bytes** | **int** |  | 

## Example

```python
from agentdrive_sdk.models.upload_abort_out import UploadAbortOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadAbortOut from a JSON string
upload_abort_out_instance = UploadAbortOut.from_json(json)
# print the JSON string representation of the object
print(UploadAbortOut.to_json())

# convert the object into a dict
upload_abort_out_dict = upload_abort_out_instance.to_dict()
# create an instance of UploadAbortOut from a dict
upload_abort_out_from_dict = UploadAbortOut.from_dict(upload_abort_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


