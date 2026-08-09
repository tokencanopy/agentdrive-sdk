# \VersionsAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**VersionsAppend**](VersionsAPI.md#VersionsAppend) | **Post** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions | Append Version
[**VersionsContent**](VersionsAPI.md#VersionsContent) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/content | Read Version Content
[**VersionsList**](VersionsAPI.md#VersionsList) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions | List Versions
[**VersionsRead**](VersionsAPI.md#VersionsRead) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id} | Read Version
[**VersionsRestore**](VersionsAPI.md#VersionsRestore) | **Post** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/restore | Restore Version



## VersionsAppend

> VersionCreatedOut VersionsAppend(ctx, driveId, artifactId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Content(content).Authorization(authorization).ContentType(contentType).Sha256(sha256).Execute()

Append Version



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
	artifactId := "artifactId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	ifMatch := "ifMatch_example" // string |
	content := os.NewFile(1234, "some_file") // *os.File | The artifact bytes.
	authorization := "authorization_example" // string |  (optional)
	contentType := "contentType_example" // string | Declared media type. (optional)
	sha256 := "sha256_example" // string | Optional content sha256 for verification. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.VersionsAPI.VersionsAppend(context.Background(), driveId, artifactId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Content(content).Authorization(authorization).ContentType(contentType).Sha256(sha256).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VersionsAPI.VersionsAppend``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VersionsAppend`: VersionCreatedOut
	fmt.Fprintf(os.Stdout, "Response from `VersionsAPI.VersionsAppend`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiVersionsAppendRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  |
 **ifMatch** | **string** |  |
 **content** | ***os.File** | The artifact bytes. |
 **authorization** | **string** |  |
 **contentType** | **string** | Declared media type. |
 **sha256** | **string** | Optional content sha256 for verification. |

### Return type

[**VersionCreatedOut**](VersionCreatedOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VersionsContent

> *os.File VersionsContent(ctx, driveId, artifactId, versionId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Read Version Content



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
	artifactId := "artifactId_example" // string |
	versionId := "versionId_example" // string |
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.VersionsAPI.VersionsContent(context.Background(), driveId, artifactId, versionId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VersionsAPI.VersionsContent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VersionsContent`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `VersionsAPI.VersionsContent`: %v\n", resp)
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

Other parameters are passed through a pointer to a apiVersionsContentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **ifNoneMatch** | **string** |  |
 **authorization** | **string** |  |

### Return type

[***os.File**](*os.File.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VersionsList

> VersionListOut VersionsList(ctx, driveId, artifactId).Limit(limit).Cursor(cursor).Authorization(authorization).Execute()

List Versions



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
	artifactId := "artifactId_example" // string |
	limit := int32(56) // int32 |  (optional)
	cursor := "cursor_example" // string |  (optional)
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.VersionsAPI.VersionsList(context.Background(), driveId, artifactId).Limit(limit).Cursor(cursor).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VersionsAPI.VersionsList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VersionsList`: VersionListOut
	fmt.Fprintf(os.Stdout, "Response from `VersionsAPI.VersionsList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**artifactId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiVersionsListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** |  |
 **cursor** | **string** |  |
 **authorization** | **string** |  |

### Return type

[**VersionListOut**](VersionListOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VersionsRead

> VersionOut VersionsRead(ctx, driveId, artifactId, versionId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Read Version



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
	artifactId := "artifactId_example" // string |
	versionId := "versionId_example" // string |
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.VersionsAPI.VersionsRead(context.Background(), driveId, artifactId, versionId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VersionsAPI.VersionsRead``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VersionsRead`: VersionOut
	fmt.Fprintf(os.Stdout, "Response from `VersionsAPI.VersionsRead`: %v\n", resp)
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

Other parameters are passed through a pointer to a apiVersionsReadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **ifNoneMatch** | **string** |  |
 **authorization** | **string** |  |

### Return type

[**VersionOut**](VersionOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VersionsRestore

> VersionCreatedOut VersionsRestore(ctx, driveId, artifactId, versionId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()

Restore Version



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
	artifactId := "artifactId_example" // string |
	versionId := "versionId_example" // string |
	idempotencyKey := "idempotencyKey_example" // string |
	ifMatch := "ifMatch_example" // string |
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.VersionsAPI.VersionsRestore(context.Background(), driveId, artifactId, versionId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VersionsAPI.VersionsRestore``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VersionsRestore`: VersionCreatedOut
	fmt.Fprintf(os.Stdout, "Response from `VersionsAPI.VersionsRestore`: %v\n", resp)
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

Other parameters are passed through a pointer to a apiVersionsRestoreRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **idempotencyKey** | **string** |  |
 **ifMatch** | **string** |  |
 **authorization** | **string** |  |

### Return type

[**VersionCreatedOut**](VersionCreatedOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
