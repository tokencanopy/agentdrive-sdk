# \UploadsAPI

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**UploadsComplete**](UploadsAPI.md#UploadsComplete) | **Post** /v0/drives/{drive_id}/uploads/{upload_id}/complete | Complete Upload
[**UploadsCreate**](UploadsAPI.md#UploadsCreate) | **Post** /v0/drives/{drive_id}/uploads | Begin Upload
[**UploadsDelete**](UploadsAPI.md#UploadsDelete) | **Delete** /v0/drives/{drive_id}/uploads/{upload_id} | Cancel Upload
[**UploadsRead**](UploadsAPI.md#UploadsRead) | **Get** /v0/drives/{drive_id}/uploads/{upload_id} | Read Upload



## UploadsComplete

> UploadSessionOut UploadsComplete(ctx, driveId, uploadId).IdempotencyKey(idempotencyKey).Authorization(authorization).Execute()

Complete Upload



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
	uploadId := "uploadId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UploadsAPI.UploadsComplete(context.Background(), driveId, uploadId).IdempotencyKey(idempotencyKey).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UploadsAPI.UploadsComplete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UploadsComplete`: UploadSessionOut
	fmt.Fprintf(os.Stdout, "Response from `UploadsAPI.UploadsComplete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**uploadId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiUploadsCompleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**UploadSessionOut**](UploadSessionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UploadsCreate

> UploadSessionOut UploadsCreate(ctx, driveId).IdempotencyKey(idempotencyKey).UploadsCreateRequest(uploadsCreateRequest).IfMatch(ifMatch).Authorization(authorization).Execute()

Begin Upload



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
	idempotencyKey := "idempotencyKey_example" // string |
	uploadsCreateRequest := *openapiclient.NewUploadsCreateRequest(*openapiclient.NewUploadsCreateRequestContent(*openapiclient.NewUploadsCreateRequestContentChecksum("Algorithm_example", "Value_example"), "MediaType_example", int32(123)), openapiclient.uploads_create_request_target{UploadsCreateRequestTargetOneOf: openapiclient.NewUploadsCreateRequestTargetOneOf("Kind_example", "Name_example", "ParentFolderId_example")}) // UploadsCreateRequest |
	ifMatch := "ifMatch_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UploadsAPI.UploadsCreate(context.Background(), driveId).IdempotencyKey(idempotencyKey).UploadsCreateRequest(uploadsCreateRequest).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UploadsAPI.UploadsCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UploadsCreate`: UploadSessionOut
	fmt.Fprintf(os.Stdout, "Response from `UploadsAPI.UploadsCreate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiUploadsCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** |  |
 **uploadsCreateRequest** | [**UploadsCreateRequest**](UploadsCreateRequest.md) |  |
 **ifMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**UploadSessionOut**](UploadSessionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UploadsDelete

> UploadSessionOut UploadsDelete(ctx, driveId, uploadId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()

Cancel Upload



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
	uploadId := "uploadId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	ifMatch := "ifMatch_example" // string |
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UploadsAPI.UploadsDelete(context.Background(), driveId, uploadId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UploadsAPI.UploadsDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UploadsDelete`: UploadSessionOut
	fmt.Fprintf(os.Stdout, "Response from `UploadsAPI.UploadsDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**uploadId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiUploadsDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **ifMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**UploadSessionOut**](UploadSessionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UploadsRead

> UploadSessionOut UploadsRead(ctx, driveId, uploadId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Read Upload



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
	uploadId := "uploadId_example" // string |
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UploadsAPI.UploadsRead(context.Background(), driveId, uploadId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UploadsAPI.UploadsRead``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UploadsRead`: UploadSessionOut
	fmt.Fprintf(os.Stdout, "Response from `UploadsAPI.UploadsRead`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**uploadId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiUploadsReadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **ifNoneMatch** | **string** |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**UploadSessionOut**](UploadSessionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
