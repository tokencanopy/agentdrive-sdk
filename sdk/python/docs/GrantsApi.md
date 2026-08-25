# agentdrive_sdk.GrantsApi

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grants_create**](GrantsApi.md#grants_create) | **POST** /v0/drives/{drive_id}/grants | Create Grant
[**grants_list**](GrantsApi.md#grants_list) | **GET** /v0/drives/{drive_id}/grants | List Grants
[**grants_read**](GrantsApi.md#grants_read) | **GET** /v0/drives/{drive_id}/grants/{grant_id} | Read Grant
[**grants_revoke**](GrantsApi.md#grants_revoke) | **DELETE** /v0/drives/{drive_id}/grants/{grant_id} | Revoke Grant
[**grants_update**](GrantsApi.md#grants_update) | **PATCH** /v0/drives/{drive_id}/grants/{grant_id} | Update Grant


# **grants_create**
> GrantOut grants_create(drive_id, idempotency_key, grant_create_in, authorization=authorization)

Create Grant

Grant one principal a role on a drive, folder, or artifact.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.grant_create_in import GrantCreateIn
from agentdrive_sdk.models.grant_out import GrantOut
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
    api_instance = agentdrive_sdk.GrantsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    grant_create_in = agentdrive_sdk.GrantCreateIn() # GrantCreateIn | 
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Create Grant
        api_response = api_instance.grants_create(drive_id, idempotency_key, grant_create_in, authorization=authorization)
        print("The response of GrantsApi->grants_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->grants_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **grant_create_in** | [**GrantCreateIn**](GrantCreateIn.md)|  | 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**GrantOut**](GrantOut.md)

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

# **grants_list**
> GrantListOut grants_list(drive_id, lifecycle=lifecycle, limit=limit, cursor=cursor, resource_type=resource_type, resource_id=resource_id, principal_type=principal_type, authorization=authorization)

List Grants

List explicit grants in the drive, keyset paginated.

**What you see depends on your role (contract change).** A caller holding
``manager`` on the drive lists EVERY grant in it. Any other caller lists
only the grants that name them — their own agent/user rows, ``workspace``
grants covering them, and ``public`` grants (which already expose the
resource to them anyway). Previously any drive ``viewer`` could page out
every principal id, role and expiry in the drive; that was an
access-graph disclosure, not a feature.

The operation is refused (404) only for a caller holding no live grant
anywhere in the drive — never for lack of ``manager``, because seeing
your own access is not a privilege. That admits folder-scoped
principals, who previously 404'd here despite having access to show. A
folder ``manager`` still sees only their own rows, not the roster of the
subtree they administer; scoping the listing by per-resource
administration authority is a follow-up this change does not claim.

``resource_id`` filters to one resource's grants and REQUIRES
``resource_type`` alongside it — a bare resource id is ambiguous across
the three resource kinds, and guessing the kind from the id prefix would
make the filter's meaning depend on an id format the contract does not
promise to keep. ``resource_type`` on its own remains a valid (and
pre-existing) filter.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.grant_list_out import GrantListOut
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
    api_instance = agentdrive_sdk.GrantsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    lifecycle = 'active' # str |  (optional) (default to 'active')
    limit = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    resource_type = 'resource_type_example' # str |  (optional)
    resource_id = 'resource_id_example' # str |  (optional)
    principal_type = 'principal_type_example' # str |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # List Grants
        api_response = api_instance.grants_list(drive_id, lifecycle=lifecycle, limit=limit, cursor=cursor, resource_type=resource_type, resource_id=resource_id, principal_type=principal_type, authorization=authorization)
        print("The response of GrantsApi->grants_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->grants_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **lifecycle** | **str**|  | [optional] [default to &#39;active&#39;]
 **limit** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **resource_type** | **str**|  | [optional] 
 **resource_id** | **str**|  | [optional] 
 **principal_type** | **str**|  | [optional] 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**GrantListOut**](GrantListOut.md)

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

# **grants_read**
> GrantOut grants_read(drive_id, grant_id, if_none_match=if_none_match, authorization=authorization)

Read Grant

Read one grant in the drive.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.grant_out import GrantOut
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
    api_instance = agentdrive_sdk.GrantsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    grant_id = 'grant_id_example' # str | 
    if_none_match = 'if_none_match_example' # str |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Read Grant
        api_response = api_instance.grants_read(drive_id, grant_id, if_none_match=if_none_match, authorization=authorization)
        print("The response of GrantsApi->grants_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->grants_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **grant_id** | **str**|  | 
 **if_none_match** | **str**|  | [optional] 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**GrantOut**](GrantOut.md)

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

# **grants_revoke**
> GrantOut grants_revoke(drive_id, grant_id, idempotency_key, if_match, authorization=authorization)

Revoke Grant

Revoke a grant (soft, sets revoked_at) under If-Match.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.grant_out import GrantOut
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
    api_instance = agentdrive_sdk.GrantsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    grant_id = 'grant_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    if_match = 'if_match_example' # str | 
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Revoke Grant
        api_response = api_instance.grants_revoke(drive_id, grant_id, idempotency_key, if_match, authorization=authorization)
        print("The response of GrantsApi->grants_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->grants_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **grant_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **if_match** | **str**|  | 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**GrantOut**](GrantOut.md)

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

# **grants_update**
> GrantOut grants_update(drive_id, grant_id, idempotency_key, if_match, grant_update_in, authorization=authorization)

Update Grant

Change a grant's role or expiry under If-Match.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.grant_out import GrantOut
from agentdrive_sdk.models.grant_update_in import GrantUpdateIn
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
    api_instance = agentdrive_sdk.GrantsApi(api_client)
    drive_id = 'drive_id_example' # str | 
    grant_id = 'grant_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | 
    if_match = 'if_match_example' # str | 
    grant_update_in = agentdrive_sdk.GrantUpdateIn() # GrantUpdateIn | 
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Update Grant
        api_response = api_instance.grants_update(drive_id, grant_id, idempotency_key, if_match, grant_update_in, authorization=authorization)
        print("The response of GrantsApi->grants_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->grants_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **grant_id** | **str**|  | 
 **idempotency_key** | **str**|  | 
 **if_match** | **str**|  | 
 **grant_update_in** | [**GrantUpdateIn**](GrantUpdateIn.md)|  | 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**GrantOut**](GrantOut.md)

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

