# ShareOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**drive_id** | **str** |  | 
**resource_type** | **str** |  | 
**resource_id** | **str** |  | 
**created_by** | **str** |  | 
**revision** | **str** |  | 
**state** | **str** |  | 
**expires_at** | **datetime** |  | 
**revoked_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**rotated_at** | **datetime** |  | 

## Example

```python
from agentdrive_sdk.models.share_out import ShareOut

# TODO update the JSON string below
json = "{}"
# create an instance of ShareOut from a JSON string
share_out_instance = ShareOut.from_json(json)
# print the JSON string representation of the object
print(ShareOut.to_json())

# convert the object into a dict
share_out_dict = share_out_instance.to_dict()
# create an instance of ShareOut from a dict
share_out_from_dict = ShareOut.from_dict(share_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


