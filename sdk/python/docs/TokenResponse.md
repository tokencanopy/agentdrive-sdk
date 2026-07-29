# TokenResponse

`POST /oauth2/token` success response. Mirrors RFC 6749 with an optional `identity_assertion` field for the claim grant path (where a fresh post-claim assertion supersedes the pre-claim one).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  |
**expires_in** | **int** | Seconds until access_token expiry. |
**identity_assertion** | **str** |  | [optional]
**scope** | **str** |  |
**token_type** | **str** |  | [optional] [default to 'Bearer']

## Example

```python
from agentdrive_sdk.models.token_response import TokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponse from a JSON string
token_response_instance = TokenResponse.from_json(json)
# print the JSON string representation of the object
print(TokenResponse.to_json())

# convert the object into a dict
token_response_dict = token_response_instance.to_dict()
# create an instance of TokenResponse from a dict
token_response_from_dict = TokenResponse.from_dict(token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
