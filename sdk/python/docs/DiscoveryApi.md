# agentdrive_sdk.DiscoveryApi

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_protected_resource**](DiscoveryApi.md#oauth_protected_resource) | **GET** /.well-known/oauth-protected-resource | Protected-resource metadata (RFC 9728)


# **oauth_protected_resource**
> Dict[str, Optional[object]] oauth_protected_resource()

Protected-resource metadata (RFC 9728)

Names the reset v0 surface as a protected resource and points clients at Hub — the only authorization server whose product tokens this deployment accepts.

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
    api_instance = agentdrive_sdk.DiscoveryApi(api_client)

    try:
        # Protected-resource metadata (RFC 9728)
        api_response = api_instance.oauth_protected_resource()
        print("The response of DiscoveryApi->oauth_protected_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->oauth_protected_resource: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, Optional[object]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

