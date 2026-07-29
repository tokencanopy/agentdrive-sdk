# CompileJobListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CompileJobOut]**](CompileJobOut.md) |  |
**jobs** | [**List[CompileJobOut]**](CompileJobOut.md) | Deprecated same-value alias for &#x60;items&#x60;; retained for compatibility. |
**next_cursor** | **str** | Opaque continuation token, or null when the listing is complete. | [optional]

## Example

```python
from agentdrive_sdk.models.compile_job_list_out import CompileJobListOut

# TODO update the JSON string below
json = "{}"
# create an instance of CompileJobListOut from a JSON string
compile_job_list_out_instance = CompileJobListOut.from_json(json)
# print the JSON string representation of the object
print(CompileJobListOut.to_json())

# convert the object into a dict
compile_job_list_out_dict = compile_job_list_out_instance.to_dict()
# create an instance of CompileJobListOut from a dict
compile_job_list_out_from_dict = CompileJobListOut.from_dict(compile_job_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
