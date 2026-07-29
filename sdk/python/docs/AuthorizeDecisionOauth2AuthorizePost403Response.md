# AuthorizeDecisionOauth2AuthorizePost403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  |
**error_description** | **str** |  | [optional]
**detail** | [**ErrorDetail**](ErrorDetail.md) |  |

## Example

```python
from agentdrive_sdk.models.authorize_decision_oauth2_authorize_post403_response import AuthorizeDecisionOauth2AuthorizePost403Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeDecisionOauth2AuthorizePost403Response from a JSON string
authorize_decision_oauth2_authorize_post403_response_instance = AuthorizeDecisionOauth2AuthorizePost403Response.from_json(json)
# print the JSON string representation of the object
print(AuthorizeDecisionOauth2AuthorizePost403Response.to_json())

# convert the object into a dict
authorize_decision_oauth2_authorize_post403_response_dict = authorize_decision_oauth2_authorize_post403_response_instance.to_dict()
# create an instance of AuthorizeDecisionOauth2AuthorizePost403Response from a dict
authorize_decision_oauth2_authorize_post403_response_from_dict = AuthorizeDecisionOauth2AuthorizePost403Response.from_dict(authorize_decision_oauth2_authorize_post403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
