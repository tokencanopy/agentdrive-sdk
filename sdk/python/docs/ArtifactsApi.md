# agentdrive_sdk.ArtifactsApi

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifacts_content**](ArtifactsApi.md#artifacts_content) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id}/content | Read Artifact Content
[**artifacts_copy**](ArtifactsApi.md#artifacts_copy) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/copy | Copy Artifact
[**artifacts_create**](ArtifactsApi.md#artifacts_create) | **POST** /v0/drives/{drive_id}/artifacts | Create Artifact
[**artifacts_delete**](ArtifactsApi.md#artifacts_delete) | **DELETE** /v0/drives/{drive_id}/artifacts/{artifact_id} | Delete Artifact
[**artifacts_list**](ArtifactsApi.md#artifacts_list) | **GET** /v0/drives/{drive_id}/artifacts | List Artifacts
[**artifacts_read**](ArtifactsApi.md#artifacts_read) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id} | Read Artifact
[**artifacts_restore**](ArtifactsApi.md#artifacts_restore) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/restore | Restore Artifact
[**artifacts_update**](ArtifactsApi.md#artifacts_update) | **PATCH** /v0/drives/{drive_id}/artifacts/{artifact_id} | Update Artifact


# **artifacts_content**
> bytes artifacts_content(drive_id, artifact_id, if_none_match=if_none_match, authorization=authorization)

Read Artifact Content

Download the head version's bytes — stream or 307 signed URL.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
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
    api_instance = agentdrive_sdk.ArtifactsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 
    if_none_match = 'if_none_match_example' # str |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Read Artifact Content
        api_response = api_instance.artifacts_content(drive_id, artifact_id, if_none_match=if_none_match, authorization=authorization)
        print("The response of ArtifactsApi->artifacts_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->artifacts_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **artifact_id** | **str**|  | 
 **if_none_match** | **str**|  | [optional] 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

**bytes**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw artifact bytes (streamed). |  * X-Request-Id - Request correlation identifier. <br>  |
**304** | If-None-Match matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**307** | Redirect to a short-lived signed URL. |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_copy**
> ArtifactOut artifacts_copy(drive_id, artifact_id, idempotency_key, artifact_copy_in, if_match=if_match, authorization=authorization)

Copy Artifact

Copy one artifact within the same drive.

Cross-drive copy is out of v0 scope and rejected (400 INVALID_ARGUMENT).
``destination_drive_id`` must equal the source drive when present.
Materializes the artifact + its selected version synchronously → 201.
``If-Match`` is optional; when present it is validated against the source
revision (412 stale).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_copy_in import ArtifactCopyIn
from agentdrive_sdk.models.artifact_out import ArtifactOut
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
    api_instance = agentdrive_sdk.ArtifactsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    artifact_copy_in = agentdrive_sdk.ArtifactCopyIn() # ArtifactCopyIn | 
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Copy Artifact
        api_response = api_instance.artifacts_copy(drive_id, artifact_id, idempotency_key, artifact_copy_in, if_match=if_match, authorization=authorization)
        print("The response of ArtifactsApi->artifacts_copy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->artifacts_copy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **artifact_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **artifact_copy_in** | [**ArtifactCopyIn**](ArtifactCopyIn.md)|  | 
 **if_match** | **str**|  | [optional] 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | A sibling already occupies the name/path, or the idempotency key was reused for a different request. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | If-Match did not match (copy/restore preconditions). |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
**428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_create**
> ArtifactOut artifacts_create(drive_id, idempotency_key, parent_id, name, content, authorization=authorization, metadata=metadata, content_type=content_type, sha256=sha256)

Create Artifact

Create one artifact with inline content — multipart only.

Multipart only (415 for a JSON body). Parts: parent_id, name, metadata, content (bytes), content_type, sha256. parent_id, name, and content are required.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
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
    api_instance = agentdrive_sdk.ArtifactsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    parent_id = 'parent_id_example' # str | Destination folder id (fld_*).
    name = 'name_example' # str | Artifact name.
    content = None # bytes | The artifact bytes.
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    metadata = None # object | Free-form JSON metadata. (optional)
    content_type = 'content_type_example' # str | Declared media type. (optional)
    sha256 = 'sha256_example' # str | Optional content sha256 for verification. (optional)

    try:
        # Create Artifact
        api_response = api_instance.artifacts_create(drive_id, idempotency_key, parent_id, name, content, authorization=authorization, metadata=metadata, content_type=content_type, sha256=sha256)
        print("The response of ArtifactsApi->artifacts_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->artifacts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **parent_id** | **str**| Destination folder id (fld_*). | 
 **name** | **str**| Artifact name. | 
 **content** | **bytes**| The artifact bytes. | 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 
 **metadata** | [**object**](object.md)| Free-form JSON metadata. | [optional] 
 **content_type** | **str**| Declared media type. | [optional] 
 **sha256** | **str**| Optional content sha256 for verification. | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | A sibling already occupies the name/path, or the idempotency key was reused for a different request. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | If-Match did not match (copy/restore preconditions). |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
**428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
**413** | The content part exceeds the inline ceiling (ARTIFACT_TOO_LARGE). Above it, use a direct upload session. |  * X-Request-Id - Request correlation identifier. <br>  |
**415** | This operation requires multipart/form-data (UNSUPPORTED_MEDIA_TYPE). |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_delete**
> ArtifactOut artifacts_delete(drive_id, artifact_id, idempotency_key, if_match, authorization=authorization)

Delete Artifact

Soft-delete one artifact (its versions stay).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
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
    api_instance = agentdrive_sdk.ArtifactsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    if_match = 'if_match_example' # str | 
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Delete Artifact
        api_response = api_instance.artifacts_delete(drive_id, artifact_id, idempotency_key, if_match, authorization=authorization)
        print("The response of ArtifactsApi->artifacts_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->artifacts_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **artifact_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **if_match** | **str**|  | 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

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
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_list**
> ArtifactListOut artifacts_list(drive_id, lifecycle=lifecycle, limit=limit, cursor=cursor, parent_id=parent_id, name=name, content_type=content_type, label=label, updated_after=updated_after, updated_before=updated_before, authorization=authorization)

List Artifacts

List the drive's artifacts, newest-first (keyset paginated).

``lifecycle`` (active|deleted|all) exposes soft-deleted artifacts.
``parent_id`` / ``name`` / ``content_type`` / ``label`` are exact-match
filters; ``updated_after`` / ``updated_before`` are inclusive bounds.
Unknown query parameters are rejected.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_list_out import ArtifactListOut
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
    api_instance = agentdrive_sdk.ArtifactsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    lifecycle = 'active' # str |  (optional) (default to 'active')
    limit = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    parent_id = 'parent_id_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    content_type = 'content_type_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # List Artifacts
        api_response = api_instance.artifacts_list(drive_id, lifecycle=lifecycle, limit=limit, cursor=cursor, parent_id=parent_id, name=name, content_type=content_type, label=label, updated_after=updated_after, updated_before=updated_before, authorization=authorization)
        print("The response of ArtifactsApi->artifacts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->artifacts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **lifecycle** | **str**|  | [optional] [default to &#39;active&#39;]
 **limit** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **parent_id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **updated_after** | **datetime**|  | [optional] 
 **updated_before** | **datetime**|  | [optional] 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**ArtifactListOut**](ArtifactListOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_read**
> ArtifactOut artifacts_read(drive_id, artifact_id, if_none_match=if_none_match, authorization=authorization)

Read Artifact

Read one active artifact. ``If-None-Match`` short-circuits to 304.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
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
    api_instance = agentdrive_sdk.ArtifactsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 
    if_none_match = 'if_none_match_example' # str |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Read Artifact
        api_response = api_instance.artifacts_read(drive_id, artifact_id, if_none_match=if_none_match, authorization=authorization)
        print("The response of ArtifactsApi->artifacts_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->artifacts_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **artifact_id** | **str**|  | 
 **if_none_match** | **str**|  | [optional] 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

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
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_restore**
> ArtifactOut artifacts_restore(drive_id, artifact_id, idempotency_key, if_match, authorization=authorization)

Restore Artifact

Restore a soft-deleted artifact atomically.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
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
    api_instance = agentdrive_sdk.ArtifactsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    if_match = 'if_match_example' # str | 
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Restore Artifact
        api_response = api_instance.artifacts_restore(drive_id, artifact_id, idempotency_key, if_match, authorization=authorization)
        print("The response of ArtifactsApi->artifacts_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->artifacts_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **artifact_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **if_match** | **str**|  | 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

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
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_update**
> ArtifactOut artifacts_update(drive_id, artifact_id, idempotency_key, if_match, artifact_update_in, authorization=authorization)

Update Artifact

Rename / move / set metadata or labels. At least one field required.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
from agentdrive_sdk.models.artifact_update_in import ArtifactUpdateIn
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
    api_instance = agentdrive_sdk.ArtifactsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    if_match = 'if_match_example' # str | 
    artifact_update_in = agentdrive_sdk.ArtifactUpdateIn() # ArtifactUpdateIn | 
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Update Artifact
        api_response = api_instance.artifacts_update(drive_id, artifact_id, idempotency_key, if_match, artifact_update_in, authorization=authorization)
        print("The response of ArtifactsApi->artifacts_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->artifacts_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **artifact_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **if_match** | **str**|  | 
 **artifact_update_in** | [**ArtifactUpdateIn**](ArtifactUpdateIn.md)|  | 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

