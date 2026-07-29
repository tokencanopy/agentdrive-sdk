# LookupValuesIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** |  |
**dataset** | **str** |  |
**limit** | **int** |  | [optional] [default to 50]

## Example

```python
from agentdrive_sdk.models.lookup_values_in import LookupValuesIn

# TODO update the JSON string below
json = "{}"
# create an instance of LookupValuesIn from a JSON string
lookup_values_in_instance = LookupValuesIn.from_json(json)
# print the JSON string representation of the object
print(LookupValuesIn.to_json())

# convert the object into a dict
lookup_values_in_dict = lookup_values_in_instance.to_dict()
# create an instance of LookupValuesIn from a dict
lookup_values_in_from_dict = LookupValuesIn.from_dict(lookup_values_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
