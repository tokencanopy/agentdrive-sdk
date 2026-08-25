# GrantOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**drive_id** | **str** |  | 
**resource_type** | **str** |  | 
**resource_id** | **str** |  | 
**principal_type** | **str** |  | 
**principal_id** | **str** |  | 
**role** | **str** |  | 
**revision** | **str** |  | 
**state** | **str** |  | 
**expires_at** | **datetime** |  | 
**revoked_at** | **datetime** |  | 
**created_at** | **datetime** |  | 

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


