# ShareCreateIn

POST /v0/drives/{id}/shares body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  | [optional]
**resource_id** | **str** |  |
**resource_type** | **str** |  |

## Example

```python
from agentdrive_sdk.models.share_create_in import ShareCreateIn

# TODO update the JSON string below
json = "{}"
# create an instance of ShareCreateIn from a JSON string
share_create_in_instance = ShareCreateIn.from_json(json)
# print the JSON string representation of the object
print(ShareCreateIn.to_json())

# convert the object into a dict
share_create_in_dict = share_create_in_instance.to_dict()
# create an instance of ShareCreateIn from a dict
share_create_in_from_dict = ShareCreateIn.from_dict(share_create_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
