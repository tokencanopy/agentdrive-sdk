# \AgentAuthAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ExtensionExchangeV0AuthExtensionExchangePost**](AgentAuthAPI.md#ExtensionExchangeV0AuthExtensionExchangePost) | **Post** /v0/auth/extension/exchange | Redeem an extension OAuth ticket for a JWT pair
[**InitiateClaimAgentIdentityClaimPost**](AgentAuthAPI.md#InitiateClaimAgentIdentityClaimPost) | **Post** /agent/identity/claim | Initiate the human-claim ceremony for an agent identity
[**JwksWellKnownJwksJsonGet**](AgentAuthAPI.md#JwksWellKnownJwksJsonGet) | **Get** /.well-known/jwks.json | JSON Web Key Set — public keys for verifying AgentDrive JWTs
[**Oauth2TokenOauth2TokenPost**](AgentAuthAPI.md#Oauth2TokenOauth2TokenPost) | **Post** /oauth2/token | Exchange a credential for an access_token
[**OauthAuthorizationServerWellKnownOauthAuthorizationServerGet**](AgentAuthAPI.md#OauthAuthorizationServerWellKnownOauthAuthorizationServerGet) | **Get** /.well-known/oauth-authorization-server | Authorization-server metadata (RFC 8414 + auth.md agent_auth block)
[**OauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet**](AgentAuthAPI.md#OauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet) | **Get** /.well-known/oauth-protected-resource/mcp | Protected-resource metadata for the MCP endpoint (RFC 9728 §3.1)
[**OauthProtectedResourceWellKnownOauthProtectedResourceGet**](AgentAuthAPI.md#OauthProtectedResourceWellKnownOauthProtectedResourceGet) | **Get** /.well-known/oauth-protected-resource | Protected-resource metadata (auth.md / RFC 9728-like discovery)
[**RegisterAgentIdentityAgentIdentityPost**](AgentAuthAPI.md#RegisterAgentIdentityAgentIdentityPost) | **Post** /agent/identity | Register an agent identity (anonymous or ID-JAG)



## ExtensionExchangeV0AuthExtensionExchangePost

> ExtensionExchangeResponse ExtensionExchangeV0AuthExtensionExchangePost(ctx).ExtensionExchangeRequest(extensionExchangeRequest).Execute()

Redeem an extension OAuth ticket for a JWT pair



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
	extensionExchangeRequest := *openapiclient.NewExtensionExchangeRequest("ExtId_example", "Ticket_example") // ExtensionExchangeRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentAuthAPI.ExtensionExchangeV0AuthExtensionExchangePost(context.Background()).ExtensionExchangeRequest(extensionExchangeRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentAuthAPI.ExtensionExchangeV0AuthExtensionExchangePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExtensionExchangeV0AuthExtensionExchangePost`: ExtensionExchangeResponse
	fmt.Fprintf(os.Stdout, "Response from `AgentAuthAPI.ExtensionExchangeV0AuthExtensionExchangePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiExtensionExchangeV0AuthExtensionExchangePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extensionExchangeRequest** | [**ExtensionExchangeRequest**](ExtensionExchangeRequest.md) |  | 

### Return type

[**ExtensionExchangeResponse**](ExtensionExchangeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## InitiateClaimAgentIdentityClaimPost

> ClaimInitResponse InitiateClaimAgentIdentityClaimPost(ctx).ClaimInitRequest(claimInitRequest).Execute()

Initiate the human-claim ceremony for an agent identity



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
	claimInitRequest := *openapiclient.NewClaimInitRequest("ClaimToken_example") // ClaimInitRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentAuthAPI.InitiateClaimAgentIdentityClaimPost(context.Background()).ClaimInitRequest(claimInitRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentAuthAPI.InitiateClaimAgentIdentityClaimPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `InitiateClaimAgentIdentityClaimPost`: ClaimInitResponse
	fmt.Fprintf(os.Stdout, "Response from `AgentAuthAPI.InitiateClaimAgentIdentityClaimPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiInitiateClaimAgentIdentityClaimPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **claimInitRequest** | [**ClaimInitRequest**](ClaimInitRequest.md) |  | 

### Return type

[**ClaimInitResponse**](ClaimInitResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## JwksWellKnownJwksJsonGet

> map[string]*interface{} JwksWellKnownJwksJsonGet(ctx).Execute()

JSON Web Key Set — public keys for verifying AgentDrive JWTs



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
	resp, r, err := apiClient.AgentAuthAPI.JwksWellKnownJwksJsonGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentAuthAPI.JwksWellKnownJwksJsonGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `JwksWellKnownJwksJsonGet`: map[string]*interface{}
	fmt.Fprintf(os.Stdout, "Response from `AgentAuthAPI.JwksWellKnownJwksJsonGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiJwksWellKnownJwksJsonGetRequest struct via the builder pattern


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


## Oauth2TokenOauth2TokenPost

> TokenResponse Oauth2TokenOauth2TokenPost(ctx).GrantType(grantType).Assertion(assertion).ClaimToken(claimToken).Execute()

Exchange a credential for an access_token



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
	grantType := "grantType_example" // string | 
	assertion := "assertion_example" // string |  (optional)
	claimToken := "claimToken_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentAuthAPI.Oauth2TokenOauth2TokenPost(context.Background()).GrantType(grantType).Assertion(assertion).ClaimToken(claimToken).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentAuthAPI.Oauth2TokenOauth2TokenPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Oauth2TokenOauth2TokenPost`: TokenResponse
	fmt.Fprintf(os.Stdout, "Response from `AgentAuthAPI.Oauth2TokenOauth2TokenPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiOauth2TokenOauth2TokenPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grantType** | **string** |  | 
 **assertion** | **string** |  | 
 **claimToken** | **string** |  | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## OauthAuthorizationServerWellKnownOauthAuthorizationServerGet

> map[string]*interface{} OauthAuthorizationServerWellKnownOauthAuthorizationServerGet(ctx).Execute()

Authorization-server metadata (RFC 8414 + auth.md agent_auth block)



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
	resp, r, err := apiClient.AgentAuthAPI.OauthAuthorizationServerWellKnownOauthAuthorizationServerGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentAuthAPI.OauthAuthorizationServerWellKnownOauthAuthorizationServerGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `OauthAuthorizationServerWellKnownOauthAuthorizationServerGet`: map[string]*interface{}
	fmt.Fprintf(os.Stdout, "Response from `AgentAuthAPI.OauthAuthorizationServerWellKnownOauthAuthorizationServerGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiOauthAuthorizationServerWellKnownOauthAuthorizationServerGetRequest struct via the builder pattern


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


## OauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet

> map[string]*interface{} OauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet(ctx).Execute()

Protected-resource metadata for the MCP endpoint (RFC 9728 §3.1)



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
	resp, r, err := apiClient.AgentAuthAPI.OauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentAuthAPI.OauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `OauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet`: map[string]*interface{}
	fmt.Fprintf(os.Stdout, "Response from `AgentAuthAPI.OauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiOauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGetRequest struct via the builder pattern


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


## OauthProtectedResourceWellKnownOauthProtectedResourceGet

> map[string]*interface{} OauthProtectedResourceWellKnownOauthProtectedResourceGet(ctx).Execute()

Protected-resource metadata (auth.md / RFC 9728-like discovery)



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
	resp, r, err := apiClient.AgentAuthAPI.OauthProtectedResourceWellKnownOauthProtectedResourceGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentAuthAPI.OauthProtectedResourceWellKnownOauthProtectedResourceGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `OauthProtectedResourceWellKnownOauthProtectedResourceGet`: map[string]*interface{}
	fmt.Fprintf(os.Stdout, "Response from `AgentAuthAPI.OauthProtectedResourceWellKnownOauthProtectedResourceGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiOauthProtectedResourceWellKnownOauthProtectedResourceGetRequest struct via the builder pattern


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


## RegisterAgentIdentityAgentIdentityPost

> AnonymousIdentityResponse RegisterAgentIdentityAgentIdentityPost(ctx).RequestBody(requestBody).Execute()

Register an agent identity (anonymous or ID-JAG)



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
	requestBody := map[string]*interface{}{"key": interface{}(123)} // map[string]*interface{} | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentAuthAPI.RegisterAgentIdentityAgentIdentityPost(context.Background()).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentAuthAPI.RegisterAgentIdentityAgentIdentityPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RegisterAgentIdentityAgentIdentityPost`: AnonymousIdentityResponse
	fmt.Fprintf(os.Stdout, "Response from `AgentAuthAPI.RegisterAgentIdentityAgentIdentityPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRegisterAgentIdentityAgentIdentityPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | **map[string]interface{}** |  | 

### Return type

[**AnonymousIdentityResponse**](AnonymousIdentityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

