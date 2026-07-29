# UploadBeginIn

Body of `POST /v0/uploads` — the large-upload begin call (large-upload- design.md §5.1). All artifact decisions are frozen here; the subsequent GCS PUT carries only bytes, and `commit` carries only the `upload_id`.  `labels`/`metadata`/`source` omitted (null) ⇒ preserve the existing artifact's value at commit; present (incl. empty) ⇒ replace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_name** | **str** |  | [optional]
**change_summary** | **str** |  | [optional]
**content_type** | **str** |  | [optional] [default to 'application/octet-stream']
**cors_origin** | **str** | Web origin (scheme://host[:port]) of the browser that will PUT the bytes, e.g. &#x60;https://app.example.com&#x60;. Set this when the &#x60;upload_url&#x60; is handed to browser code: GCS binds CORS at session initiate, so the returned session only echoes &#x60;Access-Control-Allow-Origin&#x60; (and is thus PUT-able from a browser) when opened with the caller&#39;s origin. A trusted backend relaying a browser upload forwards the browser&#39;s &#x60;Origin&#x60; here. Omit for server/desktop uploads (no CORS enforcement). | [optional]
**crc32c** | **str** |  | [optional]
**if_match** | **int** |  | [optional]
**if_none_match** | **bool** |  | [optional] [default to False]
**labels** | **List[str]** |  | [optional]
**metadata** | **Dict[str, object]** |  | [optional]
**path** | **str** |  |
**size_bytes** | **int** |  |
**source** | [**ArtifactSource**](ArtifactSource.md) |  | [optional]

## Example

```python
from agentdrive_sdk.models.upload_begin_in import UploadBeginIn

# TODO update the JSON string below
json = "{}"
# create an instance of UploadBeginIn from a JSON string
upload_begin_in_instance = UploadBeginIn.from_json(json)
# print the JSON string representation of the object
print(UploadBeginIn.to_json())

# convert the object into a dict
upload_begin_in_dict = upload_begin_in_instance.to_dict()
# create an instance of UploadBeginIn from a dict
upload_begin_in_from_dict = UploadBeginIn.from_dict(upload_begin_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
