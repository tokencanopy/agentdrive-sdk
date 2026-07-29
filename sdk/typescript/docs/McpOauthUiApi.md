# McpOauthUiApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authorizeDecisionOauth2AuthorizePost**](McpOauthUiApi.md#authorizedecisionoauth2authorizepost) | **POST** /oauth2/authorize | Authorize Decision |
| [**authorizePageOauth2AuthorizeGet**](McpOauthUiApi.md#authorizepageoauth2authorizeget) | **GET** /oauth2/authorize | Authorize Page |



## authorizeDecisionOauth2AuthorizePost

> authorizeDecisionOauth2AuthorizePost(csrf)

Authorize Decision

### Example

```ts
import {
  Configuration,
  McpOauthUiApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { AuthorizeDecisionOauth2AuthorizePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new McpOauthUiApi();

  const body = {
    // string
    csrf: csrf_example,
  } satisfies AuthorizeDecisionOauth2AuthorizePostRequest;

  try {
    const data = await api.authorizeDecisionOauth2AuthorizePost(body);
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
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Redirect to the canonical or authentication URL. |  * Location - Redirect target. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **303** | Continue after the form submission at the redirect target. |  * Location - Redirect target. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The authorization decision or request is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The selected drive is unavailable or the browser CSRF check failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Authorization rate limit exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## authorizePageOauth2AuthorizeGet

> string authorizePageOauth2AuthorizeGet()

Authorize Page

### Example

```ts
import {
  Configuration,
  McpOauthUiApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { AuthorizePageOauth2AuthorizeGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new McpOauthUiApi();

  try {
    const data = await api.authorizePageOauth2AuthorizeGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **302** | Redirect to the canonical or authentication URL. |  * Location - Redirect target. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The authorization request is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Authorization rate limit exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
