# UploadChecksumOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** |  |
**value** | **str** |  |

## Example

```python
from agentdrive_sdk.models.upload_checksum_out import UploadChecksumOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadChecksumOut from a JSON string
upload_checksum_out_instance = UploadChecksumOut.from_json(json)
# print the JSON string representation of the object
print(UploadChecksumOut.to_json())

# convert the object into a dict
upload_checksum_out_dict = upload_checksum_out_instance.to_dict()
# create an instance of UploadChecksumOut from a dict
upload_checksum_out_from_dict = UploadChecksumOut.from_dict(upload_checksum_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
