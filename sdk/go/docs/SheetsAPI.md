# \SheetsAPI

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**SheetCellsRead**](SheetsAPI.md#SheetCellsRead) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id}/cells | Sheet Cells Read
[**SheetSessionsComplete**](SheetsAPI.md#SheetSessionsComplete) | **Post** /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions/{session_id}/complete | Sheet Sessions Complete
[**SheetSessionsCreate**](SheetsAPI.md#SheetSessionsCreate) | **Post** /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions | Sheet Sessions Create
[**SheetSessionsDelete**](SheetsAPI.md#SheetSessionsDelete) | **Delete** /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions/{session_id} | Sheet Sessions Delete
[**SheetSessionsList**](SheetsAPI.md#SheetSessionsList) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions | Sheet Sessions List
[**SheetSessionsListEdits**](SheetsAPI.md#SheetSessionsListEdits) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions/{session_id}/edits | Sheet Sessions List Edits
[**SheetSessionsRead**](SheetsAPI.md#SheetSessionsRead) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions/{session_id} | Sheet Sessions Read
[**SheetSessionsReadCells**](SheetsAPI.md#SheetSessionsReadCells) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions/{session_id}/cells | Sheet Sessions Read Cells
[**SheetSessionsWriteCells**](SheetsAPI.md#SheetSessionsWriteCells) | **Post** /v0/drives/{drive_id}/artifacts/{artifact_id}/sheet-sessions/{session_id}/cells | Sheet Sessions Write Cells
[**SheetsList**](SheetsAPI.md#SheetsList) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id}/sheets | Sheets List
[**VersionCellsRead**](SheetsAPI.md#VersionCellsRead) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/cells | Version Cells Read
[**VersionSheetsList**](SheetsAPI.md#VersionSheetsList) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/sheets | Version Sheets List



## SheetCellsRead

> CellRangeOut SheetCellsRead(ctx, driveId, artifactId).Sheet(sheet).Range_(range_).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Sheet Cells Read



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
	sheet := "sheet_example" // string |  (optional)
	range_ := "range__example" // string |  (optional)
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SheetsAPI.SheetCellsRead(context.Background(), driveId, artifactId).Sheet(sheet).Range_(range_).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SheetsAPI.SheetCellsRead``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SheetCellsRead`: CellRangeOut
	fmt.Fprintf(os.Stdout, "Response from `SheetsAPI.SheetCellsRead`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSheetCellsReadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **sheet** | **string** |  |
 **range_** | **string** |  |
 **ifNoneMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**CellRangeOut**](CellRangeOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SheetSessionsComplete

> SheetSessionsComplete(ctx, driveId, artifactId, sessionId).IdempotencyKey(idempotencyKey).CompleteIn(completeIn).Authorization(authorization).Execute()

Sheet Sessions Complete



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
	sessionId := "sessionId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	completeIn := *openapiclient.NewCompleteIn() // CompleteIn |
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.SheetsAPI.SheetSessionsComplete(context.Background(), driveId, artifactId, sessionId).IdempotencyKey(idempotencyKey).CompleteIn(completeIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SheetsAPI.SheetSessionsComplete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |
**sessionId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSheetSessionsCompleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** |  |
 **completeIn** | [**CompleteIn**](CompleteIn.md) |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SheetSessionsCreate

> interface{} SheetSessionsCreate(ctx, driveId, artifactId).IdempotencyKey(idempotencyKey).SessionCreateIn(sessionCreateIn).IfMatch(ifMatch).Authorization(authorization).Execute()

Sheet Sessions Create



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
	sessionCreateIn := *openapiclient.NewSessionCreateIn() // SessionCreateIn |
	ifMatch := "ifMatch_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SheetsAPI.SheetSessionsCreate(context.Background(), driveId, artifactId).IdempotencyKey(idempotencyKey).SessionCreateIn(sessionCreateIn).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SheetsAPI.SheetSessionsCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SheetSessionsCreate`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `SheetsAPI.SheetSessionsCreate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSheetSessionsCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **sessionCreateIn** | [**SessionCreateIn**](SessionCreateIn.md) |  |
 **ifMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

**interface{}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SheetSessionsDelete

> interface{} SheetSessionsDelete(ctx, driveId, artifactId, sessionId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()

Sheet Sessions Delete



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
	sessionId := "sessionId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	ifMatch := "ifMatch_example" // string |
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SheetsAPI.SheetSessionsDelete(context.Background(), driveId, artifactId, sessionId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SheetsAPI.SheetSessionsDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SheetSessionsDelete`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `SheetsAPI.SheetSessionsDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |
**sessionId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSheetSessionsDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** |  |
 **ifMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

**interface{}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SheetSessionsList

> interface{} SheetSessionsList(ctx, driveId, artifactId).State(state).Limit(limit).Cursor(cursor).Authorization(authorization).Execute()

Sheet Sessions List



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
	state := "state_example" // string |  (optional)
	limit := int32(56) // int32 |  (optional)
	cursor := "cursor_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SheetsAPI.SheetSessionsList(context.Background(), driveId, artifactId).State(state).Limit(limit).Cursor(cursor).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SheetsAPI.SheetSessionsList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SheetSessionsList`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `SheetsAPI.SheetSessionsList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSheetSessionsListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **state** | **string** |  |
 **limit** | **int32** |  |
 **cursor** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

**interface{}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SheetSessionsListEdits

> interface{} SheetSessionsListEdits(ctx, driveId, artifactId, sessionId).Limit(limit).Cursor(cursor).Authorization(authorization).Execute()

Sheet Sessions List Edits



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
	sessionId := "sessionId_example" // string |
	limit := int32(56) // int32 |  (optional)
	cursor := "cursor_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SheetsAPI.SheetSessionsListEdits(context.Background(), driveId, artifactId, sessionId).Limit(limit).Cursor(cursor).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SheetsAPI.SheetSessionsListEdits``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SheetSessionsListEdits`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `SheetsAPI.SheetSessionsListEdits`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |
**sessionId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSheetSessionsListEditsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **limit** | **int32** |  |
 **cursor** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

**interface{}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SheetSessionsRead

> interface{} SheetSessionsRead(ctx, driveId, artifactId, sessionId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Sheet Sessions Read



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
	sessionId := "sessionId_example" // string |
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SheetsAPI.SheetSessionsRead(context.Background(), driveId, artifactId, sessionId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SheetsAPI.SheetSessionsRead``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SheetSessionsRead`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `SheetsAPI.SheetSessionsRead`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |
**sessionId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSheetSessionsReadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **ifNoneMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

**interface{}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SheetSessionsReadCells

> interface{} SheetSessionsReadCells(ctx, driveId, artifactId, sessionId).Sheet(sheet).Range_(range_).Authorization(authorization).Execute()

Sheet Sessions Read Cells



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
	sessionId := "sessionId_example" // string |
	sheet := "sheet_example" // string |  (optional)
	range_ := "range__example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SheetsAPI.SheetSessionsReadCells(context.Background(), driveId, artifactId, sessionId).Sheet(sheet).Range_(range_).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SheetsAPI.SheetSessionsReadCells``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SheetSessionsReadCells`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `SheetsAPI.SheetSessionsReadCells`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |
**sessionId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSheetSessionsReadCellsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **sheet** | **string** |  |
 **range_** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

**interface{}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SheetSessionsWriteCells

> interface{} SheetSessionsWriteCells(ctx, driveId, artifactId, sessionId).IdempotencyKey(idempotencyKey).WriteCellsIn(writeCellsIn).Authorization(authorization).Execute()

Sheet Sessions Write Cells



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
	sessionId := "sessionId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	writeCellsIn := *openapiclient.NewWriteCellsIn([]openapiclient.CellWriteIn{*openapiclient.NewCellWriteIn("Range_example", "Sheet_example", [][]interface{}{[]interface{}{nil}})}) // WriteCellsIn |
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SheetsAPI.SheetSessionsWriteCells(context.Background(), driveId, artifactId, sessionId).IdempotencyKey(idempotencyKey).WriteCellsIn(writeCellsIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SheetsAPI.SheetSessionsWriteCells``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SheetSessionsWriteCells`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `SheetsAPI.SheetSessionsWriteCells`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |
**sessionId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSheetSessionsWriteCellsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** |  |
 **writeCellsIn** | [**WriteCellsIn**](WriteCellsIn.md) |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

**interface{}**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SheetsList

> SheetIndexOut SheetsList(ctx, driveId, artifactId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Sheets List



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
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SheetsAPI.SheetsList(context.Background(), driveId, artifactId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SheetsAPI.SheetsList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SheetsList`: SheetIndexOut
	fmt.Fprintf(os.Stdout, "Response from `SheetsAPI.SheetsList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiSheetsListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **ifNoneMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**SheetIndexOut**](SheetIndexOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VersionCellsRead

> CellRangeOut VersionCellsRead(ctx, driveId, artifactId, versionId).Sheet(sheet).Range_(range_).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Version Cells Read



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
	versionId := "versionId_example" // string |
	sheet := "sheet_example" // string |  (optional)
	range_ := "range__example" // string |  (optional)
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SheetsAPI.VersionCellsRead(context.Background(), driveId, artifactId, versionId).Sheet(sheet).Range_(range_).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SheetsAPI.VersionCellsRead``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VersionCellsRead`: CellRangeOut
	fmt.Fprintf(os.Stdout, "Response from `SheetsAPI.VersionCellsRead`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |
**versionId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiVersionCellsReadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **sheet** | **string** |  |
 **range_** | **string** |  |
 **ifNoneMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**CellRangeOut**](CellRangeOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VersionSheetsList

> SheetIndexOut VersionSheetsList(ctx, driveId, artifactId, versionId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Version Sheets List



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
	versionId := "versionId_example" // string |
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SheetsAPI.VersionSheetsList(context.Background(), driveId, artifactId, versionId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SheetsAPI.VersionSheetsList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VersionSheetsList`: SheetIndexOut
	fmt.Fprintf(os.Stdout, "Response from `SheetsAPI.VersionSheetsList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |
**versionId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiVersionSheetsListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **ifNoneMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**SheetIndexOut**](SheetIndexOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
