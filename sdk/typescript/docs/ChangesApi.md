# ChangesApi

All URIs are relative to *https://drive.tokencanopy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changesList**](ChangesApi.md#changeslist) | **GET** /v0/drives/{drive_id}/changes | List Changes |



## changesList

> ChangePageOut changesList(driveId, limit, start, cursor, type, authorization)

List Changes

Pull one page of changes. Exactly one of &#x60;&#x60;start&#x60;&#x60; or &#x60;&#x60;cursor&#x60;&#x60;.  &#x60;&#x60;type&#x60;&#x60; is an optional comma-separated allow-list of exact event-type strings (e.g. &#x60;&#x60;type&#x3D;folder.created,artifact.updated&#x60;&#x60; for content only, or &#x60;&#x60;type&#x3D;grant.created,grant.updated,grant.revoked&#x60;&#x60; for grant events). A comma-list — not a single value or a &#x60;&#x60;grant.*&#x60;&#x60; glob — because the useful sync queries (\&quot;content only\&quot;, \&quot;all permission events\&quot;) are SETS of exact types, and exact-match keeps the filter\&#39;s meaning independent of the dotted naming (§6.3: unknown params are rejected; unknown type VALUES 400 here). Permission types requested by a non-manager are silently empty (the manager filter still applies), never an existence oracle.

### Example

```ts
import {
  Configuration,
  ChangesApi,
} from '@tokencanopy/agentdrive-sdk';
import type { ChangesListRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
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
    type: type_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
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
| **type** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

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
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
| **410** | The change cursor is older than retained history. Recover with a full sync: capture start&#x3D;now, enumerate current resources, then replay from the captured cursor. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
| **403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API\&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
| **400** | Malformed request (invalid query parameter, cursor, or argument). Pass exactly one of start or cursor (INVALID_REQUEST); a cursor not issued for this drive fails with INVALID_CURSOR. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

