# CompileProjectOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_compile** | **bool** |  |
**engine** | **str** |  |
**entrypoint** | **str** |  |
**fld_id** | **str** |  |

## Example

```python
from agentdrive_sdk.models.compile_project_out import CompileProjectOut

# TODO update the JSON string below
json = "{}"
# create an instance of CompileProjectOut from a JSON string
compile_project_out_instance = CompileProjectOut.from_json(json)
# print the JSON string representation of the object
print(CompileProjectOut.to_json())

# convert the object into a dict
compile_project_out_dict = compile_project_out_instance.to_dict()
# create an instance of CompileProjectOut from a dict
compile_project_out_from_dict = CompileProjectOut.from_dict(compile_project_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
