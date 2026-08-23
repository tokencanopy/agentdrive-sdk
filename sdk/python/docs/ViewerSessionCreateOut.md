# ViewerSessionCreateOut

The mint response — the ONLY response carrying the plaintext viewer credential. The credential authorizes the isolated viewer host's `/view/doc` and `/view/content` for this one pinned version, via an Authorization header only — it must never be placed in a URL, cookie, or persistent storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_id** | **str** |  |
**created_at** | **datetime** |  |
**credential** | **str** | Plaintext viewer credential. Present only on first execution of a mint; null on idempotent replay — mint a new session with a fresh Idempotency-Key to obtain a credential. | [optional]
**drive_id** | **str** |  |
**expires_at** | **datetime** |  |
**expires_in** | **int** | Seconds until the session expires, from mint time. |
**id** | **str** |  |
**version_id** | **str** |  |

## Example

```python
from agentdrive_sdk.models.viewer_session_create_out import ViewerSessionCreateOut

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerSessionCreateOut from a JSON string
viewer_session_create_out_instance = ViewerSessionCreateOut.from_json(json)
# print the JSON string representation of the object
print(ViewerSessionCreateOut.to_json())

# convert the object into a dict
viewer_session_create_out_dict = viewer_session_create_out_instance.to_dict()
# create an instance of ViewerSessionCreateOut from a dict
viewer_session_create_out_from_dict = ViewerSessionCreateOut.from_dict(viewer_session_create_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
