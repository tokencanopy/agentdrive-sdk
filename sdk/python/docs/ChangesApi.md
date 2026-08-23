# agentdrive_sdk.ChangesApi

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changes_list**](ChangesApi.md#changes_list) | **GET** /v0/drives/{drive_id}/changes | List Changes


# **changes_list**
> ChangePageOut changes_list(drive_id, limit=limit, start=start, cursor=cursor, type=type, authorization=authorization)

List Changes

Pull one page of changes. Exactly one of ``start`` or ``cursor``.

``type`` is an optional comma-separated allow-list of exact event-type
strings (e.g. ``type=folder.created,artifact.updated`` for content only, or
``type=grant.created,grant.updated,grant.revoked`` for grant events). A
comma-list — not a single value or a ``grant.*`` glob — because the useful
sync queries ("content only", "all permission events") are SETS of exact
types, and exact-match keeps the filter's meaning independent of the dotted
naming (§6.3: unknown params are rejected; unknown type VALUES 400 here).
Permission types requested by a non-manager are silently empty (the
manager filter still applies), never an existence oracle.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.change_page_out import ChangePageOut
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
    api_instance = agentdrive_sdk.ChangesApi(api_client)
    drive_id = 'drive_id_example' # str |
    limit = 56 # int |  (optional)
    start = 'start_example' # str |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # List Changes
        api_response = api_instance.changes_list(drive_id, limit=limit, start=start, cursor=cursor, type=type, authorization=authorization)
        print("The response of ChangesApi->changes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChangesApi->changes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |
 **limit** | **int**|  | [optional]
 **start** | **str**|  | [optional]
 **cursor** | **str**|  | [optional]
 **type** | **str**|  | [optional]
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional]

### Return type

[**ChangePageOut**](ChangePageOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). Pass exactly one of start or cursor (INVALID_REQUEST); a cursor not issued for this drive fails with INVALID_CURSOR. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Missing or invalid bearer token. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The resource was not found or is not visible to the caller. |  * X-Request-Id - Request correlation identifier. <br>  |
**410** | The change cursor is older than retained history. Recover with a full sync: capture start&#x3D;now, enumerate current resources, then replay from the captured cursor. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**503** | Token verification is temporarily unavailable (the Hub JWKS could not be fetched). This is the API&#39;s unavailability, not a problem with the presented credential. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
