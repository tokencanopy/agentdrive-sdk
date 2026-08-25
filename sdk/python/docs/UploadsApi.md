# agentdrive_sdk.UploadsApi

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uploads_complete**](UploadsApi.md#uploads_complete) | **POST** /v0/drives/{drive_id}/uploads/{upload_id}/complete | Complete Upload
[**uploads_create**](UploadsApi.md#uploads_create) | **POST** /v0/drives/{drive_id}/uploads | Begin Upload
[**uploads_delete**](UploadsApi.md#uploads_delete) | **DELETE** /v0/drives/{drive_id}/uploads/{upload_id} | Cancel Upload
[**uploads_read**](UploadsApi.md#uploads_read) | **GET** /v0/drives/{drive_id}/uploads/{upload_id} | Read Upload


# **uploads_complete**
> UploadSessionOut uploads_complete(drive_id, upload_id, idempotency_key, authorization=authorization)

Complete Upload

Adopt the finalized scratch object and publish exactly one immutable
artifact/version (§5.5/§6). Empty body; If-Match is not accepted — the
version precondition was captured at begin, and the transition fence
plus idempotency serializes the session itself.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.upload_session_out import UploadSessionOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://drive.tokencanopy.com
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://drive.tokencanopy.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.UploadsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    upload_id = 'upload_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Complete Upload
        api_response = api_instance.uploads_complete(drive_id, upload_id, idempotency_key, authorization=authorization)
        print("The response of UploadsApi->uploads_complete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->uploads_complete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **upload_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**UploadSessionOut**](UploadSessionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  |
**200** | Idempotent replay of completion. |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | A sibling already occupies the name/path, or the idempotency key was reused for a different request. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | If-Match did not match (copy/restore preconditions). |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
**428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
**406** | Accept does not admit application/json (NOT_ACCEPTABLE) — every upload-control response is JSON. |  * X-Request-Id - Request correlation identifier. <br>  |
**503** | Direct transfer is not fully configured/enabled (TRANSFER_DISABLED, no Retry-After), or the provider is transiently unavailable (TRANSFER_UNAVAILABLE, with Retry-After). |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploads_create**
> UploadSessionOut uploads_create(drive_id, idempotency_key, uploads_create_request, if_match=if_match, authorization=authorization)

Begin Upload

Begin one direct-upload session; the 201 response carries the one
external GCS XML resumable target, disclosed exactly once.

Strict JSON body (charset utf-8): unknown/duplicate fields, unknown discriminators, non-canonical CRC32C, and malformed ids are 400 INVALID_REQUEST. An artifact target takes NO If-Match (400 if sent); a version target REQUIRES If-Match carrying the artifact head ETag (428 absent, 412 stale) — the revision is captured for completion-time enforcement.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.upload_session_out import UploadSessionOut
from agentdrive_sdk.models.uploads_create_request import UploadsCreateRequest
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://drive.tokencanopy.com
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://drive.tokencanopy.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.UploadsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    uploads_create_request = agentdrive_sdk.UploadsCreateRequest() # UploadsCreateRequest | 
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Begin Upload
        api_response = api_instance.uploads_create(drive_id, idempotency_key, uploads_create_request, if_match=if_match, authorization=authorization)
        print("The response of UploadsApi->uploads_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->uploads_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **uploads_create_request** | [**UploadsCreateRequest**](UploadsCreateRequest.md)|  | 
 **if_match** | **str**|  | [optional] 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**UploadSessionOut**](UploadSessionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  |
**200** | Idempotent replay without transfer target. |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | A sibling already occupies the name/path, or the idempotency key was reused for a different request. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | If-Match did not match (copy/restore preconditions). |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
**428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
**406** | Accept does not admit application/json (NOT_ACCEPTABLE) — every upload-control response is JSON. |  * X-Request-Id - Request correlation identifier. <br>  |
**503** | Direct transfer is not fully configured/enabled (TRANSFER_DISABLED, no Retry-After), or the provider is transiently unavailable (TRANSFER_UNAVAILABLE, with Retry-After). |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**413** | The declared size exceeds the enabled direct-transfer ceiling (PAYLOAD_TOO_LARGE), or the control body exceeds its bound. |  * X-Request-Id - Request correlation identifier. <br>  |
**415** | The begin body must be application/json (UNSUPPORTED_MEDIA_TYPE). |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploads_delete**
> UploadSessionOut uploads_delete(drive_id, upload_id, idempotency_key, if_match, authorization=authorization)

Cancel Upload

Close publication permanently and release the reservation exactly
once (§5.4); cleanup continues independently.

If-Match must carry THE session's current strong ETag: '*' and multi-member lists cannot pin a revision and are 400 INVALID_REQUEST; a weak or foreign tag is 412. The exact same-key idempotent replay is exempt from the If-Match requirement (it reauthorizes and returns the stored 200).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.upload_session_out import UploadSessionOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://drive.tokencanopy.com
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://drive.tokencanopy.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.UploadsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    upload_id = 'upload_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    if_match = 'if_match_example' # str | 
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Cancel Upload
        api_response = api_instance.uploads_delete(drive_id, upload_id, idempotency_key, if_match, authorization=authorization)
        print("The response of UploadsApi->uploads_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->uploads_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **upload_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **if_match** | **str**|  | 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**UploadSessionOut**](UploadSessionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The mutation conflicts with current state (name/path, lifecycle). |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | If-Match did not match the resource&#39;s current revision. |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
**428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
**406** | Accept does not admit application/json (NOT_ACCEPTABLE) — every upload-control response is JSON. |  * X-Request-Id - Request correlation identifier. <br>  |
**503** | Direct transfer is not fully configured/enabled (TRANSFER_DISABLED, no Retry-After), or the provider is transiently unavailable (TRANSFER_UNAVAILABLE, with Retry-After). |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploads_read**
> UploadSessionOut uploads_read(drive_id, upload_id, if_none_match=if_none_match, authorization=authorization)

Read Upload

Non-secret recovery state (§5.3). Never a target, coordinate,
principal, reservation, continuation, or provider diagnostic.

Idempotency-Key is not part of this read's contract (manifest idempotency_class: not_required): a supplied key plays no role and creates no idempotency record.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.upload_session_out import UploadSessionOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://drive.tokencanopy.com
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://drive.tokencanopy.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.UploadsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    upload_id = 'upload_id_example' # str | 
    if_none_match = 'if_none_match_example' # str |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Read Upload
        api_response = api_instance.uploads_read(drive_id, upload_id, if_none_match=if_none_match, authorization=authorization)
        print("The response of UploadsApi->uploads_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->uploads_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **upload_id** | **str**|  | 
 **if_none_match** | **str**|  | [optional] 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**UploadSessionOut**](UploadSessionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
**304** | If-None-Match matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
**406** | Accept does not admit application/json (NOT_ACCEPTABLE) — every upload-control response is JSON. |  * X-Request-Id - Request correlation identifier. <br>  |
**503** | Direct transfer is not fully configured/enabled (TRANSFER_DISABLED, no Retry-After), or the provider is transiently unavailable (TRANSFER_UNAVAILABLE, with Retry-After). |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

