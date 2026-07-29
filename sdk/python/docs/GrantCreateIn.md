# GrantCreateIn

POST /v0/grants body. `resource` is an `art_*`/`fld_*` id or a path (resolved within the caller's drive). `expires_in` is seconds from now (omit for a permanent grant).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_in** | **int** |  | [optional]
**principal** | [**GrantPrincipalIn**](GrantPrincipalIn.md) |  |
**resource** | **str** |  |
**role** | **str** |  |

## Example

```python
from agentdrive_sdk.models.grant_create_in import GrantCreateIn

# TODO update the JSON string below
json = "{}"
# create an instance of GrantCreateIn from a JSON string
grant_create_in_instance = GrantCreateIn.from_json(json)
# print the JSON string representation of the object
print(GrantCreateIn.to_json())

# convert the object into a dict
grant_create_in_dict = grant_create_in_instance.to_dict()
# create an instance of GrantCreateIn from a dict
grant_create_in_from_dict = GrantCreateIn.from_dict(grant_create_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
