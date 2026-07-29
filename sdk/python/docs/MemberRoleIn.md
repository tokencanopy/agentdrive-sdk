# MemberRoleIn

PATCH /v0/members/{user} body — promote/demote a member.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  |

## Example

```python
from agentdrive_sdk.models.member_role_in import MemberRoleIn

# TODO update the JSON string below
json = "{}"
# create an instance of MemberRoleIn from a JSON string
member_role_in_instance = MemberRoleIn.from_json(json)
# print the JSON string representation of the object
print(MemberRoleIn.to_json())

# convert the object into a dict
member_role_in_dict = member_role_in_instance.to_dict()
# create an instance of MemberRoleIn from a dict
member_role_in_from_dict = MemberRoleIn.from_dict(member_role_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
