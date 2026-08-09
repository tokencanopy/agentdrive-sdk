# \DiscoveryAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**OauthProtectedResource**](DiscoveryAPI.md#OauthProtectedResource) | **Get** /.well-known/oauth-protected-resource | Protected-resource metadata (RFC 9728)



## OauthProtectedResource

> map[string]*interface{} OauthProtectedResource(ctx).Execute()

Protected-resource metadata (RFC 9728)



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Mnexa-AI/agentdrive-sdk/agentdrive"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DiscoveryAPI.OauthProtectedResource(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DiscoveryAPI.OauthProtectedResource``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `OauthProtectedResource`: map[string]*interface{}
	fmt.Fprintf(os.Stdout, "Response from `DiscoveryAPI.OauthProtectedResource`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiOauthProtectedResourceRequest struct via the builder pattern


### Return type

**map[string]*interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
