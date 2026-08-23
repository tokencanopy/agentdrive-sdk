# ShareCreateOut

The create/rotate response — the ONLY response carrying the plaintext secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  |
**created_by** | **str** |  |
**drive_id** | **str** |  |
**expires_at** | **datetime** |  |
**id** | **str** |  |
**resource_id** | **str** |  |
**resource_type** | **str** |  |
**revision** | **str** |  |
**revoked_at** | **datetime** |  |
**rotated_at** | **datetime** |  |
**secret** | **str** | Plaintext share secret. Present only on first execution of a create or rotate; null on idempotent replay — rotate to obtain a new secret. | [optional]
**state** | **str** |  |

## Example

```python
from agentdrive_sdk.models.share_create_out import ShareCreateOut

# TODO update the JSON string below
json = "{}"
# create an instance of ShareCreateOut from a JSON string
share_create_out_instance = ShareCreateOut.from_json(json)
# print the JSON string representation of the object
print(ShareCreateOut.to_json())

# convert the object into a dict
share_create_out_dict = share_create_out_instance.to_dict()
# create an instance of ShareCreateOut from a dict
share_create_out_from_dict = ShareCreateOut.from_dict(share_create_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
