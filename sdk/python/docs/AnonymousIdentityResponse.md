# AnonymousIdentityResponse

`POST /agent/identity` response on the anonymous path.  The agent stores `identity_assertion` as its long-lived credential and uses `claim_token` to initiate the claim ceremony when the human is ready.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_identity_id** | **str** |  |
**claim_metadata** | [**ClaimMetadata**](ClaimMetadata.md) |  |
**claim_token** | **str** | Opaque server-issued secret. Present at POST /agent/identity/claim and at POST /oauth2/token (grant_type&#x3D;claim). |
**drive_id** | **str** |  |
**expires_at** | **datetime** |  |
**identity_assertion** | **str** | JWT signed by AgentDrive, scope&#x3D;pre_claim. 30-day TTL. |

## Example

```python
from agentdrive_sdk.models.anonymous_identity_response import AnonymousIdentityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnonymousIdentityResponse from a JSON string
anonymous_identity_response_instance = AnonymousIdentityResponse.from_json(json)
# print the JSON string representation of the object
print(AnonymousIdentityResponse.to_json())

# convert the object into a dict
anonymous_identity_response_dict = anonymous_identity_response_instance.to_dict()
# create an instance of AnonymousIdentityResponse from a dict
anonymous_identity_response_from_dict = AnonymousIdentityResponse.from_dict(anonymous_identity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
