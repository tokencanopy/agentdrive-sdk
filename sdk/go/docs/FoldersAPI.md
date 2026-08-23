# \FoldersAPI

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**FoldersCopy**](FoldersAPI.md#FoldersCopy) | **Post** /v0/drives/{drive_id}/folders/{folder_id}/copy | Copy Folder
[**FoldersCreate**](FoldersAPI.md#FoldersCreate) | **Post** /v0/drives/{drive_id}/folders | Create Folder
[**FoldersDelete**](FoldersAPI.md#FoldersDelete) | **Delete** /v0/drives/{drive_id}/folders/{folder_id} | Delete Folder
[**FoldersList**](FoldersAPI.md#FoldersList) | **Get** /v0/drives/{drive_id}/folders | List Folders
[**FoldersRead**](FoldersAPI.md#FoldersRead) | **Get** /v0/drives/{drive_id}/folders/{folder_id} | Read Folder
[**FoldersRestore**](FoldersAPI.md#FoldersRestore) | **Post** /v0/drives/{drive_id}/folders/{folder_id}/restore | Restore Folder
[**FoldersUpdate**](FoldersAPI.md#FoldersUpdate) | **Patch** /v0/drives/{drive_id}/folders/{folder_id} | Update Folder



## FoldersCopy

> FolderOut FoldersCopy(ctx, driveId, folderId).IdempotencyKey(idempotencyKey).FolderCopyIn(folderCopyIn).IfMatch(ifMatch).Authorization(authorization).Execute()

Copy Folder



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
	folderId := "folderId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	folderCopyIn := *openapiclient.NewFolderCopyIn("DestinationName_example", "DestinationParentId_example") // FolderCopyIn |
	ifMatch := "ifMatch_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FoldersAPI.FoldersCopy(context.Background(), driveId, folderId).IdempotencyKey(idempotencyKey).FolderCopyIn(folderCopyIn).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FoldersAPI.FoldersCopy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FoldersCopy`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `FoldersAPI.FoldersCopy`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**folderId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiFoldersCopyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **folderCopyIn** | [**FolderCopyIn**](FolderCopyIn.md) |  |
 **ifMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FoldersCreate

> FolderOut FoldersCreate(ctx, driveId).IdempotencyKey(idempotencyKey).FolderCreateIn(folderCreateIn).Authorization(authorization).Execute()

Create Folder



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
	folderCreateIn := *openapiclient.NewFolderCreateIn("Name_example", "ParentId_example") // FolderCreateIn |
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FoldersAPI.FoldersCreate(context.Background(), driveId).IdempotencyKey(idempotencyKey).FolderCreateIn(folderCreateIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FoldersAPI.FoldersCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FoldersCreate`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `FoldersAPI.FoldersCreate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiFoldersCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** |  |
 **folderCreateIn** | [**FolderCreateIn**](FolderCreateIn.md) |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FoldersDelete

> FolderCascadeOut FoldersDelete(ctx, driveId, folderId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Recursive(recursive).Authorization(authorization).Execute()

Delete Folder



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
	folderId := "folderId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	ifMatch := "ifMatch_example" // string |
	recursive := true // bool |  (optional) (default to false)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FoldersAPI.FoldersDelete(context.Background(), driveId, folderId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Recursive(recursive).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FoldersAPI.FoldersDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FoldersDelete`: FolderCascadeOut
	fmt.Fprintf(os.Stdout, "Response from `FoldersAPI.FoldersDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**folderId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiFoldersDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **ifMatch** | **string** |  |
 **recursive** | **bool** |  | [default to false]
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**FolderCascadeOut**](FolderCascadeOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FoldersList

> FolderListOut FoldersList(ctx, driveId).Lifecycle(lifecycle).Limit(limit).Cursor(cursor).ParentId(parentId).Name(name).Authorization(authorization).Execute()

List Folders



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
	parentId := "parentId_example" // string |  (optional)
	name := "name_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FoldersAPI.FoldersList(context.Background(), driveId).Lifecycle(lifecycle).Limit(limit).Cursor(cursor).ParentId(parentId).Name(name).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FoldersAPI.FoldersList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FoldersList`: FolderListOut
	fmt.Fprintf(os.Stdout, "Response from `FoldersAPI.FoldersList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiFoldersListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **lifecycle** | **string** |  | [default to &quot;active&quot;]
 **limit** | **int32** |  |
 **cursor** | **string** |  |
 **parentId** | **string** |  |
 **name** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**FolderListOut**](FolderListOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FoldersRead

> FolderOut FoldersRead(ctx, driveId, folderId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Read Folder



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
	folderId := "folderId_example" // string |
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FoldersAPI.FoldersRead(context.Background(), driveId, folderId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FoldersAPI.FoldersRead``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FoldersRead`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `FoldersAPI.FoldersRead`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**folderId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiFoldersReadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **ifNoneMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FoldersRestore

> FolderCascadeOut FoldersRestore(ctx, driveId, folderId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()

Restore Folder



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
	folderId := "folderId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	ifMatch := "ifMatch_example" // string |
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FoldersAPI.FoldersRestore(context.Background(), driveId, folderId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FoldersAPI.FoldersRestore``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FoldersRestore`: FolderCascadeOut
	fmt.Fprintf(os.Stdout, "Response from `FoldersAPI.FoldersRestore`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**folderId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiFoldersRestoreRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **ifMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**FolderCascadeOut**](FolderCascadeOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FoldersUpdate

> FolderOut FoldersUpdate(ctx, driveId, folderId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).FolderUpdateIn(folderUpdateIn).Authorization(authorization).Execute()

Update Folder



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
	folderId := "folderId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	ifMatch := "ifMatch_example" // string |
	folderUpdateIn := *openapiclient.NewFolderUpdateIn() // FolderUpdateIn |
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FoldersAPI.FoldersUpdate(context.Background(), driveId, folderId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).FolderUpdateIn(folderUpdateIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FoldersAPI.FoldersUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FoldersUpdate`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `FoldersAPI.FoldersUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**folderId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiFoldersUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **ifMatch** | **string** |  |
 **folderUpdateIn** | [**FolderUpdateIn**](FolderUpdateIn.md) |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
