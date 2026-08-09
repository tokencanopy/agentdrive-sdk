# DiscoveryApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oauthProtectedResource**](DiscoveryApi.md#oauthprotectedresource) | **GET** /.well-known/oauth-protected-resource | Protected-resource metadata (RFC 9728) |



## oauthProtectedResource

> { [key: string]: any | null; } oauthProtectedResource()

Protected-resource metadata (RFC 9728)

Names the reset v0 surface as a protected resource and points clients at Hub — the only authorization server whose product tokens this deployment accepts.

### Example

```ts
import {
  Configuration,
  DiscoveryApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { OauthProtectedResourceRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DiscoveryApi();

  try {
    const data = await api.oauthProtectedResource();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**{ [key: string]: any | null; }**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
