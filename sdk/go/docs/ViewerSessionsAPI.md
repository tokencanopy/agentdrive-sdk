# \ViewerSessionsAPI

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ViewerSessionsCreate**](ViewerSessionsAPI.md#ViewerSessionsCreate) | **Post** /v0/drives/{drive_id}/artifacts/{artifact_id}/viewer-sessions | Create Viewer Session



## ViewerSessionsCreate

> ViewerSessionCreateOut ViewerSessionsCreate(ctx, driveId, artifactId).IdempotencyKey(idempotencyKey).ViewerSessionCreateIn(viewerSessionCreateIn).Authorization(authorization).Execute()

Create Viewer Session



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/tokencanopy/agentdrive-sdk/agentdrive"
)

func main() {
	driveId := "driveId_example" // string |
	artifactId := "artifactId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	viewerSessionCreateIn := *openapiclient.NewViewerSessionCreateIn() // ViewerSessionCreateIn |
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ViewerSessionsAPI.ViewerSessionsCreate(context.Background(), driveId, artifactId).IdempotencyKey(idempotencyKey).ViewerSessionCreateIn(viewerSessionCreateIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ViewerSessionsAPI.ViewerSessionsCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ViewerSessionsCreate`: ViewerSessionCreateOut
	fmt.Fprintf(os.Stdout, "Response from `ViewerSessionsAPI.ViewerSessionsCreate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiViewerSessionsCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **viewerSessionCreateIn** | [**ViewerSessionCreateIn**](ViewerSessionCreateIn.md) |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**ViewerSessionCreateOut**](ViewerSessionCreateOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
