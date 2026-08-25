# agentdrive_sdk.DefaultApi

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health**](DefaultApi.md#health) | **GET** /health | Health


# **health**
> HealthOut health()

Health

Liveness + DB-reachability probe. Used by Cloud Run / k8s healthchecks
and any uptime monitor. Returns 200 only if the DB pool can serve a
trivial query; 503 otherwise so the orchestrator can pull the instance
out of rotation.

NOTE: route is `/health`, NOT `/healthz`. Google's edge infrastructure
intercepts `/healthz` (legacy kubernetes-reserved path) and returns a
generic 404 before traffic reaches Cloud Run — discovered the hard way
during the first prod deploy. Don't rename back.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.health_out import HealthOut
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
    api_instance = agentdrive_sdk.DefaultApi(api_client)

    try:
        # Health
        api_response = api_instance.health()
        print("The response of DefaultApi->health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthOut**](HealthOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**503** | The database reachability probe failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

