# agentdrive_sdk.DownloadsApi

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_capabilities_create**](DownloadsApi.md#download_capabilities_create) | **POST** /v0/drives/{drive_id}/download-capabilities | Create Download Capability


# **download_capabilities_create**
> DownloadCapabilityOut download_capabilities_create(drive_id, download_capabilities_create_request, authorization=authorization)

Create Download Capability

Mint one fresh, generation-pinned signed GET target for the current
artifact head or one owned version. 200 only; every call reauthorizes
and re-mints.

Strict JSON body (charset utf-8): unknown/duplicate fields, unknown discriminators, and malformed ids are 400 INVALID_REQUEST. Idempotency-Key is FORBIDDEN on this operation (manifest idempotency_class: forbidden): a supplied key is rejected with 400 INVALID_REQUEST and no idempotency record is created — every request reauthorizes and mints a fresh signed target. The signed URL is a bearer capability after disclosure: it is bucket/object-, generation-, method-, semantic-query-, and expiry-bound only (no one-time-use or audience enforcement).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.download_capabilities_create_request import DownloadCapabilitiesCreateRequest
from agentdrive_sdk.models.download_capability_out import DownloadCapabilityOut
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
    api_instance = agentdrive_sdk.DownloadsApi(api_client)
    drive_id = 'drive_id_example' # str |
    download_capabilities_create_request = agentdrive_sdk.DownloadCapabilitiesCreateRequest() # DownloadCapabilitiesCreateRequest |
    authorization = 'authorization_example' # str | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

    try:
        # Create Download Capability
        api_response = api_instance.download_capabilities_create(drive_id, download_capabilities_create_request, authorization=authorization)
        print("The response of DownloadsApi->download_capabilities_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DownloadsApi->download_capabilities_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |
 **download_capabilities_create_request** | [**DownloadCapabilitiesCreateRequest**](DownloadCapabilitiesCreateRequest.md)|  |
 **authorization** | **str**| Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | [optional]

### Return type

[**DownloadCapabilityOut**](DownloadCapabilityOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * Cache-Control - Always no-store. <br>  * Referrer-Policy - Always no-referrer. <br>  * X-Content-Type-Options - Always nosniff — governs THIS JSON response only, never the later GCS response. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | Malformed request (invalid query parameter, cursor, or argument). |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Missing or invalid bearer token. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | Token lacks a required scope. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The parent or target resource was not found or is not visible. |  * X-Request-Id - Request correlation identifier. <br>  |
**406** | Accept does not admit application/json (NOT_ACCEPTABLE). |  * X-Request-Id - Request correlation identifier. <br>  |
**415** | The mint body must be application/json (UNSUPPORTED_MEDIA_TYPE). |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Rate limited. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**503** | Direct transfer is not fully configured/enabled (TRANSFER_DISABLED) or the direct download signer/configuration is unavailable (DOWNLOAD_SIGNING_UNAVAILABLE) — fail closed, no redirect/stream/viewer fallback, and no retry hint of their own (B8 owns retry policy). Retry-After appears only on the generic auth-unavailability 503. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
