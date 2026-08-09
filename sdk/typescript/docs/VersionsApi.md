# VersionsApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**versionsAppend**](VersionsApi.md#versionsappend) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions | Append Version |
| [**versionsContent**](VersionsApi.md#versionscontent) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/content | Read Version Content |
| [**versionsList**](VersionsApi.md#versionslist) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions | List Versions |
| [**versionsRead**](VersionsApi.md#versionsread) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id} | Read Version |
| [**versionsRestore**](VersionsApi.md#versionsrestore) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/restore | Restore Version |



## versionsAppend

> VersionCreatedOut versionsAppend(driveId, artifactId, idempotencyKey, ifMatch, content, authorization, contentType, sha256)

Append Version

Append one immutable version and rotate the artifact head.  Multipart only (415 for a JSON body). Parts: content (bytes), content_type, sha256. content is required; name, parent_id, and metadata are not accepted here.

### Example

```ts
import {
  Configuration,
  VersionsApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { VersionsAppendRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new VersionsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    artifactId: artifactId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // string
    ifMatch: ifMatch_example,
    // Blob | The artifact bytes.
    content: BINARY_DATA_HERE,
    // string (optional)
    authorization: authorization_example,
    // string | Declared media type. (optional)
    contentType: contentType_example,
    // string | Optional content sha256 for verification. (optional)
    sha256: sha256_example,
  } satisfies VersionsAppendRequest;

  try {
    const data = await api.versionsAppend(body);
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
| **artifactId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Defaults to `undefined`] |
| **content** | `Blob` | The artifact bytes. | [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |
| **contentType** | `string` | Declared media type. | [Optional] [Defaults to `undefined`] |
| **sha256** | `string` | Optional content sha256 for verification. | [Optional] [Defaults to `undefined`] |

### Return type

[**VersionCreatedOut**](VersionCreatedOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
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


## versionsContent

> Blob versionsContent(driveId, artifactId, versionId, ifNoneMatch, authorization)

Read Version Content

Download one version\&#39;s immutable bytes — stream or 307.

### Example

```ts
import {
  Configuration,
  VersionsApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { VersionsContentRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new VersionsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    artifactId: artifactId_example,
    // string
    versionId: versionId_example,
    // string (optional)
    ifNoneMatch: ifNoneMatch_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies VersionsContentRequest;

  try {
    const data = await api.versionsContent(body);
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
| **artifactId** | `string` |  | [Defaults to `undefined`] |
| **versionId** | `string` |  | [Defaults to `undefined`] |
| **ifNoneMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**Blob**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/octet-stream`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Raw artifact bytes (streamed). |  * X-Request-Id - Request correlation identifier. <br>  |
| **304** | If-None-Match matched the current ETag. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **307** | Redirect to a short-lived signed URL. |  * Location - Redirect target. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## versionsList

> VersionListOut versionsList(driveId, artifactId, limit, cursor, authorization)

List Versions

List the artifact\&#39;s version trail, newest first (ordinal DESC).

### Example

```ts
import {
  Configuration,
  VersionsApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { VersionsListRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new VersionsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    artifactId: artifactId_example,
    // number (optional)
    limit: 56,
    // string (optional)
    cursor: cursor_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies VersionsListRequest;

  try {
    const data = await api.versionsList(body);
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
| **artifactId** | `string` |  | [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**VersionListOut**](VersionListOut.md)

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


## versionsRead

> VersionOut versionsRead(driveId, artifactId, versionId, ifNoneMatch, authorization)

Read Version

Read one immutable version.

### Example

```ts
import {
  Configuration,
  VersionsApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { VersionsReadRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new VersionsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    artifactId: artifactId_example,
    // string
    versionId: versionId_example,
    // string (optional)
    ifNoneMatch: ifNoneMatch_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies VersionsReadRequest;

  try {
    const data = await api.versionsRead(body);
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
| **artifactId** | `string` |  | [Defaults to `undefined`] |
| **versionId** | `string` |  | [Defaults to `undefined`] |
| **ifNoneMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**VersionOut**](VersionOut.md)

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


## versionsRestore

> VersionCreatedOut versionsRestore(driveId, artifactId, versionId, idempotencyKey, ifMatch, authorization)

Restore Version

Restore a historical version as a NEW head version (no byte copy).

### Example

```ts
import {
  Configuration,
  VersionsApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { VersionsRestoreRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new VersionsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    artifactId: artifactId_example,
    // string
    versionId: versionId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // string
    ifMatch: ifMatch_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies VersionsRestoreRequest;

  try {
    const data = await api.versionsRestore(body);
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
| **artifactId** | `string` |  | [Defaults to `undefined`] |
| **versionId** | `string` |  | [Defaults to `undefined`] |
| **idempotencyKey** | `string` |  | [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**VersionCreatedOut**](VersionCreatedOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
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
