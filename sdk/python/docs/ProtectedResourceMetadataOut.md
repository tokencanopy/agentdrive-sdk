# ProtectedResourceMetadataOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_servers** | **List[str]** |  |
**bearer_methods_supported** | **List[str]** |  |
**resource** | **str** |  |
**scopes_supported** | **List[str]** |  |

## Example

```python
from agentdrive_sdk.models.protected_resource_metadata_out import ProtectedResourceMetadataOut

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedResourceMetadataOut from a JSON string
protected_resource_metadata_out_instance = ProtectedResourceMetadataOut.from_json(json)
# print the JSON string representation of the object
print(ProtectedResourceMetadataOut.to_json())

# convert the object into a dict
protected_resource_metadata_out_dict = protected_resource_metadata_out_instance.to_dict()
# create an instance of ProtectedResourceMetadataOut from a dict
protected_resource_metadata_out_from_dict = ProtectedResourceMetadataOut.from_dict(protected_resource_metadata_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
