# ShareErrorOut

Negotiated JSON error shape for the public share protocol.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorBody**](ErrorBody.md) |  |

## Example

```python
from agentdrive_sdk.models.share_error_out import ShareErrorOut

# TODO update the JSON string below
json = "{}"
# create an instance of ShareErrorOut from a JSON string
share_error_out_instance = ShareErrorOut.from_json(json)
# print the JSON string representation of the object
print(ShareErrorOut.to_json())

# convert the object into a dict
share_error_out_dict = share_error_out_instance.to_dict()
# create an instance of ShareErrorOut from a dict
share_error_out_from_dict = ShareErrorOut.from_dict(share_error_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
