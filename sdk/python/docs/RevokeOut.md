# RevokeOut

DELETE /v0/grants/{grn_id}, DELETE /v0/shares/{shr_id}, DELETE /v0/invitations/{invitation_id} response — the unified revoke receipt. `revoked` is a COUNT: 1 when a live row was revoked, 0 when it was already gone (DELETE is idempotent).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [optional] [default to True]
**id** | **str** |  | 
**revoked** | **int** |  | 

## Example

```python
from agentdrive_sdk.models.revoke_out import RevokeOut

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeOut from a JSON string
revoke_out_instance = RevokeOut.from_json(json)
# print the JSON string representation of the object
print(RevokeOut.to_json())

# convert the object into a dict
revoke_out_dict = revoke_out_instance.to_dict()
# create an instance of RevokeOut from a dict
revoke_out_from_dict = RevokeOut.from_dict(revoke_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


