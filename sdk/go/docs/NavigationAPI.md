# \NavigationAPI

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**EntriesList**](NavigationAPI.md#EntriesList) | **Get** /v0/drives/{drive_id}/entries | List Entries
[**Lookup**](NavigationAPI.md#Lookup) | **Get** /v0/drives/{drive_id}/lookup | Lookup



## EntriesList

> EntryListOut EntriesList(ctx, driveId).ParentId(parentId).Type_(type_).Name(name).Label(label).ContentType(contentType).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).State(state).Limit(limit).Cursor(cursor).Authorization(authorization).Execute()

List Entries



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/tokencanopy/agentdrive-sdk/agentdrive"
)

func main() {
	driveId := "driveId_example" // string |
	parentId := "parentId_example" // string |
	type_ := "type__example" // string |  (optional)
	name := "name_example" // string |  (optional)
	label := "label_example" // string |  (optional)
	contentType := "contentType_example" // string |  (optional)
	updatedAfter := time.Now() // time.Time |  (optional)
	updatedBefore := time.Now() // time.Time |  (optional)
	state := "state_example" // string |  (optional) (default to "active")
	limit := int32(56) // int32 |  (optional)
	cursor := "cursor_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NavigationAPI.EntriesList(context.Background(), driveId).ParentId(parentId).Type_(type_).Name(name).Label(label).ContentType(contentType).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).State(state).Limit(limit).Cursor(cursor).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NavigationAPI.EntriesList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `EntriesList`: EntryListOut
	fmt.Fprintf(os.Stdout, "Response from `NavigationAPI.EntriesList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiEntriesListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **parentId** | **string** |  |
 **type_** | **string** |  |
 **name** | **string** |  |
 **label** | **string** |  |
 **contentType** | **string** |  |
 **updatedAfter** | **time.Time** |  |
 **updatedBefore** | **time.Time** |  |
 **state** | **string** |  | [default to &quot;active&quot;]
 **limit** | **int32** |  |
 **cursor** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**EntryListOut**](EntryListOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## Lookup

> LookupOut Lookup(ctx, driveId).Path(path).Type_(type_).Authorization(authorization).Execute()

Lookup



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
	path := "path_example" // string |
	type_ := "type__example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NavigationAPI.Lookup(context.Background(), driveId).Path(path).Type_(type_).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NavigationAPI.Lookup``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `Lookup`: LookupOut
	fmt.Fprintf(os.Stdout, "Response from `NavigationAPI.Lookup`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiLookupRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **path** | **string** |  |
 **type_** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**LookupOut**](LookupOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
