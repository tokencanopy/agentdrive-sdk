# GrantsApi

All URIs are relative to *https://drive.tokencanopy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**grantsCreate**](GrantsApi.md#grantscreate) | **POST** /v0/drives/{drive_id}/grants | Create Grant |
| [**grantsList**](GrantsApi.md#grantslist) | **GET** /v0/drives/{drive_id}/grants | List Grants |
| [**grantsRead**](GrantsApi.md#grantsread) | **GET** /v0/drives/{drive_id}/grants/{grant_id} | Read Grant |
| [**grantsRevoke**](GrantsApi.md#grantsrevoke) | **DELETE** /v0/drives/{drive_id}/grants/{grant_id} | Revoke Grant |
| [**grantsUpdate**](GrantsApi.md#grantsupdate) | **PATCH** /v0/drives/{drive_id}/grants/{grant_id} | Update Grant |



## grantsCreate

> GrantOut grantsCreate(driveId, idempotencyKey, grantCreateIn, authorization)

Create Grant

Grant one principal a role on a drive, folder, or artifact.

### Example

```ts
import {
  Configuration,
  GrantsApi,
} from '@tokencanopy/agentdrive-sdk';
import type { GrantsCreateRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GrantsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // GrantCreateIn
    grantCreateIn: ...,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies GrantsCreateRequest;

  try {
    const data = await api.grantsCreate(body);
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
| **grantCreateIn** | [GrantCreateIn](GrantCreateIn.md) |  | |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**GrantOut**](GrantOut.md)

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


## grantsList

> GrantListOut grantsList(driveId, lifecycle, limit, cursor, resourceType, resourceId, principalType, authorization)

List Grants

List explicit grants in the drive, keyset paginated.  **What you see depends on your role (contract change).** A caller holding &#x60;&#x60;manager&#x60;&#x60; on the drive lists EVERY grant in it. Any other caller lists only the grants that name them — their own agent/user rows, &#x60;&#x60;workspace&#x60;&#x60; grants covering them, and &#x60;&#x60;public&#x60;&#x60; grants (which already expose the resource to them anyway). Previously any drive &#x60;&#x60;viewer&#x60;&#x60; could page out every principal id, role and expiry in the drive; that was an access-graph disclosure, not a feature.  The operation is refused (404) only for a caller holding no live grant anywhere in the drive — never for lack of &#x60;&#x60;manager&#x60;&#x60;, because seeing your own access is not a privilege. That admits folder-scoped principals, who previously 404\&#39;d here despite having access to show. A folder &#x60;&#x60;manager&#x60;&#x60; still sees only their own rows, not the roster of the subtree they administer; scoping the listing by per-resource administration authority is a follow-up this change does not claim.  &#x60;&#x60;resource_id&#x60;&#x60; filters to one resource\&#39;s grants and REQUIRES &#x60;&#x60;resource_type&#x60;&#x60; alongside it — a bare resource id is ambiguous across the three resource kinds, and guessing the kind from the id prefix would make the filter\&#39;s meaning depend on an id format the contract does not promise to keep. &#x60;&#x60;resource_type&#x60;&#x60; on its own remains a valid (and pre-existing) filter.

### Example

```ts
import {
  Configuration,
  GrantsApi,
} from '@tokencanopy/agentdrive-sdk';
import type { GrantsListRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GrantsApi(config);

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
    resourceType: resourceType_example,
    // string (optional)
    resourceId: resourceId_example,
    // string (optional)
    principalType: principalType_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies GrantsListRequest;

  try {
    const data = await api.grantsList(body);
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
| **resourceType** | `string` |  | [Optional] [Defaults to `undefined`] |
| **resourceId** | `string` |  | [Optional] [Defaults to `undefined`] |
| **principalType** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**GrantListOut**](GrantListOut.md)

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


## grantsRead

> GrantOut grantsRead(driveId, grantId, ifNoneMatch, authorization)

Read Grant

Read one grant in the drive.

### Example

```ts
import {
  Configuration,
  GrantsApi,
} from '@tokencanopy/agentdrive-sdk';
import type { GrantsReadRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GrantsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    grantId: grantId_example,
    // string (optional)
    ifNoneMatch: ifNoneMatch_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies GrantsReadRequest;

  try {
    const data = await api.grantsRead(body);
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
| **grantId** | `string` |  | [Defaults to `undefined`] |
| **ifNoneMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**GrantOut**](GrantOut.md)

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


## grantsRevoke

> GrantOut grantsRevoke(driveId, grantId, idempotencyKey, ifMatch, authorization)

Revoke Grant

Revoke a grant (soft, sets revoked_at) under If-Match.

### Example

```ts
import {
  Configuration,
  GrantsApi,
} from '@tokencanopy/agentdrive-sdk';
import type { GrantsRevokeRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GrantsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    grantId: grantId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // string
    ifMatch: ifMatch_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies GrantsRevokeRequest;

  try {
    const data = await api.grantsRevoke(body);
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
| **grantId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**GrantOut**](GrantOut.md)

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


## grantsUpdate

> GrantOut grantsUpdate(driveId, grantId, idempotencyKey, ifMatch, grantUpdateIn, authorization)

Update Grant

Change a grant\&#39;s role or expiry under If-Match.

### Example

```ts
import {
  Configuration,
  GrantsApi,
} from '@tokencanopy/agentdrive-sdk';
import type { GrantsUpdateRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new GrantsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    grantId: grantId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // string
    ifMatch: ifMatch_example,
    // GrantUpdateIn
    grantUpdateIn: ...,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies GrantsUpdateRequest;

  try {
    const data = await api.grantsUpdate(body);
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
| **grantId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Defaults to `undefined`] |
| **grantUpdateIn** | [GrantUpdateIn](GrantUpdateIn.md) |  | |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**GrantOut**](GrantOut.md)

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

