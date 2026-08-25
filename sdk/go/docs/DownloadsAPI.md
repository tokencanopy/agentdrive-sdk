# \DownloadsAPI

All URIs are relative to *https://drive.tokencanopy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DownloadCapabilitiesCreate**](DownloadsAPI.md#DownloadCapabilitiesCreate) | **Post** /v0/drives/{drive_id}/download-capabilities | Create Download Capability



## DownloadCapabilitiesCreate

> DownloadCapabilityOut DownloadCapabilitiesCreate(ctx, driveId).DownloadCapabilitiesCreateRequest(downloadCapabilitiesCreateRequest).Authorization(authorization).Execute()

Create Download Capability



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
	downloadCapabilitiesCreateRequest := *openapiclient.NewDownloadCapabilitiesCreateRequest(openapiclient.download_capabilities_create_request_target{DownloadCapabilitiesCreateRequestTargetOneOf: openapiclient.NewDownloadCapabilitiesCreateRequestTargetOneOf("ArtifactId_example", "Kind_example")}) // DownloadCapabilitiesCreateRequest |
	authorization := "authorization_example" // string | Deprecated: redundant with the operation's `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DownloadsAPI.DownloadCapabilitiesCreate(context.Background(), driveId).DownloadCapabilitiesCreateRequest(downloadCapabilitiesCreateRequest).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DownloadsAPI.DownloadCapabilitiesCreate``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadCapabilitiesCreate`: DownloadCapabilityOut
	fmt.Fprintf(os.Stdout, "Response from `DownloadsAPI.DownloadCapabilitiesCreate`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadCapabilitiesCreateRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **downloadCapabilitiesCreateRequest** | [**DownloadCapabilitiesCreateRequest**](DownloadCapabilitiesCreateRequest.md) |  |
 **authorization** | **string** | Deprecated: redundant with the operation&#39;s &#x60;bearerAuth&#x60; security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. |

### Return type

[**DownloadCapabilityOut**](DownloadCapabilityOut.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
