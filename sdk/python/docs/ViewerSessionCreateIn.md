# ViewerSessionCreateIn

POST /v0/drives/{id}/artifacts/{id}/viewer-sessions body.  ``version_id`` omitted (or null) pins the artifact's CURRENT head at mint time; the session never follows the head afterwards.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **str** |  | [optional] 

## Example

```python
from agentdrive_sdk.models.viewer_session_create_in import ViewerSessionCreateIn

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerSessionCreateIn from a JSON string
viewer_session_create_in_instance = ViewerSessionCreateIn.from_json(json)
# print the JSON string representation of the object
print(ViewerSessionCreateIn.to_json())

# convert the object into a dict
viewer_session_create_in_dict = viewer_session_create_in_instance.to_dict()
# create an instance of ViewerSessionCreateIn from a dict
viewer_session_create_in_from_dict = ViewerSessionCreateIn.from_dict(viewer_session_create_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


