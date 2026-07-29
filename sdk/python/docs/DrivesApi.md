# agentdrive_sdk.DrivesApi

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_drive_key_route_v0_drives_drive_id_keys_post**](DrivesApi.md#create_drive_key_route_v0_drives_drive_id_keys_post) | **POST** /v0/drives/{drive_id}/keys | Create a drive API key
[**create_drive_route_v0_drives_post**](DrivesApi.md#create_drive_route_v0_drives_post) | **POST** /v0/drives | Create a drive in your active space
[**list_drive_keys_route_v0_drives_drive_id_keys_get**](DrivesApi.md#list_drive_keys_route_v0_drives_drive_id_keys_get) | **GET** /v0/drives/{drive_id}/keys | List a drive&#39;s API keys
[**list_drives_route_v0_drives_get**](DrivesApi.md#list_drives_route_v0_drives_get) | **GET** /v0/drives | List the drives you can see
[**rename_drive_route_v0_drives_drive_id_patch**](DrivesApi.md#rename_drive_route_v0_drives_drive_id_patch) | **PATCH** /v0/drives/{drive_id} | Rename a drive you own
[**revoke_drive_key_route_v0_drives_drive_id_keys_key_id_revoke_post**](DrivesApi.md#revoke_drive_key_route_v0_drives_drive_id_keys_key_id_revoke_post) | **POST** /v0/drives/{drive_id}/keys/{key_id}/revoke | Revoke a drive API key
[**rotate_one_key_route_v0_drives_drive_id_keys_key_id_rotate_post**](DrivesApi.md#rotate_one_key_route_v0_drives_drive_id_keys_key_id_rotate_post) | **POST** /v0/drives/{drive_id}/keys/{key_id}/rotate | Rotate one API key


# **create_drive_key_route_v0_drives_drive_id_keys_post**
> DriveApiKeyCreateOut create_drive_key_route_v0_drives_drive_id_keys_post(drive_id, drive_api_key_create_in)

Create a drive API key

Mint a new `ad_live_` key for a drive you manage — a drive may hold several (one per agent/integration). A `label` (a name for the key) is **required**. **Manager only** (404 no-leak otherwise), `full`-scope user token. The raw key is returned **once** — store it now.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.drive_api_key_create_in import DriveApiKeyCreateIn
from agentdrive_sdk.models.drive_api_key_create_out import DriveApiKeyCreateOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DrivesApi(api_client)
    drive_id = 'drive_id_example' # str |
    drive_api_key_create_in = agentdrive_sdk.DriveApiKeyCreateIn() # DriveApiKeyCreateIn |

    try:
        # Create a drive API key
        api_response = api_instance.create_drive_key_route_v0_drives_drive_id_keys_post(drive_id, drive_api_key_create_in)
        print("The response of DrivesApi->create_drive_key_route_v0_drives_drive_id_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DrivesApi->create_drive_key_route_v0_drives_drive_id_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |
 **drive_api_key_create_in** | [**DriveApiKeyCreateIn**](DriveApiKeyCreateIn.md)|  |

### Return type

[**DriveApiKeyCreateOut**](DriveApiKeyCreateOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The key label or scope is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The drive does not exist for this user. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drive_route_v0_drives_post**
> DriveCreateOut create_drive_route_v0_drives_post(drive_create_in)

Create a drive in your active space

Create a named drive. Any **member** of the space may create one; the creator becomes its **owner**. Requires a `full`-scope user token. The response carries the drive's `ad_live_` API key **once** (`api_key`) — store it now, it is never returned again (mint more keys via `POST /v0/drives/{id}/keys`).

The target workspace is the user's active organization (`users.default_org`); cross-workspace creation names no other workspace in v0.

A space may hold up to its plan's drive limit (workspaces-v2 §4.6; seat-aware for shared drives). A caller at the limit is blocked with `403 DRIVE_LIMIT_REACHED`; the limit is tier-governed, not a hard cap.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.drive_create_in import DriveCreateIn
from agentdrive_sdk.models.drive_create_out import DriveCreateOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DrivesApi(api_client)
    drive_create_in = agentdrive_sdk.DriveCreateIn() # DriveCreateIn |

    try:
        # Create a drive in your active space
        api_response = api_instance.create_drive_route_v0_drives_post(drive_create_in)
        print("The response of DrivesApi->create_drive_route_v0_drives_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DrivesApi->create_drive_route_v0_drives_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_create_in** | [**DriveCreateIn**](DriveCreateIn.md)|  |

### Return type

[**DriveCreateOut**](DriveCreateOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_drive_keys_route_v0_drives_drive_id_keys_get**
> DriveApiKeyListOut list_drive_keys_route_v0_drives_drive_id_keys_get(drive_id, cursor=cursor, limit=limit)

List a drive's API keys

List the `ad_live_` keys for a drive you manage (oldest first, including recently-revoked rows — filter on `revoked_at` for live only). **Manager only** (404 no-leak otherwise). A `read`-scope user token may list (metadata reveals no secret), mirroring `GET /v0/drives`. Metadata only — the raw key is never returned after mint.

**Cursor pagination:** when more results exist, the response carries `next_cursor`. Pass it back as `?cursor=<token>` to fetch the next page; `null` means the listing is complete. `limit` is clamped to [1, 100] (default 50), never rejected.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.drive_api_key_list_out import DriveApiKeyListOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DrivesApi(api_client)
    drive_id = 'drive_id_example' # str |
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List a drive's API keys
        api_response = api_instance.list_drive_keys_route_v0_drives_drive_id_keys_get(drive_id, cursor=cursor, limit=limit)
        print("The response of DrivesApi->list_drive_keys_route_v0_drives_drive_id_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DrivesApi->list_drive_keys_route_v0_drives_drive_id_keys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**DriveApiKeyListOut**](DriveApiKeyListOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The drive does not exist for this user. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_drives_route_v0_drives_get**
> DriveList list_drives_route_v0_drives_get(cursor=cursor, limit=limit)

List the drives you can see

Returns drive **metadata** (workspaces-design §4.2): an **admin** sees the whole active workspace's drive inventory (every owner); a **member** sees only the drives they own. Metadata only — owner, size, timestamps — never a raw API key, and never an authorization to read a drive's contents. A `read`-scope token may call this; mutations require `full`.

**Cursor pagination:** when more results exist, the response carries `next_cursor`. Pass it back as `?cursor=<token>` to fetch the next page; `null` means the listing is complete. `limit` is clamped to [1, 100] (default 50), never rejected.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.drive_list import DriveList
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DrivesApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List the drives you can see
        api_response = api_instance.list_drives_route_v0_drives_get(cursor=cursor, limit=limit)
        print("The response of DrivesApi->list_drives_route_v0_drives_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DrivesApi->list_drives_route_v0_drives_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**DriveList**](DriveList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_drive_route_v0_drives_drive_id_patch**
> DriveOut rename_drive_route_v0_drives_drive_id_patch(drive_id, drive_rename_in)

Rename a drive you own

Rename a drive. **Owner only** — a drive id that isn't yours returns 404 (no-leak). Requires a `full`-scope user token.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.drive_out import DriveOut
from agentdrive_sdk.models.drive_rename_in import DriveRenameIn
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DrivesApi(api_client)
    drive_id = 'drive_id_example' # str |
    drive_rename_in = agentdrive_sdk.DriveRenameIn() # DriveRenameIn |

    try:
        # Rename a drive you own
        api_response = api_instance.rename_drive_route_v0_drives_drive_id_patch(drive_id, drive_rename_in)
        print("The response of DrivesApi->rename_drive_route_v0_drives_drive_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DrivesApi->rename_drive_route_v0_drives_drive_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |
 **drive_rename_in** | [**DriveRenameIn**](DriveRenameIn.md)|  |

### Return type

[**DriveOut**](DriveOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The drive update is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No such drive exists for this principal. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The drive update conflicts with current workspace state. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_drive_key_route_v0_drives_drive_id_keys_key_id_revoke_post**
> revoke_drive_key_route_v0_drives_drive_id_keys_key_id_revoke_post(drive_id, key_id)

Revoke a drive API key

Revoke one `ad_live_` key of a drive you manage — anything using it loses access immediately. **Manager only** (404 no-leak otherwise), `full`-scope user token. Idempotent: revoking an unknown/already-revoked key returns 204 too (no existence oracle).

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DrivesApi(api_client)
    drive_id = 'drive_id_example' # str |
    key_id = 'key_id_example' # str |

    try:
        # Revoke a drive API key
        api_instance.revoke_drive_key_route_v0_drives_drive_id_keys_key_id_revoke_post(drive_id, key_id)
    except Exception as e:
        print("Exception when calling DrivesApi->revoke_drive_key_route_v0_drives_drive_id_keys_key_id_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |
 **key_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The drive or key does not exist for this user. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_one_key_route_v0_drives_drive_id_keys_key_id_rotate_post**
> DriveApiKeyCreateOut rotate_one_key_route_v0_drives_drive_id_keys_key_id_rotate_post(drive_id, key_id)

Rotate one API key

Rotate a single `ad_live_` key: revoke `key_id` and mint a replacement that inherits its label. **Only that key** is affected — the drive's other keys keep working. **Manager only** (404 no-leak otherwise), `full`-scope user token. The new key is returned **once** — store it now. A `key_id` that isn't a live key of this drive is a 404.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.drive_api_key_create_out import DriveApiKeyCreateOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DrivesApi(api_client)
    drive_id = 'drive_id_example' # str |
    key_id = 'key_id_example' # str |

    try:
        # Rotate one API key
        api_response = api_instance.rotate_one_key_route_v0_drives_drive_id_keys_key_id_rotate_post(drive_id, key_id)
        print("The response of DrivesApi->rotate_one_key_route_v0_drives_drive_id_keys_key_id_rotate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DrivesApi->rotate_one_key_route_v0_drives_drive_id_keys_key_id_rotate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |
 **key_id** | **str**|  |

### Return type

[**DriveApiKeyCreateOut**](DriveApiKeyCreateOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The drive or key does not exist for this user. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
