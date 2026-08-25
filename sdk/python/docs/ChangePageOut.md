# ChangePageOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ChangeOut]**](ChangeOut.md) |  | 
**next_cursor** | **str** |  | 
**has_more** | **bool** |  | 

## Example

```python
from agentdrive_sdk.models.change_page_out import ChangePageOut

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePageOut from a JSON string
change_page_out_instance = ChangePageOut.from_json(json)
# print the JSON string representation of the object
print(ChangePageOut.to_json())

# convert the object into a dict
change_page_out_dict = change_page_out_instance.to_dict()
# create an instance of ChangePageOut from a dict
change_page_out_from_dict = ChangePageOut.from_dict(change_page_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


