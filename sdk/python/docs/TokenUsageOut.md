# TokenUsageOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embed** | **int** |  |
**llm_cached** | **int** |  |
**llm_input** | **int** |  |
**llm_output** | **int** |  |

## Example

```python
from agentdrive_sdk.models.token_usage_out import TokenUsageOut

# TODO update the JSON string below
json = "{}"
# create an instance of TokenUsageOut from a JSON string
token_usage_out_instance = TokenUsageOut.from_json(json)
# print the JSON string representation of the object
print(TokenUsageOut.to_json())

# convert the object into a dict
token_usage_out_dict = token_usage_out_instance.to_dict()
# create an instance of TokenUsageOut from a dict
token_usage_out_from_dict = TokenUsageOut.from_dict(token_usage_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
