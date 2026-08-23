# UploadChunksOut

How to stream chunks against the session URI the initiation's ``Location`` disclosed: the unchanged ``gcs-xml-resumable`` protocol (PUT + ``Content-Range``, 308/``Range`` resume).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  |
**required_headers** | **Dict[str, str]** |  |

## Example

```python
from agentdrive_sdk.models.upload_chunks_out import UploadChunksOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadChunksOut from a JSON string
upload_chunks_out_instance = UploadChunksOut.from_json(json)
# print the JSON string representation of the object
print(UploadChunksOut.to_json())

# convert the object into a dict
upload_chunks_out_dict = upload_chunks_out_instance.to_dict()
# create an instance of UploadChunksOut from a dict
upload_chunks_out_from_dict = UploadChunksOut.from_dict(upload_chunks_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
