# DrivesApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**drivesCreate**](DrivesApi.md#drivescreate) | **POST** /v0/drives | Create Drive |
| [**drivesDelete**](DrivesApi.md#drivesdelete) | **DELETE** /v0/drives/{drive_id} | Delete Drive |
| [**drivesList**](DrivesApi.md#driveslist) | **GET** /v0/drives | List Drives |
| [**drivesRead**](DrivesApi.md#drivesread) | **GET** /v0/drives/{drive_id} | Read Drive |
| [**drivesRestore**](DrivesApi.md#drivesrestore) | **POST** /v0/drives/{drive_id}/restore | Restore Drive |
| [**drivesUpdate**](DrivesApi.md#drivesupdate) | **PATCH** /v0/drives/{drive_id} | Update Drive |
| [**drivesUsage**](DrivesApi.md#drivesusage) | **GET** /v0/drives/{drive_id}/usage | Drive Usage |



## drivesCreate

> DriveOut drivesCreate(idempotencyKey, driveCreateIn, authorization)

Create Drive

Create a drive with its structural root folder and creator-manager grant(s) in one transaction; idempotent under the &#x60;&#x60;Idempotency-Key&#x60;&#x60;.

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DrivesCreateRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DrivesApi(config);

  const body = {
    // string
    idempotencyKey: idempotencyKey_example,
    // DriveCreateIn
    driveCreateIn: ...,
    // string (optional)
    authorization: authorization_example,
  } satisfies DrivesCreateRequest;

  try {
    const data = await api.drivesCreate(body);
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
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **driveCreateIn** | [DriveCreateIn](DriveCreateIn.md) |  | |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveOut**](DriveOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | A sibling already occupies the name/path, or the idempotency key was reused for a different request. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match did not match (copy/restore preconditions). |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## drivesDelete

> DriveOut drivesDelete(driveId, idempotencyKey, ifMatch, authorization)

Delete Drive

Soft-delete a drive. Returns 200 with the deleted representation so the client has the post-delete revision/ETag for a restore.

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DrivesDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DrivesApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // string
    ifMatch: ifMatch_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies DrivesDeleteRequest;

  try {
    const data = await api.drivesDelete(body);
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
| **ifMatch** | `string` |  | [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveOut**](DriveOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The mutation conflicts with current state (name/path, lifecycle). |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match did not match the resource\&#39;s current revision. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## drivesList

> DriveListOut drivesList(lifecycle, limit, cursor, authorization)

List Drives

List the actor\&#39;s workspace drives, newest-first (keyset paginated).  &#x60;&#x60;lifecycle&#x60;&#x60; (active|deleted|all) exposes soft-deleted drives so a manager can read the post-delete revision as the If-Match source for a restore. Unknown query parameters are rejected (§6.3).

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DrivesListRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DrivesApi(config);

  const body = {
    // string (optional)
    lifecycle: lifecycle_example,
    // number (optional)
    limit: 56,
    // string (optional)
    cursor: cursor_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies DrivesListRequest;

  try {
    const data = await api.drivesList(body);
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
| **lifecycle** | `string` |  | [Optional] [Defaults to `&#39;active&#39;`] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveListOut**](DriveListOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## drivesRead

> DriveOut drivesRead(driveId, ifNoneMatch, authorization)

Read Drive

Read one active drive. ETag &#x3D; quoted revision; matching &#x60;&#x60;If-None-Match&#x60;&#x60; → 304. Deleted and cross-workspace drives are 404.

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DrivesReadRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DrivesApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string (optional)
    ifNoneMatch: ifNoneMatch_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies DrivesReadRequest;

  try {
    const data = await api.drivesRead(body);
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
| **ifNoneMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveOut**](DriveOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **304** | If-None-Match matched the current ETag. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## drivesRestore

> DriveOut drivesRestore(driveId, idempotencyKey, ifMatch, authorization)

Restore Drive

Restore a soft-deleted drive. If-Match must carry the post-delete revision; restoring an already-active drive is 409 CONFLICT.

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DrivesRestoreRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DrivesApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // string
    ifMatch: ifMatch_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies DrivesRestoreRequest;

  try {
    const data = await api.drivesRestore(body);
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
| **ifMatch** | `string` |  | [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveOut**](DriveOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The mutation conflicts with current state (name/path, lifecycle). |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match did not match the resource\&#39;s current revision. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## drivesUpdate

> DriveOut drivesUpdate(driveId, idempotencyKey, ifMatch, driveUpdateIn, authorization)

Update Drive

Rename / update a drive\&#39;s metadata. Requires &#x60;&#x60;Idempotency-Key&#x60;&#x60; and &#x60;&#x60;If-Match&#x60;&#x60; (428 absent, 412 stale); bumps the revision.

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DrivesUpdateRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DrivesApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // string
    ifMatch: ifMatch_example,
    // DriveUpdateIn
    driveUpdateIn: ...,
    // string (optional)
    authorization: authorization_example,
  } satisfies DrivesUpdateRequest;

  try {
    const data = await api.drivesUpdate(body);
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
| **ifMatch** | `string` |  | [Defaults to `undefined`] |
| **driveUpdateIn** | [DriveUpdateIn](DriveUpdateIn.md) |  | |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveOut**](DriveOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The mutation conflicts with current state (name/path, lifecycle). |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match did not match the resource\&#39;s current revision. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## drivesUsage

> DriveUsageOut drivesUsage(driveId, authorization)

Drive Usage

Byte counters for one active drive: storage is the live sum of its versions\&#39; sizes; retrieval reads the counter the content-read slice maintains (0 until it lands).

### Example

```ts
import {
  Configuration,
  DrivesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DrivesUsageRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DrivesApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies DrivesUsageRequest;

  try {
    const data = await api.drivesUsage(body);
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveUsageOut**](DriveUsageOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
