# TokensApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listTokensV0TokensGet**](TokensApi.md#listtokensv0tokensget) | **GET** /v0/tokens | List your user-identity tokens |
| [**revokeTokenV0TokensTokenIdRevokePost**](TokensApi.md#revoketokenv0tokenstokenidrevokepost) | **POST** /v0/tokens/{token_id}/revoke | Revoke one of your user-identity tokens |



## listTokensV0TokensGet

> UserTokenList listTokensV0TokensGet(cursor, limit)

List your user-identity tokens

List the &#x60;ad_user_&#x60; tokens belonging to the authenticated user. Metadata only — the raw token is shown once at mint (web only) and is never returned here. Includes recently-revoked tokens (with &#x60;revoked_at&#x60; set) so the caller can audit them; newest first.  **Cursor pagination:** when more results exist, the response carries &#x60;next_cursor&#x60;. Pass it back as &#x60;?cursor&#x3D;&lt;token&gt;&#x60; to fetch the next page; &#x60;null&#x60; means the listing is complete. &#x60;limit&#x60; is clamped to [1, 100] (default 50), never rejected.

### Example

```ts
import {
  Configuration,
  TokensApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListTokensV0TokensGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TokensApi(config);

  const body = {
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
  } satisfies ListTokensV0TokensGetRequest;

  try {
    const data = await api.listTokensV0TokensGet(body);
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
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**UserTokenList**](UserTokenList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## revokeTokenV0TokensTokenIdRevokePost

> UserTokenOut revokeTokenV0TokensTokenIdRevokePost(tokenId)

Revoke one of your user-identity tokens

Revoke a single &#x60;ad_user_&#x60; token by id. Scoped to the authenticated user: a token id that isn\&#39;t yours returns 404 (no-leak). Idempotent — revoking an already-revoked token also returns 404 (it is no longer a live token of yours to revoke). On success the revoked token\&#39;s metadata is returned with &#x60;revoked_at&#x60; set.

### Example

```ts
import {
  Configuration,
  TokensApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RevokeTokenV0TokensTokenIdRevokePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new TokensApi(config);

  const body = {
    // string
    tokenId: tokenId_example,
  } satisfies RevokeTokenV0TokensTokenIdRevokePostRequest;

  try {
    const data = await api.revokeTokenV0TokensTokenIdRevokePost(body);
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
| **tokenId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**UserTokenOut**](UserTokenOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The token does not exist for this user. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
