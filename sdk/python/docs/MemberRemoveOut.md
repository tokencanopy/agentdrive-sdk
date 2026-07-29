# MemberRemoveOut

DELETE /v0/members/{user_id} response — the member-removal receipt. `id` is the removed user's id (replaces the ad-hoc `removed` key).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  |
**ok** | **bool** |  | [optional] [default to True]
**organization_id** | **str** |  |

## Example

```python
from agentdrive_sdk.models.member_remove_out import MemberRemoveOut

# TODO update the JSON string below
json = "{}"
# create an instance of MemberRemoveOut from a JSON string
member_remove_out_instance = MemberRemoveOut.from_json(json)
# print the JSON string representation of the object
print(MemberRemoveOut.to_json())

# convert the object into a dict
member_remove_out_dict = member_remove_out_instance.to_dict()
# create an instance of MemberRemoveOut from a dict
member_remove_out_from_dict = MemberRemoveOut.from_dict(member_remove_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
