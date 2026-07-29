# InvitationOut

One workspace invitation — metadata only; the raw token is never surfaced over the API (it lives only in the invite email).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  |
**email** | **str** |  |
**expires_at** | **datetime** |  |
**id** | **str** |  |
**invited_by** | **str** |  | [optional]
**organization_id** | **str** |  |
**role** | **str** |  |
**status** | **str** |  |

## Example

```python
from agentdrive_sdk.models.invitation_out import InvitationOut

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationOut from a JSON string
invitation_out_instance = InvitationOut.from_json(json)
# print the JSON string representation of the object
print(InvitationOut.to_json())

# convert the object into a dict
invitation_out_dict = invitation_out_instance.to_dict()
# create an instance of InvitationOut from a dict
invitation_out_from_dict = InvitationOut.from_dict(invitation_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
