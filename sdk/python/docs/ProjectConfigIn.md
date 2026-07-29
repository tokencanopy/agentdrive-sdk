# ProjectConfigIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_compile** | **bool** |  | [optional] [default to False]
**engine** | **str** |  | [optional]
**entrypoint** | **str** |  |

## Example

```python
from agentdrive_sdk.models.project_config_in import ProjectConfigIn

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectConfigIn from a JSON string
project_config_in_instance = ProjectConfigIn.from_json(json)
# print the JSON string representation of the object
print(ProjectConfigIn.to_json())

# convert the object into a dict
project_config_in_dict = project_config_in_instance.to_dict()
# create an instance of ProjectConfigIn from a dict
project_config_in_from_dict = ProjectConfigIn.from_dict(project_config_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
