# GrantPrincipalIn

Who a grant is for. `anyone` carries no id/email; `org`/`agent` require `id`; `user` requires exactly one of `id` / `email` (an email with no account becomes a pending-email invite resolved on sign-in).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional]
**id** | **str** |  | [optional]
**type** | **str** |  |

## Example

```python
from agentdrive_sdk.models.grant_principal_in import GrantPrincipalIn

# TODO update the JSON string below
json = "{}"
# create an instance of GrantPrincipalIn from a JSON string
grant_principal_in_instance = GrantPrincipalIn.from_json(json)
# print the JSON string representation of the object
print(GrantPrincipalIn.to_json())

# convert the object into a dict
grant_principal_in_dict = grant_principal_in_instance.to_dict()
# create an instance of GrantPrincipalIn from a dict
grant_principal_in_from_dict = GrantPrincipalIn.from_dict(grant_principal_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
