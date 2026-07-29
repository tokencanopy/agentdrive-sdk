# CompileOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **str** |  | [optional]
**entrypoint** | **str** |  | [optional]
**wait** | **bool** |  | [optional] [default to False]

## Example

```python
from agentdrive_sdk.models.compile_options import CompileOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CompileOptions from a JSON string
compile_options_instance = CompileOptions.from_json(json)
# print the JSON string representation of the object
print(CompileOptions.to_json())

# convert the object into a dict
compile_options_dict = compile_options_instance.to_dict()
# create an instance of CompileOptions from a dict
compile_options_from_dict = CompileOptions.from_dict(compile_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
