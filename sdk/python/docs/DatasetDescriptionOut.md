# DatasetDescriptionOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[QueryColumnOut]**](QueryColumnOut.md) |  |
**dataset** | **str** |  |

## Example

```python
from agentdrive_sdk.models.dataset_description_out import DatasetDescriptionOut

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetDescriptionOut from a JSON string
dataset_description_out_instance = DatasetDescriptionOut.from_json(json)
# print the JSON string representation of the object
print(DatasetDescriptionOut.to_json())

# convert the object into a dict
dataset_description_out_dict = dataset_description_out_instance.to_dict()
# create an instance of DatasetDescriptionOut from a dict
dataset_description_out_from_dict = DatasetDescriptionOut.from_dict(dataset_description_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
