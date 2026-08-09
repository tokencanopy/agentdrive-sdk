# \SharesAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**SharesCreate**](SharesAPI.md#SharesCreate) | **Post** /v0/drives/{drive_id}/shares | Create Share
[**SharesList**](SharesAPI.md#SharesList) | **Get** /v0/drives/{drive_id}/shares | List Shares
[**SharesRead**](SharesAPI.md#SharesRead) | **Get** /v0/drives/{drive_id}/shares/{share_id} | Read Share
[**SharesRevoke**](SharesAPI.md#SharesRevoke) | **Delete** /v0/drives/{drive_id}/shares/{share_id} | Revoke Share
[**SharesRotate**](SharesAPI.md#SharesRotate) | **Post** /v0/drives/{drive_id}/shares/{share_id}/rotate | Rotate Share



## SharesCreate

> ShareCreateOut SharesCreate(ctx, driveId).IdempotencyKey(idempotencyKey).ShareCreateIn(shareCreateIn).Authorization(authorization).Execute()

Create Share



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
	shareCreateIn := *openapiclient.NewShareCreateIn("ResourceId_example", "ResourceType_example") // ShareCreateIn |
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SharesAPI.SharesCreate(context.Background(), driveId).IdempotencyKey(idempotencyKey).ShareCreateIn(shareCreateIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SharesAPI.SharesCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SharesCreate`: ShareCreateOut
	fmt.Fprintf(os.Stdout, "Response from `SharesAPI.SharesCreate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSharesCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** |  |
 **shareCreateIn** | [**ShareCreateIn**](ShareCreateIn.md) |  |
 **authorization** | **string** |  |

### Return type

[**ShareCreateOut**](ShareCreateOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SharesList

> ShareListOut SharesList(ctx, driveId).Lifecycle(lifecycle).Limit(limit).Cursor(cursor).ResourceType(resourceType).ResourceId(resourceId).Authorization(authorization).Execute()

List Shares



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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SharesAPI.SharesList(context.Background(), driveId).Lifecycle(lifecycle).Limit(limit).Cursor(cursor).ResourceType(resourceType).ResourceId(resourceId).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SharesAPI.SharesList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SharesList`: ShareListOut
	fmt.Fprintf(os.Stdout, "Response from `SharesAPI.SharesList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSharesListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **lifecycle** | **string** |  | [default to &quot;active&quot;]
 **limit** | **int32** |  |
 **cursor** | **string** |  |
 **resourceType** | **string** |  |
 **resourceId** | **string** |  |
 **authorization** | **string** |  |

### Return type

[**ShareListOut**](ShareListOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SharesRead

> ShareOut SharesRead(ctx, driveId, shareId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Read Share



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
	shareId := "shareId_example" // string |
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SharesAPI.SharesRead(context.Background(), driveId, shareId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SharesAPI.SharesRead``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SharesRead`: ShareOut
	fmt.Fprintf(os.Stdout, "Response from `SharesAPI.SharesRead`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**shareId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSharesReadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **ifNoneMatch** | **string** |  |
 **authorization** | **string** |  |

### Return type

[**ShareOut**](ShareOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SharesRevoke

> ShareOut SharesRevoke(ctx, driveId, shareId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()

Revoke Share



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
	shareId := "shareId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	ifMatch := "ifMatch_example" // string |
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SharesAPI.SharesRevoke(context.Background(), driveId, shareId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SharesAPI.SharesRevoke``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SharesRevoke`: ShareOut
	fmt.Fprintf(os.Stdout, "Response from `SharesAPI.SharesRevoke`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**shareId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSharesRevokeRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **ifMatch** | **string** |  |
 **authorization** | **string** |  |

### Return type

[**ShareOut**](ShareOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SharesRotate

> ShareCreateOut SharesRotate(ctx, driveId, shareId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()

Rotate Share



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
	shareId := "shareId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	ifMatch := "ifMatch_example" // string |
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SharesAPI.SharesRotate(context.Background(), driveId, shareId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SharesAPI.SharesRotate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SharesRotate`: ShareCreateOut
	fmt.Fprintf(os.Stdout, "Response from `SharesAPI.SharesRotate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**shareId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSharesRotateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **ifMatch** | **string** |  |
 **authorization** | **string** |  |

### Return type

[**ShareCreateOut**](ShareCreateOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
