# WorkspacesApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWorkspaceRouteV0WorkspacesPost**](WorkspacesApi.md#createworkspaceroutev0workspacespost) | **POST** /v0/workspaces | Create a new shared drive |
| [**listWorkspacesRouteV0WorkspacesGet**](WorkspacesApi.md#listworkspacesroutev0workspacesget) | **GET** /v0/workspaces | List the spaces you belong to |
| [**renameWorkspaceRouteV0WorkspacesOrgIdPatch**](WorkspacesApi.md#renameworkspaceroutev0workspacesorgidpatch) | **PATCH** /v0/workspaces/{org_id} | Rename a shared drive you administer |



## createWorkspaceRouteV0WorkspacesPost

> WorkspaceCreateOut createWorkspaceRouteV0WorkspacesPost(workspaceCreateIn)

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
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WorkspacesApi(config);

  const body = {
    // WorkspaceCreateIn
    workspaceCreateIn: ...,
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

### Return type

[**WorkspaceCreateOut**](WorkspaceCreateOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The workspace name or request is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The workspace conflicts with an existing organization. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listWorkspacesRouteV0WorkspacesGet

> WorkspaceList listWorkspacesRouteV0WorkspacesGet(cursor, limit)

List the spaces you belong to

Return every space the caller is a member of, each carrying the caller\&#39;s &#x60;role&#x60; in it. Metadata only. A &#x60;read&#x60;-scope token is sufficient.  **Cursor pagination:** when more results exist, the response carries &#x60;next_cursor&#x60;. Pass it back as &#x60;?cursor&#x3D;&lt;token&gt;&#x60; to fetch the next page; &#x60;null&#x60; means the listing is complete. &#x60;limit&#x60; is clamped to [1, 100] (default 50), never rejected.

### Example

```ts
import {
  Configuration,
  WorkspacesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListWorkspacesRouteV0WorkspacesGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WorkspacesApi(config);

  const body = {
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
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
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**WorkspaceList**](WorkspaceList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## renameWorkspaceRouteV0WorkspacesOrgIdPatch

> WorkspaceOut renameWorkspaceRouteV0WorkspacesOrgIdPatch(orgId, workspaceRenameIn)

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
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WorkspacesApi(config);

  const body = {
    // string
    orgId: orgId_example,
    // WorkspaceRenameIn
    workspaceRenameIn: ...,
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

### Return type

[**WorkspaceOut**](WorkspaceOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The workspace update is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The workspace does not exist for this user. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
