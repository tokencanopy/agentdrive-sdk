# UploadInitiationOut

The V4-signed XML resumable initiation target (§5.6 as amended 2026-08-20). Secret material: the URL plus the exact signed header values. The client POSTs it with EXACTLY ``required_headers`` and an empty body; the 201 response's ``Location`` header is the resumable session URI. CLOSED schema on purpose — a generated client must not learn a broader security-sensitive target contract than the wire carries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**method** | **str** |  | 
**required_headers** | **Dict[str, str]** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from agentdrive_sdk.models.upload_initiation_out import UploadInitiationOut

# TODO update the JSON string below
json = "{}"
# create an instance of UploadInitiationOut from a JSON string
upload_initiation_out_instance = UploadInitiationOut.from_json(json)
# print the JSON string representation of the object
print(UploadInitiationOut.to_json())

# convert the object into a dict
upload_initiation_out_dict = upload_initiation_out_instance.to_dict()
# create an instance of UploadInitiationOut from a dict
upload_initiation_out_from_dict = UploadInitiationOut.from_dict(upload_initiation_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


