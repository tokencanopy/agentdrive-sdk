# \WorkspacesAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateWorkspaceRouteV0WorkspacesPost**](WorkspacesAPI.md#CreateWorkspaceRouteV0WorkspacesPost) | **Post** /v0/workspaces | Create a new shared drive
[**ListWorkspacesRouteV0WorkspacesGet**](WorkspacesAPI.md#ListWorkspacesRouteV0WorkspacesGet) | **Get** /v0/workspaces | List the spaces you belong to
[**RenameWorkspaceRouteV0WorkspacesOrgIdPatch**](WorkspacesAPI.md#RenameWorkspaceRouteV0WorkspacesOrgIdPatch) | **Patch** /v0/workspaces/{org_id} | Rename a shared drive you administer



## CreateWorkspaceRouteV0WorkspacesPost

> WorkspaceCreateOut CreateWorkspaceRouteV0WorkspacesPost(ctx).WorkspaceCreateIn(workspaceCreateIn).Authorization(authorization).Execute()

Create a new shared drive



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
	workspaceCreateIn := *openapiclient.NewWorkspaceCreateIn("Name_example") // WorkspaceCreateIn | 
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WorkspacesAPI.CreateWorkspaceRouteV0WorkspacesPost(context.Background()).WorkspaceCreateIn(workspaceCreateIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkspacesAPI.CreateWorkspaceRouteV0WorkspacesPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateWorkspaceRouteV0WorkspacesPost`: WorkspaceCreateOut
	fmt.Fprintf(os.Stdout, "Response from `WorkspacesAPI.CreateWorkspaceRouteV0WorkspacesPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateWorkspaceRouteV0WorkspacesPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceCreateIn** | [**WorkspaceCreateIn**](WorkspaceCreateIn.md) |  | 
 **authorization** | **string** |  | 

### Return type

[**WorkspaceCreateOut**](WorkspaceCreateOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListWorkspacesRouteV0WorkspacesGet

> WorkspaceList ListWorkspacesRouteV0WorkspacesGet(ctx).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()

List the spaces you belong to



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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WorkspacesAPI.ListWorkspacesRouteV0WorkspacesGet(context.Background()).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkspacesAPI.ListWorkspacesRouteV0WorkspacesGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListWorkspacesRouteV0WorkspacesGet`: WorkspaceList
	fmt.Fprintf(os.Stdout, "Response from `WorkspacesAPI.ListWorkspacesRouteV0WorkspacesGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListWorkspacesRouteV0WorkspacesGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **string** |  | 
 **limit** | **int32** |  | 
 **authorization** | **string** |  | 

### Return type

[**WorkspaceList**](WorkspaceList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RenameWorkspaceRouteV0WorkspacesOrgIdPatch

> WorkspaceOut RenameWorkspaceRouteV0WorkspacesOrgIdPatch(ctx, orgId).WorkspaceRenameIn(workspaceRenameIn).Authorization(authorization).Execute()

Rename a shared drive you administer



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
	orgId := "orgId_example" // string | 
	workspaceRenameIn := *openapiclient.NewWorkspaceRenameIn("Name_example") // WorkspaceRenameIn | 
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WorkspacesAPI.RenameWorkspaceRouteV0WorkspacesOrgIdPatch(context.Background(), orgId).WorkspaceRenameIn(workspaceRenameIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WorkspacesAPI.RenameWorkspaceRouteV0WorkspacesOrgIdPatch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RenameWorkspaceRouteV0WorkspacesOrgIdPatch`: WorkspaceOut
	fmt.Fprintf(os.Stdout, "Response from `WorkspacesAPI.RenameWorkspaceRouteV0WorkspacesOrgIdPatch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**orgId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRenameWorkspaceRouteV0WorkspacesOrgIdPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **workspaceRenameIn** | [**WorkspaceRenameIn**](WorkspaceRenameIn.md) |  | 
 **authorization** | **string** |  | 

### Return type

[**WorkspaceOut**](WorkspaceOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

