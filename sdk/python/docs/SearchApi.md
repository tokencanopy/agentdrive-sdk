# agentdrive_sdk.SearchApi

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drive_search**](SearchApi.md#drive_search) | **GET** /v0/drives/{drive_id}/search | Drive Search


# **drive_search**
> SearchPageOut drive_search(drive_id, q, mode=mode, limit=limit, cursor=cursor, parent_id=parent_id, content_type=content_type, label=label, updated_after=updated_after, updated_before=updated_before, authorization=authorization)

Drive Search

Search the drive's live artifacts. ``q`` is required and must be
non-empty.

``mode`` selects the retrieval engine: ``lexical``, ``hybrid``, or
``semantic``. This deployment enables ``lexical`` only; requesting a
disabled mode fails ``400 SEARCH_MODE_UNAVAILABLE``.

Each hit's ``snippet`` is HTML-safe by contract: artifact content is
entity-escaped and only the server's own ``<mark>``/``</mark>`` highlight
pair survives, so a client may render it as HTML.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.search_page_out import SearchPageOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://drive.tokencanopy.com
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://drive.tokencanopy.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.SearchApi(api_client)
    drive_id = 'drive_id_example' # str | 
    q = 'q_example' # str | 
    mode = 'lexical' # str |  (optional) (default to 'lexical')
    limit = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    parent_id = 'parent_id_example' # str |  (optional)
    content_type = 'content_type_example' # str |  (optional)
    label = 'label_example' # str |  (optional)
    updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Drive Search
        api_response = api_instance.drive_search(drive_id, q, mode=mode, limit=limit, cursor=cursor, parent_id=parent_id, content_type=content_type, label=label, updated_after=updated_after, updated_before=updated_before, authorization=authorization)
        print("The response of SearchApi->drive_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->drive_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **q** | **str**|  | 
 **mode** | **str**|  | [optional] [default to &#39;lexical&#39;]
 **limit** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **parent_id** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **label** | **str**|  | [optional] 
 **updated_after** | **datetime**|  | [optional] 
 **updated_before** | **datetime**|  | [optional] 
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional] 

### Return type

[**SearchPageOut**](SearchPageOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Missing or invalid bearer token. |  * X-Request-Id - Request correlation identifier. <br>  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API&#39;s unavailability, not a problem with the presented credential. |  * X-Request-Id - Request correlation identifier. <br>  * Retry-After - Seconds until the caller should retry. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). Requesting a disabled search mode fails with SEARCH_MODE_UNAVAILABLE. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

