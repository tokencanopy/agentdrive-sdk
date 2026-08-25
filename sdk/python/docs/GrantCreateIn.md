# GrantCreateIn

POST /v0/drives/{id}/grants body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_type** | **str** |  | 
**principal_id** | **str** | Required for &#x60;agent&#x60;, &#x60;user&#x60;, and &#x60;workspace&#x60;; omitted only for &#x60;public&#x60;. For &#x60;agent&#x60; and &#x60;user&#x60; it is checked against that type&#39;s id prefix (&#x60;tcagt_&#x60; / &#x60;tcusr_&#x60;) and a mismatch is &#x60;422 VALIDATION_ERROR&#x60;. The prefix is all AgentDrive asserts: these ids are minted by Hub, so their full shape is not AgentDrive&#39;s to enforce, and a well-formed id naming a principal that does not exist — or belongs to another workspace — is accepted here and simply never matches a token. The rule is conditional on &#x60;principal_type&#x60;, so it is enforced at the boundary rather than expressible as one JSON Schema &#x60;pattern&#x60;. | [optional] 
**resource_type** | **str** |  | 
**resource_id** | **str** |  | 
**role** | **str** |  | 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from agentdrive_sdk.models.grant_create_in import GrantCreateIn

# TODO update the JSON string below
json = "{}"
# create an instance of GrantCreateIn from a JSON string
grant_create_in_instance = GrantCreateIn.from_json(json)
# print the JSON string representation of the object
print(GrantCreateIn.to_json())

# convert the object into a dict
grant_create_in_dict = grant_create_in_instance.to_dict()
# create an instance of GrantCreateIn from a dict
grant_create_in_from_dict = GrantCreateIn.from_dict(grant_create_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


