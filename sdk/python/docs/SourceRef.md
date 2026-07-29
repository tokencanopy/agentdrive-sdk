# SourceRef

One typed provenance ref. `type` is open-vocabulary (server validates only length, not the value), so callers can declare new types as their integrations evolve. `id` is the type-specific identifier — for `type='artifact'` this is an `art_…` ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  |
**metadata** | **Dict[str, object]** |  | [optional]
**type** | **str** |  |

## Example

```python
from agentdrive_sdk.models.source_ref import SourceRef

# TODO update the JSON string below
json = "{}"
# create an instance of SourceRef from a JSON string
source_ref_instance = SourceRef.from_json(json)
# print the JSON string representation of the object
print(SourceRef.to_json())

# convert the object into a dict
source_ref_dict = source_ref_instance.to_dict()
# create an instance of SourceRef from a dict
source_ref_from_dict = SourceRef.from_dict(source_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
