# WorkspacesApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWorkspaceRouteV0WorkspacesPost**](WorkspacesApi.md#createworkspaceroutev0workspacespost) | **POST** /v0/workspaces | Create a new shared drive |
| [**listWorkspacesRouteV0WorkspacesGet**](WorkspacesApi.md#listworkspacesroutev0workspacesget) | **GET** /v0/workspaces | List the spaces you belong to |
| [**renameWorkspaceRouteV0WorkspacesOrgIdPatch**](WorkspacesApi.md#renameworkspaceroutev0workspacesorgidpatch) | **PATCH** /v0/workspaces/{org_id} | Rename a shared drive you administer |



## createWorkspaceRouteV0WorkspacesPost

> WorkspaceCreateOut createWorkspaceRouteV0WorkspacesPost(workspaceCreateIn, authorization)

Create a new shared drive

Create a new **shared drive** — a shared, multi-member space (the &#x60;workspaces&#x60; path is retained for API stability). You become its **admin** and get a starter drive; the starter drive\&#39;s &#x60;ad_live_&#x60; key is returned **once** (&#x60;starter_drive_api_key&#x60;).  A user may administer up to their plan\&#39;s number of shared drives (workspaces-v2 §4.6). A caller at the limit is blocked with &#x60;403 WORKSPACE_LIMIT_REACHED&#x60;. Requires a &#x60;full&#x60;-scope user token.

### Example

```ts
import {
  Configuration,
  WorkspacesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateWorkspaceRouteV0WorkspacesPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new WorkspacesApi();

  const body = {
    // WorkspaceCreateIn
    workspaceCreateIn: ...,
    // string (optional)
    authorization: authorization_example,
  } satisfies CreateWorkspaceRouteV0WorkspacesPostRequest;

  try {
    const data = await api.createWorkspaceRouteV0WorkspacesPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **workspaceCreateIn** | [WorkspaceCreateIn](WorkspaceCreateIn.md) |  | |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**WorkspaceCreateOut**](WorkspaceCreateOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listWorkspacesRouteV0WorkspacesGet

> WorkspaceList listWorkspacesRouteV0WorkspacesGet(authorization)

List the spaces you belong to

Return every space the caller is a member of, each carrying the caller\&#39;s &#x60;role&#x60; in it. Metadata only. A &#x60;read&#x60;-scope token is sufficient.

### Example

```ts
import {
  Configuration,
  WorkspacesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListWorkspacesRouteV0WorkspacesGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new WorkspacesApi();

  const body = {
    // string (optional)
    authorization: authorization_example,
  } satisfies ListWorkspacesRouteV0WorkspacesGetRequest;

  try {
    const data = await api.listWorkspacesRouteV0WorkspacesGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**WorkspaceList**](WorkspaceList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## renameWorkspaceRouteV0WorkspacesOrgIdPatch

> WorkspaceOut renameWorkspaceRouteV0WorkspacesOrgIdPatch(orgId, workspaceRenameIn, authorization)

Rename a shared drive you administer

Rename a shared drive. **Admin only** — one you don\&#39;t administer (or aren\&#39;t a member of) returns 404 (no-leak). Requires a &#x60;full&#x60;-scope user token.

### Example

```ts
import {
  Configuration,
  WorkspacesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RenameWorkspaceRouteV0WorkspacesOrgIdPatchRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new WorkspacesApi();

  const body = {
    // string
    orgId: orgId_example,
    // WorkspaceRenameIn
    workspaceRenameIn: ...,
    // string (optional)
    authorization: authorization_example,
  } satisfies RenameWorkspaceRouteV0WorkspacesOrgIdPatchRequest;

  try {
    const data = await api.renameWorkspaceRouteV0WorkspacesOrgIdPatch(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **orgId** | `string` |  | [Defaults to `undefined`] |
| **workspaceRenameIn** | [WorkspaceRenameIn](WorkspaceRenameIn.md) |  | |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**WorkspaceOut**](WorkspaceOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

