# DownloadUrlOut

A URL the caller can GET to fetch the artifact's bytes.  `direct=True` ⇒ a short-lived signed GCS URL on `storage.googleapis.com` (client downloads straight from GCS; `expires_at` is set). `direct=False` ⇒ the proxy `/download` endpoint on the API host (no expiry) — returned for sub-threshold artifacts or when signing is unavailable. The URL is opaque: callers should not parse it. See large-download-design.md §5.1.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  |
**direct** | **bool** |  |
**download_url** | **str** |  |
**expires_at** | **datetime** |  | [optional]
**filename** | **str** |  |
**size_bytes** | **int** |  |

## Example

```python
from agentdrive_sdk.models.download_url_out import DownloadUrlOut

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadUrlOut from a JSON string
download_url_out_instance = DownloadUrlOut.from_json(json)
# print the JSON string representation of the object
print(DownloadUrlOut.to_json())

# convert the object into a dict
download_url_out_dict = download_url_out_instance.to_dict()
# create an instance of DownloadUrlOut from a dict
download_url_out_from_dict = DownloadUrlOut.from_dict(download_url_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
