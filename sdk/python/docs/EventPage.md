# EventPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EventOut]**](EventOut.md) |  |
**next_cursor** | **str** |  | [optional]

## Example

```python
from agentdrive_sdk.models.event_page import EventPage

# TODO update the JSON string below
json = "{}"
# create an instance of EventPage from a JSON string
event_page_instance = EventPage.from_json(json)
# print the JSON string representation of the object
print(EventPage.to_json())

# convert the object into a dict
event_page_dict = event_page_instance.to_dict()
# create an instance of EventPage from a dict
event_page_from_dict = EventPage.from_dict(event_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
