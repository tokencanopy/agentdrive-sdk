# \McpOauthUiAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AuthorizeDecisionOauth2AuthorizePost**](McpOauthUiAPI.md#AuthorizeDecisionOauth2AuthorizePost) | **Post** /oauth2/authorize | Authorize Decision
[**AuthorizePageOauth2AuthorizeGet**](McpOauthUiAPI.md#AuthorizePageOauth2AuthorizeGet) | **Get** /oauth2/authorize | Authorize Page



## AuthorizeDecisionOauth2AuthorizePost

> AuthorizeDecisionOauth2AuthorizePost(ctx).Csrf(csrf).Execute()

Authorize Decision

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
	csrf := "csrf_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.McpOauthUiAPI.AuthorizeDecisionOauth2AuthorizePost(context.Background()).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `McpOauthUiAPI.AuthorizeDecisionOauth2AuthorizePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAuthorizeDecisionOauth2AuthorizePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **string** |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AuthorizePageOauth2AuthorizeGet

> string AuthorizePageOauth2AuthorizeGet(ctx).Execute()

Authorize Page

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
	resp, r, err := apiClient.McpOauthUiAPI.AuthorizePageOauth2AuthorizeGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `McpOauthUiAPI.AuthorizePageOauth2AuthorizeGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AuthorizePageOauth2AuthorizeGet`: string
	fmt.Fprintf(os.Stdout, "Response from `McpOauthUiAPI.AuthorizePageOauth2AuthorizeGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiAuthorizePageOauth2AuthorizeGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
