# ShareOut

A live share link as seen on list/management — NEVER carries the `share_key` (that is the credential, returned only at mint/rotate).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_count** | **int** |  | [optional] [default to 0]
**audience** | **str** |  |
**created_at** | **datetime** |  |
**expires_at** | **datetime** |  | [optional]
**has_password** | **bool** |  |
**id** | **str** |  |
**last_accessed_at** | **datetime** |  | [optional]
**resource_id** | **str** |  |
**resource_type** | **str** |  |
**role** | **str** |  |

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
