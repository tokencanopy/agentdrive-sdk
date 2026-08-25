# ViewerSessionsApi

All URIs are relative to *https://drive.tokencanopy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**viewerSessionsCreate**](ViewerSessionsApi.md#viewersessionscreate) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/viewer-sessions | Create Viewer Session |



## viewerSessionsCreate

> ViewerSessionCreateOut viewerSessionsCreate(driveId, artifactId, idempotencyKey, viewerSessionCreateIn, authorization)

Create Viewer Session

Mint a viewer session pinned to one immutable version. The response carries the plaintext credential — the only response that does — and is never cacheable.

### Example

```ts
import {
  Configuration,
  ViewerSessionsApi,
} from '@tokencanopy/agentdrive-sdk';
import type { ViewerSessionsCreateRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ViewerSessionsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    artifactId: artifactId_example,
    // string
    idempotencyKey: idempotencyKey_example,
    // ViewerSessionCreateIn
    viewerSessionCreateIn: ...,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies ViewerSessionsCreateRequest;

  try {
    const data = await api.viewerSessionsCreate(body);
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
| **viewerSessionCreateIn** | [ViewerSessionCreateIn](ViewerSessionCreateIn.md) |  | |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**ViewerSessionCreateOut**](ViewerSessionCreateOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | A sibling already occupies the name/path, or the idempotency key was reused for a different request. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match did not match (copy/restore preconditions). |  * X-Request-Id - Request correlation identifier. <br>  |
| **428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | The private viewer is not enabled on this deployment (VIEWER_DISABLED — fail closed, no fallback, and no Retry-After: operator enablement has no honest client retry time), or token verification is temporarily unavailable (the generic auth-unavailability 503, which does carry Retry-After). |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

