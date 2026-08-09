# SharesRedemptionApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharesRedeem**](SharesRedemptionApi.md#sharesredeem) | **GET** /s/{share_key} | Redeem Share |



## sharesRedeem

> any sharesRedeem(shareKey)

Redeem Share

The un-slashed form. Browsers are canonicalized onto &#x60;/s/{key}/&#x60;.  This inherits the published &#x60;shares_redeem&#x60; operation id from the route it replaced, because for an API client it *is* that operation, unchanged: same URL, same JSON &#x60;Accept&#x60;, same bytes, same uniform 404. Only the browser arm is new. Dropping it from the spec would have described the route as gone while it kept answering.  The page links its own sub-resources relatively (&#x60;content&#x60;), and relative resolution replaces the last path segment: from &#x60;/s/KEY&#x60; that reaches &#x60;/s/content&#x60;, from &#x60;/s/KEY/&#x60; it reaches &#x60;/s/KEY/content&#x60;. The trailing slash is what makes an image on a share page load at all. Links already in the wild have no slash, so this redirect is how they keep working.  It is unconditional and runs before any lookup — redirecting only for keys that resolve would turn the status code into an existence oracle and undo the anti-enumeration property the rest of this module maintains.  Only browsers are moved. JSON and byte clients are answered in place, so the shipped v0 contract for this URL is unchanged, redirect included.

### Example

```ts
import {
  Configuration,
  SharesRedemptionApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { SharesRedeemRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new SharesRedemptionApi();

  const body = {
    // string
    shareKey: shareKey_example,
  } satisfies SharesRedeemRequest;

  try {
    const data = await api.sharesRedeem(body);
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
| **shareKey** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
