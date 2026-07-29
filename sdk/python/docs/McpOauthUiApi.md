# agentdrive_sdk.McpOauthUiApi

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_decision_oauth2_authorize_post**](McpOauthUiApi.md#authorize_decision_oauth2_authorize_post) | **POST** /oauth2/authorize | Authorize Decision
[**authorize_page_oauth2_authorize_get**](McpOauthUiApi.md#authorize_page_oauth2_authorize_get) | **GET** /oauth2/authorize | Authorize Page


# **authorize_decision_oauth2_authorize_post**
> authorize_decision_oauth2_authorize_post(csrf)

Authorize Decision

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.McpOauthUiApi(api_client)
    csrf = 'csrf_example' # str |

    try:
        # Authorize Decision
        api_instance.authorize_decision_oauth2_authorize_post(csrf)
    except Exception as e:
        print("Exception when calling McpOauthUiApi->authorize_decision_oauth2_authorize_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the canonical or authentication URL. |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**303** | Continue after the form submission at the redirect target. |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The authorization decision or request is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The selected drive is unavailable or the browser CSRF check failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Authorization rate limit exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_page_oauth2_authorize_get**
> str authorize_page_oauth2_authorize_get()

Authorize Page

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.McpOauthUiApi(api_client)

    try:
        # Authorize Page
        api_response = api_instance.authorize_page_oauth2_authorize_get()
        print("The response of McpOauthUiApi->authorize_page_oauth2_authorize_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling McpOauthUiApi->authorize_page_oauth2_authorize_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**302** | Redirect to the canonical or authentication URL. |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The authorization request is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Authorization rate limit exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
