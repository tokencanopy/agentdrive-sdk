# agentdrive_sdk.ViewerSessionsApi

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**viewer_sessions_create**](ViewerSessionsApi.md#viewer_sessions_create) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/viewer-sessions | Create Viewer Session


# **viewer_sessions_create**
> ViewerSessionCreateOut viewer_sessions_create(drive_id, artifact_id, idempotency_key, viewer_session_create_in, authorization=authorization)

Create Viewer Session

Mint a viewer session pinned to one immutable version. The response
carries the plaintext credential — the only response that does — and is
never cacheable.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.viewer_session_create_in import ViewerSessionCreateIn
from agentdrive_sdk.models.viewer_session_create_out import ViewerSessionCreateOut
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
    api_instance = agentdrive_sdk.ViewerSessionsApi(api_client)
    drive_id = 'drive_id_example' # str |
    artifact_id = 'artifact_id_example' # str |
    idempotency_key = 'idempotency_key_example' # str |
    viewer_session_create_in = agentdrive_sdk.ViewerSessionCreateIn() # ViewerSessionCreateIn |
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Create Viewer Session
        api_response = api_instance.viewer_sessions_create(drive_id, artifact_id, idempotency_key, viewer_session_create_in, authorization=authorization)
        print("The response of ViewerSessionsApi->viewer_sessions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewerSessionsApi->viewer_sessions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |
 **artifact_id** | **str**|  |
 **idempotency_key** | **str**|  |
 **viewer_session_create_in** | [**ViewerSessionCreateIn**](ViewerSessionCreateIn.md)|  |
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional]

### Return type

[**ViewerSessionCreateOut**](ViewerSessionCreateOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Missing or invalid bearer token. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | A sibling already occupies the name/path, or the idempotency key was reused for a different request. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | If-Match did not match (copy/restore preconditions). |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**428** | If-Match is required for this mutation. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**503** | The private viewer is not enabled on this deployment (VIEWER_DISABLED — fail closed, no fallback, and no Retry-After: operator enablement has no honest client retry time), or token verification is temporarily unavailable (the generic auth-unavailability 503, which does carry Retry-After). |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
