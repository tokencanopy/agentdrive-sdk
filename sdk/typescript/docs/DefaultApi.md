# DefaultApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**health**](DefaultApi.md#health) | **GET** /health | Health |



## health

> HealthOut health()

Health

Liveness + DB-reachability probe. Used by Cloud Run / k8s healthchecks and any uptime monitor. Returns 200 only if the DB pool can serve a trivial query; 503 otherwise so the orchestrator can pull the instance out of rotation.  NOTE: route is &#x60;/health&#x60;, NOT &#x60;/healthz&#x60;. Google\&#39;s edge infrastructure intercepts &#x60;/healthz&#x60; (legacy kubernetes-reserved path) and returns a generic 404 before traffic reaches Cloud Run — discovered the hard way during the first prod deploy. Don\&#39;t rename back.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { HealthRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.health();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthOut**](HealthOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **503** | The database reachability probe failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
