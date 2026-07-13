# agentdrive_sdk.WorkspacesApi

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace_route_v0_workspaces_post**](WorkspacesApi.md#create_workspace_route_v0_workspaces_post) | **POST** /v0/workspaces | Create a new shared drive
[**list_workspaces_route_v0_workspaces_get**](WorkspacesApi.md#list_workspaces_route_v0_workspaces_get) | **GET** /v0/workspaces | List the spaces you belong to
[**rename_workspace_route_v0_workspaces_org_id_patch**](WorkspacesApi.md#rename_workspace_route_v0_workspaces_org_id_patch) | **PATCH** /v0/workspaces/{org_id} | Rename a shared drive you administer


# **create_workspace_route_v0_workspaces_post**
> WorkspaceCreateOut create_workspace_route_v0_workspaces_post(workspace_create_in, authorization=authorization)

Create a new shared drive

Create a new **shared drive** — a shared, multi-member space (the `workspaces` path is retained for API stability). You become its **admin** and get a starter drive; the starter drive's `ad_live_` key is returned **once** (`starter_drive_api_key`).

A user may administer up to their plan's number of shared drives (workspaces-v2 §4.6). A caller at the limit is blocked with `403 WORKSPACE_LIMIT_REACHED`. Requires a `full`-scope user token.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.WorkspacesApi(api_client)
    workspace_create_in = agentdrive_sdk.WorkspaceCreateIn() # WorkspaceCreateIn | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Create a new shared drive
        api_response = api_instance.create_workspace_route_v0_workspaces_post(workspace_create_in, authorization=authorization)
        print("The response of WorkspacesApi->create_workspace_route_v0_workspaces_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->create_workspace_route_v0_workspaces_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_create_in** | [**WorkspaceCreateIn**](WorkspaceCreateIn.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**WorkspaceCreateOut**](WorkspaceCreateOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces_route_v0_workspaces_get**
> WorkspaceList list_workspaces_route_v0_workspaces_get(cursor=cursor, limit=limit, authorization=authorization)

List the spaces you belong to

Return every space the caller is a member of, each carrying the caller's `role` in it. Metadata only. A `read`-scope token is sufficient.

**Cursor pagination:** when more results exist, the response carries `next_cursor`. Pass it back as `?cursor=<token>` to fetch the next page; `null` means the listing is complete. `limit` is clamped to [1, 100] (default 50), never rejected.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.WorkspacesApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List the spaces you belong to
        api_response = api_instance.list_workspaces_route_v0_workspaces_get(cursor=cursor, limit=limit, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**WorkspaceList**](WorkspaceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_workspace_route_v0_workspaces_org_id_patch**
> WorkspaceOut rename_workspace_route_v0_workspaces_org_id_patch(org_id, workspace_rename_in, authorization=authorization)

Rename a shared drive you administer

Rename a shared drive. **Admin only** — one you don't administer (or aren't a member of) returns 404 (no-leak). Requires a `full`-scope user token.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.WorkspacesApi(api_client)
    org_id = 'org_id_example' # str | 
    workspace_rename_in = agentdrive_sdk.WorkspaceRenameIn() # WorkspaceRenameIn | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Rename a shared drive you administer
        api_response = api_instance.rename_workspace_route_v0_workspaces_org_id_patch(org_id, workspace_rename_in, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**WorkspaceOut**](WorkspaceOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

