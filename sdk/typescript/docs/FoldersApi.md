# FoldersApi

All URIs are relative to *https://drive.tokencanopy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**foldersCopy**](FoldersApi.md#folderscopy) | **POST** /v0/drives/{drive_id}/folders/{folder_id}/copy | Copy Folder |
| [**foldersCreate**](FoldersApi.md#folderscreate) | **POST** /v0/drives/{drive_id}/folders | Create Folder |
| [**foldersDelete**](FoldersApi.md#foldersdelete) | **DELETE** /v0/drives/{drive_id}/folders/{folder_id} | Delete Folder |
| [**foldersList**](FoldersApi.md#folderslist) | **GET** /v0/drives/{drive_id}/folders | List Folders |
| [**foldersRead**](FoldersApi.md#foldersread) | **GET** /v0/drives/{drive_id}/folders/{folder_id} | Read Folder |
| [**foldersRestore**](FoldersApi.md#foldersrestore) | **POST** /v0/drives/{drive_id}/folders/{folder_id}/restore | Restore Folder |
| [**foldersUpdate**](FoldersApi.md#foldersupdate) | **PATCH** /v0/drives/{drive_id}/folders/{folder_id} | Update Folder |



## foldersCopy

> FolderOut foldersCopy(driveId, folderId, idempotencyKey, folderCopyIn, ifMatch, authorization)

Copy Folder

Copy a folder\&#39;s subtree within the same drive.  Cross-drive copy is out of v0 scope and rejected (400 INVALID_ARGUMENT). &#x60;&#x60;destination_drive_id&#x60;&#x60; must equal the source drive when present. Materializes the subtree synchronously → 201 + the copied folder. The source root, descendant folders, and artifacts may total at most 5,000 live resources; larger copies fail with 409 SUBTREE_TOO_LARGE. &#x60;&#x60;If-Match&#x60;&#x60; is optional; when present it is validated against the source revision (412 stale).

### Example

```ts
import {
  Configuration,
  FoldersApi,
} from '@tokencanopy/agentdrive-sdk';
import type { FoldersCopyRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FoldersApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    folderId: folderId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // FolderCopyIn
    folderCopyIn: ...,
    // string (optional)
    ifMatch: ifMatch_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies FoldersCopyRequest;

  try {
    const data = await api.foldersCopy(body);
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
| **folderId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **folderCopyIn** | [FolderCopyIn](FolderCopyIn.md) |  | |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | A sibling already occupies the name/path, or the idempotency key was reused for a different request. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match did not match (copy/restore preconditions). |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## foldersCreate

> FolderOut foldersCreate(driveId, idempotencyKey, folderCreateIn, authorization)

Create Folder

Create one folder under &#x60;parent_id&#x60;; idempotent under the &#x60;&#x60;Idempotency-Key&#x60;&#x60;.

### Example

```ts
import {
  Configuration,
  FoldersApi,
} from '@tokencanopy/agentdrive-sdk';
import type { FoldersCreateRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FoldersApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // FolderCreateIn
    folderCreateIn: ...,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies FoldersCreateRequest;

  try {
    const data = await api.foldersCreate(body);
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
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **folderCreateIn** | [FolderCreateIn](FolderCreateIn.md) |  | |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | A sibling already occupies the name/path, or the idempotency key was reused for a different request. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match did not match (copy/restore preconditions). |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## foldersDelete

> FolderCascadeOut foldersDelete(driveId, folderId, idempotencyKey, ifMatch, recursive, authorization)

Delete Folder

Soft-delete a folder and its full live subtree (folders + artifacts) in one transaction. A non-empty subtree requires &#x60;&#x60;recursive&#x3D;true&#x60;&#x60; (409 FOLDER_RECURSIVE_REQUIRED otherwise). Returns the deleted root representation plus exact cascade counts and the post-delete revision/ETag for a restore.

### Example

```ts
import {
  Configuration,
  FoldersApi,
} from '@tokencanopy/agentdrive-sdk';
import type { FoldersDeleteRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FoldersApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    folderId: folderId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // string
    ifMatch: ifMatch_example,
    // boolean (optional)
    recursive: true,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies FoldersDeleteRequest;

  try {
    const data = await api.foldersDelete(body);
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
| **folderId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Defaults to `undefined`] |
| **recursive** | `boolean` |  | [Optional] [Defaults to `false`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderCascadeOut**](FolderCascadeOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The mutation conflicts with current state (name/path, lifecycle). |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match did not match the resource\&#39;s current revision. |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## foldersList

> FolderListOut foldersList(driveId, lifecycle, limit, cursor, parentId, name, authorization)

List Folders

List the drive\&#39;s folders, newest-first (keyset paginated).  &#x60;&#x60;lifecycle&#x60;&#x60; (active|deleted|all) exposes soft-deleted folders so the post-delete revision can be read as the If-Match source for a restore. &#x60;&#x60;parent_id&#x60;&#x60; / &#x60;&#x60;name&#x60;&#x60; are exact-match filters. Unknown query parameters are rejected (§6.3).

### Example

```ts
import {
  Configuration,
  FoldersApi,
} from '@tokencanopy/agentdrive-sdk';
import type { FoldersListRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FoldersApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string (optional)
    lifecycle: lifecycle_example,
    // number (optional)
    limit: 56,
    // string (optional)
    cursor: cursor_example,
    // string (optional)
    parentId: parentId_example,
    // string (optional)
    name: name_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies FoldersListRequest;

  try {
    const data = await api.foldersList(body);
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
| **lifecycle** | `string` |  | [Optional] [Defaults to `&#39;active&#39;`] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **parentId** | `string` |  | [Optional] [Defaults to `undefined`] |
| **name** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderListOut**](FolderListOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## foldersRead

> FolderOut foldersRead(driveId, folderId, ifNoneMatch, authorization)

Read Folder

Read one active folder. ETag &#x3D; quoted revision; matching &#x60;&#x60;If-None-Match&#x60;&#x60; → 304. Deleted and cross-workspace folders are 404.

### Example

```ts
import {
  Configuration,
  FoldersApi,
} from '@tokencanopy/agentdrive-sdk';
import type { FoldersReadRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FoldersApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    folderId: folderId_example,
    // string (optional)
    ifNoneMatch: ifNoneMatch_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies FoldersReadRequest;

  try {
    const data = await api.foldersRead(body);
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
| **folderId** | `string` |  | [Defaults to `undefined`] |
| **ifNoneMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **304** | If-None-Match matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## foldersRestore

> FolderCascadeOut foldersRestore(driveId, folderId, idempotencyKey, ifMatch, authorization)

Restore Folder

Restore a soft-deleted folder and its deleted subtree atomically. If-Match must carry the post-delete revision; restoring an already-active folder is 409 CONFLICT.

### Example

```ts
import {
  Configuration,
  FoldersApi,
} from '@tokencanopy/agentdrive-sdk';
import type { FoldersRestoreRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FoldersApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    folderId: folderId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // string
    ifMatch: ifMatch_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies FoldersRestoreRequest;

  try {
    const data = await api.foldersRestore(body);
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
| **folderId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderCascadeOut**](FolderCascadeOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The mutation conflicts with current state (name/path, lifecycle). |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match did not match the resource\&#39;s current revision. |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## foldersUpdate

> FolderOut foldersUpdate(driveId, folderId, idempotencyKey, ifMatch, folderUpdateIn, authorization)

Update Folder

Rename / move / update a folder\&#39;s metadata. Requires &#x60;&#x60;Idempotency-Key&#x60;&#x60; and &#x60;&#x60;If-Match&#x60;&#x60; (428 absent, 412 stale); bumps the revision.

### Example

```ts
import {
  Configuration,
  FoldersApi,
} from '@tokencanopy/agentdrive-sdk';
import type { FoldersUpdateRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new FoldersApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    folderId: folderId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // string
    ifMatch: ifMatch_example,
    // FolderUpdateIn
    folderUpdateIn: ...,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies FoldersUpdateRequest;

  try {
    const data = await api.foldersUpdate(body);
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
| **folderId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Defaults to `undefined`] |
| **folderUpdateIn** | [FolderUpdateIn](FolderUpdateIn.md) |  | |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The mutation conflicts with current state (name/path, lifecycle). |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match did not match the resource\&#39;s current revision. |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

