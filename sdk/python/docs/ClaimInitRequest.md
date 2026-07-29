# ClaimInitRequest

`POST /agent/identity/claim` body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_token** | **str** | The per-identity claim_token returned by POST /agent/identity. |
**email** | **str** | Optional hint to display on the /claim page so the human knows which account the agent expected. Not enforced (design §14 question #3). | [optional]

## Example

```python
from agentdrive_sdk.models.claim_init_request import ClaimInitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimInitRequest from a JSON string
claim_init_request_instance = ClaimInitRequest.from_json(json)
# print the JSON string representation of the object
print(ClaimInitRequest.to_json())

# convert the object into a dict
claim_init_request_dict = claim_init_request_instance.to_dict()
# create an instance of ClaimInitRequest from a dict
claim_init_request_from_dict = ClaimInitRequest.from_dict(claim_init_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
