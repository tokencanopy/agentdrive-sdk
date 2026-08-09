# ChangesApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changesList**](ChangesApi.md#changeslist) | **GET** /v0/drives/{drive_id}/changes | List Changes |



## changesList

> ChangePageOut changesList(driveId, limit, start, cursor, authorization)

List Changes

Pull one page of changes. Exactly one of &#x60;&#x60;start&#x60;&#x60; or &#x60;&#x60;cursor&#x60;&#x60;.

### Example

```ts
import {
  Configuration,
  ChangesApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ChangesListRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ChangesApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // number (optional)
    limit: 56,
    // 'now' | 'beginning' (optional)
    start: start_example,
    // string (optional)
    cursor: cursor_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies ChangesListRequest;

  try {
    const data = await api.changesList(body);
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
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |
| **start** | `now`, `beginning` |  | [Optional] [Defaults to `undefined`] [Enum: now, beginning] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ChangePageOut**](ChangePageOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). Pass exactly one of start or cursor (INVALID_REQUEST); a cursor not issued for this drive fails with INVALID_CURSOR. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **410** | The change cursor is older than retained history. Recover with a full sync: capture start&#x3D;now, enumerate current resources, then replay from the captured cursor. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
