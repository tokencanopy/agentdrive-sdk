# GrantOut

A live grant. Audit fields (`granted_by_*`, `on_behalf_of`) are surfaced so a manager can see who shared what.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts_affected** | **int** |  | [optional]
**created_at** | **datetime** |  |
**expires_at** | **datetime** |  | [optional]
**granted_by_id** | **str** |  |
**granted_by_type** | **str** |  |
**id** | **str** |  |
**on_behalf_of** | **str** |  | [optional]
**principal_email** | **str** |  | [optional]
**principal_id** | **str** |  | [optional]
**principal_type** | **str** |  |
**resource_id** | **str** |  |
**resource_type** | **str** |  |
**role** | **str** |  |

## Example

```python
from agentdrive_sdk.models.grant_out import GrantOut

# TODO update the JSON string below
json = "{}"
# create an instance of GrantOut from a JSON string
grant_out_instance = GrantOut.from_json(json)
# print the JSON string representation of the object
print(GrantOut.to_json())

# convert the object into a dict
grant_out_dict = grant_out_instance.to_dict()
# create an instance of GrantOut from a dict
grant_out_from_dict = GrantOut.from_dict(grant_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
