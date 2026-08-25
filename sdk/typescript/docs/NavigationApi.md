# NavigationApi

All URIs are relative to *https://drive.tokencanopy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**entriesList**](NavigationApi.md#entrieslist) | **GET** /v0/drives/{drive_id}/entries | List Entries |
| [**lookup**](NavigationApi.md#lookup) | **GET** /v0/drives/{drive_id}/lookup | Lookup |



## entriesList

> EntryListOut entriesList(driveId, parentId, type, name, label, contentType, updatedAfter, updatedBefore, state, limit, cursor, authorization)

List Entries

List one folder\&#39;s direct children across the shared namespace.

### Example

```ts
import {
  Configuration,
  NavigationApi,
} from '@tokencanopy/agentdrive-sdk';
import type { EntriesListRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new NavigationApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    parentId: parentId_example,
    // string (optional)
    type: type_example,
    // string (optional)
    name: name_example,
    // string (optional)
    label: label_example,
    // string (optional)
    contentType: contentType_example,
    // Date (optional)
    updatedAfter: 2013-10-20T19:20:30+01:00,
    // Date (optional)
    updatedBefore: 2013-10-20T19:20:30+01:00,
    // string (optional)
    state: state_example,
    // number (optional)
    limit: 56,
    // string (optional)
    cursor: cursor_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies EntriesListRequest;

  try {
    const data = await api.entriesList(body);
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
| **parentId** | `string` |  | [Defaults to `undefined`] |
| **type** | `string` |  | [Optional] [Defaults to `undefined`] |
| **name** | `string` |  | [Optional] [Defaults to `undefined`] |
| **label** | `string` |  | [Optional] [Defaults to `undefined`] |
| **contentType** | `string` |  | [Optional] [Defaults to `undefined`] |
| **updatedAfter** | `Date` |  | [Optional] [Defaults to `undefined`] |
| **updatedBefore** | `Date` |  | [Optional] [Defaults to `undefined`] |
| **state** | `string` |  | [Optional] [Defaults to `&#39;active&#39;`] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**EntryListOut**](EntryListOut.md)

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


## lookup

> LookupOut lookup(driveId, path, type, authorization)

Lookup

Resolve a complete root-relative path to one stable resource id.

### Example

```ts
import {
  Configuration,
  NavigationApi,
} from '@tokencanopy/agentdrive-sdk';
import type { LookupRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new NavigationApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    path: path_example,
    // string (optional)
    type: type_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies LookupRequest;

  try {
    const data = await api.lookup(body);
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
| **path** | `string` |  | [Defaults to `undefined`] |
| **type** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` | Deprecated: redundant with the operation\&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [Optional] [Defaults to `undefined`] |

### Return type

[**LookupOut**](LookupOut.md)

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

