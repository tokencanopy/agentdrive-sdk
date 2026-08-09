# \SearchAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DriveSearch**](SearchAPI.md#DriveSearch) | **Get** /v0/drives/{drive_id}/search | Drive Search



## DriveSearch

> SearchPageOut DriveSearch(ctx, driveId).Q(q).Mode(mode).Limit(limit).Cursor(cursor).ParentId(parentId).ContentType(contentType).Label(label).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).Authorization(authorization).Execute()

Drive Search



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/Mnexa-AI/agentdrive-sdk/agentdrive"
)

func main() {
	driveId := "driveId_example" // string |
	q := "q_example" // string |
	mode := "mode_example" // string |  (optional) (default to "lexical")
	limit := int32(56) // int32 |  (optional)
	cursor := "cursor_example" // string |  (optional)
	parentId := "parentId_example" // string |  (optional)
	contentType := "contentType_example" // string |  (optional)
	label := "label_example" // string |  (optional)
	updatedAfter := time.Now() // time.Time |  (optional)
	updatedBefore := time.Now() // time.Time |  (optional)
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SearchAPI.DriveSearch(context.Background(), driveId).Q(q).Mode(mode).Limit(limit).Cursor(cursor).ParentId(parentId).ContentType(contentType).Label(label).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SearchAPI.DriveSearch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DriveSearch`: SearchPageOut
	fmt.Fprintf(os.Stdout, "Response from `SearchAPI.DriveSearch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDriveSearchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **q** | **string** |  |
 **mode** | **string** |  | [default to &quot;lexical&quot;]
 **limit** | **int32** |  |
 **cursor** | **string** |  |
 **parentId** | **string** |  |
 **contentType** | **string** |  |
 **label** | **string** |  |
 **updatedAfter** | **time.Time** |  |
 **updatedBefore** | **time.Time** |  |
 **authorization** | **string** |  |

### Return type

[**SearchPageOut**](SearchPageOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
