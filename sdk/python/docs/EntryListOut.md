# EntryListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[EntriesInner]**](EntriesInner.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.entry_list_out import EntryListOut

# TODO update the JSON string below
json = "{}"
# create an instance of EntryListOut from a JSON string
entry_list_out_instance = EntryListOut.from_json(json)
# print the JSON string representation of the object
print(EntryListOut.to_json())

# convert the object into a dict
entry_list_out_dict = entry_list_out_instance.to_dict()
# create an instance of EntryListOut from a dict
entry_list_out_from_dict = EntryListOut.from_dict(entry_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


