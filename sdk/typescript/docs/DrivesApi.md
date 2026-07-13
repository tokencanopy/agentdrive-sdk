# DrivesApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDriveKeyRouteV0DrivesDriveIdKeysPost**](DrivesApi.md#createdrivekeyroutev0drivesdriveidkeyspost) | **POST** /v0/drives/{drive_id}/keys | Create a drive API key |
| [**createDriveRouteV0DrivesPost**](DrivesApi.md#createdriveroutev0drivespost) | **POST** /v0/drives | Create a drive in your active space |
| [**listDriveKeysRouteV0DrivesDriveIdKeysGet**](DrivesApi.md#listdrivekeysroutev0drivesdriveidkeysget) | **GET** /v0/drives/{drive_id}/keys | List a drive\&#39;s API keys |
| [**listDrivesRouteV0DrivesGet**](DrivesApi.md#listdrivesroutev0drivesget) | **GET** /v0/drives | List the drives you can see |
| [**renameDriveRouteV0DrivesDriveIdPatch**](DrivesApi.md#renamedriveroutev0drivesdriveidpatch) | **PATCH** /v0/drives/{drive_id} | Rename a drive you own |
| [**revokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePost**](DrivesApi.md#revokedrivekeyroutev0drivesdriveidkeyskeyidrevokepost) | **POST** /v0/drives/{drive_id}/keys/{key_id}/revoke | Revoke a drive API key |
| [**rotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost**](DrivesApi.md#rotateonekeyroutev0drivesdriveidkeyskeyidrotatepost) | **POST** /v0/drives/{drive_id}/keys/{key_id}/rotate | Rotate one API key |



## createDriveKeyRouteV0DrivesDriveIdKeysPost

> DriveApiKeyCreateOut createDriveKeyRouteV0DrivesDriveIdKeysPost(driveId, driveApiKeyCreateIn, authorization)

Create a drive API key

Mint a new &#x60;ad_live_&#x60; key for a drive you manage — a drive may hold several (one per agent/integration). A &#x60;label&#x60; (a name for the key) is **required**. **Manager only** (404 no-leak otherwise), &#x60;full&#x60;-scope user token. The raw key is returned **once** — store it now.

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateDriveKeyRouteV0DrivesDriveIdKeysPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DrivesApi();

  const body = {
    // string
    driveId: driveId_example,
    // DriveApiKeyCreateIn
    driveApiKeyCreateIn: ...,
    // string (optional)
    authorization: authorization_example,
  } satisfies CreateDriveKeyRouteV0DrivesDriveIdKeysPostRequest;

  try {
    const data = await api.createDriveKeyRouteV0DrivesDriveIdKeysPost(body);
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
| **driveId** | `string` |  | [Defaults to `undefined`] |
| **driveApiKeyCreateIn** | [DriveApiKeyCreateIn](DriveApiKeyCreateIn.md) |  | |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveApiKeyCreateOut**](DriveApiKeyCreateOut.md)

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


## createDriveRouteV0DrivesPost

> DriveCreateOut createDriveRouteV0DrivesPost(driveCreateIn, authorization)

Create a drive in your active space

Create a named drive. Any **member** of the space may create one; the creator becomes its **owner**. Requires a &#x60;full&#x60;-scope user token. The response carries the drive\&#39;s &#x60;ad_live_&#x60; API key **once** (&#x60;api_key&#x60;) — store it now, it is never returned again (mint more keys via &#x60;POST /v0/drives/{id}/keys&#x60;).  The target workspace is the user\&#39;s active organization (&#x60;users.default_org&#x60;); cross-workspace creation names no other workspace in v0.  A space may hold up to its plan\&#39;s drive limit (workspaces-v2 §4.6; seat-aware for shared drives). A caller at the limit is blocked with &#x60;403 DRIVE_LIMIT_REACHED&#x60;; the limit is tier-governed, not a hard cap.

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateDriveRouteV0DrivesPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DrivesApi();

  const body = {
    // DriveCreateIn
    driveCreateIn: ...,
    // string (optional)
    authorization: authorization_example,
  } satisfies CreateDriveRouteV0DrivesPostRequest;

  try {
    const data = await api.createDriveRouteV0DrivesPost(body);
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
| **driveCreateIn** | [DriveCreateIn](DriveCreateIn.md) |  | |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveCreateOut**](DriveCreateOut.md)

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


## listDriveKeysRouteV0DrivesDriveIdKeysGet

> DriveApiKeyListOut listDriveKeysRouteV0DrivesDriveIdKeysGet(driveId, cursor, limit, authorization)

List a drive\&#39;s API keys

List the &#x60;ad_live_&#x60; keys for a drive you manage (oldest first, including recently-revoked rows — filter on &#x60;revoked_at&#x60; for live only). **Manager only** (404 no-leak otherwise). A &#x60;read&#x60;-scope user token may list (metadata reveals no secret), mirroring &#x60;GET /v0/drives&#x60;. Metadata only — the raw key is never returned after mint.  **Cursor pagination:** when more results exist, the response carries &#x60;next_cursor&#x60;. Pass it back as &#x60;?cursor&#x3D;&lt;token&gt;&#x60; to fetch the next page; &#x60;null&#x60; means the listing is complete. &#x60;limit&#x60; is clamped to [1, 100] (default 50), never rejected.

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListDriveKeysRouteV0DrivesDriveIdKeysGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DrivesApi();

  const body = {
    // string
    driveId: driveId_example,
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
    // string (optional)
    authorization: authorization_example,
  } satisfies ListDriveKeysRouteV0DrivesDriveIdKeysGetRequest;

  try {
    const data = await api.listDriveKeysRouteV0DrivesDriveIdKeysGet(body);
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
| **driveId** | `string` |  | [Defaults to `undefined`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveApiKeyListOut**](DriveApiKeyListOut.md)

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


## listDrivesRouteV0DrivesGet

> DriveList listDrivesRouteV0DrivesGet(cursor, limit, authorization)

List the drives you can see

Returns drive **metadata** (workspaces-design §4.2): an **admin** sees the whole active workspace\&#39;s drive inventory (every owner); a **member** sees only the drives they own. Metadata only — owner, size, timestamps — never a raw API key, and never an authorization to read a drive\&#39;s contents. A &#x60;read&#x60;-scope token may call this; mutations require &#x60;full&#x60;.  **Cursor pagination:** when more results exist, the response carries &#x60;next_cursor&#x60;. Pass it back as &#x60;?cursor&#x3D;&lt;token&gt;&#x60; to fetch the next page; &#x60;null&#x60; means the listing is complete. &#x60;limit&#x60; is clamped to [1, 100] (default 50), never rejected.

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListDrivesRouteV0DrivesGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DrivesApi();

  const body = {
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
    // string (optional)
    authorization: authorization_example,
  } satisfies ListDrivesRouteV0DrivesGetRequest;

  try {
    const data = await api.listDrivesRouteV0DrivesGet(body);
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveList**](DriveList.md)

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


## renameDriveRouteV0DrivesDriveIdPatch

> DriveOut renameDriveRouteV0DrivesDriveIdPatch(driveId, driveRenameIn, authorization)

Rename a drive you own

Rename a drive. **Owner only** — a drive id that isn\&#39;t yours returns 404 (no-leak). Requires a &#x60;full&#x60;-scope user token.

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RenameDriveRouteV0DrivesDriveIdPatchRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DrivesApi();

  const body = {
    // string
    driveId: driveId_example,
    // DriveRenameIn
    driveRenameIn: ...,
    // string (optional)
    authorization: authorization_example,
  } satisfies RenameDriveRouteV0DrivesDriveIdPatchRequest;

  try {
    const data = await api.renameDriveRouteV0DrivesDriveIdPatch(body);
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
| **driveId** | `string` |  | [Defaults to `undefined`] |
| **driveRenameIn** | [DriveRenameIn](DriveRenameIn.md) |  | |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveOut**](DriveOut.md)

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


## revokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePost

> revokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePost(driveId, keyId, authorization)

Revoke a drive API key

Revoke one &#x60;ad_live_&#x60; key of a drive you manage — anything using it loses access immediately. **Manager only** (404 no-leak otherwise), &#x60;full&#x60;-scope user token. Idempotent: revoking an unknown/already-revoked key returns 204 too (no existence oracle).

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RevokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DrivesApi();

  const body = {
    // string
    driveId: driveId_example,
    // string
    keyId: keyId_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies RevokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePostRequest;

  try {
    const data = await api.revokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePost(body);
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
| **driveId** | `string` |  | [Defaults to `undefined`] |
| **keyId** | `string` |  | [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## rotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost

> DriveApiKeyCreateOut rotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost(driveId, keyId, authorization)

Rotate one API key

Rotate a single &#x60;ad_live_&#x60; key: revoke &#x60;key_id&#x60; and mint a replacement that inherits its label. **Only that key** is affected — the drive\&#39;s other keys keep working. **Manager only** (404 no-leak otherwise), &#x60;full&#x60;-scope user token. The new key is returned **once** — store it now. A &#x60;key_id&#x60; that isn\&#39;t a live key of this drive is a 404.

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DrivesApi();

  const body = {
    // string
    driveId: driveId_example,
    // string
    keyId: keyId_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies RotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePostRequest;

  try {
    const data = await api.rotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost(body);
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
| **driveId** | `string` |  | [Defaults to `undefined`] |
| **keyId** | `string` |  | [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveApiKeyCreateOut**](DriveApiKeyCreateOut.md)

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

