# UploadBeginOut

Response of `POST /v0/uploads`. PUT the bytes to `upload_url` (no auth header — the URL is the credential), then `POST .../commit`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  |
**headers** | **Dict[str, str]** |  |
**max_bytes** | **int** |  |
**method** | **str** |  | [optional] [default to 'PUT']
**upload_id** | **str** |  |
**upload_url** | **str** |  |

## Example

```python
from agentdrive_sdk.models.upload_begin_out import UploadBeginOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadBeginOut from a JSON string
upload_begin_out_instance = UploadBeginOut.from_json(json)
# print the JSON string representation of the object
print(UploadBeginOut.to_json())

# convert the object into a dict
upload_begin_out_dict = upload_begin_out_instance.to_dict()
# create an instance of UploadBeginOut from a dict
upload_begin_out_from_dict = UploadBeginOut.from_dict(upload_begin_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
