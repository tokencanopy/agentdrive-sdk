# ShareListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ShareOut]**](ShareOut.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.share_list_out import ShareListOut

# TODO update the JSON string below
json = "{}"
# create an instance of ShareListOut from a JSON string
share_list_out_instance = ShareListOut.from_json(json)
# print the JSON string representation of the object
print(ShareListOut.to_json())

# convert the object into a dict
share_list_out_dict = share_list_out_instance.to_dict()
# create an instance of ShareListOut from a dict
share_list_out_from_dict = ShareListOut.from_dict(share_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


