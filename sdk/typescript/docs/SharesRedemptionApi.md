# SharesRedemptionApi

All URIs are relative to *https://drive.tokencanopy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharesRedeem**](SharesRedemptionApi.md#sharesredeem) | **GET** /s/{share_key} | Redeem Share |



## sharesRedeem

> any sharesRedeem(shareKey)

Redeem Share

The un-slashed form. Browsers are canonicalized onto &#x60;/s/{key}/&#x60;.  This keeps the published &#x60;shares_redeem&#x60; operation id because it remains the same redemption operation: same URL, JSON &#x60;Accept&#x60;, byte/JSON result, and uniform 404. In a split deployment the share host authorizes a specific non-HTML request and then 308s it to this same path on the configured public renderer; the renderer (or direct-renderer rollback) returns the existing result. Dropping the route from the spec would have described a live operation as gone.  The page links its own sub-resources relatively (&#x60;content&#x60;), and relative resolution replaces the last path segment: from &#x60;/s/KEY&#x60; that reaches &#x60;/s/content&#x60;, from &#x60;/s/KEY/&#x60; it reaches &#x60;/s/KEY/content&#x60;. The trailing slash is what makes an image on a share page load at all. Links already in the wild have no slash, so this redirect is how they keep working.  It is unconditional and runs before any lookup — redirecting only for keys that resolve would turn the status code into an existence oracle and undo the anti-enumeration property the rest of this module maintains.  HTML navigation is canonicalized to the trailing-slash form. Non-HTML clients are answered in place by the renderer/direct rollback, or moved to the renderer only after the credential resolves on the share host.

### Example

```ts
import {
  Configuration,
  SharesRedemptionApi,
} from '@tokencanopy/agentdrive-sdk';
import type { SharesRedeemRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
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

