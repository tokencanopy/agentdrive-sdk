# UserTokenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UserTokenOut]**](UserTokenOut.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from agentdrive_sdk.models.user_token_list import UserTokenList

# TODO update the JSON string below
json = "{}"
# create an instance of UserTokenList from a JSON string
user_token_list_instance = UserTokenList.from_json(json)
# print the JSON string representation of the object
print(UserTokenList.to_json())

# convert the object into a dict
user_token_list_dict = user_token_list_instance.to_dict()
# create an instance of UserTokenList from a dict
user_token_list_from_dict = UserTokenList.from_dict(user_token_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


