# ShareRedeemOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  |
**role** | **str** |  |
**token** | **str** |  |
**url** | **str** |  |

## Example

```python
from agentdrive_sdk.models.share_redeem_out import ShareRedeemOut

# TODO update the JSON string below
json = "{}"
# create an instance of ShareRedeemOut from a JSON string
share_redeem_out_instance = ShareRedeemOut.from_json(json)
# print the JSON string representation of the object
print(ShareRedeemOut.to_json())

# convert the object into a dict
share_redeem_out_dict = share_redeem_out_instance.to_dict()
# create an instance of ShareRedeemOut from a dict
share_redeem_out_from_dict = ShareRedeemOut.from_dict(share_redeem_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
