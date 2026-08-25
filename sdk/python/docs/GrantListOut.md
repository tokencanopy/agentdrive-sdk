# GrantListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GrantOut]**](GrantOut.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.grant_list_out import GrantListOut

# TODO update the JSON string below
json = "{}"
# create an instance of GrantListOut from a JSON string
grant_list_out_instance = GrantListOut.from_json(json)
# print the JSON string representation of the object
print(GrantListOut.to_json())

# convert the object into a dict
grant_list_out_dict = grant_list_out_instance.to_dict()
# create an instance of GrantListOut from a dict
grant_list_out_from_dict = GrantListOut.from_dict(grant_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


