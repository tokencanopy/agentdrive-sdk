# GrantPatchIn

PATCH /v0/grants/{grn_id} body. Field absence = unchanged; explicit `expires_in: null` clears the expiry (makes the grant permanent).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_in** | **int** |  | [optional]
**role** | **str** |  | [optional]

## Example

```python
from agentdrive_sdk.models.grant_patch_in import GrantPatchIn

# TODO update the JSON string below
json = "{}"
# create an instance of GrantPatchIn from a JSON string
grant_patch_in_instance = GrantPatchIn.from_json(json)
# print the JSON string representation of the object
print(GrantPatchIn.to_json())

# convert the object into a dict
grant_patch_in_dict = grant_patch_in_instance.to_dict()
# create an instance of GrantPatchIn from a dict
grant_patch_in_from_dict = GrantPatchIn.from_dict(grant_patch_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
