# \TokensAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ListTokensV0TokensGet**](TokensAPI.md#ListTokensV0TokensGet) | **Get** /v0/tokens | List your user-identity tokens
[**RevokeTokenV0TokensTokenIdRevokePost**](TokensAPI.md#RevokeTokenV0TokensTokenIdRevokePost) | **Post** /v0/tokens/{token_id}/revoke | Revoke one of your user-identity tokens



## ListTokensV0TokensGet

> UserTokenList ListTokensV0TokensGet(ctx).Cursor(cursor).Limit(limit).Execute()

List your user-identity tokens



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
	cursor := "cursor_example" // string |  (optional)
	limit := int32(56) // int32 |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TokensAPI.ListTokensV0TokensGet(context.Background()).Cursor(cursor).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TokensAPI.ListTokensV0TokensGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListTokensV0TokensGet`: UserTokenList
	fmt.Fprintf(os.Stdout, "Response from `TokensAPI.ListTokensV0TokensGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListTokensV0TokensGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **string** |  |
 **limit** | **int32** |  |

### Return type

[**UserTokenList**](UserTokenList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RevokeTokenV0TokensTokenIdRevokePost

> UserTokenOut RevokeTokenV0TokensTokenIdRevokePost(ctx, tokenId).Execute()

Revoke one of your user-identity tokens



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
	tokenId := "tokenId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TokensAPI.RevokeTokenV0TokensTokenIdRevokePost(context.Background(), tokenId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TokensAPI.RevokeTokenV0TokensTokenIdRevokePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RevokeTokenV0TokensTokenIdRevokePost`: UserTokenOut
	fmt.Fprintf(os.Stdout, "Response from `TokensAPI.RevokeTokenV0TokensTokenIdRevokePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**tokenId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiRevokeTokenV0TokensTokenIdRevokePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**UserTokenOut**](UserTokenOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
