# ShareCreateIn

POST /v0/shares body. `resource` is an `art_*`/`fld_*` id or a path. `expires_in` is seconds from now (omit for the default: none for a human creator, a short TTL for an agent). `password` (optional) gates redemption.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_in** | **int** |  | [optional]
**password** | **str** |  | [optional]
**resource** | **str** |  |
**role** | **str** |  | [optional] [default to 'viewer']

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
