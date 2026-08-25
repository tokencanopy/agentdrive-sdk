# UploadsApi

All URIs are relative to *https://drive.tokencanopy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**uploadsComplete**](UploadsApi.md#uploadscomplete) | **POST** /v0/drives/{drive_id}/uploads/{upload_id}/complete | Complete Upload |
| [**uploadsCreate**](UploadsApi.md#uploadscreateoperation) | **POST** /v0/drives/{drive_id}/uploads | Begin Upload |
| [**uploadsDelete**](UploadsApi.md#uploadsdelete) | **DELETE** /v0/drives/{drive_id}/uploads/{upload_id} | Cancel Upload |
| [**uploadsRead**](UploadsApi.md#uploadsread) | **GET** /v0/drives/{drive_id}/uploads/{upload_id} | Read Upload |



## uploadsComplete

> UploadSessionOut uploadsComplete(driveId, uploadId, idempotencyKey, authorization)

Complete Upload

Adopt the finalized scratch object and publish exactly one immutable artifact/version (§5.5/§6). Empty body; If-Match is not accepted — the version precondition was captured at begin, and the transition fence plus idempotency serializes the session itself.

### Example

```ts
import {
  Configuration,
  UploadsApi,
} from '@tokencanopy/agentdrive-sdk';
import type { UploadsCompleteRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new UploadsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    uploadId: uploadId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies UploadsCompleteRequest;

  try {
    const data = await api.uploadsComplete(body);
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
| **uploadId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**UploadSessionOut**](UploadSessionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  |
| **200** | Idempotent replay of completion. |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | A sibling already occupies the name/path, or the idempotency key was reused for a different request. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match did not match (copy/restore preconditions). |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **406** | Accept does not admit application/json (NOT_ACCEPTABLE) — every upload-control response is JSON. |  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Direct transfer is not fully configured/enabled (TRANSFER_DISABLED, no Retry-After), or the provider is transiently unavailable (TRANSFER_UNAVAILABLE, with Retry-After). |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## uploadsCreate

> UploadSessionOut uploadsCreate(driveId, idempotencyKey, uploadsCreateRequest, ifMatch, authorization)

Begin Upload

Begin one direct-upload session; the 201 response carries the one external GCS XML resumable target, disclosed exactly once.  Strict JSON body (charset utf-8): unknown/duplicate fields, unknown discriminators, non-canonical CRC32C, and malformed ids are 400 INVALID_REQUEST. An artifact target takes NO If-Match (400 if sent); a version target REQUIRES If-Match carrying the artifact head ETag (428 absent, 412 stale) — the revision is captured for completion-time enforcement.

### Example

```ts
import {
  Configuration,
  UploadsApi,
} from '@tokencanopy/agentdrive-sdk';
import type { UploadsCreateOperationRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new UploadsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // UploadsCreateRequest
    uploadsCreateRequest: ...,
    // string (optional)
    ifMatch: ifMatch_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies UploadsCreateOperationRequest;

  try {
    const data = await api.uploadsCreate(body);
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
| **uploadsCreateRequest** | [UploadsCreateRequest](UploadsCreateRequest.md) |  | |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**UploadSessionOut**](UploadSessionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  |
| **200** | Idempotent replay without transfer target. |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | A sibling already occupies the name/path, or the idempotency key was reused for a different request. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match did not match (copy/restore preconditions). |  * X-Request-Id - Request correlation identifier. <br>  * ETag - Current strong entity tag. <br>  |
| **428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **406** | Accept does not admit application/json (NOT_ACCEPTABLE) — every upload-control response is JSON. |  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Direct transfer is not fully configured/enabled (TRANSFER_DISABLED, no Retry-After), or the provider is transiently unavailable (TRANSFER_UNAVAILABLE, with Retry-After). |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **413** | The declared size exceeds the enabled direct-transfer ceiling (PAYLOAD_TOO_LARGE), or the control body exceeds its bound. |  * X-Request-Id - Request correlation identifier. <br>  |
| **415** | The begin body must be application/json (UNSUPPORTED_MEDIA_TYPE). |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## uploadsDelete

> UploadSessionOut uploadsDelete(driveId, uploadId, idempotencyKey, ifMatch, authorization)

Cancel Upload

Close publication permanently and release the reservation exactly once (§5.4); cleanup continues independently.  If-Match must carry THE session\&#39;s current strong ETag: \&#39;*\&#39; and multi-member lists cannot pin a revision and are 400 INVALID_REQUEST; a weak or foreign tag is 412. The exact same-key idempotent replay is exempt from the If-Match requirement (it reauthorizes and returns the stored 200).

### Example

```ts
import {
  Configuration,
  UploadsApi,
} from '@tokencanopy/agentdrive-sdk';
import type { UploadsDeleteRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new UploadsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    uploadId: uploadId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // string
    ifMatch: ifMatch_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies UploadsDeleteRequest;

  try {
    const data = await api.uploadsDelete(body);
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
| **uploadId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**UploadSessionOut**](UploadSessionOut.md)

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
| **406** | Accept does not admit application/json (NOT_ACCEPTABLE) — every upload-control response is JSON. |  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Direct transfer is not fully configured/enabled (TRANSFER_DISABLED, no Retry-After), or the provider is transiently unavailable (TRANSFER_UNAVAILABLE, with Retry-After). |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## uploadsRead

> UploadSessionOut uploadsRead(driveId, uploadId, ifNoneMatch, authorization)

Read Upload

Non-secret recovery state (§5.3). Never a target, coordinate, principal, reservation, continuation, or provider diagnostic.  Idempotency-Key is not part of this read\&#39;s contract (manifest idempotency_class: not_required): a supplied key plays no role and creates no idempotency record.

### Example

```ts
import {
  Configuration,
  UploadsApi,
} from '@tokencanopy/agentdrive-sdk';
import type { UploadsReadRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new UploadsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    uploadId: uploadId_example,
    // string (optional)
    ifNoneMatch: ifNoneMatch_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies UploadsReadRequest;

  try {
    const data = await api.uploadsRead(body);
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
| **uploadId** | `string` |  | [Defaults to `undefined`] |
| **ifNoneMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**UploadSessionOut**](UploadSessionOut.md)

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
| **406** | Accept does not admit application/json (NOT_ACCEPTABLE) — every upload-control response is JSON. |  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Direct transfer is not fully configured/enabled (TRANSFER_DISABLED, no Retry-After), or the provider is transiently unavailable (TRANSFER_UNAVAILABLE, with Retry-After). |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

