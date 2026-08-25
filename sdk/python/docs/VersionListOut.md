# VersionListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[VersionOut]**](VersionOut.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from agentdrive_sdk.models.version_list_out import VersionListOut

# TODO update the JSON string below
json = "{}"
# create an instance of VersionListOut from a JSON string
version_list_out_instance = VersionListOut.from_json(json)
# print the JSON string representation of the object
print(VersionListOut.to_json())

# convert the object into a dict
version_list_out_dict = version_list_out_instance.to_dict()
# create an instance of VersionListOut from a dict
version_list_out_from_dict = VersionListOut.from_dict(version_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


