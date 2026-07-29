# \DefaultAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AbortUploadV0UploadsUploadIdDelete**](DefaultAPI.md#AbortUploadV0UploadsUploadIdDelete) | **Delete** /v0/uploads/{upload_id} | Abort a large (direct-to-GCS) upload session
[**BeginUploadV0UploadsPost**](DefaultAPI.md#BeginUploadV0UploadsPost) | **Post** /v0/uploads | Begin a large (direct-to-GCS) upload
[**CallbackAuthCallbackGet**](DefaultAPI.md#CallbackAuthCallbackGet) | **Get** /auth/callback | Callback
[**CancelJobV0JobsJobIdCancelPost**](DefaultAPI.md#CancelJobV0JobsJobIdCancelPost) | **Post** /v0/jobs/{job_id}/cancel | Cancel a queued/running job
[**CommitUploadV0UploadsUploadIdCommitPost**](DefaultAPI.md#CommitUploadV0UploadsUploadIdCommitPost) | **Post** /v0/uploads/{upload_id}/commit | Commit a large (direct-to-GCS) upload
[**CopyArtifactRouteV0ArtifactsArtIdCopyPost**](DefaultAPI.md#CopyArtifactRouteV0ArtifactsArtIdCopyPost) | **Post** /v0/artifacts/{art_id}/copy | Duplicate an artifact to a new path (CAS-shared, new ID)
[**CopyFolderByIdV0FoldersFldIdCopyPost**](DefaultAPI.md#CopyFolderByIdV0FoldersFldIdCopyPost) | **Post** /v0/folders/{fld_id}/copy | Duplicate a folder subtree to a new path (CAS-shared, new IDs)
[**CreateFolderByPathV0FoldersPathPut**](DefaultAPI.md#CreateFolderByPathV0FoldersPathPut) | **Put** /v0/folders/{path} | Create a folder (idempotent)
[**CreateGrantRouteV0GrantsPost**](DefaultAPI.md#CreateGrantRouteV0GrantsPost) | **Post** /v0/grants | Create (or fetch) a per-principal grant on a resource
[**CreateShareRouteV0SharesPost**](DefaultAPI.md#CreateShareRouteV0SharesPost) | **Post** /v0/shares | Mint a share link (returns the share_key once)
[**DeleteArtifactByIdRouteV0ArtifactsArtIdDelete**](DefaultAPI.md#DeleteArtifactByIdRouteV0ArtifactsArtIdDelete) | **Delete** /v0/artifacts/{art_id} | Soft-delete an artifact by its stable ID
[**DeleteArtifactV0ArtifactsPathDelete**](DefaultAPI.md#DeleteArtifactV0ArtifactsPathDelete) | **Delete** /v0/artifacts/{path} | Delete Artifact
[**DeleteDriveRouteV0DrivesDriveIdDelete**](DefaultAPI.md#DeleteDriveRouteV0DrivesDriveIdDelete) | **Delete** /v0/drives/{drive_id} | Soft-delete a drive
[**DeleteFolderByIdV0FoldersFldIdDelete**](DefaultAPI.md#DeleteFolderByIdV0FoldersFldIdDelete) | **Delete** /v0/folders/{fld_id} | Soft-delete a folder by stable ID (cascade with ?recursive&#x3D;true)
[**DeleteFolderByPathV0FoldersPathDelete**](DefaultAPI.md#DeleteFolderByPathV0FoldersPathDelete) | **Delete** /v0/folders/{path} | Soft-delete a folder (cascade with ?recursive&#x3D;true)
[**DeleteGrantRouteV0GrantsGrnIdDelete**](DefaultAPI.md#DeleteGrantRouteV0GrantsGrnIdDelete) | **Delete** /v0/grants/{grn_id} | Revoke a grant (can_manage, or self-revoke own grant)
[**DeleteShareRouteV0SharesShrIdDelete**](DefaultAPI.md#DeleteShareRouteV0SharesShrIdDelete) | **Delete** /v0/shares/{shr_id} | Revoke a share link (requires can_manage)
[**DownloadArtifactByIdV0ArtifactsArtIdDownloadGet**](DefaultAPI.md#DownloadArtifactByIdV0ArtifactsArtIdDownloadGet) | **Get** /v0/artifacts/{art_id}/download | Stream the artifact bytes by stable ID (never rendered HTML)
[**DownloadArtifactByPathV0ArtifactsPathDownloadGet**](DefaultAPI.md#DownloadArtifactByPathV0ArtifactsPathDownloadGet) | **Get** /v0/artifacts/{path}/download | Stream the artifact bytes by path (never rendered HTML)
[**DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet**](DefaultAPI.md#DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet) | **Get** /v0/artifacts/{art_id}/versions/{version_number}/download | Stream bytes for a specific version (machine surface)
[**DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet**](DefaultAPI.md#DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet) | **Get** /v0/artifacts/{art_id}/download-url | Signed direct-from-GCS download URL by stable ID
[**DownloadUrlByPathV0ArtifactsPathDownloadUrlGet**](DefaultAPI.md#DownloadUrlByPathV0ArtifactsPathDownloadUrlGet) | **Get** /v0/artifacts/{path}/download-url | Signed direct-from-GCS download URL by path
[**DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet**](DefaultAPI.md#DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet) | **Get** /v0/artifacts/{art_id}/versions/{version_number}/download-url | Signed direct-from-GCS download URL for a specific version
[**EnqueueJobV0ProjectsFldIdJobsPost**](DefaultAPI.md#EnqueueJobV0ProjectsFldIdJobsPost) | **Post** /v0/projects/{fld_id}/jobs | Enqueue a compile job for a project (folder)
[**ExtensionStartAuthExtensionStartGet**](DefaultAPI.md#ExtensionStartAuthExtensionStartGet) | **Get** /auth/extension/start | Extension Start
[**FindV0FindGet**](DefaultAPI.md#FindV0FindGet) | **Get** /v0/find | Hybrid passage retrieval over the full file body
[**GetArtifactByIdMetaV0ArtifactsArtIdMetaGet**](DefaultAPI.md#GetArtifactByIdMetaV0ArtifactsArtIdMetaGet) | **Get** /v0/artifacts/{art_id}/meta | Artifact metadata by stable ID (same shape as path /meta)
[**GetArtifactByIdV0ArtifactsArtIdGet**](DefaultAPI.md#GetArtifactByIdV0ArtifactsArtIdGet) | **Get** /v0/artifacts/{art_id} | Canonical lookup of an artifact by its stable ID
[**GetArtifactMetaV0ArtifactsPathMetaGet**](DefaultAPI.md#GetArtifactMetaV0ArtifactsPathMetaGet) | **Get** /v0/artifacts/{path}/meta | Get Artifact Meta
[**GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet**](DefaultAPI.md#GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet) | **Get** /v0/artifacts/{art_id}/versions/{version_number} | Metadata for a specific version of an artifact
[**GetDriveRouteV0DrivesDriveIdGet**](DefaultAPI.md#GetDriveRouteV0DrivesDriveIdGet) | **Get** /v0/drives/{drive_id} | Drive overview by id (same shape as /drives/me)
[**GetFeedbackStatusV0FeedbackFbkIdGet**](DefaultAPI.md#GetFeedbackStatusV0FeedbackFbkIdGet) | **Get** /v0/feedback/{fbk_id} | Get Feedback Status
[**GetFolderByIdMetaV0FoldersFldIdMetaGet**](DefaultAPI.md#GetFolderByIdMetaV0FoldersFldIdMetaGet) | **Get** /v0/folders/{fld_id}/meta | Folder metadata by stable ID (same shape as the bare id route)
[**GetFolderByIdV0FoldersFldIdGet**](DefaultAPI.md#GetFolderByIdV0FoldersFldIdGet) | **Get** /v0/folders/{fld_id} | Canonical lookup of a folder by its stable ID
[**GetFolderByPathMetaV0FoldersPathMetaGet**](DefaultAPI.md#GetFolderByPathMetaV0FoldersPathMetaGet) | **Get** /v0/folders/{path}/meta | Folder metadata by path (same shape as the bare path route)
[**GetFolderByPathV0FoldersPathGet**](DefaultAPI.md#GetFolderByPathV0FoldersPathGet) | **Get** /v0/folders/{path} | Read folder metadata by path
[**GetGrantRouteV0GrantsGrnIdGet**](DefaultAPI.md#GetGrantRouteV0GrantsGrnIdGet) | **Get** /v0/grants/{grn_id} | Read a single grant (can_manage, or the grant&#39;s own principal)
[**GetJobLogsV0JobsJobIdLogsGet**](DefaultAPI.md#GetJobLogsV0JobsJobIdLogsGet) | **Get** /v0/jobs/{job_id}/logs | Raw compile log (text/plain)
[**GetJobV0JobsJobIdGet**](DefaultAPI.md#GetJobV0JobsJobIdGet) | **Get** /v0/jobs/{job_id} | Poll a job
[**GetProjectV0ProjectsFldIdGet**](DefaultAPI.md#GetProjectV0ProjectsFldIdGet) | **Get** /v0/projects/{fld_id} | Get a project&#39;s compile config
[**GetShareRouteV0SharesShrIdGet**](DefaultAPI.md#GetShareRouteV0SharesShrIdGet) | **Get** /v0/shares/{shr_id} | Read a single share link&#39;s metadata (requires can_manage)
[**GetUploadStatusV0UploadsUploadIdGet**](DefaultAPI.md#GetUploadStatusV0UploadsUploadIdGet) | **Get** /v0/uploads/{upload_id} | Get the status of a large (direct-to-GCS) upload session
[**HealthHealthGet**](DefaultAPI.md#HealthHealthGet) | **Get** /health | Health
[**ListArtifactVersionsV0ArtifactsArtIdVersionsGet**](DefaultAPI.md#ListArtifactVersionsV0ArtifactsArtIdVersionsGet) | **Get** /v0/artifacts/{art_id}/versions | List versions of an artifact, newest first
[**ListArtifactsV0ArtifactsGet**](DefaultAPI.md#ListArtifactsV0ArtifactsGet) | **Get** /v0/artifacts | List artifacts in the drive
[**ListEventsRouteV0EventsGet**](DefaultAPI.md#ListEventsRouteV0EventsGet) | **Get** /v0/events | Read the append-only event log for the authenticated drive
[**ListGrantsRouteV0GrantsGet**](DefaultAPI.md#ListGrantsRouteV0GrantsGet) | **Get** /v0/grants | List live grants on a resource (requires can_manage)
[**ListProjectJobsV0ProjectsFldIdJobsGet**](DefaultAPI.md#ListProjectJobsV0ProjectsFldIdJobsGet) | **Get** /v0/projects/{fld_id}/jobs | List a project&#39;s jobs
[**ListSharesRouteV0SharesGet**](DefaultAPI.md#ListSharesRouteV0SharesGet) | **Get** /v0/shares | List live share links on a resource (requires can_manage)
[**ListTrashRouteV0DrivesDriveIdTrashGet**](DefaultAPI.md#ListTrashRouteV0DrivesDriveIdTrashGet) | **Get** /v0/drives/{drive_id}/trash | List the authenticated drive&#39;s trash
[**LoginAuthLoginGet**](DefaultAPI.md#LoginAuthLoginGet) | **Get** /auth/login | Login
[**LogoutAuthLogoutPost**](DefaultAPI.md#LogoutAuthLogoutPost) | **Post** /auth/logout | Logout
[**MeUsageV0DrivesMeUsageGet**](DefaultAPI.md#MeUsageV0DrivesMeUsageGet) | **Get** /v0/drives/me/usage | Current-period usage + caps for the authenticated drive
[**MeV0DrivesMeGet**](DefaultAPI.md#MeV0DrivesMeGet) | **Get** /v0/drives/me | Me
[**MoveArtifactRouteV0ArtifactsArtIdMovePost**](DefaultAPI.md#MoveArtifactRouteV0ArtifactsArtIdMovePost) | **Post** /v0/artifacts/{art_id}/move | Rename / move an artifact to a new path
[**MoveFolderByIdV0FoldersFldIdMovePost**](DefaultAPI.md#MoveFolderByIdV0FoldersFldIdMovePost) | **Post** /v0/folders/{fld_id}/move | Rename / move a folder by stable ID (cascade descendants)
[**MoveFolderByPathV0FoldersPathMovePost**](DefaultAPI.md#MoveFolderByPathV0FoldersPathMovePost) | **Post** /v0/folders/{path}/move | Rename / move a folder (cascade-update descendants)
[**PatchArtifactRouteV0ArtifactsArtIdPatch**](DefaultAPI.md#PatchArtifactRouteV0ArtifactsArtIdPatch) | **Patch** /v0/artifacts/{art_id} | Edit artifact metadata (labels / metadata / source)
[**PatchFolderByIdV0FoldersFldIdPatch**](DefaultAPI.md#PatchFolderByIdV0FoldersFldIdPatch) | **Patch** /v0/folders/{fld_id} | Update folder metadata by stable ID
[**PatchFolderByPathV0FoldersPathPatch**](DefaultAPI.md#PatchFolderByPathV0FoldersPathPatch) | **Patch** /v0/folders/{path} | Update folder metadata by path
[**PatchGrantRouteV0GrantsGrnIdPatch**](DefaultAPI.md#PatchGrantRouteV0GrantsGrnIdPatch) | **Patch** /v0/grants/{grn_id} | Update a grant&#39;s role and/or expiry (requires can_manage)
[**PostDescribeV0QueryDescribePost**](DefaultAPI.md#PostDescribeV0QueryDescribePost) | **Post** /v0/query/describe | Describe a dataset&#39;s column schema
[**PostFeedbackV0FeedbackPost**](DefaultAPI.md#PostFeedbackV0FeedbackPost) | **Post** /v0/feedback | Post Feedback
[**PostLookupValuesV0QueryLookupValuesPost**](DefaultAPI.md#PostLookupValuesV0QueryLookupValuesPost) | **Post** /v0/query/lookup-values | List distinct values of a dataset column
[**PostQueryV0QueryPost**](DefaultAPI.md#PostQueryV0QueryPost) | **Post** /v0/query | Run a read-only SQL query over authorized datasets
[**PutArtifactV0ArtifactsPathPut**](DefaultAPI.md#PutArtifactV0ArtifactsPathPut) | **Put** /v0/artifacts/{path} | Upload (or overwrite) an artifact
[**PutProjectV0ProjectsFldIdPut**](DefaultAPI.md#PutProjectV0ProjectsFldIdPut) | **Put** /v0/projects/{fld_id} | Set a project&#39;s compile config (entrypoint/engine/auto_compile)
[**RedeemShareSShareKeyGet**](DefaultAPI.md#RedeemShareSShareKeyGet) | **Get** /s/{share_key} | Redeem Share
[**RedeemShareWithPasswordSShareKeyPost**](DefaultAPI.md#RedeemShareWithPasswordSShareKeyPost) | **Post** /s/{share_key} | Redeem Share With Password
[**RestoreArtifactV0ArtifactsArtIdRestorePost**](DefaultAPI.md#RestoreArtifactV0ArtifactsArtIdRestorePost) | **Post** /v0/artifacts/{art_id}/restore | Restore a soft-deleted artifact
[**RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost**](DefaultAPI.md#RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost) | **Post** /v0/artifacts/{art_id}/versions/{version_number}/restore | Restore a previous version as a new head version
[**RestoreDriveRouteV0DrivesDriveIdRestorePost**](DefaultAPI.md#RestoreDriveRouteV0DrivesDriveIdRestorePost) | **Post** /v0/drives/{drive_id}/restore | Restore a soft-deleted drive
[**RestoreFolderByIdV0FoldersFldIdRestorePost**](DefaultAPI.md#RestoreFolderByIdV0FoldersFldIdRestorePost) | **Post** /v0/folders/{fld_id}/restore | Restore a soft-deleted folder (cascade)
[**RotateShareRouteV0SharesShrIdRotatePost**](DefaultAPI.md#RotateShareRouteV0SharesShrIdRotatePost) | **Post** /v0/shares/{shr_id}/rotate | Revoke + reissue a share link&#39;s key (requires can_share)
[**SearchV0SearchGet**](DefaultAPI.md#SearchV0SearchGet) | **Get** /v0/search | Full-text search over artifacts in the drive
[**ViewArtifactHeadAArtIdHeadGet**](DefaultAPI.md#ViewArtifactHeadAArtIdHeadGet) | **Get** /a/{art_id}/head | View Artifact Head
[**ViewArtifactVersionVArtIdVersionGet**](DefaultAPI.md#ViewArtifactVersionVArtIdVersionGet) | **Get** /v/{art_id}/{version} | View Artifact Version
[**ViewFileDriveIdPathGet**](DefaultAPI.md#ViewFileDriveIdPathGet) | **Get** /{drive_id}/{path} | View File
[**ViewPermalinkArtifactAArtIdGet**](DefaultAPI.md#ViewPermalinkArtifactAArtIdGet) | **Get** /a/{art_id} | View Permalink Artifact
[**ViewPermalinkFolderFFldIdGet**](DefaultAPI.md#ViewPermalinkFolderFFldIdGet) | **Get** /f/{fld_id} | View Permalink Folder



## AbortUploadV0UploadsUploadIdDelete

> UploadAbortOut AbortUploadV0UploadsUploadIdDelete(ctx, uploadId).Execute()

Abort a large (direct-to-GCS) upload session



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
	uploadId := "uploadId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.AbortUploadV0UploadsUploadIdDelete(context.Background(), uploadId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.AbortUploadV0UploadsUploadIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AbortUploadV0UploadsUploadIdDelete`: UploadAbortOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.AbortUploadV0UploadsUploadIdDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**uploadId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiAbortUploadV0UploadsUploadIdDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**UploadAbortOut**](UploadAbortOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BeginUploadV0UploadsPost

> UploadBeginOut BeginUploadV0UploadsPost(ctx).UploadBeginIn(uploadBeginIn).Execute()

Begin a large (direct-to-GCS) upload



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
	uploadBeginIn := *openapiclient.NewUploadBeginIn("Path_example", int32(123)) // UploadBeginIn |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.BeginUploadV0UploadsPost(context.Background()).UploadBeginIn(uploadBeginIn).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.BeginUploadV0UploadsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BeginUploadV0UploadsPost`: UploadBeginOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.BeginUploadV0UploadsPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiBeginUploadV0UploadsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uploadBeginIn** | [**UploadBeginIn**](UploadBeginIn.md) |  |

### Return type

[**UploadBeginOut**](UploadBeginOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CallbackAuthCallbackGet

> string CallbackAuthCallbackGet(ctx).Code(code).State(state).Error_(error_).Execute()

Callback



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
	code := "code_example" // string |  (optional)
	state := "state_example" // string |  (optional)
	error_ := "error__example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CallbackAuthCallbackGet(context.Background()).Code(code).State(state).Error_(error_).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CallbackAuthCallbackGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CallbackAuthCallbackGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CallbackAuthCallbackGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCallbackAuthCallbackGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **string** |  |
 **state** | **string** |  |
 **error_** | **string** |  |

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CancelJobV0JobsJobIdCancelPost

> CompileJobOut CancelJobV0JobsJobIdCancelPost(ctx, jobId).Execute()

Cancel a queued/running job

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
	jobId := "jobId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CancelJobV0JobsJobIdCancelPost(context.Background(), jobId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CancelJobV0JobsJobIdCancelPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CancelJobV0JobsJobIdCancelPost`: CompileJobOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CancelJobV0JobsJobIdCancelPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**jobId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiCancelJobV0JobsJobIdCancelPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CompileJobOut**](CompileJobOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CommitUploadV0UploadsUploadIdCommitPost

> ArtifactOut CommitUploadV0UploadsUploadIdCommitPost(ctx, uploadId).Execute()

Commit a large (direct-to-GCS) upload



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
	uploadId := "uploadId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CommitUploadV0UploadsUploadIdCommitPost(context.Background(), uploadId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CommitUploadV0UploadsUploadIdCommitPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CommitUploadV0UploadsUploadIdCommitPost`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CommitUploadV0UploadsUploadIdCommitPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**uploadId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiCommitUploadV0UploadsUploadIdCommitPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CopyArtifactRouteV0ArtifactsArtIdCopyPost

> ArtifactOut CopyArtifactRouteV0ArtifactsArtIdCopyPost(ctx, artId).CopyIn(copyIn).XAgentdriveActor(xAgentdriveActor).IfNoneMatch(ifNoneMatch).Execute()

Duplicate an artifact to a new path (CAS-shared, new ID)



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
	artId := "artId_example" // string |
	copyIn := *openapiclient.NewCopyIn("Path_example") // CopyIn |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CopyArtifactRouteV0ArtifactsArtIdCopyPost(context.Background(), artId).CopyIn(copyIn).XAgentdriveActor(xAgentdriveActor).IfNoneMatch(ifNoneMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CopyArtifactRouteV0ArtifactsArtIdCopyPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CopyArtifactRouteV0ArtifactsArtIdCopyPost`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CopyArtifactRouteV0ArtifactsArtIdCopyPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiCopyArtifactRouteV0ArtifactsArtIdCopyPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **copyIn** | [**CopyIn**](CopyIn.md) |  |
 **xAgentdriveActor** | **string** |  |
 **ifNoneMatch** | **string** |  |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CopyFolderByIdV0FoldersFldIdCopyPost

> FolderCopyOut CopyFolderByIdV0FoldersFldIdCopyPost(ctx, fldId).FolderCopyIn(folderCopyIn).XAgentdriveActor(xAgentdriveActor).IfNoneMatch(ifNoneMatch).Execute()

Duplicate a folder subtree to a new path (CAS-shared, new IDs)



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
	fldId := "fldId_example" // string |
	folderCopyIn := *openapiclient.NewFolderCopyIn("Path_example") // FolderCopyIn |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CopyFolderByIdV0FoldersFldIdCopyPost(context.Background(), fldId).FolderCopyIn(folderCopyIn).XAgentdriveActor(xAgentdriveActor).IfNoneMatch(ifNoneMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CopyFolderByIdV0FoldersFldIdCopyPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CopyFolderByIdV0FoldersFldIdCopyPost`: FolderCopyOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CopyFolderByIdV0FoldersFldIdCopyPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiCopyFolderByIdV0FoldersFldIdCopyPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **folderCopyIn** | [**FolderCopyIn**](FolderCopyIn.md) |  |
 **xAgentdriveActor** | **string** |  |
 **ifNoneMatch** | **string** |  |

### Return type

[**FolderCopyOut**](FolderCopyOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateFolderByPathV0FoldersPathPut

> FolderOut CreateFolderByPathV0FoldersPathPut(ctx, path).XAgentdriveActor(xAgentdriveActor).IfNoneMatch(ifNoneMatch).FolderCreateIn(folderCreateIn).Execute()

Create a folder (idempotent)



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
	path := "path_example" // string |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)
	folderCreateIn := *openapiclient.NewFolderCreateIn() // FolderCreateIn |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CreateFolderByPathV0FoldersPathPut(context.Background(), path).XAgentdriveActor(xAgentdriveActor).IfNoneMatch(ifNoneMatch).FolderCreateIn(folderCreateIn).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateFolderByPathV0FoldersPathPut``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateFolderByPathV0FoldersPathPut`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CreateFolderByPathV0FoldersPathPut`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiCreateFolderByPathV0FoldersPathPutRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xAgentdriveActor** | **string** |  |
 **ifNoneMatch** | **string** |  |
 **folderCreateIn** | [**FolderCreateIn**](FolderCreateIn.md) |  |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateGrantRouteV0GrantsPost

> GrantOut CreateGrantRouteV0GrantsPost(ctx).GrantCreateIn(grantCreateIn).XAgentdriveActor(xAgentdriveActor).Execute()

Create (or fetch) a per-principal grant on a resource

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
	grantCreateIn := *openapiclient.NewGrantCreateIn(*openapiclient.NewGrantPrincipalIn("Type_example"), "Resource_example", "Role_example") // GrantCreateIn |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CreateGrantRouteV0GrantsPost(context.Background()).GrantCreateIn(grantCreateIn).XAgentdriveActor(xAgentdriveActor).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateGrantRouteV0GrantsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateGrantRouteV0GrantsPost`: GrantOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CreateGrantRouteV0GrantsPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateGrantRouteV0GrantsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grantCreateIn** | [**GrantCreateIn**](GrantCreateIn.md) |  |
 **xAgentdriveActor** | **string** |  |

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateShareRouteV0SharesPost

> ShareMintOut CreateShareRouteV0SharesPost(ctx).ShareCreateIn(shareCreateIn).XAgentdriveActor(xAgentdriveActor).Execute()

Mint a share link (returns the share_key once)

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
	shareCreateIn := *openapiclient.NewShareCreateIn("Resource_example") // ShareCreateIn |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CreateShareRouteV0SharesPost(context.Background()).ShareCreateIn(shareCreateIn).XAgentdriveActor(xAgentdriveActor).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateShareRouteV0SharesPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateShareRouteV0SharesPost`: ShareMintOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CreateShareRouteV0SharesPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateShareRouteV0SharesPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shareCreateIn** | [**ShareCreateIn**](ShareCreateIn.md) |  |
 **xAgentdriveActor** | **string** |  |

### Return type

[**ShareMintOut**](ShareMintOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteArtifactByIdRouteV0ArtifactsArtIdDelete

> ArtifactDeleteOut DeleteArtifactByIdRouteV0ArtifactsArtIdDelete(ctx, artId).IfMatch(ifMatch).XAgentdriveActor(xAgentdriveActor).Execute()

Soft-delete an artifact by its stable ID



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
	artId := "artId_example" // string |
	ifMatch := "ifMatch_example" // string |  (optional)
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteArtifactByIdRouteV0ArtifactsArtIdDelete(context.Background(), artId).IfMatch(ifMatch).XAgentdriveActor(xAgentdriveActor).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteArtifactByIdRouteV0ArtifactsArtIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteArtifactByIdRouteV0ArtifactsArtIdDelete`: ArtifactDeleteOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DeleteArtifactByIdRouteV0ArtifactsArtIdDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteArtifactByIdRouteV0ArtifactsArtIdDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **ifMatch** | **string** |  |
 **xAgentdriveActor** | **string** |  |

### Return type

[**ArtifactDeleteOut**](ArtifactDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteArtifactV0ArtifactsPathDelete

> ArtifactDeleteOut DeleteArtifactV0ArtifactsPathDelete(ctx, path).IfMatch(ifMatch).XAgentdriveActor(xAgentdriveActor).Execute()

Delete Artifact



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
	path := "path_example" // string |
	ifMatch := "ifMatch_example" // string |  (optional)
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteArtifactV0ArtifactsPathDelete(context.Background(), path).IfMatch(ifMatch).XAgentdriveActor(xAgentdriveActor).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteArtifactV0ArtifactsPathDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteArtifactV0ArtifactsPathDelete`: ArtifactDeleteOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DeleteArtifactV0ArtifactsPathDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteArtifactV0ArtifactsPathDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **ifMatch** | **string** |  |
 **xAgentdriveActor** | **string** |  |

### Return type

[**ArtifactDeleteOut**](ArtifactDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteDriveRouteV0DrivesDriveIdDelete

> DriveDeleteOut DeleteDriveRouteV0DrivesDriveIdDelete(ctx, driveId).Confirm(confirm).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Soft-delete a drive



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
	confirm := "confirm_example" // string |  (optional)
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteDriveRouteV0DrivesDriveIdDelete(context.Background(), driveId).Confirm(confirm).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteDriveRouteV0DrivesDriveIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteDriveRouteV0DrivesDriveIdDelete`: DriveDeleteOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DeleteDriveRouteV0DrivesDriveIdDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteDriveRouteV0DrivesDriveIdDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **confirm** | **string** |  |
 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**DriveDeleteOut**](DriveDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteFolderByIdV0FoldersFldIdDelete

> FolderDeleteOut DeleteFolderByIdV0FoldersFldIdDelete(ctx, fldId).Recursive(recursive).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Soft-delete a folder by stable ID (cascade with ?recursive=true)

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
	fldId := "fldId_example" // string |
	recursive := true // bool |  (optional) (default to false)
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteFolderByIdV0FoldersFldIdDelete(context.Background(), fldId).Recursive(recursive).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteFolderByIdV0FoldersFldIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteFolderByIdV0FoldersFldIdDelete`: FolderDeleteOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DeleteFolderByIdV0FoldersFldIdDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteFolderByIdV0FoldersFldIdDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **recursive** | **bool** |  | [default to false]
 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**FolderDeleteOut**](FolderDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteFolderByPathV0FoldersPathDelete

> FolderDeleteOut DeleteFolderByPathV0FoldersPathDelete(ctx, path).Recursive(recursive).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Soft-delete a folder (cascade with ?recursive=true)



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
	path := "path_example" // string |
	recursive := true // bool |  (optional) (default to false)
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteFolderByPathV0FoldersPathDelete(context.Background(), path).Recursive(recursive).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteFolderByPathV0FoldersPathDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteFolderByPathV0FoldersPathDelete`: FolderDeleteOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DeleteFolderByPathV0FoldersPathDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteFolderByPathV0FoldersPathDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **recursive** | **bool** |  | [default to false]
 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**FolderDeleteOut**](FolderDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteGrantRouteV0GrantsGrnIdDelete

> RevokeOut DeleteGrantRouteV0GrantsGrnIdDelete(ctx, grnId).XAgentdriveActor(xAgentdriveActor).Execute()

Revoke a grant (can_manage, or self-revoke own grant)

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
	grnId := "grnId_example" // string |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteGrantRouteV0GrantsGrnIdDelete(context.Background(), grnId).XAgentdriveActor(xAgentdriveActor).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteGrantRouteV0GrantsGrnIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteGrantRouteV0GrantsGrnIdDelete`: RevokeOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DeleteGrantRouteV0GrantsGrnIdDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**grnId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteGrantRouteV0GrantsGrnIdDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xAgentdriveActor** | **string** |  |

### Return type

[**RevokeOut**](RevokeOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteShareRouteV0SharesShrIdDelete

> RevokeOut DeleteShareRouteV0SharesShrIdDelete(ctx, shrId).XAgentdriveActor(xAgentdriveActor).Execute()

Revoke a share link (requires can_manage)

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
	shrId := "shrId_example" // string |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteShareRouteV0SharesShrIdDelete(context.Background(), shrId).XAgentdriveActor(xAgentdriveActor).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteShareRouteV0SharesShrIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteShareRouteV0SharesShrIdDelete`: RevokeOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DeleteShareRouteV0SharesShrIdDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**shrId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteShareRouteV0SharesShrIdDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xAgentdriveActor** | **string** |  |

### Return type

[**RevokeOut**](RevokeOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadArtifactByIdV0ArtifactsArtIdDownloadGet

> *os.File DownloadArtifactByIdV0ArtifactsArtIdDownloadGet(ctx, artId).Execute()

Stream the artifact bytes by stable ID (never rendered HTML)

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
	artId := "artId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DownloadArtifactByIdV0ArtifactsArtIdDownloadGet(context.Background(), artId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DownloadArtifactByIdV0ArtifactsArtIdDownloadGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadArtifactByIdV0ArtifactsArtIdDownloadGet`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DownloadArtifactByIdV0ArtifactsArtIdDownloadGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadArtifactByIdV0ArtifactsArtIdDownloadGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[***os.File**](*os.File.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadArtifactByPathV0ArtifactsPathDownloadGet

> *os.File DownloadArtifactByPathV0ArtifactsPathDownloadGet(ctx, path).Execute()

Stream the artifact bytes by path (never rendered HTML)



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
	path := "path_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DownloadArtifactByPathV0ArtifactsPathDownloadGet(context.Background(), path).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DownloadArtifactByPathV0ArtifactsPathDownloadGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadArtifactByPathV0ArtifactsPathDownloadGet`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DownloadArtifactByPathV0ArtifactsPathDownloadGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadArtifactByPathV0ArtifactsPathDownloadGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[***os.File**](*os.File.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet

> *os.File DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet(ctx, artId, versionNumber).Execute()

Stream bytes for a specific version (machine surface)

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
	artId := "artId_example" // string |
	versionNumber := int32(56) // int32 |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet(context.Background(), artId, versionNumber).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |
**versionNumber** | **int32** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[***os.File**](*os.File.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet

> DownloadUrlOut DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet(ctx, artId).Execute()

Signed direct-from-GCS download URL by stable ID



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
	artId := "artId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet(context.Background(), artId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet`: DownloadUrlOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadUrlByIdV0ArtifactsArtIdDownloadUrlGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadUrlByPathV0ArtifactsPathDownloadUrlGet

> DownloadUrlOut DownloadUrlByPathV0ArtifactsPathDownloadUrlGet(ctx, path).Execute()

Signed direct-from-GCS download URL by path



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
	path := "path_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DownloadUrlByPathV0ArtifactsPathDownloadUrlGet(context.Background(), path).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DownloadUrlByPathV0ArtifactsPathDownloadUrlGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadUrlByPathV0ArtifactsPathDownloadUrlGet`: DownloadUrlOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DownloadUrlByPathV0ArtifactsPathDownloadUrlGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadUrlByPathV0ArtifactsPathDownloadUrlGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet

> DownloadUrlOut DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet(ctx, artId, versionNumber).Execute()

Signed direct-from-GCS download URL for a specific version



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
	artId := "artId_example" // string |
	versionNumber := int32(56) // int32 |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet(context.Background(), artId, versionNumber).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet`: DownloadUrlOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |
**versionNumber** | **int32** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiDownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## EnqueueJobV0ProjectsFldIdJobsPost

> CompileJobOut EnqueueJobV0ProjectsFldIdJobsPost(ctx, fldId).CompileJobIn(compileJobIn).XAgentdriveActor(xAgentdriveActor).Execute()

Enqueue a compile job for a project (folder)

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
	fldId := "fldId_example" // string |
	compileJobIn := *openapiclient.NewCompileJobIn() // CompileJobIn |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.EnqueueJobV0ProjectsFldIdJobsPost(context.Background(), fldId).CompileJobIn(compileJobIn).XAgentdriveActor(xAgentdriveActor).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.EnqueueJobV0ProjectsFldIdJobsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `EnqueueJobV0ProjectsFldIdJobsPost`: CompileJobOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.EnqueueJobV0ProjectsFldIdJobsPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiEnqueueJobV0ProjectsFldIdJobsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **compileJobIn** | [**CompileJobIn**](CompileJobIn.md) |  |
 **xAgentdriveActor** | **string** |  |

### Return type

[**CompileJobOut**](CompileJobOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExtensionStartAuthExtensionStartGet

> ExtensionStartAuthExtensionStartGet(ctx).ExtId(extId).Execute()

Extension Start



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
	extId := "extId_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.ExtensionStartAuthExtensionStartGet(context.Background()).ExtId(extId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ExtensionStartAuthExtensionStartGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiExtensionStartAuthExtensionStartGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extId** | **string** |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FindV0FindGet

> FindPage FindV0FindGet(ctx).Q(q).Mode(mode).Label(label).FileType(fileType).Prefix(prefix).Modality(modality).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).Limit(limit).Execute()

Hybrid passage retrieval over the full file body



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
	q := "q_example" // string |
	mode := "mode_example" // string |  (optional) (default to "hybrid")
	label := []string{"Inner_example"} // []string |  (optional)
	fileType := "fileType_example" // string |  (optional)
	prefix := "prefix_example" // string |  (optional)
	modality := []*string{"Inner_example"} // []*string |  (optional)
	updatedAfter := time.Now() // time.Time |  (optional)
	updatedBefore := time.Now() // time.Time |  (optional)
	limit := int32(56) // int32 |  (optional) (default to 20)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.FindV0FindGet(context.Background()).Q(q).Mode(mode).Label(label).FileType(fileType).Prefix(prefix).Modality(modality).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.FindV0FindGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FindV0FindGet`: FindPage
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.FindV0FindGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiFindV0FindGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **string** |  |
 **mode** | **string** |  | [default to &quot;hybrid&quot;]
 **label** | **[]string** |  |
 **fileType** | **string** |  |
 **prefix** | **string** |  |
 **modality** | **[]string** |  |
 **updatedAfter** | **time.Time** |  |
 **updatedBefore** | **time.Time** |  |
 **limit** | **int32** |  | [default to 20]

### Return type

[**FindPage**](FindPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetArtifactByIdMetaV0ArtifactsArtIdMetaGet

> ArtifactOut GetArtifactByIdMetaV0ArtifactsArtIdMetaGet(ctx, artId).Execute()

Artifact metadata by stable ID (same shape as path /meta)

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
	artId := "artId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetArtifactByIdMetaV0ArtifactsArtIdMetaGet(context.Background(), artId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetArtifactByIdMetaV0ArtifactsArtIdMetaGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetArtifactByIdMetaV0ArtifactsArtIdMetaGet`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetArtifactByIdMetaV0ArtifactsArtIdMetaGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetArtifactByIdMetaV0ArtifactsArtIdMetaGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetArtifactByIdV0ArtifactsArtIdGet

> ArtifactOut GetArtifactByIdV0ArtifactsArtIdGet(ctx, artId).Execute()

Canonical lookup of an artifact by its stable ID

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
	artId := "artId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetArtifactByIdV0ArtifactsArtIdGet(context.Background(), artId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetArtifactByIdV0ArtifactsArtIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetArtifactByIdV0ArtifactsArtIdGet`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetArtifactByIdV0ArtifactsArtIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetArtifactByIdV0ArtifactsArtIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetArtifactMetaV0ArtifactsPathMetaGet

> ArtifactOut GetArtifactMetaV0ArtifactsPathMetaGet(ctx, path).Execute()

Get Artifact Meta

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
	path := "path_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetArtifactMetaV0ArtifactsPathMetaGet(context.Background(), path).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetArtifactMetaV0ArtifactsPathMetaGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetArtifactMetaV0ArtifactsPathMetaGet`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetArtifactMetaV0ArtifactsPathMetaGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetArtifactMetaV0ArtifactsPathMetaGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet

> VersionOut GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet(ctx, artId, versionNumber).Execute()

Metadata for a specific version of an artifact

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
	artId := "artId_example" // string |
	versionNumber := int32(56) // int32 |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet(context.Background(), artId, versionNumber).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet`: VersionOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |
**versionNumber** | **int32** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**VersionOut**](VersionOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDriveRouteV0DrivesDriveIdGet

> DriveReadOut GetDriveRouteV0DrivesDriveIdGet(ctx, driveId).Execute()

Drive overview by id (same shape as /drives/me)



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetDriveRouteV0DrivesDriveIdGet(context.Background(), driveId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetDriveRouteV0DrivesDriveIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetDriveRouteV0DrivesDriveIdGet`: DriveReadOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetDriveRouteV0DrivesDriveIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetDriveRouteV0DrivesDriveIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**DriveReadOut**](DriveReadOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFeedbackStatusV0FeedbackFbkIdGet

> FeedbackStatusOut GetFeedbackStatusV0FeedbackFbkIdGet(ctx, fbkId).Execute()

Get Feedback Status



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
	fbkId := "fbkId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetFeedbackStatusV0FeedbackFbkIdGet(context.Background(), fbkId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetFeedbackStatusV0FeedbackFbkIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFeedbackStatusV0FeedbackFbkIdGet`: FeedbackStatusOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetFeedbackStatusV0FeedbackFbkIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fbkId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetFeedbackStatusV0FeedbackFbkIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**FeedbackStatusOut**](FeedbackStatusOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFolderByIdMetaV0FoldersFldIdMetaGet

> FolderOut GetFolderByIdMetaV0FoldersFldIdMetaGet(ctx, fldId).Execute()

Folder metadata by stable ID (same shape as the bare id route)

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
	fldId := "fldId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetFolderByIdMetaV0FoldersFldIdMetaGet(context.Background(), fldId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetFolderByIdMetaV0FoldersFldIdMetaGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFolderByIdMetaV0FoldersFldIdMetaGet`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetFolderByIdMetaV0FoldersFldIdMetaGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetFolderByIdMetaV0FoldersFldIdMetaGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFolderByIdV0FoldersFldIdGet

> FolderOut GetFolderByIdV0FoldersFldIdGet(ctx, fldId).Execute()

Canonical lookup of a folder by its stable ID

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
	fldId := "fldId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetFolderByIdV0FoldersFldIdGet(context.Background(), fldId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetFolderByIdV0FoldersFldIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFolderByIdV0FoldersFldIdGet`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetFolderByIdV0FoldersFldIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetFolderByIdV0FoldersFldIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFolderByPathMetaV0FoldersPathMetaGet

> FolderOut GetFolderByPathMetaV0FoldersPathMetaGet(ctx, path).Execute()

Folder metadata by path (same shape as the bare path route)

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
	path := "path_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetFolderByPathMetaV0FoldersPathMetaGet(context.Background(), path).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetFolderByPathMetaV0FoldersPathMetaGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFolderByPathMetaV0FoldersPathMetaGet`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetFolderByPathMetaV0FoldersPathMetaGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetFolderByPathMetaV0FoldersPathMetaGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFolderByPathV0FoldersPathGet

> FolderOut GetFolderByPathV0FoldersPathGet(ctx, path).Execute()

Read folder metadata by path

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
	path := "path_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetFolderByPathV0FoldersPathGet(context.Background(), path).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetFolderByPathV0FoldersPathGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFolderByPathV0FoldersPathGet`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetFolderByPathV0FoldersPathGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetFolderByPathV0FoldersPathGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetGrantRouteV0GrantsGrnIdGet

> GrantOut GetGrantRouteV0GrantsGrnIdGet(ctx, grnId).Execute()

Read a single grant (can_manage, or the grant's own principal)



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
	grnId := "grnId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetGrantRouteV0GrantsGrnIdGet(context.Background(), grnId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetGrantRouteV0GrantsGrnIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetGrantRouteV0GrantsGrnIdGet`: GrantOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetGrantRouteV0GrantsGrnIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**grnId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetGrantRouteV0GrantsGrnIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetJobLogsV0JobsJobIdLogsGet

> string GetJobLogsV0JobsJobIdLogsGet(ctx, jobId).Execute()

Raw compile log (text/plain)

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
	jobId := "jobId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetJobLogsV0JobsJobIdLogsGet(context.Background(), jobId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetJobLogsV0JobsJobIdLogsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetJobLogsV0JobsJobIdLogsGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetJobLogsV0JobsJobIdLogsGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**jobId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetJobLogsV0JobsJobIdLogsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**string**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetJobV0JobsJobIdGet

> CompileJobOut GetJobV0JobsJobIdGet(ctx, jobId).Execute()

Poll a job

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
	jobId := "jobId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetJobV0JobsJobIdGet(context.Background(), jobId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetJobV0JobsJobIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetJobV0JobsJobIdGet`: CompileJobOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetJobV0JobsJobIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**jobId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetJobV0JobsJobIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CompileJobOut**](CompileJobOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProjectV0ProjectsFldIdGet

> CompileProjectOut GetProjectV0ProjectsFldIdGet(ctx, fldId).Execute()

Get a project's compile config

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
	fldId := "fldId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetProjectV0ProjectsFldIdGet(context.Background(), fldId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetProjectV0ProjectsFldIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetProjectV0ProjectsFldIdGet`: CompileProjectOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetProjectV0ProjectsFldIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetProjectV0ProjectsFldIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CompileProjectOut**](CompileProjectOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetShareRouteV0SharesShrIdGet

> ShareOut GetShareRouteV0SharesShrIdGet(ctx, shrId).Execute()

Read a single share link's metadata (requires can_manage)



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
	shrId := "shrId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetShareRouteV0SharesShrIdGet(context.Background(), shrId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetShareRouteV0SharesShrIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetShareRouteV0SharesShrIdGet`: ShareOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetShareRouteV0SharesShrIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**shrId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetShareRouteV0SharesShrIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ShareOut**](ShareOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetUploadStatusV0UploadsUploadIdGet

> UploadStatusOut GetUploadStatusV0UploadsUploadIdGet(ctx, uploadId).Execute()

Get the status of a large (direct-to-GCS) upload session



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
	uploadId := "uploadId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetUploadStatusV0UploadsUploadIdGet(context.Background(), uploadId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetUploadStatusV0UploadsUploadIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetUploadStatusV0UploadsUploadIdGet`: UploadStatusOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetUploadStatusV0UploadsUploadIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**uploadId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiGetUploadStatusV0UploadsUploadIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**UploadStatusOut**](UploadStatusOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## HealthHealthGet

> HealthOut HealthHealthGet(ctx).Execute()

Health



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.HealthHealthGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.HealthHealthGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `HealthHealthGet`: HealthOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.HealthHealthGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiHealthHealthGetRequest struct via the builder pattern


### Return type

[**HealthOut**](HealthOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListArtifactVersionsV0ArtifactsArtIdVersionsGet

> VersionPage ListArtifactVersionsV0ArtifactsArtIdVersionsGet(ctx, artId).Cursor(cursor).Limit(limit).Execute()

List versions of an artifact, newest first



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
	artId := "artId_example" // string |
	cursor := "cursor_example" // string |  (optional)
	limit := int32(56) // int32 |  (optional) (default to 50)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListArtifactVersionsV0ArtifactsArtIdVersionsGet(context.Background(), artId).Cursor(cursor).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ListArtifactVersionsV0ArtifactsArtIdVersionsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListArtifactVersionsV0ArtifactsArtIdVersionsGet`: VersionPage
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ListArtifactVersionsV0ArtifactsArtIdVersionsGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiListArtifactVersionsV0ArtifactsArtIdVersionsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **cursor** | **string** |  |
 **limit** | **int32** |  | [default to 50]

### Return type

[**VersionPage**](VersionPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListArtifactsV0ArtifactsGet

> Page ListArtifactsV0ArtifactsGet(ctx).Prefix(prefix).Label(label).FileType(fileType).Cursor(cursor).Limit(limit).Execute()

List artifacts in the drive



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
	prefix := "prefix_example" // string |  (optional) (default to "")
	label := []*string{"Inner_example"} // []*string |  (optional)
	fileType := "fileType_example" // string |  (optional)
	cursor := "cursor_example" // string |  (optional)
	limit := int32(56) // int32 |  (optional) (default to 50)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListArtifactsV0ArtifactsGet(context.Background()).Prefix(prefix).Label(label).FileType(fileType).Cursor(cursor).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ListArtifactsV0ArtifactsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListArtifactsV0ArtifactsGet`: Page
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ListArtifactsV0ArtifactsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListArtifactsV0ArtifactsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **string** |  | [default to &quot;&quot;]
 **label** | **[]string** |  |
 **fileType** | **string** |  |
 **cursor** | **string** |  |
 **limit** | **int32** |  | [default to 50]

### Return type

[**Page**](Page.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListEventsRouteV0EventsGet

> EventPage ListEventsRouteV0EventsGet(ctx).ArtId(artId).Action(action).Since(since).Before(before).Cursor(cursor).Limit(limit).Execute()

Read the append-only event log for the authenticated drive



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
	artId := "artId_example" // string |  (optional)
	action := "action_example" // string |  (optional)
	since := time.Now() // time.Time |  (optional)
	before := time.Now() // time.Time |  (optional)
	cursor := "cursor_example" // string |  (optional)
	limit := int32(56) // int32 |  (optional) (default to 50)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListEventsRouteV0EventsGet(context.Background()).ArtId(artId).Action(action).Since(since).Before(before).Cursor(cursor).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ListEventsRouteV0EventsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListEventsRouteV0EventsGet`: EventPage
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ListEventsRouteV0EventsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListEventsRouteV0EventsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artId** | **string** |  |
 **action** | **string** |  |
 **since** | **time.Time** |  |
 **before** | **time.Time** |  |
 **cursor** | **string** |  |
 **limit** | **int32** |  | [default to 50]

### Return type

[**EventPage**](EventPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListGrantsRouteV0GrantsGet

> GrantList ListGrantsRouteV0GrantsGet(ctx).Resource(resource).Cursor(cursor).Limit(limit).Execute()

List live grants on a resource (requires can_manage)



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
	resource := "resource_example" // string | art_*_/fld_* id or a path
	cursor := "cursor_example" // string |  (optional)
	limit := int32(56) // int32 |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListGrantsRouteV0GrantsGet(context.Background()).Resource(resource).Cursor(cursor).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ListGrantsRouteV0GrantsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListGrantsRouteV0GrantsGet`: GrantList
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ListGrantsRouteV0GrantsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListGrantsRouteV0GrantsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **string** | art_*_/fld_* id or a path |
 **cursor** | **string** |  |
 **limit** | **int32** |  |

### Return type

[**GrantList**](GrantList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListProjectJobsV0ProjectsFldIdJobsGet

> CompileJobListOut ListProjectJobsV0ProjectsFldIdJobsGet(ctx, fldId).Status(status).Limit(limit).Cursor(cursor).Execute()

List a project's jobs



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
	fldId := "fldId_example" // string |
	status := "status_example" // string |  (optional)
	limit := int32(56) // int32 |  (optional) (default to 50)
	cursor := "cursor_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListProjectJobsV0ProjectsFldIdJobsGet(context.Background(), fldId).Status(status).Limit(limit).Cursor(cursor).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ListProjectJobsV0ProjectsFldIdJobsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListProjectJobsV0ProjectsFldIdJobsGet`: CompileJobListOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ListProjectJobsV0ProjectsFldIdJobsGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiListProjectJobsV0ProjectsFldIdJobsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **status** | **string** |  |
 **limit** | **int32** |  | [default to 50]
 **cursor** | **string** |  |

### Return type

[**CompileJobListOut**](CompileJobListOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSharesRouteV0SharesGet

> ShareList ListSharesRouteV0SharesGet(ctx).Resource(resource).Cursor(cursor).Limit(limit).Execute()

List live share links on a resource (requires can_manage)



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
	resource := "resource_example" // string | art_*_/fld_* id or a path
	cursor := "cursor_example" // string |  (optional)
	limit := int32(56) // int32 |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListSharesRouteV0SharesGet(context.Background()).Resource(resource).Cursor(cursor).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ListSharesRouteV0SharesGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSharesRouteV0SharesGet`: ShareList
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ListSharesRouteV0SharesGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListSharesRouteV0SharesGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **string** | art_*_/fld_* id or a path |
 **cursor** | **string** |  |
 **limit** | **int32** |  |

### Return type

[**ShareList**](ShareList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListTrashRouteV0DrivesDriveIdTrashGet

> TrashOut ListTrashRouteV0DrivesDriveIdTrashGet(ctx, driveId).Cursor(cursor).Limit(limit).Execute()

List the authenticated drive's trash



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
	resp, r, err := apiClient.DefaultAPI.ListTrashRouteV0DrivesDriveIdTrashGet(context.Background(), driveId).Cursor(cursor).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ListTrashRouteV0DrivesDriveIdTrashGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListTrashRouteV0DrivesDriveIdTrashGet`: TrashOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ListTrashRouteV0DrivesDriveIdTrashGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiListTrashRouteV0DrivesDriveIdTrashGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **cursor** | **string** |  |
 **limit** | **int32** |  |

### Return type

[**TrashOut**](TrashOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## LoginAuthLoginGet

> LoginAuthLoginGet(ctx).ReturnTo(returnTo).Execute()

Login



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
	returnTo := "returnTo_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.LoginAuthLoginGet(context.Background()).ReturnTo(returnTo).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.LoginAuthLoginGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiLoginAuthLoginGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returnTo** | **string** |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## LogoutAuthLogoutPost

> LogoutAuthLogoutPost(ctx).Csrf(csrf).Execute()

Logout



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
	csrf := "csrf_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.LogoutAuthLogoutPost(context.Background()).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.LogoutAuthLogoutPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiLogoutAuthLogoutPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **string** |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MeUsageV0DrivesMeUsageGet

> DriveUsageOut MeUsageV0DrivesMeUsageGet(ctx).Execute()

Current-period usage + caps for the authenticated drive



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.MeUsageV0DrivesMeUsageGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.MeUsageV0DrivesMeUsageGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MeUsageV0DrivesMeUsageGet`: DriveUsageOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.MeUsageV0DrivesMeUsageGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiMeUsageV0DrivesMeUsageGetRequest struct via the builder pattern


### Return type

[**DriveUsageOut**](DriveUsageOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MeV0DrivesMeGet

> DriveReadOut MeV0DrivesMeGet(ctx).Execute()

Me



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.MeV0DrivesMeGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.MeV0DrivesMeGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MeV0DrivesMeGet`: DriveReadOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.MeV0DrivesMeGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiMeV0DrivesMeGetRequest struct via the builder pattern


### Return type

[**DriveReadOut**](DriveReadOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MoveArtifactRouteV0ArtifactsArtIdMovePost

> ArtifactOut MoveArtifactRouteV0ArtifactsArtIdMovePost(ctx, artId).ArtifactMoveIn(artifactMoveIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Rename / move an artifact to a new path



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
	artId := "artId_example" // string |
	artifactMoveIn := *openapiclient.NewArtifactMoveIn("Path_example") // ArtifactMoveIn |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.MoveArtifactRouteV0ArtifactsArtIdMovePost(context.Background(), artId).ArtifactMoveIn(artifactMoveIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.MoveArtifactRouteV0ArtifactsArtIdMovePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MoveArtifactRouteV0ArtifactsArtIdMovePost`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.MoveArtifactRouteV0ArtifactsArtIdMovePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiMoveArtifactRouteV0ArtifactsArtIdMovePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **artifactMoveIn** | [**ArtifactMoveIn**](ArtifactMoveIn.md) |  |
 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MoveFolderByIdV0FoldersFldIdMovePost

> FolderOut MoveFolderByIdV0FoldersFldIdMovePost(ctx, fldId).FolderMoveIn(folderMoveIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Rename / move a folder by stable ID (cascade descendants)

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
	fldId := "fldId_example" // string |
	folderMoveIn := *openapiclient.NewFolderMoveIn("Path_example") // FolderMoveIn |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.MoveFolderByIdV0FoldersFldIdMovePost(context.Background(), fldId).FolderMoveIn(folderMoveIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.MoveFolderByIdV0FoldersFldIdMovePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MoveFolderByIdV0FoldersFldIdMovePost`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.MoveFolderByIdV0FoldersFldIdMovePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiMoveFolderByIdV0FoldersFldIdMovePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **folderMoveIn** | [**FolderMoveIn**](FolderMoveIn.md) |  |
 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MoveFolderByPathV0FoldersPathMovePost

> FolderOut MoveFolderByPathV0FoldersPathMovePost(ctx, path).FolderMoveIn(folderMoveIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Rename / move a folder (cascade-update descendants)



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
	path := "path_example" // string |
	folderMoveIn := *openapiclient.NewFolderMoveIn("Path_example") // FolderMoveIn |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.MoveFolderByPathV0FoldersPathMovePost(context.Background(), path).FolderMoveIn(folderMoveIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.MoveFolderByPathV0FoldersPathMovePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MoveFolderByPathV0FoldersPathMovePost`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.MoveFolderByPathV0FoldersPathMovePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiMoveFolderByPathV0FoldersPathMovePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **folderMoveIn** | [**FolderMoveIn**](FolderMoveIn.md) |  |
 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchArtifactRouteV0ArtifactsArtIdPatch

> ArtifactOut PatchArtifactRouteV0ArtifactsArtIdPatch(ctx, artId).ArtifactPatchIn(artifactPatchIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Edit artifact metadata (labels / metadata / source)



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
	artId := "artId_example" // string |
	artifactPatchIn := *openapiclient.NewArtifactPatchIn() // ArtifactPatchIn |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PatchArtifactRouteV0ArtifactsArtIdPatch(context.Background(), artId).ArtifactPatchIn(artifactPatchIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PatchArtifactRouteV0ArtifactsArtIdPatch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchArtifactRouteV0ArtifactsArtIdPatch`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PatchArtifactRouteV0ArtifactsArtIdPatch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiPatchArtifactRouteV0ArtifactsArtIdPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **artifactPatchIn** | [**ArtifactPatchIn**](ArtifactPatchIn.md) |  |
 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchFolderByIdV0FoldersFldIdPatch

> FolderOut PatchFolderByIdV0FoldersFldIdPatch(ctx, fldId).FolderPatchIn(folderPatchIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Update folder metadata by stable ID

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
	fldId := "fldId_example" // string |
	folderPatchIn := *openapiclient.NewFolderPatchIn() // FolderPatchIn |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PatchFolderByIdV0FoldersFldIdPatch(context.Background(), fldId).FolderPatchIn(folderPatchIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PatchFolderByIdV0FoldersFldIdPatch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchFolderByIdV0FoldersFldIdPatch`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PatchFolderByIdV0FoldersFldIdPatch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiPatchFolderByIdV0FoldersFldIdPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **folderPatchIn** | [**FolderPatchIn**](FolderPatchIn.md) |  |
 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchFolderByPathV0FoldersPathPatch

> FolderOut PatchFolderByPathV0FoldersPathPatch(ctx, path).FolderPatchIn(folderPatchIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Update folder metadata by path



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
	path := "path_example" // string |
	folderPatchIn := *openapiclient.NewFolderPatchIn() // FolderPatchIn |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PatchFolderByPathV0FoldersPathPatch(context.Background(), path).FolderPatchIn(folderPatchIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PatchFolderByPathV0FoldersPathPatch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchFolderByPathV0FoldersPathPatch`: FolderOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PatchFolderByPathV0FoldersPathPatch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiPatchFolderByPathV0FoldersPathPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **folderPatchIn** | [**FolderPatchIn**](FolderPatchIn.md) |  |
 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchGrantRouteV0GrantsGrnIdPatch

> GrantOut PatchGrantRouteV0GrantsGrnIdPatch(ctx, grnId).GrantPatchIn(grantPatchIn).XAgentdriveActor(xAgentdriveActor).Execute()

Update a grant's role and/or expiry (requires can_manage)

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
	grnId := "grnId_example" // string |
	grantPatchIn := *openapiclient.NewGrantPatchIn() // GrantPatchIn |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PatchGrantRouteV0GrantsGrnIdPatch(context.Background(), grnId).GrantPatchIn(grantPatchIn).XAgentdriveActor(xAgentdriveActor).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PatchGrantRouteV0GrantsGrnIdPatch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchGrantRouteV0GrantsGrnIdPatch`: GrantOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PatchGrantRouteV0GrantsGrnIdPatch`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**grnId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiPatchGrantRouteV0GrantsGrnIdPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **grantPatchIn** | [**GrantPatchIn**](GrantPatchIn.md) |  |
 **xAgentdriveActor** | **string** |  |

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PostDescribeV0QueryDescribePost

> DatasetDescriptionOut PostDescribeV0QueryDescribePost(ctx).DescribeIn(describeIn).Execute()

Describe a dataset's column schema

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
	describeIn := *openapiclient.NewDescribeIn("Dataset_example") // DescribeIn |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PostDescribeV0QueryDescribePost(context.Background()).DescribeIn(describeIn).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PostDescribeV0QueryDescribePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PostDescribeV0QueryDescribePost`: DatasetDescriptionOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PostDescribeV0QueryDescribePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPostDescribeV0QueryDescribePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describeIn** | [**DescribeIn**](DescribeIn.md) |  |

### Return type

[**DatasetDescriptionOut**](DatasetDescriptionOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PostFeedbackV0FeedbackPost

> FeedbackCreateOut PostFeedbackV0FeedbackPost(ctx).Execute()

Post Feedback



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PostFeedbackV0FeedbackPost(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PostFeedbackV0FeedbackPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PostFeedbackV0FeedbackPost`: FeedbackCreateOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PostFeedbackV0FeedbackPost`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiPostFeedbackV0FeedbackPostRequest struct via the builder pattern


### Return type

[**FeedbackCreateOut**](FeedbackCreateOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PostLookupValuesV0QueryLookupValuesPost

> LookupValuesOut PostLookupValuesV0QueryLookupValuesPost(ctx).LookupValuesIn(lookupValuesIn).Execute()

List distinct values of a dataset column

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
	lookupValuesIn := *openapiclient.NewLookupValuesIn("Column_example", "Dataset_example") // LookupValuesIn |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PostLookupValuesV0QueryLookupValuesPost(context.Background()).LookupValuesIn(lookupValuesIn).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PostLookupValuesV0QueryLookupValuesPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PostLookupValuesV0QueryLookupValuesPost`: LookupValuesOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PostLookupValuesV0QueryLookupValuesPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPostLookupValuesV0QueryLookupValuesPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookupValuesIn** | [**LookupValuesIn**](LookupValuesIn.md) |  |

### Return type

[**LookupValuesOut**](LookupValuesOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PostQueryV0QueryPost

> ResponsePostQueryV0QueryPost PostQueryV0QueryPost(ctx).QueryIn(queryIn).Execute()

Run a read-only SQL query over authorized datasets

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
	queryIn := *openapiclient.NewQueryIn("Sql_example") // QueryIn |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PostQueryV0QueryPost(context.Background()).QueryIn(queryIn).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PostQueryV0QueryPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PostQueryV0QueryPost`: ResponsePostQueryV0QueryPost
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PostQueryV0QueryPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPostQueryV0QueryPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryIn** | [**QueryIn**](QueryIn.md) |  |

### Return type

[**ResponsePostQueryV0QueryPost**](ResponsePostQueryV0QueryPost.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PutArtifactV0ArtifactsPathPut

> ArtifactOut PutArtifactV0ArtifactsPathPut(ctx, path).ContentType(contentType).XAgentdriveLabels(xAgentdriveLabels).XAgentdriveMetadata(xAgentdriveMetadata).XAgentdriveSource(xAgentdriveSource).XAgentdriveActor(xAgentdriveActor).XAgentdriveChangeSummary(xAgentdriveChangeSummary).XAgentdriveChecksum(xAgentdriveChecksum).ContentMd5(contentMd5).IfMatch(ifMatch).IfNoneMatch(ifNoneMatch).Execute()

Upload (or overwrite) an artifact



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
	path := "path_example" // string |
	contentType := "contentType_example" // string |  (optional) (default to "application/octet-stream")
	xAgentdriveLabels := "xAgentdriveLabels_example" // string |  (optional)
	xAgentdriveMetadata := "xAgentdriveMetadata_example" // string |  (optional)
	xAgentdriveSource := "xAgentdriveSource_example" // string |  (optional)
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	xAgentdriveChangeSummary := "xAgentdriveChangeSummary_example" // string |  (optional)
	xAgentdriveChecksum := "xAgentdriveChecksum_example" // string |  (optional)
	contentMd5 := "contentMd5_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)
	ifNoneMatch := "ifNoneMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PutArtifactV0ArtifactsPathPut(context.Background(), path).ContentType(contentType).XAgentdriveLabels(xAgentdriveLabels).XAgentdriveMetadata(xAgentdriveMetadata).XAgentdriveSource(xAgentdriveSource).XAgentdriveActor(xAgentdriveActor).XAgentdriveChangeSummary(xAgentdriveChangeSummary).XAgentdriveChecksum(xAgentdriveChecksum).ContentMd5(contentMd5).IfMatch(ifMatch).IfNoneMatch(ifNoneMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PutArtifactV0ArtifactsPathPut``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PutArtifactV0ArtifactsPathPut`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PutArtifactV0ArtifactsPathPut`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiPutArtifactV0ArtifactsPathPutRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **contentType** | **string** |  | [default to &quot;application/octet-stream&quot;]
 **xAgentdriveLabels** | **string** |  |
 **xAgentdriveMetadata** | **string** |  |
 **xAgentdriveSource** | **string** |  |
 **xAgentdriveActor** | **string** |  |
 **xAgentdriveChangeSummary** | **string** |  |
 **xAgentdriveChecksum** | **string** |  |
 **contentMd5** | **string** |  |
 **ifMatch** | **string** |  |
 **ifNoneMatch** | **string** |  |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PutProjectV0ProjectsFldIdPut

> CompileProjectOut PutProjectV0ProjectsFldIdPut(ctx, fldId).ProjectConfigIn(projectConfigIn).Execute()

Set a project's compile config (entrypoint/engine/auto_compile)

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
	fldId := "fldId_example" // string |
	projectConfigIn := *openapiclient.NewProjectConfigIn("Entrypoint_example") // ProjectConfigIn |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PutProjectV0ProjectsFldIdPut(context.Background(), fldId).ProjectConfigIn(projectConfigIn).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PutProjectV0ProjectsFldIdPut``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PutProjectV0ProjectsFldIdPut`: CompileProjectOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PutProjectV0ProjectsFldIdPut`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiPutProjectV0ProjectsFldIdPutRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **projectConfigIn** | [**ProjectConfigIn**](ProjectConfigIn.md) |  |

### Return type

[**CompileProjectOut**](CompileProjectOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RedeemShareSShareKeyGet

> ShareRedeemOut RedeemShareSShareKeyGet(ctx, shareKey).Execute()

Redeem Share

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
	shareKey := "shareKey_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RedeemShareSShareKeyGet(context.Background(), shareKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RedeemShareSShareKeyGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RedeemShareSShareKeyGet`: ShareRedeemOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RedeemShareSShareKeyGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**shareKey** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiRedeemShareSShareKeyGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ShareRedeemOut**](ShareRedeemOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RedeemShareWithPasswordSShareKeyPost

> ShareRedeemOut RedeemShareWithPasswordSShareKeyPost(ctx, shareKey).Password(password).Execute()

Redeem Share With Password

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
	shareKey := "shareKey_example" // string |
	password := "password_example" // string |  (optional) (default to "")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RedeemShareWithPasswordSShareKeyPost(context.Background(), shareKey).Password(password).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RedeemShareWithPasswordSShareKeyPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RedeemShareWithPasswordSShareKeyPost`: ShareRedeemOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RedeemShareWithPasswordSShareKeyPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**shareKey** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiRedeemShareWithPasswordSShareKeyPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **password** | **string** |  | [default to &quot;&quot;]

### Return type

[**ShareRedeemOut**](ShareRedeemOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreArtifactV0ArtifactsArtIdRestorePost

> ArtifactOut RestoreArtifactV0ArtifactsArtIdRestorePost(ctx, artId).Rename(rename).Overwrite(overwrite).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Restore a soft-deleted artifact



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
	artId := "artId_example" // string |
	rename := "rename_example" // string | Restore at this path instead of the original. Soft-deletes the live occupant at the original path with audit `metadata.cause='restore_conflict_rename'`. Mutually exclusive with `overwrite`. (optional)
	overwrite := true // bool | Soft-delete the live occupant at the original path and restore there. Audit `metadata.cause='restore_conflict_overwrite'`. Mutually exclusive with `rename`. (optional) (default to false)
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RestoreArtifactV0ArtifactsArtIdRestorePost(context.Background(), artId).Rename(rename).Overwrite(overwrite).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RestoreArtifactV0ArtifactsArtIdRestorePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreArtifactV0ArtifactsArtIdRestorePost`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RestoreArtifactV0ArtifactsArtIdRestorePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiRestoreArtifactV0ArtifactsArtIdRestorePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **rename** | **string** | Restore at this path instead of the original. Soft-deletes the live occupant at the original path with audit &#x60;metadata.cause&#x3D;&#39;restore_conflict_rename&#39;&#x60;. Mutually exclusive with &#x60;overwrite&#x60;. |
 **overwrite** | **bool** | Soft-delete the live occupant at the original path and restore there. Audit &#x60;metadata.cause&#x3D;&#39;restore_conflict_overwrite&#39;&#x60;. Mutually exclusive with &#x60;rename&#x60;. | [default to false]
 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost

> ArtifactOut RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost(ctx, artId, versionNumber).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Restore a previous version as a new head version



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
	artId := "artId_example" // string |
	versionNumber := int32(56) // int32 |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost(context.Background(), artId, versionNumber).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost`: ArtifactOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |
**versionNumber** | **int32** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiRestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreDriveRouteV0DrivesDriveIdRestorePost

> DriveRestoreOut RestoreDriveRouteV0DrivesDriveIdRestorePost(ctx, driveId).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Restore a soft-deleted drive



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
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RestoreDriveRouteV0DrivesDriveIdRestorePost(context.Background(), driveId).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RestoreDriveRouteV0DrivesDriveIdRestorePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreDriveRouteV0DrivesDriveIdRestorePost`: DriveRestoreOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RestoreDriveRouteV0DrivesDriveIdRestorePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiRestoreDriveRouteV0DrivesDriveIdRestorePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**DriveRestoreOut**](DriveRestoreOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreFolderByIdV0FoldersFldIdRestorePost

> FolderRestoreOut RestoreFolderByIdV0FoldersFldIdRestorePost(ctx, fldId).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()

Restore a soft-deleted folder (cascade)



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
	fldId := "fldId_example" // string |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	ifMatch := "ifMatch_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RestoreFolderByIdV0FoldersFldIdRestorePost(context.Background(), fldId).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RestoreFolderByIdV0FoldersFldIdRestorePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreFolderByIdV0FoldersFldIdRestorePost`: FolderRestoreOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RestoreFolderByIdV0FoldersFldIdRestorePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiRestoreFolderByIdV0FoldersFldIdRestorePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xAgentdriveActor** | **string** |  |
 **ifMatch** | **string** |  |

### Return type

[**FolderRestoreOut**](FolderRestoreOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RotateShareRouteV0SharesShrIdRotatePost

> ShareMintOut RotateShareRouteV0SharesShrIdRotatePost(ctx, shrId).XAgentdriveActor(xAgentdriveActor).Execute()

Revoke + reissue a share link's key (requires can_share)

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
	shrId := "shrId_example" // string |
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RotateShareRouteV0SharesShrIdRotatePost(context.Background(), shrId).XAgentdriveActor(xAgentdriveActor).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RotateShareRouteV0SharesShrIdRotatePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RotateShareRouteV0SharesShrIdRotatePost`: ShareMintOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RotateShareRouteV0SharesShrIdRotatePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**shrId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiRotateShareRouteV0SharesShrIdRotatePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xAgentdriveActor** | **string** |  |

### Return type

[**ShareMintOut**](ShareMintOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SearchV0SearchGet

> SearchPage SearchV0SearchGet(ctx).Q(q).Label(label).FileType(fileType).Prefix(prefix).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).Limit(limit).Execute()

Full-text search over artifacts in the drive



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
	q := "q_example" // string |
	label := []string{"Inner_example"} // []string |  (optional)
	fileType := "fileType_example" // string |  (optional)
	prefix := "prefix_example" // string |  (optional)
	updatedAfter := time.Now() // time.Time |  (optional)
	updatedBefore := time.Now() // time.Time |  (optional)
	limit := int32(56) // int32 |  (optional) (default to 20)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.SearchV0SearchGet(context.Background()).Q(q).Label(label).FileType(fileType).Prefix(prefix).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.SearchV0SearchGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SearchV0SearchGet`: SearchPage
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.SearchV0SearchGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSearchV0SearchGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **string** |  |
 **label** | **[]string** |  |
 **fileType** | **string** |  |
 **prefix** | **string** |  |
 **updatedAfter** | **time.Time** |  |
 **updatedBefore** | **time.Time** |  |
 **limit** | **int32** |  | [default to 20]

### Return type

[**SearchPage**](SearchPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ViewArtifactHeadAArtIdHeadGet

> ArtifactHeadOut ViewArtifactHeadAArtIdHeadGet(ctx, artId).Execute()

View Artifact Head



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
	artId := "artId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ViewArtifactHeadAArtIdHeadGet(context.Background(), artId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ViewArtifactHeadAArtIdHeadGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ViewArtifactHeadAArtIdHeadGet`: ArtifactHeadOut
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ViewArtifactHeadAArtIdHeadGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiViewArtifactHeadAArtIdHeadGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ArtifactHeadOut**](ArtifactHeadOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ViewArtifactVersionVArtIdVersionGet

> *os.File ViewArtifactVersionVArtIdVersionGet(ctx, artId, version).Raw(raw).Download(download).Execute()

View Artifact Version



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
	artId := "artId_example" // string |
	version := int32(56) // int32 |
	raw := int32(56) // int32 |  (optional) (default to 0)
	download := int32(56) // int32 |  (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ViewArtifactVersionVArtIdVersionGet(context.Background(), artId, version).Raw(raw).Download(download).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ViewArtifactVersionVArtIdVersionGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ViewArtifactVersionVArtIdVersionGet`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ViewArtifactVersionVArtIdVersionGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |
**version** | **int32** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiViewArtifactVersionVArtIdVersionGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **raw** | **int32** |  | [default to 0]
 **download** | **int32** |  | [default to 0]

### Return type

[***os.File**](*os.File.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, text/html, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ViewFileDriveIdPathGet

> *os.File ViewFileDriveIdPathGet(ctx, driveId, path).Raw(raw).Download(download).Execute()

View File

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
	path := "path_example" // string |
	raw := int32(56) // int32 |  (optional) (default to 0)
	download := int32(56) // int32 |  (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ViewFileDriveIdPathGet(context.Background(), driveId, path).Raw(raw).Download(download).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ViewFileDriveIdPathGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ViewFileDriveIdPathGet`: *os.File
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ViewFileDriveIdPathGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  |
**path** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiViewFileDriveIdPathGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **raw** | **int32** |  | [default to 0]
 **download** | **int32** |  | [default to 0]

### Return type

[***os.File**](*os.File.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, text/html, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ViewPermalinkArtifactAArtIdGet

> ViewPermalinkArtifactAArtIdGet(ctx, artId).Execute()

View Permalink Artifact



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
	artId := "artId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.ViewPermalinkArtifactAArtIdGet(context.Background(), artId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ViewPermalinkArtifactAArtIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiViewPermalinkArtifactAArtIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ViewPermalinkFolderFFldIdGet

> ViewPermalinkFolderFFldIdGet(ctx, fldId).Execute()

View Permalink Folder



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
	fldId := "fldId_example" // string |

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DefaultAPI.ViewPermalinkFolderFFldIdGet(context.Background(), fldId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ViewPermalinkFolderFFldIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  |

### Other Parameters

Other parameters are passed through a pointer to a apiViewPermalinkFolderFFldIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)
