# \McpOauthAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Oauth2RegisterOauth2RegisterPost**](McpOauthAPI.md#Oauth2RegisterOauth2RegisterPost) | **Post** /oauth2/register | Dynamic Client Registration (RFC 7591)
[**Oauth2RevokeOauth2RevokePost**](McpOauthAPI.md#Oauth2RevokeOauth2RevokePost) | **Post** /oauth2/revoke | Token revocation (RFC 7009)



## Oauth2RegisterOauth2RegisterPost

> ClientRegistrationOut Oauth2RegisterOauth2RegisterPost(ctx).Execute()

Dynamic Client Registration (RFC 7591)



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
	resp, r, err := apiClient.McpOauthAPI.Oauth2RegisterOauth2RegisterPost(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `McpOauthAPI.Oauth2RegisterOauth2RegisterPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Oauth2RegisterOauth2RegisterPost`: ClientRegistrationOut
	fmt.Fprintf(os.Stdout, "Response from `McpOauthAPI.Oauth2RegisterOauth2RegisterPost`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiOauth2RegisterOauth2RegisterPostRequest struct via the builder pattern


### Return type

[**ClientRegistrationOut**](ClientRegistrationOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Oauth2RevokeOauth2RevokePost

> map[string]interface{} Oauth2RevokeOauth2RevokePost(ctx).Execute()

Token revocation (RFC 7009)



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
	resp, r, err := apiClient.McpOauthAPI.Oauth2RevokeOauth2RevokePost(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `McpOauthAPI.Oauth2RevokeOauth2RevokePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Oauth2RevokeOauth2RevokePost`: map[string]interface{}
	fmt.Fprintf(os.Stdout, "Response from `McpOauthAPI.Oauth2RevokeOauth2RevokePost`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiOauth2RevokeOauth2RevokePostRequest struct via the builder pattern


### Return type

**map[string]interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
