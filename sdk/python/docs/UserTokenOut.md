# UserTokenOut

One `ad_user_` token — metadata only. The raw token is NEVER exposed over the API (minting is web-only, reveal-once); this shape omits both the raw value and the stored hash by construction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**prefix** | **str** |  | 
**label** | **str** |  | [optional] 
**scope** | **str** |  | 
**default_drive_id** | **str** |  | [optional] 
**last_used_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**revoked_at** | **datetime** |  | [optional] 

## Example

```python
from agentdrive_sdk.models.user_token_out import UserTokenOut

# TODO update the JSON string below
json = "{}"
# create an instance of UserTokenOut from a JSON string
user_token_out_instance = UserTokenOut.from_json(json)
# print the JSON string representation of the object
print(UserTokenOut.to_json())

# convert the object into a dict
user_token_out_dict = user_token_out_instance.to_dict()
# create an instance of UserTokenOut from a dict
user_token_out_from_dict = UserTokenOut.from_dict(user_token_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


