# ClaimInitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_attempt_token** | **str** | Per-attempt opaque token; the agent does not need to present it. |
**expires_at** | **datetime** |  |
**user_code** | **str** | Human-readable code the user types/sees on /claim. |
**verification_uri** | **str** | URL to direct the human to. |
**verification_uri_complete** | **str** | Convenience: same as &#x60;verification_uri&#x60; but with the user_code pre-baked so the human doesn&#39;t have to type it. RFC 8628 idiom. |

## Example

```python
from agentdrive_sdk.models.claim_init_response import ClaimInitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimInitResponse from a JSON string
claim_init_response_instance = ClaimInitResponse.from_json(json)
# print the JSON string representation of the object
print(ClaimInitResponse.to_json())

# convert the object into a dict
claim_init_response_dict = claim_init_response_instance.to_dict()
# create an instance of ClaimInitResponse from a dict
claim_init_response_from_dict = ClaimInitResponse.from_dict(claim_init_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
