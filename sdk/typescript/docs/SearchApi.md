# SearchApi

All URIs are relative to *https://drive.tokencanopy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**driveSearch**](SearchApi.md#drivesearch) | **GET** /v0/drives/{drive_id}/search | Drive Search |



## driveSearch

> SearchPageOut driveSearch(driveId, q, mode, limit, cursor, parentId, contentType, label, updatedAfter, updatedBefore, authorization)

Drive Search

Search the drive\&#39;s live artifacts. &#x60;&#x60;q&#x60;&#x60; is required and must be non-empty.  &#x60;&#x60;mode&#x60;&#x60; selects the retrieval engine: &#x60;&#x60;lexical&#x60;&#x60;, &#x60;&#x60;hybrid&#x60;&#x60;, or &#x60;&#x60;semantic&#x60;&#x60;. This deployment enables &#x60;&#x60;lexical&#x60;&#x60; only; requesting a disabled mode fails &#x60;&#x60;400 SEARCH_MODE_UNAVAILABLE&#x60;&#x60;.  Each hit\&#39;s &#x60;&#x60;snippet&#x60;&#x60; is HTML-safe by contract: artifact content is entity-escaped and only the server\&#39;s own &#x60;&#x60;&lt;mark&gt;&#x60;&#x60;/&#x60;&#x60;&lt;/mark&gt;&#x60;&#x60; highlight pair survives, so a client may render it as HTML.

### Example

```ts
import {
  Configuration,
  SearchApi,
} from '@tokencanopy/agentdrive-sdk';
import type { DriveSearchRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SearchApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    q: q_example,
    // 'lexical' | 'hybrid' | 'semantic' (optional)
    mode: mode_example,
    // number (optional)
    limit: 56,
    // string (optional)
    cursor: cursor_example,
    // string (optional)
    parentId: parentId_example,
    // string (optional)
    contentType: contentType_example,
    // string (optional)
    label: label_example,
    // Date (optional)
    updatedAfter: 2013-10-20T19:20:30+01:00,
    // Date (optional)
    updatedBefore: 2013-10-20T19:20:30+01:00,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies DriveSearchRequest;

  try {
    const data = await api.driveSearch(body);
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
| **q** | `string` |  | [Defaults to `undefined`] |
| **mode** | `lexical`, `hybrid`, `semantic` |  | [Optional] [Defaults to `&#39;lexical&#39;`] [Enum: lexical, hybrid, semantic] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **parentId** | `string` |  | [Optional] [Defaults to `undefined`] |
| **contentType** | `string` |  | [Optional] [Defaults to `undefined`] |
| **label** | `string` |  | [Optional] [Defaults to `undefined`] |
| **updatedAfter** | `Date` |  | [Optional] [Defaults to `undefined`] |
| **updatedBefore** | `Date` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**SearchPageOut**](SearchPageOut.md)

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
| **400** | Malformed request (invalid query parameter, cursor, or argument). Requesting a disabled search mode fails with SEARCH_MODE_UNAVAILABLE. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

