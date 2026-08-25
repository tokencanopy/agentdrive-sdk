# \ArtifactsAPI

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ArtifactsContent**](ArtifactsAPI.md#ArtifactsContent) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id}/content | Read Artifact Content
[**ArtifactsCopy**](ArtifactsAPI.md#ArtifactsCopy) | **Post** /v0/drives/{drive_id}/artifacts/{artifact_id}/copy | Copy Artifact
[**ArtifactsCreate**](ArtifactsAPI.md#ArtifactsCreate) | **Post** /v0/drives/{drive_id}/artifacts | Create Artifact
[**ArtifactsDelete**](ArtifactsAPI.md#ArtifactsDelete) | **Delete** /v0/drives/{drive_id}/artifacts/{artifact_id} | Delete Artifact
[**ArtifactsList**](ArtifactsAPI.md#ArtifactsList) | **Get** /v0/drives/{drive_id}/artifacts | List Artifacts
[**ArtifactsRead**](ArtifactsAPI.md#ArtifactsRead) | **Get** /v0/drives/{drive_id}/artifacts/{artifact_id} | Read Artifact
[**ArtifactsRestore**](ArtifactsAPI.md#ArtifactsRestore) | **Post** /v0/drives/{drive_id}/artifacts/{artifact_id}/restore | Restore Artifact
[**ArtifactsUpdate**](ArtifactsAPI.md#ArtifactsUpdate) | **Patch** /v0/drives/{drive_id}/artifacts/{artifact_id} | Update Artifact



## ArtifactsContent

> *os.File ArtifactsContent(ctx, driveId, artifactId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Read Artifact Content



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
	resp, r, err := apiClient.ArtifactsAPI.ArtifactsContent(context.Background(), driveId, artifactId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsAPI.ArtifactsContent``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ArtifactsContent`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsAPI.ArtifactsContent`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  | 
**artifactId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiArtifactsContentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **ifNoneMatch** | **string** |  | 
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | 

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


## ArtifactsCopy

> ArtifactOut ArtifactsCopy(ctx, driveId, artifactId).IdempotencyKey(idempotencyKey).ArtifactCopyIn(artifactCopyIn).IfMatch(ifMatch).Authorization(authorization).Execute()

Copy Artifact



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
	artifactCopyIn := *openapiclient.NewArtifactCopyIn("DestinationParentId_example", "DestinationName_example") // ArtifactCopyIn | 
	ifMatch := "ifMatch_example" // string |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ArtifactsAPI.ArtifactsCopy(context.Background(), driveId, artifactId).IdempotencyKey(idempotencyKey).ArtifactCopyIn(artifactCopyIn).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsAPI.ArtifactsCopy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ArtifactsCopy`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsAPI.ArtifactsCopy`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  | 
**artifactId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiArtifactsCopyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  | 
 **artifactCopyIn** | [**ArtifactCopyIn**](ArtifactCopyIn.md) |  | 
 **ifMatch** | **string** |  | 
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ArtifactsCreate

> ArtifactOut ArtifactsCreate(ctx, driveId).IdempotencyKey(idempotencyKey).ParentId(parentId).Name(name).Content(content).Authorization(authorization).Metadata(metadata).ContentType(contentType).Sha256(sha256).Execute()

Create Artifact



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
	parentId := "parentId_example" // string | Destination folder id (fld_*).
	name := "name_example" // string | Artifact name.
	content := os.NewFile(1234, "some_file") // *os.File | The artifact bytes.
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
	metadata := map[string]interface{}{ ... } // map[string]interface{} | Free-form JSON metadata. (optional)
	contentType := "contentType_example" // string | Declared media type. (optional)
	sha256 := "sha256_example" // string | Optional content sha256 for verification. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ArtifactsAPI.ArtifactsCreate(context.Background(), driveId).IdempotencyKey(idempotencyKey).ParentId(parentId).Name(name).Content(content).Authorization(authorization).Metadata(metadata).ContentType(contentType).Sha256(sha256).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsAPI.ArtifactsCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ArtifactsCreate`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsAPI.ArtifactsCreate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiArtifactsCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **idempotencyKey** | **string** |  | 
 **parentId** | **string** | Destination folder id (fld_*). | 
 **name** | **string** | Artifact name. | 
 **content** | ***os.File** | The artifact bytes. | 
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | 
 **metadata** | [**map[string]interface{}**](map[string]interface{}.md) | Free-form JSON metadata. | 
 **contentType** | **string** | Declared media type. | 
 **sha256** | **string** | Optional content sha256 for verification. | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ArtifactsDelete

> ArtifactOut ArtifactsDelete(ctx, driveId, artifactId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()

Delete Artifact



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
	ifMatch := "ifMatch_example" // string | 
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ArtifactsAPI.ArtifactsDelete(context.Background(), driveId, artifactId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsAPI.ArtifactsDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ArtifactsDelete`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsAPI.ArtifactsDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  | 
**artifactId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiArtifactsDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  | 
 **ifMatch** | **string** |  | 
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ArtifactsList

> ArtifactListOut ArtifactsList(ctx, driveId).Lifecycle(lifecycle).Limit(limit).Cursor(cursor).ParentId(parentId).Name(name).ContentType(contentType).Label(label).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).Authorization(authorization).Execute()

List Artifacts



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
	lifecycle := "lifecycle_example" // string |  (optional) (default to "active")
	limit := int32(56) // int32 |  (optional)
	cursor := "cursor_example" // string |  (optional)
	parentId := "parentId_example" // string |  (optional)
	name := "name_example" // string |  (optional)
	contentType := "contentType_example" // string |  (optional)
	label := "label_example" // string |  (optional)
	updatedAfter := time.Now() // time.Time |  (optional)
	updatedBefore := time.Now() // time.Time |  (optional)
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ArtifactsAPI.ArtifactsList(context.Background(), driveId).Lifecycle(lifecycle).Limit(limit).Cursor(cursor).ParentId(parentId).Name(name).ContentType(contentType).Label(label).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsAPI.ArtifactsList``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ArtifactsList`: ArtifactListOut
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsAPI.ArtifactsList`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiArtifactsListRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **lifecycle** | **string** |  | [default to &quot;active&quot;]
 **limit** | **int32** |  | 
 **cursor** | **string** |  | 
 **parentId** | **string** |  | 
 **name** | **string** |  | 
 **contentType** | **string** |  | 
 **label** | **string** |  | 
 **updatedAfter** | **time.Time** |  | 
 **updatedBefore** | **time.Time** |  | 
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | 

### Return type

[**ArtifactListOut**](ArtifactListOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ArtifactsRead

> ArtifactOut ArtifactsRead(ctx, driveId, artifactId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

Read Artifact



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
	resp, r, err := apiClient.ArtifactsAPI.ArtifactsRead(context.Background(), driveId, artifactId).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsAPI.ArtifactsRead``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ArtifactsRead`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsAPI.ArtifactsRead`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  | 
**artifactId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiArtifactsReadRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **ifNoneMatch** | **string** |  | 
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ArtifactsRestore

> ArtifactOut ArtifactsRestore(ctx, driveId, artifactId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()

Restore Artifact



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
	ifMatch := "ifMatch_example" // string | 
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ArtifactsAPI.ArtifactsRestore(context.Background(), driveId, artifactId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsAPI.ArtifactsRestore``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ArtifactsRestore`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsAPI.ArtifactsRestore`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  | 
**artifactId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiArtifactsRestoreRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  | 
 **ifMatch** | **string** |  | 
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ArtifactsUpdate

> ArtifactOut ArtifactsUpdate(ctx, driveId, artifactId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).ArtifactUpdateIn(artifactUpdateIn).Authorization(authorization).Execute()

Update Artifact



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
	ifMatch := "ifMatch_example" // string | 
	artifactUpdateIn := *openapiclient.NewArtifactUpdateIn() // ArtifactUpdateIn | 
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ArtifactsAPI.ArtifactsUpdate(context.Background(), driveId, artifactId).IdempotencyKey(idempotencyKey).IfMatch(ifMatch).ArtifactUpdateIn(artifactUpdateIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ArtifactsAPI.ArtifactsUpdate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ArtifactsUpdate`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `ArtifactsAPI.ArtifactsUpdate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  | 
**artifactId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiArtifactsUpdateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **idempotencyKey** | **string** |  | 
 **ifMatch** | **string** |  | 
 **artifactUpdateIn** | [**ArtifactUpdateIn**](ArtifactUpdateIn.md) |  | 
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

