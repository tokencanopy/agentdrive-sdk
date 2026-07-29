# AgentAuthMetadataOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_endpoint** | **str** |  |
**events_endpoint** | **str** |  |
**identity_assertion** | [**IdentityAssertionMetadataOut**](IdentityAssertionMetadataOut.md) |  |
**identity_endpoint** | **str** |  |
**identity_types_supported** | **List[str]** |  |
**skill** | **str** |  |
**spec_version** | **str** |  |

## Example

```python
from agentdrive_sdk.models.agent_auth_metadata_out import AgentAuthMetadataOut

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAuthMetadataOut from a JSON string
agent_auth_metadata_out_instance = AgentAuthMetadataOut.from_json(json)
# print the JSON string representation of the object
print(AgentAuthMetadataOut.to_json())

# convert the object into a dict
agent_auth_metadata_out_dict = agent_auth_metadata_out_instance.to_dict()
# create an instance of AgentAuthMetadataOut from a dict
agent_auth_metadata_out_from_dict = AgentAuthMetadataOut.from_dict(agent_auth_metadata_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
