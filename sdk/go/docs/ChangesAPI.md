# \ChangesAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ChangesList**](ChangesAPI.md#ChangesList) | **Get** /v0/drives/{drive_id}/changes | List Changes



## ChangesList

> ChangePageOut ChangesList(ctx, driveId).Limit(limit).Start(start).Cursor(cursor).Authorization(authorization).Execute()

List Changes



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
	limit := int32(56) // int32 |  (optional)
	start := "start_example" // string |  (optional)
	cursor := "cursor_example" // string |  (optional)
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ChangesAPI.ChangesList(context.Background(), driveId).Limit(limit).Start(start).Cursor(cursor).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ChangesAPI.ChangesList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ChangesList`: ChangePageOut
	fmt.Fprintf(os.Stdout, "Response from `ChangesAPI.ChangesList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiChangesListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** |  |
 **start** | **string** |  |
 **cursor** | **string** |  |
 **authorization** | **string** |  |

### Return type

[**ChangePageOut**](ChangePageOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
