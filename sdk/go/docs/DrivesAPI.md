# \DrivesAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateDriveKeyRouteV0DrivesDriveIdKeysPost**](DrivesAPI.md#CreateDriveKeyRouteV0DrivesDriveIdKeysPost) | **Post** /v0/drives/{drive_id}/keys | Create a drive API key
[**CreateDriveRouteV0DrivesPost**](DrivesAPI.md#CreateDriveRouteV0DrivesPost) | **Post** /v0/drives | Create a drive in your active space
[**ListDriveKeysRouteV0DrivesDriveIdKeysGet**](DrivesAPI.md#ListDriveKeysRouteV0DrivesDriveIdKeysGet) | **Get** /v0/drives/{drive_id}/keys | List a drive&#39;s API keys
[**ListDrivesRouteV0DrivesGet**](DrivesAPI.md#ListDrivesRouteV0DrivesGet) | **Get** /v0/drives | List the drives you can see
[**RenameDriveRouteV0DrivesDriveIdPatch**](DrivesAPI.md#RenameDriveRouteV0DrivesDriveIdPatch) | **Patch** /v0/drives/{drive_id} | Rename a drive you own
[**RevokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePost**](DrivesAPI.md#RevokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePost) | **Post** /v0/drives/{drive_id}/keys/{key_id}/revoke | Revoke a drive API key
[**RotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost**](DrivesAPI.md#RotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost) | **Post** /v0/drives/{drive_id}/keys/{key_id}/rotate | Rotate one API key



## CreateDriveKeyRouteV0DrivesDriveIdKeysPost

> DriveApiKeyCreateOut CreateDriveKeyRouteV0DrivesDriveIdKeysPost(ctx, driveId).DriveApiKeyCreateIn(driveApiKeyCreateIn).Execute()

Create a drive API key



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
	driveApiKeyCreateIn := *openapiclient.NewDriveApiKeyCreateIn("Label_example") // DriveApiKeyCreateIn |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DrivesAPI.CreateDriveKeyRouteV0DrivesDriveIdKeysPost(context.Background(), driveId).DriveApiKeyCreateIn(driveApiKeyCreateIn).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DrivesAPI.CreateDriveKeyRouteV0DrivesDriveIdKeysPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateDriveKeyRouteV0DrivesDriveIdKeysPost`: DriveApiKeyCreateOut
	fmt.Fprintf(os.Stdout, "Response from `DrivesAPI.CreateDriveKeyRouteV0DrivesDriveIdKeysPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiCreateDriveKeyRouteV0DrivesDriveIdKeysPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **driveApiKeyCreateIn** | [**DriveApiKeyCreateIn**](DriveApiKeyCreateIn.md) |  |

### Return type

[**DriveApiKeyCreateOut**](DriveApiKeyCreateOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateDriveRouteV0DrivesPost

> DriveCreateOut CreateDriveRouteV0DrivesPost(ctx).DriveCreateIn(driveCreateIn).Execute()

Create a drive in your active space



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
	driveCreateIn := *openapiclient.NewDriveCreateIn("Name_example") // DriveCreateIn |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DrivesAPI.CreateDriveRouteV0DrivesPost(context.Background()).DriveCreateIn(driveCreateIn).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DrivesAPI.CreateDriveRouteV0DrivesPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateDriveRouteV0DrivesPost`: DriveCreateOut
	fmt.Fprintf(os.Stdout, "Response from `DrivesAPI.CreateDriveRouteV0DrivesPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateDriveRouteV0DrivesPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driveCreateIn** | [**DriveCreateIn**](DriveCreateIn.md) |  |

### Return type

[**DriveCreateOut**](DriveCreateOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListDriveKeysRouteV0DrivesDriveIdKeysGet

> DriveApiKeyListOut ListDriveKeysRouteV0DrivesDriveIdKeysGet(ctx, driveId).Cursor(cursor).Limit(limit).Execute()

List a drive's API keys



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
	cursor := "cursor_example" // string |  (optional)
	limit := int32(56) // int32 |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DrivesAPI.ListDriveKeysRouteV0DrivesDriveIdKeysGet(context.Background(), driveId).Cursor(cursor).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DrivesAPI.ListDriveKeysRouteV0DrivesDriveIdKeysGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListDriveKeysRouteV0DrivesDriveIdKeysGet`: DriveApiKeyListOut
	fmt.Fprintf(os.Stdout, "Response from `DrivesAPI.ListDriveKeysRouteV0DrivesDriveIdKeysGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiListDriveKeysRouteV0DrivesDriveIdKeysGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **cursor** | **string** |  |
 **limit** | **int32** |  |

### Return type

[**DriveApiKeyListOut**](DriveApiKeyListOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListDrivesRouteV0DrivesGet

> DriveList ListDrivesRouteV0DrivesGet(ctx).Cursor(cursor).Limit(limit).Execute()

List the drives you can see



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
	cursor := "cursor_example" // string |  (optional)
	limit := int32(56) // int32 |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DrivesAPI.ListDrivesRouteV0DrivesGet(context.Background()).Cursor(cursor).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DrivesAPI.ListDrivesRouteV0DrivesGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListDrivesRouteV0DrivesGet`: DriveList
	fmt.Fprintf(os.Stdout, "Response from `DrivesAPI.ListDrivesRouteV0DrivesGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListDrivesRouteV0DrivesGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **string** |  |
 **limit** | **int32** |  |

### Return type

[**DriveList**](DriveList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RenameDriveRouteV0DrivesDriveIdPatch

> DriveOut RenameDriveRouteV0DrivesDriveIdPatch(ctx, driveId).DriveRenameIn(driveRenameIn).Execute()

Rename a drive you own



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
	driveRenameIn := *openapiclient.NewDriveRenameIn("Name_example") // DriveRenameIn |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DrivesAPI.RenameDriveRouteV0DrivesDriveIdPatch(context.Background(), driveId).DriveRenameIn(driveRenameIn).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DrivesAPI.RenameDriveRouteV0DrivesDriveIdPatch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RenameDriveRouteV0DrivesDriveIdPatch`: DriveOut
	fmt.Fprintf(os.Stdout, "Response from `DrivesAPI.RenameDriveRouteV0DrivesDriveIdPatch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiRenameDriveRouteV0DrivesDriveIdPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **driveRenameIn** | [**DriveRenameIn**](DriveRenameIn.md) |  |

### Return type

[**DriveOut**](DriveOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RevokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePost

> RevokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePost(ctx, driveId, keyId).Execute()

Revoke a drive API key



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
	keyId := "keyId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DrivesAPI.RevokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePost(context.Background(), driveId, keyId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DrivesAPI.RevokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**keyId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiRevokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost

> DriveApiKeyCreateOut RotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost(ctx, driveId, keyId).Execute()

Rotate one API key



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
	keyId := "keyId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DrivesAPI.RotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost(context.Background(), driveId, keyId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DrivesAPI.RotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost`: DriveApiKeyCreateOut
	fmt.Fprintf(os.Stdout, "Response from `DrivesAPI.RotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**keyId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiRotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**DriveApiKeyCreateOut**](DriveApiKeyCreateOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
