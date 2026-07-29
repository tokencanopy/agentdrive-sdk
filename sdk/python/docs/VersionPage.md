# VersionPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[VersionOut]**](VersionOut.md) |  |
**next_cursor** | **str** |  | [optional]
**pruned_before** | **int** |  | [optional]

## Example

```python
from agentdrive_sdk.models.version_page import VersionPage

# TODO update the JSON string below
json = "{}"
# create an instance of VersionPage from a JSON string
version_page_instance = VersionPage.from_json(json)
# print the JSON string representation of the object
print(VersionPage.to_json())

# convert the object into a dict
version_page_dict = version_page_instance.to_dict()
# create an instance of VersionPage from a dict
version_page_from_dict = VersionPage.from_dict(version_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
