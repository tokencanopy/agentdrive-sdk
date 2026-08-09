# \GrantsAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GrantsCreate**](GrantsAPI.md#GrantsCreate) | **Post** /v0/drives/{drive_id}/grants | Create Grant
[**GrantsList**](GrantsAPI.md#GrantsList) | **Get** /v0/drives/{drive_id}/grants | List Grants
[**GrantsRead**](GrantsAPI.md#GrantsRead) | **Get** /v0/drives/{drive_id}/grants/{grant_id} | Read Grant
[**GrantsRevoke**](GrantsAPI.md#GrantsRevoke) | **Delete** /v0/drives/{drive_id}/grants/{grant_id} | Revoke Grant
[**GrantsUpdate**](GrantsAPI.md#GrantsUpdate) | **Patch** /v0/drives/{drive_id}/grants/{grant_id} | Update Grant



## GrantsCreate

> GrantOut GrantsCreate(ctx, driveId).IdempotencyKey(idempotencyKey).GrantCreateIn(grantCreateIn).Authorization(authorization).Execute()

Create Grant



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
	driveId := "driveId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	grantCreateIn := *openapiclient.NewGrantCreateIn("PrincipalType_example", "ResourceId_example", "ResourceType_example", "Role_example") // GrantCreateIn |
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GrantsAPI.GrantsCreate(context.Background(), driveId).IdempotencyKey(idempotencyKey).GrantCreateIn(grantCreateIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GrantsAPI.GrantsCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GrantsCreate`: GrantOut
	fmt.Fprintf(os.Stdout, "Response from `GrantsAPI.GrantsCreate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGrantsCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** |  |
 **grantCreateIn** | [**GrantCreateIn**](GrantCreateIn.md) |  |
 **authorization** | **string** |  |

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GrantsList

> GrantListOut GrantsList(ctx, driveId).Lifecycle(lifecycle).Limit(limit).Cursor(cursor).ResourceType(resourceType).ResourceId(resourceId).PrincipalType(principalType).Authorization(authorization).Execute()

List Grants



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
	driveId := "driveId_example" // string |
	lifecycle := "lifecycle_example" // string |  (optional) (default to "active")
	limit := int32(56) // int32 |  (optional)
	cursor := "cursor_example" // string |  (optional)
	resourceType := "resourceType_example" // string |  (optional)
	resourceId := "resourceId_example" // string |  (optional)
	principalType := "principalType_example" // string |  (optional)
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GrantsAPI.GrantsList(context.Background(), driveId).Lifecycle(lifecycle).Limit(limit).Cursor(cursor).ResourceType(resourceType).ResourceId(resourceId).PrincipalType(principalType).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GrantsAPI.GrantsList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GrantsList`: GrantListOut
	fmt.Fprintf(os.Stdout, "Response from `GrantsAPI.GrantsList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGrantsListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **lifecycle** | **string** |  | [default to &quot;active&quot;]
 **limit** | **int32** |  |
 **cursor** | **string** |  |
 **resourceType** | **string** |  |
 **resourceId** | **string** |  |
 **principalType** | **string** |  |
 **authorization** | **string** |  |

### Return type

[**GrantListOut**](GrantListOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GrantsRead

> GrantOut GrantsRead(ctx, driveId, grantId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Read Grant



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
	driveId := "driveId_example" // string |
	grantId := "grantId_example" // string |
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GrantsAPI.GrantsRead(context.Background(), driveId, grantId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GrantsAPI.GrantsRead``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GrantsRead`: GrantOut
	fmt.Fprintf(os.Stdout, "Response from `GrantsAPI.GrantsRead`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**grantId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGrantsReadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **ifNoneMatch** | **string** |  |
 **authorization** | **string** |  |

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GrantsRevoke

> GrantOut GrantsRevoke(ctx, driveId, grantId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()

Revoke Grant



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
	driveId := "driveId_example" // string |
	grantId := "grantId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	ifMatch := "ifMatch_example" // string |
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GrantsAPI.GrantsRevoke(context.Background(), driveId, grantId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GrantsAPI.GrantsRevoke``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GrantsRevoke`: GrantOut
	fmt.Fprintf(os.Stdout, "Response from `GrantsAPI.GrantsRevoke`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**grantId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGrantsRevokeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **ifMatch** | **string** |  |
 **authorization** | **string** |  |

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GrantsUpdate

> GrantOut GrantsUpdate(ctx, driveId, grantId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).GrantUpdateIn(grantUpdateIn).Authorization(authorization).Execute()

Update Grant



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
	driveId := "driveId_example" // string |
	grantId := "grantId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	ifMatch := "ifMatch_example" // string |
	grantUpdateIn := *openapiclient.NewGrantUpdateIn() // GrantUpdateIn |
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.GrantsAPI.GrantsUpdate(context.Background(), driveId, grantId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).GrantUpdateIn(grantUpdateIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `GrantsAPI.GrantsUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GrantsUpdate`: GrantOut
	fmt.Fprintf(os.Stdout, "Response from `GrantsAPI.GrantsUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**grantId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGrantsUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **ifMatch** | **string** |  |
 **grantUpdateIn** | [**GrantUpdateIn**](GrantUpdateIn.md) |  |
 **authorization** | **string** |  |

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
