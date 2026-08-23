# GrantUpdateIn

PATCH /v0/drives/{id}/grants/{grant_id} body — at least one field is required. An explicit ``expires_at: null`` clears the expiry; omitting it leaves it unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  | [optional]
**role** | **str** |  | [optional]

## Example

```python
from agentdrive_sdk.models.grant_update_in import GrantUpdateIn

# TODO update the JSON string below
json = "{}"
# create an instance of GrantUpdateIn from a JSON string
grant_update_in_instance = GrantUpdateIn.from_json(json)
# print the JSON string representation of the object
print(GrantUpdateIn.to_json())

# convert the object into a dict
grant_update_in_dict = grant_update_in_instance.to_dict()
# create an instance of GrantUpdateIn from a dict
grant_update_in_from_dict = GrantUpdateIn.from_dict(grant_update_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
