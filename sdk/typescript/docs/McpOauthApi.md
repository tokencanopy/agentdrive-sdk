# McpOauthApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oauth2RegisterOauth2RegisterPost**](McpOauthApi.md#oauth2registeroauth2registerpost) | **POST** /oauth2/register | Dynamic Client Registration (RFC 7591) |
| [**oauth2RevokeOauth2RevokePost**](McpOauthApi.md#oauth2revokeoauth2revokepost) | **POST** /oauth2/revoke | Token revocation (RFC 7009) |



## oauth2RegisterOauth2RegisterPost

> ClientRegistrationOut oauth2RegisterOauth2RegisterPost()

Dynamic Client Registration (RFC 7591)

Anonymous registration endpoint for MCP clients. Public clients only (PKCE, no client_secret). Returns the registered metadata plus the assigned &#x60;client_id&#x60;. Registration grants nothing by itself — every token still requires a user consent ceremony at /oauth2/authorize.

### Example

```ts
import {
  Configuration,
  McpOauthApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { Oauth2RegisterOauth2RegisterPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new McpOauthApi();

  try {
    const data = await api.oauth2RegisterOauth2RegisterPost();
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

[**ClientRegistrationOut**](ClientRegistrationOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | Invalid client metadata. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Registration rate limit exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## oauth2RevokeOauth2RevokePost

> object oauth2RevokeOauth2RevokePost()

Token revocation (RFC 7009)

Revokes an &#x60;adat_&#x60; access token (that token only) or an &#x60;adrt_&#x60; refresh token (the whole rotation chain). Unknown tokens return 200 per RFC 7009 §2.2 — existence is not revealed. Public-client endpoint auth (&#x60;client_id&#x60; form param, no secret).

### Example

```ts
import {
  Configuration,
  McpOauthApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { Oauth2RevokeOauth2RevokePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new McpOauthApi();

  try {
    const data = await api.oauth2RevokeOauth2RevokePost();
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

**object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | Invalid revocation request. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Client authentication failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | Token type is unsupported. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Revocation rate limit exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
