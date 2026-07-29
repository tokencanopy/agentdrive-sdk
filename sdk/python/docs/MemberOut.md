# MemberOut

One live member of a workspace — metadata for the members page / `GET /v0/members`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  |
**email** | **str** |  |
**first_name** | **str** |  | [optional]
**last_name** | **str** |  | [optional]
**role** | **str** |  |
**user_id** | **str** |  |

## Example

```python
from agentdrive_sdk.models.member_out import MemberOut

# TODO update the JSON string below
json = "{}"
# create an instance of MemberOut from a JSON string
member_out_instance = MemberOut.from_json(json)
# print the JSON string representation of the object
print(MemberOut.to_json())

# convert the object into a dict
member_out_dict = member_out_instance.to_dict()
# create an instance of MemberOut from a dict
member_out_from_dict = MemberOut.from_dict(member_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
