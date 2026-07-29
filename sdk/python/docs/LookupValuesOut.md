# LookupValuesOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** |  |
**dataset** | **str** |  |
**values** | **List[object]** |  |

## Example

```python
from agentdrive_sdk.models.lookup_values_out import LookupValuesOut

# TODO update the JSON string below
json = "{}"
# create an instance of LookupValuesOut from a JSON string
lookup_values_out_instance = LookupValuesOut.from_json(json)
# print the JSON string representation of the object
print(LookupValuesOut.to_json())

# convert the object into a dict
lookup_values_out_dict = lookup_values_out_instance.to_dict()
# create an instance of LookupValuesOut from a dict
lookup_values_out_from_dict = LookupValuesOut.from_dict(lookup_values_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
