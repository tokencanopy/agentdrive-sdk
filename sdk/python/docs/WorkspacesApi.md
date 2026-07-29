# agentdrive_sdk.WorkspacesApi

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace_route_v0_workspaces_post**](WorkspacesApi.md#create_workspace_route_v0_workspaces_post) | **POST** /v0/workspaces | Create a new shared drive
[**list_workspaces_route_v0_workspaces_get**](WorkspacesApi.md#list_workspaces_route_v0_workspaces_get) | **GET** /v0/workspaces | List the spaces you belong to
[**rename_workspace_route_v0_workspaces_org_id_patch**](WorkspacesApi.md#rename_workspace_route_v0_workspaces_org_id_patch) | **PATCH** /v0/workspaces/{org_id} | Rename a shared drive you administer


# **create_workspace_route_v0_workspaces_post**
> WorkspaceCreateOut create_workspace_route_v0_workspaces_post(workspace_create_in)

Create a new shared drive

Create a new **shared drive** — a shared, multi-member space (the `workspaces` path is retained for API stability). You become its **admin** and get a starter drive; the starter drive's `ad_live_` key is returned **once** (`starter_drive_api_key`).

A user may administer up to their plan's number of shared drives (workspaces-v2 §4.6). A caller at the limit is blocked with `403 WORKSPACE_LIMIT_REACHED`. Requires a `full`-scope user token.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.workspace_create_in import WorkspaceCreateIn
from agentdrive_sdk.models.workspace_create_out import WorkspaceCreateOut
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
    api_instance = agentdrive_sdk.WorkspacesApi(api_client)
    workspace_create_in = agentdrive_sdk.WorkspaceCreateIn() # WorkspaceCreateIn |

    try:
        # Create a new shared drive
        api_response = api_instance.create_workspace_route_v0_workspaces_post(workspace_create_in)
        print("The response of WorkspacesApi->create_workspace_route_v0_workspaces_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->create_workspace_route_v0_workspaces_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_create_in** | [**WorkspaceCreateIn**](WorkspaceCreateIn.md)|  |

### Return type

[**WorkspaceCreateOut**](WorkspaceCreateOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The workspace name or request is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The workspace conflicts with an existing organization. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces_route_v0_workspaces_get**
> WorkspaceList list_workspaces_route_v0_workspaces_get(cursor=cursor, limit=limit)

List the spaces you belong to

Return every space the caller is a member of, each carrying the caller's `role` in it. Metadata only. A `read`-scope token is sufficient.

**Cursor pagination:** when more results exist, the response carries `next_cursor`. Pass it back as `?cursor=<token>` to fetch the next page; `null` means the listing is complete. `limit` is clamped to [1, 100] (default 50), never rejected.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.workspace_list import WorkspaceList
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
    api_instance = agentdrive_sdk.WorkspacesApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List the spaces you belong to
        api_response = api_instance.list_workspaces_route_v0_workspaces_get(cursor=cursor, limit=limit)
        print("The response of WorkspacesApi->list_workspaces_route_v0_workspaces_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->list_workspaces_route_v0_workspaces_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**WorkspaceList**](WorkspaceList.md)

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

# **rename_workspace_route_v0_workspaces_org_id_patch**
> WorkspaceOut rename_workspace_route_v0_workspaces_org_id_patch(org_id, workspace_rename_in)

Rename a shared drive you administer

Rename a shared drive. **Admin only** — one you don't administer (or aren't a member of) returns 404 (no-leak). Requires a `full`-scope user token.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.workspace_out import WorkspaceOut
from agentdrive_sdk.models.workspace_rename_in import WorkspaceRenameIn
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
    api_instance = agentdrive_sdk.WorkspacesApi(api_client)
    org_id = 'org_id_example' # str |
    workspace_rename_in = agentdrive_sdk.WorkspaceRenameIn() # WorkspaceRenameIn |

    try:
        # Rename a shared drive you administer
        api_response = api_instance.rename_workspace_route_v0_workspaces_org_id_patch(org_id, workspace_rename_in)
        print("The response of WorkspacesApi->rename_workspace_route_v0_workspaces_org_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->rename_workspace_route_v0_workspaces_org_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  |
 **workspace_rename_in** | [**WorkspaceRenameIn**](WorkspaceRenameIn.md)|  |

### Return type

[**WorkspaceOut**](WorkspaceOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The workspace update is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The workspace does not exist for this user. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
