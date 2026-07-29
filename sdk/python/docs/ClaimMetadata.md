# ClaimMetadata

Hints the agent's UI/CLI can use when initiating the claim ceremony. Decoupled from the `claim_token` itself so future additions don't change the token's shape.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_endpoint** | **str** |  |
**supported_email_hints** | **bool** |  | [optional] [default to True]

## Example

```python
from agentdrive_sdk.models.claim_metadata import ClaimMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimMetadata from a JSON string
claim_metadata_instance = ClaimMetadata.from_json(json)
# print the JSON string representation of the object
print(ClaimMetadata.to_json())

# convert the object into a dict
claim_metadata_dict = claim_metadata_instance.to_dict()
# create an instance of ClaimMetadata from a dict
claim_metadata_from_dict = ClaimMetadata.from_dict(claim_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
