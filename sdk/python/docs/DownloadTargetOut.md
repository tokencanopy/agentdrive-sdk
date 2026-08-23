# DownloadTargetOut

The one signed, generation-pinned direct GET target (B3 §5.7). Secret material: present only in the fresh mint response, never in any stored record, replay, or log. CLOSED schema on purpose: Packet 5 and generated clients must not learn a broader security-sensitive target contract than the wire actually carries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_disposition** | **str** |  |
**method** | **str** |  |
**required_headers** | **object** |  |
**url** | **str** |  |

## Example

```python
from agentdrive_sdk.models.download_target_out import DownloadTargetOut

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadTargetOut from a JSON string
download_target_out_instance = DownloadTargetOut.from_json(json)
# print the JSON string representation of the object
print(DownloadTargetOut.to_json())

# convert the object into a dict
download_target_out_dict = download_target_out_instance.to_dict()
# create an instance of DownloadTargetOut from a dict
download_target_out_from_dict = DownloadTargetOut.from_dict(download_target_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
