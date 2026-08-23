# LookupOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  |
**parent_id** | **str** |  |
**revision** | **str** |  |
**type** | **str** |  |

## Example

```python
from agentdrive_sdk.models.lookup_out import LookupOut

# TODO update the JSON string below
json = "{}"
# create an instance of LookupOut from a JSON string
lookup_out_instance = LookupOut.from_json(json)
# print the JSON string representation of the object
print(LookupOut.to_json())

# convert the object into a dict
lookup_out_dict = lookup_out_instance.to_dict()
# create an instance of LookupOut from a dict
lookup_out_from_dict = LookupOut.from_dict(lookup_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
