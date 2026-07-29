# ShareMintOut

The create/rotate response — the ONLY place the `share_key` and its redemption `url` are exposed.

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
**share_key** | **str** |  |
**url** | **str** |  |

## Example

```python
from agentdrive_sdk.models.share_mint_out import ShareMintOut

# TODO update the JSON string below
json = "{}"
# create an instance of ShareMintOut from a JSON string
share_mint_out_instance = ShareMintOut.from_json(json)
# print the JSON string representation of the object
print(ShareMintOut.to_json())

# convert the object into a dict
share_mint_out_dict = share_mint_out_instance.to_dict()
# create an instance of ShareMintOut from a dict
share_mint_out_from_dict = ShareMintOut.from_dict(share_mint_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
