# CompileJobOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_hit** | **bool** |  |
**diagnostics** | [**List[CompileDiagnosticOut]**](CompileDiagnosticOut.md) |  | [optional]
**duration_ms** | **int** |  | [optional]
**engine** | **str** |  |
**job_id** | **str** |  |
**logs_url** | **str** |  | [optional]
**output** | **Dict[str, object]** |  | [optional]
**status** | **str** |  |
**task** | **str** |  |

## Example

```python
from agentdrive_sdk.models.compile_job_out import CompileJobOut

# TODO update the JSON string below
json = "{}"
# create an instance of CompileJobOut from a JSON string
compile_job_out_instance = CompileJobOut.from_json(json)
# print the JSON string representation of the object
print(CompileJobOut.to_json())

# convert the object into a dict
compile_job_out_dict = compile_job_out_instance.to_dict()
# create an instance of CompileJobOut from a dict
compile_job_out_from_dict = CompileJobOut.from_dict(compile_job_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
