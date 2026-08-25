# agentdrive_sdk.VersionsApi

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**versions_append**](VersionsApi.md#versions_append) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions | Append Version
[**versions_content**](VersionsApi.md#versions_content) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/content | Read Version Content
[**versions_list**](VersionsApi.md#versions_list) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions | List Versions
[**versions_read**](VersionsApi.md#versions_read) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id} | Read Version
[**versions_restore**](VersionsApi.md#versions_restore) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/restore | Restore Version


# **versions_append**
> VersionCreatedOut versions_append(drive_id, artifact_id, idempotency_key, if_match, content, authorization=authorization, content_type=content_type, sha256=sha256)

Append Version

Append one immutable version and rotate the artifact head.

Multipart only (415 for a JSON body). Parts: content (bytes), content_type, sha256. content is required; name, parent_id, and metadata are not accepted here.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.version_created_out import VersionCreatedOut
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
    api_instance = agentdrive_sdk.VersionsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    if_match = 'if_match_example' # str | 
    content = None # bytes | The artifact bytes.
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    content_type = 'content_type_example' # str | Declared media type. (optional)
    sha256 = 'sha256_example' # str | Optional content sha256 for verification. (optional)

    try:
        # Append Version
        api_response = api_instance.versions_append(drive_id, artifact_id, idempotency_key, if_match, content, authorization=authorization, content_type=content_type, sha256=sha256)
        print("The response of VersionsApi->versions_append:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->versions_append: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **artifact_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **if_match** | **str**|  | 
 **content** | **bytes**| The artifact bytes. | 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 
 **content_type** | **str**| Declared media type. | [optional] 
 **sha256** | **str**| Optional content sha256 for verification. | [optional] 

### Return type

[**VersionCreatedOut**](VersionCreatedOut.md)

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
**404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The mutation conflicts with current state (name/path, lifecycle). |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | If-Match did not match the resource&#39;s current revision. |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
**428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
**413** | The content part exceeds the inline ceiling (ARTIFACT_TOO_LARGE). Above it, use a direct upload session. |  * X-Request-Id - Request correlation identifier. <br>  |
**415** | This operation requires multipart/form-data (UNSUPPORTED_MEDIA_TYPE). |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **versions_content**
> bytes versions_content(drive_id, artifact_id, version_id, if_none_match=if_none_match, authorization=authorization)

Read Version Content

Download one version's immutable bytes — stream or 307.

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
    api_instance = agentdrive_sdk.VersionsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 
    version_id = 'version_id_example' # str | 
    if_none_match = 'if_none_match_example' # str |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Read Version Content
        api_response = api_instance.versions_content(drive_id, artifact_id, version_id, if_none_match=if_none_match, authorization=authorization)
        print("The response of VersionsApi->versions_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->versions_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **artifact_id** | **str**|  | 
 **version_id** | **str**|  | 
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

# **versions_list**
> VersionListOut versions_list(drive_id, artifact_id, limit=limit, cursor=cursor, authorization=authorization)

List Versions

List the artifact's version trail, newest first (ordinal DESC).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.version_list_out import VersionListOut
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
    api_instance = agentdrive_sdk.VersionsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 
    limit = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # List Versions
        api_response = api_instance.versions_list(drive_id, artifact_id, limit=limit, cursor=cursor, authorization=authorization)
        print("The response of VersionsApi->versions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->versions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **artifact_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**VersionListOut**](VersionListOut.md)

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

# **versions_read**
> VersionOut versions_read(drive_id, artifact_id, version_id, if_none_match=if_none_match, authorization=authorization)

Read Version

Read one immutable version.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.version_out import VersionOut
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
    api_instance = agentdrive_sdk.VersionsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 
    version_id = 'version_id_example' # str | 
    if_none_match = 'if_none_match_example' # str |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Read Version
        api_response = api_instance.versions_read(drive_id, artifact_id, version_id, if_none_match=if_none_match, authorization=authorization)
        print("The response of VersionsApi->versions_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->versions_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **artifact_id** | **str**|  | 
 **version_id** | **str**|  | 
 **if_none_match** | **str**|  | [optional] 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**VersionOut**](VersionOut.md)

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

# **versions_restore**
> VersionCreatedOut versions_restore(drive_id, artifact_id, version_id, idempotency_key, if_match, authorization=authorization)

Restore Version

Restore a historical version as a NEW head version (no byte copy).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.version_created_out import VersionCreatedOut
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
    api_instance = agentdrive_sdk.VersionsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    artifact_id = 'artifact_id_example' # str | 
    version_id = 'version_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    if_match = 'if_match_example' # str | 
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Restore Version
        api_response = api_instance.versions_restore(drive_id, artifact_id, version_id, idempotency_key, if_match, authorization=authorization)
        print("The response of VersionsApi->versions_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->versions_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **artifact_id** | **str**|  | 
 **version_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **if_match** | **str**|  | 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**VersionCreatedOut**](VersionCreatedOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  |
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

