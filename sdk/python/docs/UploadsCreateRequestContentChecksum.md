# UploadsCreateRequestContentChecksum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** |  | 
**value** | **str** | Canonical padded standard-base64 CRC32C of exactly four bytes (GCS metadata form). | 

## Example

```python
from agentdrive_sdk.models.uploads_create_request_content_checksum import UploadsCreateRequestContentChecksum

# TODO update the JSON string below
json = "{}"
# create an instance of UploadsCreateRequestContentChecksum from a JSON string
uploads_create_request_content_checksum_instance = UploadsCreateRequestContentChecksum.from_json(json)
# print the JSON string representation of the object
print(UploadsCreateRequestContentChecksum.to_json())

# convert the object into a dict
uploads_create_request_content_checksum_dict = uploads_create_request_content_checksum_instance.to_dict()
# create an instance of UploadsCreateRequestContentChecksum from a dict
uploads_create_request_content_checksum_from_dict = UploadsCreateRequestContentChecksum.from_dict(uploads_create_request_content_checksum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


