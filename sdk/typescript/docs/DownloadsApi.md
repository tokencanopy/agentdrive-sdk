# DownloadsApi

All URIs are relative to *https://drive.tokencanopy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadCapabilitiesCreate**](DownloadsApi.md#downloadcapabilitiescreateoperation) | **POST** /v0/drives/{drive_id}/download-capabilities | Create Download Capability |



## downloadCapabilitiesCreate

> DownloadCapabilityOut downloadCapabilitiesCreate(driveId, downloadCapabilitiesCreateRequest, authorization)

Create Download Capability

Mint one fresh, generation-pinned signed GET target for the current artifact head or one owned version. 200 only; every call reauthorizes and re-mints.  Strict JSON body (charset utf-8): unknown/duplicate fields, unknown discriminators, and malformed ids are 400 INVALID_REQUEST. Idempotency-Key is FORBIDDEN on this operation (manifest idempotency_class: forbidden): a supplied key is rejected with 400 INVALID_REQUEST and no idempotency record is created — every request reauthorizes and mints a fresh signed target. The signed URL is a bearer capability after disclosure: it is bucket/object-, generation-, method-, semantic-query-, and expiry-bound only (no one-time-use or audience enforcement).

### Example

```ts
import {
  Configuration,
  DownloadsApi,
} from '@tokencanopy/agentdrive-sdk';
import type { DownloadCapabilitiesCreateOperationRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DownloadsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // DownloadCapabilitiesCreateRequest
    downloadCapabilitiesCreateRequest: ...,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies DownloadCapabilitiesCreateOperationRequest;

  try {
    const data = await api.downloadCapabilitiesCreate(body);
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
| **downloadCapabilitiesCreateRequest** | [DownloadCapabilitiesCreateRequest](DownloadCapabilitiesCreateRequest.md) |  | |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**DownloadCapabilityOut**](DownloadCapabilityOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * Cache-Control - Always no-store. <br>  * Referrer-Policy - Always no-referrer. <br>  * X-Content-Type-Options - Always nosniff — governs THIS JSON response only, never the later GCS response. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
| **406** | Accept does not admit application/json (NOT_ACCEPTABLE). |  * X-Request-Id - Request correlation identifier. <br>  |
| **415** | The mint body must be application/json (UNSUPPORTED_MEDIA_TYPE). |  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Direct transfer is not fully configured/enabled (TRANSFER_DISABLED) or the direct download signer/configuration is unavailable (DOWNLOAD_SIGNING_UNAVAILABLE) — fail closed, no redirect/stream/viewer fallback, and no retry hint of their own (B8 owns retry policy). Retry-After appears only on the generic auth-unavailability 503. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

