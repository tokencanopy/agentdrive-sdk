# MemberInviteIn

POST /v0/members/invite body — invite a person by email.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  |
**role** | **str** |  | [optional] [default to 'member']

## Example

```python
from agentdrive_sdk.models.member_invite_in import MemberInviteIn

# TODO update the JSON string below
json = "{}"
# create an instance of MemberInviteIn from a JSON string
member_invite_in_instance = MemberInviteIn.from_json(json)
# print the JSON string representation of the object
print(MemberInviteIn.to_json())

# convert the object into a dict
member_invite_in_dict = member_invite_in_instance.to_dict()
# create an instance of MemberInviteIn from a dict
member_invite_in_from_dict = MemberInviteIn.from_dict(member_invite_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
