# CompileJobIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**CompileOptions**](CompileOptions.md) |  | [optional]
**task** | **str** |  | [optional] [default to 'latex.compile']

## Example

```python
from agentdrive_sdk.models.compile_job_in import CompileJobIn

# TODO update the JSON string below
json = "{}"
# create an instance of CompileJobIn from a JSON string
compile_job_in_instance = CompileJobIn.from_json(json)
# print the JSON string representation of the object
print(CompileJobIn.to_json())

# convert the object into a dict
compile_job_in_dict = compile_job_in_instance.to_dict()
# create an instance of CompileJobIn from a dict
compile_job_in_from_dict = CompileJobIn.from_dict(compile_job_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
