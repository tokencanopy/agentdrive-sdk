# IdentityAssertionMetadataOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  |
**iss** | **str** |  |
**version** | **int** |  |

## Example

```python
from agentdrive_sdk.models.identity_assertion_metadata_out import IdentityAssertionMetadataOut

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAssertionMetadataOut from a JSON string
identity_assertion_metadata_out_instance = IdentityAssertionMetadataOut.from_json(json)
# print the JSON string representation of the object
print(IdentityAssertionMetadataOut.to_json())

# convert the object into a dict
identity_assertion_metadata_out_dict = identity_assertion_metadata_out_instance.to_dict()
# create an instance of IdentityAssertionMetadataOut from a dict
identity_assertion_metadata_out_from_dict = IdentityAssertionMetadataOut.from_dict(identity_assertion_metadata_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
