# agentdrive_sdk.SharesRedemptionApi

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shares_redeem**](SharesRedemptionApi.md#shares_redeem) | **GET** /s/{share_key} | Redeem Share


# **shares_redeem**
> object shares_redeem(share_key)

Redeem Share

The un-slashed form. Browsers are canonicalized onto `/s/{key}/`.

This keeps the published `shares_redeem` operation id because it remains
the same redemption operation: same URL, JSON `Accept`, byte/JSON result,
and uniform 404. In a split deployment the share host authorizes a
specific non-HTML request and then 308s it to this same path on the
configured public renderer; the renderer (or direct-renderer rollback)
returns the existing result. Dropping the route from the spec would have
described a live operation as gone.

The page links its own sub-resources relatively (`content`), and relative
resolution replaces the last path segment: from `/s/KEY` that reaches
`/s/content`, from `/s/KEY/` it reaches `/s/KEY/content`. The trailing
slash is what makes an image on a share page load at all. Links already in
the wild have no slash, so this redirect is how they keep working.

It is unconditional and runs before any lookup — redirecting only for keys
that resolve would turn the status code into an existence oracle and undo
the anti-enumeration property the rest of this module maintains.

HTML navigation is canonicalized to the trailing-slash form. Non-HTML
clients are answered in place by the renderer/direct rollback, or moved
to the renderer only after the credential resolves on the share host.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://drive.tokencanopy.com
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://drive.tokencanopy.com"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.SharesRedemptionApi(api_client)
    share_key = 'share_key_example' # str | 

    try:
        # Redeem Share
        api_response = api_instance.shares_redeem(share_key)
        print("The response of SharesRedemptionApi->shares_redeem:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesRedemptionApi->shares_redeem: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_key** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

