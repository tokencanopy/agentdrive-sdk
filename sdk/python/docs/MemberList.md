# MemberList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MemberOut]**](MemberOut.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from agentdrive_sdk.models.member_list import MemberList

# TODO update the JSON string below
json = "{}"
# create an instance of MemberList from a JSON string
member_list_instance = MemberList.from_json(json)
# print the JSON string representation of the object
print(MemberList.to_json())

# convert the object into a dict
member_list_dict = member_list_instance.to_dict()
# create an instance of MemberList from a dict
member_list_from_dict = MemberList.from_dict(member_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


