# CompileDiagnosticOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional]
**file** | **str** |  | [optional]
**line** | **int** |  | [optional]
**message** | **str** |  |
**severity** | **str** |  |
**suggestion** | **str** |  | [optional]

## Example

```python
from agentdrive_sdk.models.compile_diagnostic_out import CompileDiagnosticOut

# TODO update the JSON string below
json = "{}"
# create an instance of CompileDiagnosticOut from a JSON string
compile_diagnostic_out_instance = CompileDiagnosticOut.from_json(json)
# print the JSON string representation of the object
print(CompileDiagnosticOut.to_json())

# convert the object into a dict
compile_diagnostic_out_dict = compile_diagnostic_out_instance.to_dict()
# create an instance of CompileDiagnosticOut from a dict
compile_diagnostic_out_from_dict = CompileDiagnosticOut.from_dict(compile_diagnostic_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
