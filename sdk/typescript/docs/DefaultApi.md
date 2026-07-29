# DefaultApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**abortUploadV0UploadsUploadIdDelete**](DefaultApi.md#abortuploadv0uploadsuploadiddelete) | **DELETE** /v0/uploads/{upload_id} | Abort a large (direct-to-GCS) upload session |
| [**beginUploadV0UploadsPost**](DefaultApi.md#beginuploadv0uploadspost) | **POST** /v0/uploads | Begin a large (direct-to-GCS) upload |
| [**callbackAuthCallbackGet**](DefaultApi.md#callbackauthcallbackget) | **GET** /auth/callback | Callback |
| [**cancelJobV0JobsJobIdCancelPost**](DefaultApi.md#canceljobv0jobsjobidcancelpost) | **POST** /v0/jobs/{job_id}/cancel | Cancel a queued/running job |
| [**commitUploadV0UploadsUploadIdCommitPost**](DefaultApi.md#commituploadv0uploadsuploadidcommitpost) | **POST** /v0/uploads/{upload_id}/commit | Commit a large (direct-to-GCS) upload |
| [**copyArtifactRouteV0ArtifactsArtIdCopyPost**](DefaultApi.md#copyartifactroutev0artifactsartidcopypost) | **POST** /v0/artifacts/{art_id}/copy | Duplicate an artifact to a new path (CAS-shared, new ID) |
| [**copyFolderByIdV0FoldersFldIdCopyPost**](DefaultApi.md#copyfolderbyidv0foldersfldidcopypost) | **POST** /v0/folders/{fld_id}/copy | Duplicate a folder subtree to a new path (CAS-shared, new IDs) |
| [**createFolderByPathV0FoldersPathPut**](DefaultApi.md#createfolderbypathv0folderspathput) | **PUT** /v0/folders/{path} | Create a folder (idempotent) |
| [**createGrantRouteV0GrantsPost**](DefaultApi.md#creategrantroutev0grantspost) | **POST** /v0/grants | Create (or fetch) a per-principal grant on a resource |
| [**createShareRouteV0SharesPost**](DefaultApi.md#createshareroutev0sharespost) | **POST** /v0/shares | Mint a share link (returns the share_key once) |
| [**deleteArtifactByIdRouteV0ArtifactsArtIdDelete**](DefaultApi.md#deleteartifactbyidroutev0artifactsartiddelete) | **DELETE** /v0/artifacts/{art_id} | Soft-delete an artifact by its stable ID |
| [**deleteArtifactV0ArtifactsPathDelete**](DefaultApi.md#deleteartifactv0artifactspathdelete) | **DELETE** /v0/artifacts/{path} | Delete Artifact |
| [**deleteDriveRouteV0DrivesDriveIdDelete**](DefaultApi.md#deletedriveroutev0drivesdriveiddelete) | **DELETE** /v0/drives/{drive_id} | Soft-delete a drive |
| [**deleteFolderByIdV0FoldersFldIdDelete**](DefaultApi.md#deletefolderbyidv0foldersfldiddelete) | **DELETE** /v0/folders/{fld_id} | Soft-delete a folder by stable ID (cascade with ?recursive&#x3D;true) |
| [**deleteFolderByPathV0FoldersPathDelete**](DefaultApi.md#deletefolderbypathv0folderspathdelete) | **DELETE** /v0/folders/{path} | Soft-delete a folder (cascade with ?recursive&#x3D;true) |
| [**deleteGrantRouteV0GrantsGrnIdDelete**](DefaultApi.md#deletegrantroutev0grantsgrniddelete) | **DELETE** /v0/grants/{grn_id} | Revoke a grant (can_manage, or self-revoke own grant) |
| [**deleteShareRouteV0SharesShrIdDelete**](DefaultApi.md#deleteshareroutev0sharesshriddelete) | **DELETE** /v0/shares/{shr_id} | Revoke a share link (requires can_manage) |
| [**downloadArtifactByIdV0ArtifactsArtIdDownloadGet**](DefaultApi.md#downloadartifactbyidv0artifactsartiddownloadget) | **GET** /v0/artifacts/{art_id}/download | Stream the artifact bytes by stable ID (never rendered HTML) |
| [**downloadArtifactByPathV0ArtifactsPathDownloadGet**](DefaultApi.md#downloadartifactbypathv0artifactspathdownloadget) | **GET** /v0/artifacts/{path}/download | Stream the artifact bytes by path (never rendered HTML) |
| [**downloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet**](DefaultApi.md#downloadartifactversionv0artifactsartidversionsversionnumberdownloadget) | **GET** /v0/artifacts/{art_id}/versions/{version_number}/download | Stream bytes for a specific version (machine surface) |
| [**downloadUrlByIdV0ArtifactsArtIdDownloadUrlGet**](DefaultApi.md#downloadurlbyidv0artifactsartiddownloadurlget) | **GET** /v0/artifacts/{art_id}/download-url | Signed direct-from-GCS download URL by stable ID |
| [**downloadUrlByPathV0ArtifactsPathDownloadUrlGet**](DefaultApi.md#downloadurlbypathv0artifactspathdownloadurlget) | **GET** /v0/artifacts/{path}/download-url | Signed direct-from-GCS download URL by path |
| [**downloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet**](DefaultApi.md#downloadurlversionv0artifactsartidversionsversionnumberdownloadurlget) | **GET** /v0/artifacts/{art_id}/versions/{version_number}/download-url | Signed direct-from-GCS download URL for a specific version |
| [**enqueueJobV0ProjectsFldIdJobsPost**](DefaultApi.md#enqueuejobv0projectsfldidjobspost) | **POST** /v0/projects/{fld_id}/jobs | Enqueue a compile job for a project (folder) |
| [**extensionStartAuthExtensionStartGet**](DefaultApi.md#extensionstartauthextensionstartget) | **GET** /auth/extension/start | Extension Start |
| [**findV0FindGet**](DefaultApi.md#findv0findget) | **GET** /v0/find | Hybrid passage retrieval over the full file body |
| [**getArtifactByIdMetaV0ArtifactsArtIdMetaGet**](DefaultApi.md#getartifactbyidmetav0artifactsartidmetaget) | **GET** /v0/artifacts/{art_id}/meta | Artifact metadata by stable ID (same shape as path /meta) |
| [**getArtifactByIdV0ArtifactsArtIdGet**](DefaultApi.md#getartifactbyidv0artifactsartidget) | **GET** /v0/artifacts/{art_id} | Canonical lookup of an artifact by its stable ID |
| [**getArtifactMetaV0ArtifactsPathMetaGet**](DefaultApi.md#getartifactmetav0artifactspathmetaget) | **GET** /v0/artifacts/{path}/meta | Get Artifact Meta |
| [**getArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet**](DefaultApi.md#getartifactversionv0artifactsartidversionsversionnumberget) | **GET** /v0/artifacts/{art_id}/versions/{version_number} | Metadata for a specific version of an artifact |
| [**getDriveRouteV0DrivesDriveIdGet**](DefaultApi.md#getdriveroutev0drivesdriveidget) | **GET** /v0/drives/{drive_id} | Drive overview by id (same shape as /drives/me) |
| [**getFeedbackStatusV0FeedbackFbkIdGet**](DefaultApi.md#getfeedbackstatusv0feedbackfbkidget) | **GET** /v0/feedback/{fbk_id} | Get Feedback Status |
| [**getFolderByIdMetaV0FoldersFldIdMetaGet**](DefaultApi.md#getfolderbyidmetav0foldersfldidmetaget) | **GET** /v0/folders/{fld_id}/meta | Folder metadata by stable ID (same shape as the bare id route) |
| [**getFolderByIdV0FoldersFldIdGet**](DefaultApi.md#getfolderbyidv0foldersfldidget) | **GET** /v0/folders/{fld_id} | Canonical lookup of a folder by its stable ID |
| [**getFolderByPathMetaV0FoldersPathMetaGet**](DefaultApi.md#getfolderbypathmetav0folderspathmetaget) | **GET** /v0/folders/{path}/meta | Folder metadata by path (same shape as the bare path route) |
| [**getFolderByPathV0FoldersPathGet**](DefaultApi.md#getfolderbypathv0folderspathget) | **GET** /v0/folders/{path} | Read folder metadata by path |
| [**getGrantRouteV0GrantsGrnIdGet**](DefaultApi.md#getgrantroutev0grantsgrnidget) | **GET** /v0/grants/{grn_id} | Read a single grant (can_manage, or the grant\&#39;s own principal) |
| [**getJobLogsV0JobsJobIdLogsGet**](DefaultApi.md#getjoblogsv0jobsjobidlogsget) | **GET** /v0/jobs/{job_id}/logs | Raw compile log (text/plain) |
| [**getJobV0JobsJobIdGet**](DefaultApi.md#getjobv0jobsjobidget) | **GET** /v0/jobs/{job_id} | Poll a job |
| [**getProjectV0ProjectsFldIdGet**](DefaultApi.md#getprojectv0projectsfldidget) | **GET** /v0/projects/{fld_id} | Get a project\&#39;s compile config |
| [**getShareRouteV0SharesShrIdGet**](DefaultApi.md#getshareroutev0sharesshridget) | **GET** /v0/shares/{shr_id} | Read a single share link\&#39;s metadata (requires can_manage) |
| [**getUploadStatusV0UploadsUploadIdGet**](DefaultApi.md#getuploadstatusv0uploadsuploadidget) | **GET** /v0/uploads/{upload_id} | Get the status of a large (direct-to-GCS) upload session |
| [**healthHealthGet**](DefaultApi.md#healthhealthget) | **GET** /health | Health |
| [**listArtifactVersionsV0ArtifactsArtIdVersionsGet**](DefaultApi.md#listartifactversionsv0artifactsartidversionsget) | **GET** /v0/artifacts/{art_id}/versions | List versions of an artifact, newest first |
| [**listArtifactsV0ArtifactsGet**](DefaultApi.md#listartifactsv0artifactsget) | **GET** /v0/artifacts | List artifacts in the drive |
| [**listEventsRouteV0EventsGet**](DefaultApi.md#listeventsroutev0eventsget) | **GET** /v0/events | Read the append-only event log for the authenticated drive |
| [**listGrantsRouteV0GrantsGet**](DefaultApi.md#listgrantsroutev0grantsget) | **GET** /v0/grants | List live grants on a resource (requires can_manage) |
| [**listProjectJobsV0ProjectsFldIdJobsGet**](DefaultApi.md#listprojectjobsv0projectsfldidjobsget) | **GET** /v0/projects/{fld_id}/jobs | List a project\&#39;s jobs |
| [**listSharesRouteV0SharesGet**](DefaultApi.md#listsharesroutev0sharesget) | **GET** /v0/shares | List live share links on a resource (requires can_manage) |
| [**listTrashRouteV0DrivesDriveIdTrashGet**](DefaultApi.md#listtrashroutev0drivesdriveidtrashget) | **GET** /v0/drives/{drive_id}/trash | List the authenticated drive\&#39;s trash |
| [**loginAuthLoginGet**](DefaultApi.md#loginauthloginget) | **GET** /auth/login | Login |
| [**logoutAuthLogoutPost**](DefaultApi.md#logoutauthlogoutpost) | **POST** /auth/logout | Logout |
| [**meUsageV0DrivesMeUsageGet**](DefaultApi.md#meusagev0drivesmeusageget) | **GET** /v0/drives/me/usage | Current-period usage + caps for the authenticated drive |
| [**meV0DrivesMeGet**](DefaultApi.md#mev0drivesmeget) | **GET** /v0/drives/me | Me |
| [**moveArtifactRouteV0ArtifactsArtIdMovePost**](DefaultApi.md#moveartifactroutev0artifactsartidmovepost) | **POST** /v0/artifacts/{art_id}/move | Rename / move an artifact to a new path |
| [**moveFolderByIdV0FoldersFldIdMovePost**](DefaultApi.md#movefolderbyidv0foldersfldidmovepost) | **POST** /v0/folders/{fld_id}/move | Rename / move a folder by stable ID (cascade descendants) |
| [**moveFolderByPathV0FoldersPathMovePost**](DefaultApi.md#movefolderbypathv0folderspathmovepost) | **POST** /v0/folders/{path}/move | Rename / move a folder (cascade-update descendants) |
| [**patchArtifactRouteV0ArtifactsArtIdPatch**](DefaultApi.md#patchartifactroutev0artifactsartidpatch) | **PATCH** /v0/artifacts/{art_id} | Edit artifact metadata (labels / metadata / source) |
| [**patchFolderByIdV0FoldersFldIdPatch**](DefaultApi.md#patchfolderbyidv0foldersfldidpatch) | **PATCH** /v0/folders/{fld_id} | Update folder metadata by stable ID |
| [**patchFolderByPathV0FoldersPathPatch**](DefaultApi.md#patchfolderbypathv0folderspathpatch) | **PATCH** /v0/folders/{path} | Update folder metadata by path |
| [**patchGrantRouteV0GrantsGrnIdPatch**](DefaultApi.md#patchgrantroutev0grantsgrnidpatch) | **PATCH** /v0/grants/{grn_id} | Update a grant\&#39;s role and/or expiry (requires can_manage) |
| [**postDescribeV0QueryDescribePost**](DefaultApi.md#postdescribev0querydescribepost) | **POST** /v0/query/describe | Describe a dataset\&#39;s column schema |
| [**postFeedbackV0FeedbackPost**](DefaultApi.md#postfeedbackv0feedbackpost) | **POST** /v0/feedback | Post Feedback |
| [**postLookupValuesV0QueryLookupValuesPost**](DefaultApi.md#postlookupvaluesv0querylookupvaluespost) | **POST** /v0/query/lookup-values | List distinct values of a dataset column |
| [**postQueryV0QueryPost**](DefaultApi.md#postqueryv0querypost) | **POST** /v0/query | Run a read-only SQL query over authorized datasets |
| [**putArtifactV0ArtifactsPathPut**](DefaultApi.md#putartifactv0artifactspathput) | **PUT** /v0/artifacts/{path} | Upload (or overwrite) an artifact |
| [**putProjectV0ProjectsFldIdPut**](DefaultApi.md#putprojectv0projectsfldidput) | **PUT** /v0/projects/{fld_id} | Set a project\&#39;s compile config (entrypoint/engine/auto_compile) |
| [**redeemShareSShareKeyGet**](DefaultApi.md#redeemsharessharekeyget) | **GET** /s/{share_key} | Redeem Share |
| [**redeemShareWithPasswordSShareKeyPost**](DefaultApi.md#redeemsharewithpasswordssharekeypost) | **POST** /s/{share_key} | Redeem Share With Password |
| [**restoreArtifactV0ArtifactsArtIdRestorePost**](DefaultApi.md#restoreartifactv0artifactsartidrestorepost) | **POST** /v0/artifacts/{art_id}/restore | Restore a soft-deleted artifact |
| [**restoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost**](DefaultApi.md#restoreartifactversionv0artifactsartidversionsversionnumberrestorepost) | **POST** /v0/artifacts/{art_id}/versions/{version_number}/restore | Restore a previous version as a new head version |
| [**restoreDriveRouteV0DrivesDriveIdRestorePost**](DefaultApi.md#restoredriveroutev0drivesdriveidrestorepost) | **POST** /v0/drives/{drive_id}/restore | Restore a soft-deleted drive |
| [**restoreFolderByIdV0FoldersFldIdRestorePost**](DefaultApi.md#restorefolderbyidv0foldersfldidrestorepost) | **POST** /v0/folders/{fld_id}/restore | Restore a soft-deleted folder (cascade) |
| [**rotateShareRouteV0SharesShrIdRotatePost**](DefaultApi.md#rotateshareroutev0sharesshridrotatepost) | **POST** /v0/shares/{shr_id}/rotate | Revoke + reissue a share link\&#39;s key (requires can_share) |
| [**searchV0SearchGet**](DefaultApi.md#searchv0searchget) | **GET** /v0/search | Full-text search over artifacts in the drive |
| [**viewArtifactHeadAArtIdHeadGet**](DefaultApi.md#viewartifactheadaartidheadget) | **GET** /a/{art_id}/head | View Artifact Head |
| [**viewArtifactVersionVArtIdVersionGet**](DefaultApi.md#viewartifactversionvartidversionget) | **GET** /v/{art_id}/{version} | View Artifact Version |
| [**viewFileDriveIdPathGet**](DefaultApi.md#viewfiledriveidpathget) | **GET** /{drive_id}/{path} | View File |
| [**viewPermalinkArtifactAArtIdGet**](DefaultApi.md#viewpermalinkartifactaartidget) | **GET** /a/{art_id} | View Permalink Artifact |
| [**viewPermalinkFolderFFldIdGet**](DefaultApi.md#viewpermalinkfolderffldidget) | **GET** /f/{fld_id} | View Permalink Folder |



## abortUploadV0UploadsUploadIdDelete

> UploadAbortOut abortUploadV0UploadsUploadIdDelete(uploadId)

Abort a large (direct-to-GCS) upload session

Release an open upload session: return its reserved quota to the drive and mark it aborted. Idempotent — aborting an already-aborted or already-expired session succeeds with &#x60;released_bytes: 0&#x60;. A committed session cannot be aborted (409 ALREADY_COMMITTED). No write budget is charged — this frees resources rather than consuming them.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { AbortUploadV0UploadsUploadIdDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    uploadId: uploadId_example,
  } satisfies AbortUploadV0UploadsUploadIdDeleteRequest;

  try {
    const data = await api.abortUploadV0UploadsUploadIdDelete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **uploadId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**UploadAbortOut**](UploadAbortOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No such upload for this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | Upload already committed and cannot be aborted. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## beginUploadV0UploadsPost

> UploadBeginOut beginUploadV0UploadsPost(uploadBeginIn)

Begin a large (direct-to-GCS) upload

Reserve quota and open a resumable upload session for a file larger than the buffered-upload limit. Returns a &#x60;upload_url&#x60; to PUT the raw bytes to DIRECTLY (no Authorization header — the URL is the credential), then call &#x60;/v0/uploads/{upload_id}/commit&#x60;. All artifact decisions (path, labels, metadata, source, if_match) are frozen here.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { BeginUploadV0UploadsPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // UploadBeginIn
    uploadBeginIn: ...,
  } satisfies BeginUploadV0UploadsPostRequest;

  try {
    const data = await api.beginUploadV0UploadsPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **uploadBeginIn** | [UploadBeginIn](UploadBeginIn.md) |  | |

### Return type

[**UploadBeginOut**](UploadBeginOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | Invalid path, labels, metadata, or source. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | Path reserved for the system (WIKI_RESERVED). |  * X-Request-Id - Request correlation identifier. <br>  |
| **413** | size_bytes exceeds the per-artifact cap or storage quota. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Drive\&#39;s per-hour write budget exhausted. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## callbackAuthCallbackGet

> string callbackAuthCallbackGet(code, state, error)

Callback

Complete a sign-in.  Handles the auth provider\&#39;s OAuth callback and shapes failures into user-readable errors:   * an invalid or expired login flow — LOGIN_FLOW_INVALID (400);   * an invalid or already-used authorization code — AUTH_CODE_INVALID (400);   * the upstream auth provider being unavailable — WORKOS_UNAVAILABLE (502),     returned with Retry-After.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CallbackAuthCallbackGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string (optional)
    code: code_example,
    // string (optional)
    state: state_example,
    // string (optional)
    error: error_example,
  } satisfies CallbackAuthCallbackGetRequest;

  try {
    const data = await api.callbackAuthCallbackGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **code** | `string` |  | [Optional] [Defaults to `undefined`] |
| **state** | `string` |  | [Optional] [Defaults to `undefined`] |
| **error** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Extension authentication handoff page. |  * X-Request-Id - Request correlation identifier. <br>  |
| **302** | Redirect to the canonical or authentication URL. |  * Location - Redirect target. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The login flow or authorization code is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | Account recovery is required or the Hub principal conflicts with the existing account link. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **502** | The upstream identity provider is temporarily unavailable. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Extension authentication is temporarily disabled. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## cancelJobV0JobsJobIdCancelPost

> CompileJobOut cancelJobV0JobsJobIdCancelPost(jobId)

Cancel a queued/running job

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CancelJobV0JobsJobIdCancelPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    jobId: jobId_example,
  } satisfies CancelJobV0JobsJobIdCancelPostRequest;

  try {
    const data = await api.cancelJobV0JobsJobIdCancelPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **jobId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**CompileJobOut**](CompileJobOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No such compile job exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## commitUploadV0UploadsUploadIdCommitPost

> ArtifactOut commitUploadV0UploadsUploadIdCommitPost(uploadId)

Commit a large (direct-to-GCS) upload

Finalize the upload begun at &#x60;/v0/uploads&#x60;: AgentDrive verifies the object that landed in GCS (size + checksum) and creates the artifact. Idempotent — a retry after a successful commit returns the same artifact. The write budget is charged when the upload session is created; commit retries are not charged again.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CommitUploadV0UploadsUploadIdCommitPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    uploadId: uploadId_example,
  } satisfies CommitUploadV0UploadsUploadIdCommitPostRequest;

  try {
    const data = await api.commitUploadV0UploadsUploadIdCommitPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **uploadId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No such upload for this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | Uploaded object size differs from declared size_bytes. |  * X-Request-Id - Request correlation identifier. <br>  |
| **410** | Upload session expired. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match precondition failed or create-only conflict. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **413** | Committing the upload would exceed the storage quota. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | Drive\&#39;s per-hour write budget exhausted. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## copyArtifactRouteV0ArtifactsArtIdCopyPost

> ArtifactOut copyArtifactRouteV0ArtifactsArtIdCopyPost(artId, copyIn, xAgentdriveActor, ifNoneMatch)

Duplicate an artifact to a new path (CAS-shared, new ID)

Create a new artifact at &#x60;path&#x60; whose bytes are identical to the source artifact\&#39;s. The copy reuses the source\&#39;s CAS object (zero new storage) but gets a fresh &#x60;art_…&#x60; ID, a fresh version 1, and — by default — &#x60;source.refs &#x3D; [{type: \&#39;artifact\&#39;, id: \&#39;&lt;source&gt;\&#39;}]&#x60; so provenance is preserved.  Quota: the copy\&#39;s &#x60;size_bytes&#x60; is added to the drive\&#39;s &#x60;storage_bytes&#x60; even though physical bytes are shared.  Source-version pin: pass &#x60;from_generation&#x60; in the body to require the source\&#39;s current content generation (&#x60;version_number&#x60;) to equal it (→ 412 SOURCE_VERSION_MISMATCH); a concurrent source *metadata* edit does NOT fail the copy. Destination create-only: &#x60;If-None-Match: *&#x60; returns 412 CREATE_CONFLICT (instead of 409 PATH_CONFLICT) when the target path is occupied.  Returns 409 PATH_CONFLICT if the target path is already taken; 413 STORAGE_QUOTA_EXCEEDED if the copy would push the drive over its limit.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CopyArtifactRouteV0ArtifactsArtIdCopyPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
    // CopyIn
    copyIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifNoneMatch: ifNoneMatch_example,
  } satisfies CopyArtifactRouteV0ArtifactsArtIdCopyPostRequest;

  try {
    const data = await api.copyArtifactRouteV0ArtifactsArtIdCopyPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |
| **copyIn** | [CopyIn](CopyIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifNoneMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The destination path or source metadata is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The source artifact does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The destination path is already occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **413** | The copy would exceed the drive storage limit. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## copyFolderByIdV0FoldersFldIdCopyPost

> FolderCopyOut copyFolderByIdV0FoldersFldIdCopyPost(fldId, folderCopyIn, xAgentdriveActor, ifNoneMatch)

Duplicate a folder subtree to a new path (CAS-shared, new IDs)

Clone the folder identified by URL id — and every descendant folder + artifact — under the body\&#39;s &#x60;path&#x60; (canonical, trailing slash). Each copied artifact reuses the source\&#39;s CAS object (zero new storage) but gets a fresh &#x60;art_…&#x60; ID, a fresh version 1, and &#x60;source.refs &#x3D; [{type: \&#39;artifact\&#39;, id: \&#39;&lt;source&gt;\&#39;}]&#x60; provenance. The new folder gets a fresh &#x60;fld_…&#x60; ID and the source\&#39;s description.  The entire subtree is copied in a SINGLE transaction — either every row lands or none does.  Quota: each copy\&#39;s &#x60;size_bytes&#x60; counts against the drive\&#39;s &#x60;storage_bytes&#x60; even though physical bytes are shared.  Source-version pin: pass &#x60;from_metageneration&#x60; in the body to require the source folder\&#39;s current &#x60;metageneration&#x60; to equal it (→ 412 SOURCE_VERSION_MISMATCH). Destination create-only: &#x60;If-None-Match: *&#x60; returns 412 CREATE_CONFLICT (instead of 409 FOLDER_PATH_CONFLICT) when the destination folder is occupied.  Returns 409 &#x60;FOLDER_PATH_CONFLICT&#x60; if the destination collides with a live folder or artifact; 400 &#x60;FOLDER_PATH_INVALID&#x60; if &#x60;path&#x60; is non-canonical; 413 &#x60;SUBTREE_TOO_LARGE&#x60; if the source holds more than 5000 artifacts; 413 &#x60;STORAGE_QUOTA_EXCEEDED&#x60; if the copy would push the drive over its limit.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CopyFolderByIdV0FoldersFldIdCopyPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    fldId: fldId_example,
    // FolderCopyIn
    folderCopyIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifNoneMatch: ifNoneMatch_example,
  } satisfies CopyFolderByIdV0FoldersFldIdCopyPostRequest;

  try {
    const data = await api.copyFolderByIdV0FoldersFldIdCopyPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fldId** | `string` |  | [Defaults to `undefined`] |
| **folderCopyIn** | [FolderCopyIn](FolderCopyIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifNoneMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderCopyOut**](FolderCopyOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The destination path is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The destination path is already occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **413** | The copied subtree would exceed the drive storage limit. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createFolderByPathV0FoldersPathPut

> FolderOut createFolderByPathV0FoldersPathPut(path, xAgentdriveActor, ifNoneMatch, folderCreateIn)

Create a folder (idempotent)

Create a folder at the URL path. Idempotent create-at-known-URI (mirrors &#x60;PUT /v0/artifacts/{path}&#x60;) — a second call for the same live path returns the existing row unchanged (metadata updates require PATCH). Returns 201 on create, 200 when the folder already exists.  Send &#x60;If-None-Match: *&#x60; to make it strictly create-only: an existing folder then returns 412 CREATE_CONFLICT instead of the idempotent 200.  Returns 409 &#x60;FOLDER_PATH_CONFLICT&#x60; if a live artifact occupies the file form of the path (e.g. mkdir &#x60;/foo/&#x60; when an artifact lives at &#x60;/foo&#x60;).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateFolderByPathV0FoldersPathPutRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    path: path_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifNoneMatch: ifNoneMatch_example,
    // FolderCreateIn (optional)
    folderCreateIn: ...,
  } satisfies CreateFolderByPathV0FoldersPathPutRequest;

  try {
    const data = await api.createFolderByPathV0FoldersPathPut(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | `string` |  | [Defaults to `undefined`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifNoneMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **folderCreateIn** | [FolderCreateIn](FolderCreateIn.md) |  | [Optional] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The existing folder was returned unchanged. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **201** | Successful Response |  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The folder path is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The folder conflicts with an existing path. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createGrantRouteV0GrantsPost

> GrantOut createGrantRouteV0GrantsPost(grantCreateIn, xAgentdriveActor)

Create (or fetch) a per-principal grant on a resource

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateGrantRouteV0GrantsPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // GrantCreateIn
    grantCreateIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
  } satisfies CreateGrantRouteV0GrantsPostRequest;

  try {
    const data = await api.createGrantRouteV0GrantsPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **grantCreateIn** | [GrantCreateIn](GrantCreateIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The grant or expiry is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The target resource does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createShareRouteV0SharesPost

> ShareMintOut createShareRouteV0SharesPost(shareCreateIn, xAgentdriveActor)

Mint a share link (returns the share_key once)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateShareRouteV0SharesPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // ShareCreateIn
    shareCreateIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
  } satisfies CreateShareRouteV0SharesPostRequest;

  try {
    const data = await api.createShareRouteV0SharesPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **shareCreateIn** | [ShareCreateIn](ShareCreateIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ShareMintOut**](ShareMintOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The share settings or expiry are invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The target resource does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteArtifactByIdRouteV0ArtifactsArtIdDelete

> ArtifactDeleteOut deleteArtifactByIdRouteV0ArtifactsArtIdDelete(artId, ifMatch, xAgentdriveActor)

Soft-delete an artifact by its stable ID

Soft-delete the artifact with this &#x60;art_…&#x60; ID. Same semantics + response shape as the path-based &#x60;DELETE /v0/artifacts/{path}&#x60; (reversible until the GC cron hard-deletes at &#x60;purge_at&#x60;; &#x60;restore_url&#x60; points at the by-id restore), but keys on the immutable id so a concurrent rename can\&#39;t change the target.  Returns 404 ARTIFACT_NOT_FOUND if no live artifact has this id; 403 WIKI_RESERVED for &#x60;_wiki/&#x60; artifacts (system-managed); 412 if &#x60;If-Match&#x60; doesn\&#39;t match the current version. Declared before the &#x60;{path:path}&#x60; family so the id convertor wins for DELETEs.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DeleteArtifactByIdRouteV0ArtifactsArtIdDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
    // string (optional)
    ifMatch: ifMatch_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
  } satisfies DeleteArtifactByIdRouteV0ArtifactsArtIdDeleteRequest;

  try {
    const data = await api.deleteArtifactByIdRouteV0ArtifactsArtIdDelete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactDeleteOut**](ArtifactDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No live artifact with this ID exists. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match does not match the current artifact. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteArtifactV0ArtifactsPathDelete

> ArtifactDeleteOut deleteArtifactV0ArtifactsPathDelete(path, ifMatch, xAgentdriveActor)

Delete Artifact

Soft-delete the artifact at the given path.  A delete WITHOUT an &#x60;If-Match&#x60; precondition is last-writer-wins and will silently remove a concurrently-modified artifact.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DeleteArtifactV0ArtifactsPathDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    path: path_example,
    // string (optional)
    ifMatch: ifMatch_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
  } satisfies DeleteArtifactV0ArtifactsPathDeleteRequest;

  try {
    const data = await api.deleteArtifactV0ArtifactsPathDelete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | `string` |  | [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactDeleteOut**](ArtifactDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No such live artifact exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteDriveRouteV0DrivesDriveIdDelete

> DriveDeleteOut deleteDriveRouteV0DrivesDriveIdDelete(driveId, confirm, xAgentdriveActor, ifMatch)

Soft-delete a drive

Mark the drive for cleanup. All tenant data (artifacts, versions, wiki, embeddings, events) is hidden via the &#x60;live_*&#x60; views and CASCADE-removed by the GC cleanup cron at &#x60;purge_at&#x60;. Restore via &#x60;POST /v0/drives/{id}/restore&#x60; while the row is still in trash. The path-param &#x60;drive_id&#x60; MUST match the authenticated drive.  Accepts either an &#x60;ad_live_&#x60; per-drive key (deletes that key\&#39;s drive) or an &#x60;ad_user_&#x60; user token selecting an owned drive (workspaces-design §5.3); a &#x60;read&#x60;-scope user token is rejected with 403 &#x60;INSUFFICIENT_SCOPE&#x60;. **Guard (§8):** a workspace must retain at least one live drive — deleting the workspace\&#39;s last live drive returns 409 &#x60;LAST_DRIVE&#x60;.  **Explicit confirmation required:** pass &#x60;?confirm&#x3D;DELETE&#x60; or the request is rejected with 400 &#x60;CONFIRM_REQUIRED&#x60;. Tenant-level deletion is the largest-blast-radius operation on the API; the static token forces a deliberate act (soft-delete still gives a restore window on top).  **Optimistic concurrency:** send &#x60;If-Match&#x60; with the drive\&#39;s composite ETag (&#x60;\&quot;&lt;drv_id&gt;.0.&lt;metageneration&gt;\&quot;&#x60;, from a drive read) to make the delete conditional — a stale token returns 412 PRECONDITION_FAILED. A delete WITHOUT an &#x60;If-Match&#x60; precondition is last-writer-wins and will silently trash a concurrently-modified drive.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DeleteDriveRouteV0DrivesDriveIdDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string (optional)
    confirm: confirm_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies DeleteDriveRouteV0DrivesDriveIdDeleteRequest;

  try {
    const data = await api.deleteDriveRouteV0DrivesDriveIdDelete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **driveId** | `string` |  | [Defaults to `undefined`] |
| **confirm** | `string` |  | [Optional] [Defaults to `undefined`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveDeleteOut**](DriveDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The explicit DELETE confirmation is missing. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No such drive exists for this principal. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The workspace must retain at least one live drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteFolderByIdV0FoldersFldIdDelete

> FolderDeleteOut deleteFolderByIdV0FoldersFldIdDelete(fldId, recursive, xAgentdriveActor, ifMatch)

Soft-delete a folder by stable ID (cascade with ?recursive&#x3D;true)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DeleteFolderByIdV0FoldersFldIdDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    fldId: fldId_example,
    // boolean (optional)
    recursive: true,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies DeleteFolderByIdV0FoldersFldIdDeleteRequest;

  try {
    const data = await api.deleteFolderByIdV0FoldersFldIdDelete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fldId** | `string` |  | [Defaults to `undefined`] |
| **recursive** | `boolean` |  | [Optional] [Defaults to `false`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderDeleteOut**](FolderDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteFolderByPathV0FoldersPathDelete

> FolderDeleteOut deleteFolderByPathV0FoldersPathDelete(path, recursive, xAgentdriveActor, ifMatch)

Soft-delete a folder (cascade with ?recursive&#x3D;true)

Soft-delete the folder. Refuses if the folder has live descendants unless &#x60;?recursive&#x3D;true&#x60; is set, in which case ALL descendant folders + artifacts are soft-deleted in the same transaction.  Returns 409 &#x60;FOLDER_RECURSIVE_REQUIRED&#x60; (with descendant counts in &#x60;colliding_path&#x60;) when recursion is needed but the flag isn\&#39;t set. Retention window is frozen on &#x60;purge_at&#x60; per deletion-design.md §5.1; mid-retention tier changes don\&#39;t shift it.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DeleteFolderByPathV0FoldersPathDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    path: path_example,
    // boolean (optional)
    recursive: true,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies DeleteFolderByPathV0FoldersPathDeleteRequest;

  try {
    const data = await api.deleteFolderByPathV0FoldersPathDelete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | `string` |  | [Defaults to `undefined`] |
| **recursive** | `boolean` |  | [Optional] [Defaults to `false`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderDeleteOut**](FolderDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteGrantRouteV0GrantsGrnIdDelete

> RevokeOut deleteGrantRouteV0GrantsGrnIdDelete(grnId, xAgentdriveActor)

Revoke a grant (can_manage, or self-revoke own grant)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DeleteGrantRouteV0GrantsGrnIdDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    grnId: grnId_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
  } satisfies DeleteGrantRouteV0GrantsGrnIdDeleteRequest;

  try {
    const data = await api.deleteGrantRouteV0GrantsGrnIdDelete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **grnId** | `string` |  | [Defaults to `undefined`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**RevokeOut**](RevokeOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The grant does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteShareRouteV0SharesShrIdDelete

> RevokeOut deleteShareRouteV0SharesShrIdDelete(shrId, xAgentdriveActor)

Revoke a share link (requires can_manage)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DeleteShareRouteV0SharesShrIdDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    shrId: shrId_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
  } satisfies DeleteShareRouteV0SharesShrIdDeleteRequest;

  try {
    const data = await api.deleteShareRouteV0SharesShrIdDelete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **shrId** | `string` |  | [Defaults to `undefined`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**RevokeOut**](RevokeOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The share does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadArtifactByIdV0ArtifactsArtIdDownloadGet

> Blob downloadArtifactByIdV0ArtifactsArtIdDownloadGet(artId)

Stream the artifact bytes by stable ID (never rendered HTML)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DownloadArtifactByIdV0ArtifactsArtIdDownloadGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
  } satisfies DownloadArtifactByIdV0ArtifactsArtIdDownloadGetRequest;

  try {
    const data = await api.downloadArtifactByIdV0ArtifactsArtIdDownloadGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |

### Return type

**Blob**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/octet-stream`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Raw artifact bytes. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No live artifact with this ID exists. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadArtifactByPathV0ArtifactsPathDownloadGet

> Blob downloadArtifactByPathV0ArtifactsPathDownloadGet(path)

Stream the artifact bytes by path (never rendered HTML)

Same bytes-only machine surface as &#x60;/{art_id}/download&#x60; but resolves the artifact by path, so callers don\&#39;t have to resolve path→id first. Applies the identical CSP &#x60;sandbox&#x60; + &#x60;nosniff&#x60; posture (never serves HTML inline as active content).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DownloadArtifactByPathV0ArtifactsPathDownloadGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    path: path_example,
  } satisfies DownloadArtifactByPathV0ArtifactsPathDownloadGetRequest;

  try {
    const data = await api.downloadArtifactByPathV0ArtifactsPathDownloadGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | `string` |  | [Defaults to `undefined`] |

### Return type

**Blob**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/octet-stream`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Raw artifact bytes. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No live artifact exists at this path. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet

> Blob downloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet(artId, versionNumber)

Stream bytes for a specific version (machine surface)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
    // number
    versionNumber: 56,
  } satisfies DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGetRequest;

  try {
    const data = await api.downloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |
| **versionNumber** | `number` |  | [Defaults to `undefined`] |

### Return type

**Blob**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/octet-stream`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Raw artifact bytes. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The artifact or version does not exist. |  * X-Request-Id - Request correlation identifier. <br>  |
| **410** | The requested version has been pruned. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadUrlByIdV0ArtifactsArtIdDownloadUrlGet

> DownloadUrlOut downloadUrlByIdV0ArtifactsArtIdDownloadUrlGet(artId)

Signed direct-from-GCS download URL by stable ID

Returns a URL for the artifact\&#39;s bytes. For large artifacts (&gt;&#x3D; the signed-download threshold) when signing is available, it\&#39;s a short-lived **signed GCS URL** the client fetches directly (&#x60;direct:true&#x60;, &#x60;expires_at&#x60; set); otherwise the **proxy** &#x60;/download&#x60; URL (&#x60;direct:false&#x60;). Treat the URL as opaque. large-download-design.md §5.1.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
  } satisfies DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGetRequest;

  try {
    const data = await api.downloadUrlByIdV0ArtifactsArtIdDownloadUrlGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The artifact does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadUrlByPathV0ArtifactsPathDownloadUrlGet

> DownloadUrlOut downloadUrlByPathV0ArtifactsPathDownloadUrlGet(path)

Signed direct-from-GCS download URL by path

Same as &#x60;/{art_id}/download-url&#x60; but resolves the artifact by path. The returned proxy URL (when &#x60;direct:false&#x60;) still points at the by-id &#x60;/download&#x60; endpoint. large-download-design.md §5.1.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DownloadUrlByPathV0ArtifactsPathDownloadUrlGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    path: path_example,
  } satisfies DownloadUrlByPathV0ArtifactsPathDownloadUrlGetRequest;

  try {
    const data = await api.downloadUrlByPathV0ArtifactsPathDownloadUrlGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | `string` |  | [Defaults to `undefined`] |

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The artifact does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet

> DownloadUrlOut downloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet(artId, versionNumber)

Signed direct-from-GCS download URL for a specific version

Same as &#x60;/{art_id}/download-url&#x60; but for a specific version\&#39;s bytes (&#x60;direct:true&#x60; signed GCS URL when large + signing available, else the proxy &#x60;/versions/{n}/download&#x60; URL). large-download-design.md §5.1.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
    // number
    versionNumber: 56,
  } satisfies DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGetRequest;

  try {
    const data = await api.downloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |
| **versionNumber** | `number` |  | [Defaults to `undefined`] |

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The artifact or version does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **410** | The requested version was pruned by retention. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## enqueueJobV0ProjectsFldIdJobsPost

> CompileJobOut enqueueJobV0ProjectsFldIdJobsPost(fldId, compileJobIn, xAgentdriveActor)

Enqueue a compile job for a project (folder)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { EnqueueJobV0ProjectsFldIdJobsPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    fldId: fldId_example,
    // CompileJobIn
    compileJobIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
  } satisfies EnqueueJobV0ProjectsFldIdJobsPostRequest;

  try {
    const data = await api.enqueueJobV0ProjectsFldIdJobsPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fldId** | `string` |  | [Defaults to `undefined`] |
| **compileJobIn** | [CompileJobIn](CompileJobIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**CompileJobOut**](CompileJobOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **202** | Compile accepted and queued or running. |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The task, engine, entrypoint, or project is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **402** | The current plan does not permit this compile. |  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The project folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **413** | The compile project exceeds an input or storage limit. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## extensionStartAuthExtensionStartGet

> extensionStartAuthExtensionStartGet(extId)

Extension Start

Begin a sign-in flow on behalf of a Chrome extension.  Provider follows AUTH_MODE (WorkOS AuthKit or the TokenCanopy hub), exactly like /auth/login. Stamps &#x60;for&#x3D;ext&#x60; + &#x60;ext_id&#x60; into the signed OAuth state so the callback handler knows to render the extension handoff page instead of setting a session cookie.  Three short-circuits, all surface as actionable errors:   * EXTENSION_AUTH_DISABLED (503): kill switch flipped off.   * UNKNOWN_EXTENSION (400): &#x60;ext_id&#x60; not on the allow-list.   * Missing &#x60;ext_id&#x60; query string (400 INVALID_REQUEST).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ExtensionStartAuthExtensionStartGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string (optional)
    extId: extId_example,
  } satisfies ExtensionStartAuthExtensionStartGetRequest;

  try {
    const data = await api.extensionStartAuthExtensionStartGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **extId** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Redirect to the canonical or authentication URL. |  * Location - Redirect target. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The extension ID is missing or not allowed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Extension authentication is temporarily disabled. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## findV0FindGet

> FindPage findV0FindGet(q, mode, label, fileType, prefix, modality, updatedAfter, updatedBefore, limit)

Hybrid passage retrieval over the full file body

Passage-level chunk RAG over &#x60;embed_chunks&#x60;. Lexical (&#x60;chunk_tsv&#x60;, GIN) + semantic (HNSW over &#x60;embedding&#x60;) are run in parallel and fused via Reciprocal Rank Fusion (k&#x3D;60). Unlike &#x60;/v0/search&#x60;, which only sees the first ~16 KB preview of each artifact, &#x60;/v0/find&#x60; reaches the full file body.  **Modes:** - &#x60;hybrid&#x60; (default) — lexical + semantic, RRF-fused. - &#x60;lexical&#x60; — &#x60;chunk_tsv&#x60; only. Best for exact tokens, identifiers, code snippets. - &#x60;semantic&#x60; — embedding only. Best for conceptual queries where the surface terms differ from the query phrasing.  **Granularity:** results are passages, not files. A long document with multiple matching regions returns multiple hits with distinct &#x60;ord&#x60; values; consecutive &#x60;ord&#x60;s overlap by ~400 tokens. Dedupe by &#x60;art_id&#x60; if you want one row per file.  **Span citations:** &#x60;char_start&#x60;/&#x60;char_end&#x60; for text &amp; code, &#x60;page_start&#x60;/&#x60;page_end&#x60; for PDFs, &#x60;time_start_ms&#x60;/&#x60;time_end_ms&#x60; for audio &amp; video. Only the modality-relevant pair is populated.  **Filters:** &#x60;label&#x60;, &#x60;file_type&#x60;, &#x60;prefix&#x60;, &#x60;modality&#x60; (repeatable), &#x60;updated_after&#x60; / &#x60;updated_before&#x60; (RFC 3339 timestamps, inclusive bounds on &#x60;updated_at&#x60;, applied to both legs).  **Wiki coverage:** &#x60;/v0/find&#x60; excludes &#x60;_wiki/&#x60; paths by default and — importantly — does NOT cover them even when the caller passes &#x60;prefix&#x3D;_wiki/...&#x60;. Wiki pages are not embedded by the pipeline (they\&#39;re system-generated output, not user input), so &#x60;embed_chunks&#x60; has no rows for them and the join returns empty. Use &#x60;wiki_search&#x60; (or &#x60;list&#x60;/&#x60;grep&#x60; with a &#x60;_wiki/&#x60; prefix) for the wiki layer.  **Embedding availability:** when &#x60;GEMINI_API_KEY&#x60; is not configured, &#x60;mode&#x3D;semantic&#x60; returns 503; &#x60;mode&#x3D;hybrid&#x60; logs a warning and falls back to lexical-only; &#x60;mode&#x3D;lexical&#x60; is unaffected.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { FindV0FindGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    q: q_example,
    // 'hybrid' | 'lexical' | 'semantic' (optional)
    mode: mode_example,
    // Array<string> (optional)
    label: ...,
    // string (optional)
    fileType: fileType_example,
    // string (optional)
    prefix: prefix_example,
    // Array<string> (optional)
    modality: ...,
    // Date (optional)
    updatedAfter: 2013-10-20T19:20:30+01:00,
    // Date (optional)
    updatedBefore: 2013-10-20T19:20:30+01:00,
    // number (optional)
    limit: 56,
  } satisfies FindV0FindGetRequest;

  try {
    const data = await api.findV0FindGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **q** | `string` |  | [Defaults to `undefined`] |
| **mode** | `hybrid`, `lexical`, `semantic` |  | [Optional] [Defaults to `&#39;hybrid&#39;`] [Enum: hybrid, lexical, semantic] |
| **label** | `Array<string>` |  | [Optional] |
| **fileType** | `string` |  | [Optional] [Defaults to `undefined`] |
| **prefix** | `string` |  | [Optional] [Defaults to `undefined`] |
| **modality** | `Array<string>` |  | [Optional] |
| **updatedAfter** | `Date` |  | [Optional] [Defaults to `undefined`] |
| **updatedBefore** | `Date` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `20`] |

### Return type

[**FindPage**](FindPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | Semantic embeddings are unavailable; use lexical or hybrid mode. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getArtifactByIdMetaV0ArtifactsArtIdMetaGet

> ArtifactOut getArtifactByIdMetaV0ArtifactsArtIdMetaGet(artId)

Artifact metadata by stable ID (same shape as path /meta)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetArtifactByIdMetaV0ArtifactsArtIdMetaGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
  } satisfies GetArtifactByIdMetaV0ArtifactsArtIdMetaGetRequest;

  try {
    const data = await api.getArtifactByIdMetaV0ArtifactsArtIdMetaGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No such artifact exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getArtifactByIdV0ArtifactsArtIdGet

> ArtifactOut getArtifactByIdV0ArtifactsArtIdGet(artId)

Canonical lookup of an artifact by its stable ID

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetArtifactByIdV0ArtifactsArtIdGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
  } satisfies GetArtifactByIdV0ArtifactsArtIdGetRequest;

  try {
    const data = await api.getArtifactByIdV0ArtifactsArtIdGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No such artifact exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getArtifactMetaV0ArtifactsPathMetaGet

> ArtifactOut getArtifactMetaV0ArtifactsPathMetaGet(path)

Get Artifact Meta

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetArtifactMetaV0ArtifactsPathMetaGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    path: path_example,
  } satisfies GetArtifactMetaV0ArtifactsPathMetaGetRequest;

  try {
    const data = await api.getArtifactMetaV0ArtifactsPathMetaGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The artifact does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet

> VersionOut getArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet(artId, versionNumber)

Metadata for a specific version of an artifact

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
    // number
    versionNumber: 56,
  } satisfies GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGetRequest;

  try {
    const data = await api.getArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |
| **versionNumber** | `number` |  | [Defaults to `undefined`] |

### Return type

[**VersionOut**](VersionOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The artifact or version does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **410** | The requested version was pruned by retention. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getDriveRouteV0DrivesDriveIdGet

> DriveReadOut getDriveRouteV0DrivesDriveIdGet(driveId)

Drive overview by id (same shape as /drives/me)

Identical to &#x60;GET /v0/drives/me&#x60; — the by-id singleton so &#x60;Location&#x60;-style URLs and scripted clients can address the drive canonically. The path-param &#x60;drive_id&#x60; MUST match the authenticated drive (mirrors the delete/trash routes\&#39; no-leak 404). Emits the drive\&#39;s composite &#x60;ETag&#x60; header (&#x60;\&quot;&lt;drv_id&gt;.0.&lt;metageneration&gt;\&quot;&#x60;).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetDriveRouteV0DrivesDriveIdGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    driveId: driveId_example,
  } satisfies GetDriveRouteV0DrivesDriveIdGetRequest;

  try {
    const data = await api.getDriveRouteV0DrivesDriveIdGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **driveId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**DriveReadOut**](DriveReadOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No matching authenticated drive exists. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFeedbackStatusV0FeedbackFbkIdGet

> FeedbackStatusOut getFeedbackStatusV0FeedbackFbkIdGet(fbkId)

Get Feedback Status

Lifecycle status of feedback THIS drive filed. Foreign tickets read as 404 — indistinguishable from absent.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetFeedbackStatusV0FeedbackFbkIdGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    fbkId: fbkId_example,
  } satisfies GetFeedbackStatusV0FeedbackFbkIdGetRequest;

  try {
    const data = await api.getFeedbackStatusV0FeedbackFbkIdGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fbkId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**FeedbackStatusOut**](FeedbackStatusOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The feedback ticket does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFolderByIdMetaV0FoldersFldIdMetaGet

> FolderOut getFolderByIdMetaV0FoldersFldIdMetaGet(fldId)

Folder metadata by stable ID (same shape as the bare id route)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetFolderByIdMetaV0FoldersFldIdMetaGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    fldId: fldId_example,
  } satisfies GetFolderByIdMetaV0FoldersFldIdMetaGetRequest;

  try {
    const data = await api.getFolderByIdMetaV0FoldersFldIdMetaGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fldId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFolderByIdV0FoldersFldIdGet

> FolderOut getFolderByIdV0FoldersFldIdGet(fldId)

Canonical lookup of a folder by its stable ID

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetFolderByIdV0FoldersFldIdGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    fldId: fldId_example,
  } satisfies GetFolderByIdV0FoldersFldIdGetRequest;

  try {
    const data = await api.getFolderByIdV0FoldersFldIdGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fldId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFolderByPathMetaV0FoldersPathMetaGet

> FolderOut getFolderByPathMetaV0FoldersPathMetaGet(path)

Folder metadata by path (same shape as the bare path route)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetFolderByPathMetaV0FoldersPathMetaGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    path: path_example,
  } satisfies GetFolderByPathMetaV0FoldersPathMetaGetRequest;

  try {
    const data = await api.getFolderByPathMetaV0FoldersPathMetaGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | `string` |  | [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFolderByPathV0FoldersPathGet

> FolderOut getFolderByPathV0FoldersPathGet(path)

Read folder metadata by path

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetFolderByPathV0FoldersPathGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    path: path_example,
  } satisfies GetFolderByPathV0FoldersPathGetRequest;

  try {
    const data = await api.getFolderByPathV0FoldersPathGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | `string` |  | [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getGrantRouteV0GrantsGrnIdGet

> GrantOut getGrantRouteV0GrantsGrnIdGet(grnId)

Read a single grant (can_manage, or the grant\&#39;s own principal)

The &#x60;Location&#x60; target of &#x60;POST /v0/grants&#x60;. Authorization mirrors DELETE: &#x60;can_manage&#x60; on the granted resource, or the caller IS the grant\&#39;s own principal (a grantee may read — like revoke — their own grant). A revoked grant reads as 404 (same no-leak shape as a foreign/absent id); DELETE stays idempotent on it.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetGrantRouteV0GrantsGrnIdGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    grnId: grnId_example,
  } satisfies GetGrantRouteV0GrantsGrnIdGetRequest;

  try {
    const data = await api.getGrantRouteV0GrantsGrnIdGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **grnId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The grant does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getJobLogsV0JobsJobIdLogsGet

> string getJobLogsV0JobsJobIdLogsGet(jobId)

Raw compile log (text/plain)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetJobLogsV0JobsJobIdLogsGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    jobId: jobId_example,
  } satisfies GetJobLogsV0JobsJobIdLogsGetRequest;

  try {
    const data = await api.getJobLogsV0JobsJobIdLogsGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **jobId** | `string` |  | [Defaults to `undefined`] |

### Return type

**string**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/plain`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Raw compile log. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The job or its captured log does not exist. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getJobV0JobsJobIdGet

> CompileJobOut getJobV0JobsJobIdGet(jobId)

Poll a job

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetJobV0JobsJobIdGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    jobId: jobId_example,
  } satisfies GetJobV0JobsJobIdGetRequest;

  try {
    const data = await api.getJobV0JobsJobIdGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **jobId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**CompileJobOut**](CompileJobOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No such compile job exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getProjectV0ProjectsFldIdGet

> CompileProjectOut getProjectV0ProjectsFldIdGet(fldId)

Get a project\&#39;s compile config

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetProjectV0ProjectsFldIdGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    fldId: fldId_example,
  } satisfies GetProjectV0ProjectsFldIdGetRequest;

  try {
    const data = await api.getProjectV0ProjectsFldIdGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fldId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**CompileProjectOut**](CompileProjectOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The project folder does not exist or has no compile configuration. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getShareRouteV0SharesShrIdGet

> ShareOut getShareRouteV0SharesShrIdGet(shrId)

Read a single share link\&#39;s metadata (requires can_manage)

The &#x60;Location&#x60; target of &#x60;POST /v0/shares&#x60;. Metadata ONLY — &#x60;ShareOut&#x60; never carries the raw &#x60;share_key&#x60;/URL (returned exactly once at mint/rotate, §4.5). Authorization mirrors DELETE: &#x60;can_manage&#x60; on the shared resource. A revoked share reads as 404 (same no-leak shape as a foreign/absent id).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetShareRouteV0SharesShrIdGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    shrId: shrId_example,
  } satisfies GetShareRouteV0SharesShrIdGetRequest;

  try {
    const data = await api.getShareRouteV0SharesShrIdGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **shrId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ShareOut**](ShareOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The share does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getUploadStatusV0UploadsUploadIdGet

> UploadStatusOut getUploadStatusV0UploadsUploadIdGet(uploadId)

Get the status of a large (direct-to-GCS) upload session

Report the live state of an upload session begun at &#x60;/v0/uploads&#x60;. &#x60;state&#x60; is derived: &#x60;initiated&#x60; (open — PUT the bytes then commit), &#x60;committed&#x60; (artifact created), &#x60;aborted&#x60; (released via DELETE), or &#x60;expired&#x60; (past &#x60;expires_at&#x60; without a commit). Read-only; charges the read budget.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetUploadStatusV0UploadsUploadIdGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    uploadId: uploadId_example,
  } satisfies GetUploadStatusV0UploadsUploadIdGetRequest;

  try {
    const data = await api.getUploadStatusV0UploadsUploadIdGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **uploadId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**UploadStatusOut**](UploadStatusOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No such upload for this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## healthHealthGet

> HealthOut healthHealthGet()

Health

Liveness + DB-reachability probe. Used by Cloud Run / k8s healthchecks and any uptime monitor. Returns 200 only if the DB pool can serve a trivial query; 503 otherwise so the orchestrator can pull the instance out of rotation.  NOTE: route is &#x60;/health&#x60;, NOT &#x60;/healthz&#x60;. Google\&#39;s edge infrastructure intercepts &#x60;/healthz&#x60; (legacy kubernetes-reserved path) and returns a generic 404 before traffic reaches Cloud Run — discovered the hard way during the first prod deploy. Don\&#39;t rename back.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { HealthHealthGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.healthHealthGet();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthOut**](HealthOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | The database reachability probe failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listArtifactVersionsV0ArtifactsArtIdVersionsGet

> VersionPage listArtifactVersionsV0ArtifactsArtIdVersionsGet(artId, cursor, limit)

List versions of an artifact, newest first

Returns versions in descending &#x60;version_number&#x60; order. Cursor pagination via &#x60;?cursor&#x3D;&lt;token&gt;&#x60;; &#x60;next_cursor&#x60; is non-null when the page is full and more older versions may exist.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListArtifactVersionsV0ArtifactsArtIdVersionsGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
  } satisfies ListArtifactVersionsV0ArtifactsArtIdVersionsGetRequest;

  try {
    const data = await api.listArtifactVersionsV0ArtifactsArtIdVersionsGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `50`] |

### Return type

[**VersionPage**](VersionPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The pagination cursor is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The artifact does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listArtifactsV0ArtifactsGet

> Page listArtifactsV0ArtifactsGet(prefix, label, fileType, cursor, limit)

List artifacts in the drive

Returns artifacts sorted by path. Filter by &#x60;prefix&#x60;, &#x60;label&#x60; (repeatable + AND-combined), and &#x60;file_type&#x60;.  **Cursor pagination:** when more results exist, the response carries &#x60;next_cursor&#x60;. Pass it back as &#x60;?cursor&#x3D;&lt;token&gt;&#x60; to fetch the next page. &#x60;next_cursor&#x60; is &#x60;null&#x60; on the final page. Filters MUST stay consistent across pages — the cursor encodes only the keyset position, not the filter set, so the client is responsible for re-sending the same filter on each page.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListArtifactsV0ArtifactsGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string (optional)
    prefix: prefix_example,
    // Array<string> (optional)
    label: ...,
    // string (optional)
    fileType: fileType_example,
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
  } satisfies ListArtifactsV0ArtifactsGetRequest;

  try {
    const data = await api.listArtifactsV0ArtifactsGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **prefix** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **label** | `Array<string>` |  | [Optional] |
| **fileType** | `string` |  | [Optional] [Defaults to `undefined`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `50`] |

### Return type

[**Page**](Page.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The pagination cursor is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listEventsRouteV0EventsGet

> EventPage listEventsRouteV0EventsGet(artId, action, since, before, cursor, limit)

Read the append-only event log for the authenticated drive

Returns events newest-first. Filters compose with AND.  **Cursor pagination:** pass the oldest event\&#39;s &#x60;created_at&#x60; from the previous page as &#x60;before&#x60; to fetch the next page back in time. Combine &#x60;since&#x60; + &#x60;before&#x60; to bound a window.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListEventsRouteV0EventsGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string (optional)
    artId: artId_example,
    // string (optional)
    action: action_example,
    // Date (optional)
    since: 2013-10-20T19:20:30+01:00,
    // Date (optional)
    before: 2013-10-20T19:20:30+01:00,
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
  } satisfies ListEventsRouteV0EventsGetRequest;

  try {
    const data = await api.listEventsRouteV0EventsGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Optional] [Defaults to `undefined`] |
| **action** | `string` |  | [Optional] [Defaults to `undefined`] |
| **since** | `Date` |  | [Optional] [Defaults to `undefined`] |
| **before** | `Date` |  | [Optional] [Defaults to `undefined`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `50`] |

### Return type

[**EventPage**](EventPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The pagination cursor is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listGrantsRouteV0GrantsGet

> GrantList listGrantsRouteV0GrantsGet(resource, cursor, limit)

List live grants on a resource (requires can_manage)

**Cursor pagination:** when more results exist, the response carries &#x60;next_cursor&#x60;. Pass it back as &#x60;?cursor&#x3D;&lt;token&gt;&#x60; to fetch the next page; &#x60;null&#x60; means the listing is complete. &#x60;limit&#x60; is clamped to [1, 100] (default 50), never rejected. The &#x60;resource&#x60; filter must be re-sent on every page — the cursor encodes only the keyset position.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListGrantsRouteV0GrantsGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string | art_*_/fld_* id or a path
    resource: resource_example,
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
  } satisfies ListGrantsRouteV0GrantsGetRequest;

  try {
    const data = await api.listGrantsRouteV0GrantsGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource** | `string` | art_*_/fld_* id or a path | [Defaults to `undefined`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**GrantList**](GrantList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The cursor or resource reference is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The target resource does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listProjectJobsV0ProjectsFldIdJobsGet

> CompileJobListOut listProjectJobsV0ProjectsFldIdJobsGet(fldId, status, limit, cursor)

List a project\&#39;s jobs

List compile jobs newest first in stable &#x60;(created_at, job_id)&#x60; descending order. Pass a non-null &#x60;next_cursor&#x60; back as &#x60;cursor&#x60; to continue; malformed cursors return &#x60;400 BAD_CURSOR&#x60;. The cursor contains only the keyset position, so a &#x60;status&#x60; filter must be re-sent unchanged on every page. &#x60;limit&#x60; retains its existing default of 50 and validated range of 1 through 200.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListProjectJobsV0ProjectsFldIdJobsGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    fldId: fldId_example,
    // string (optional)
    status: status_example,
    // number (optional)
    limit: 56,
    // string (optional)
    cursor: cursor_example,
  } satisfies ListProjectJobsV0ProjectsFldIdJobsGetRequest;

  try {
    const data = await api.listProjectJobsV0ProjectsFldIdJobsGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fldId** | `string` |  | [Defaults to `undefined`] |
| **status** | `string` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `50`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**CompileJobListOut**](CompileJobListOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The status filter is invalid, or the cursor is malformed (&#x60;BAD_CURSOR&#x60;). |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The project folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSharesRouteV0SharesGet

> ShareList listSharesRouteV0SharesGet(resource, cursor, limit)

List live share links on a resource (requires can_manage)

**Cursor pagination:** when more results exist, the response carries &#x60;next_cursor&#x60;. Pass it back as &#x60;?cursor&#x3D;&lt;token&gt;&#x60; to fetch the next page; &#x60;null&#x60; means the listing is complete. &#x60;limit&#x60; is clamped to [1, 100] (default 50), never rejected. The &#x60;resource&#x60; filter must be re-sent on every page — the cursor encodes only the keyset position.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListSharesRouteV0SharesGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string | art_*_/fld_* id or a path
    resource: resource_example,
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
  } satisfies ListSharesRouteV0SharesGetRequest;

  try {
    const data = await api.listSharesRouteV0SharesGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource** | `string` | art_*_/fld_* id or a path | [Defaults to `undefined`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ShareList**](ShareList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The cursor or resource reference is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The target resource does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listTrashRouteV0DrivesDriveIdTrashGet

> TrashOut listTrashRouteV0DrivesDriveIdTrashGet(driveId, cursor, limit)

List the authenticated drive\&#39;s trash

Returns soft-deleted artifacts on the drive plus the drive\&#39;s own soft-delete state (if applicable). The path-param &#x60;drive_id&#x60; MUST match the authenticated drive.  **Compatibility window:** &#x60;limit&#x60; or &#x60;cursor&#x60; opts into cursor pagination. Unadorned requests retain the legacy complete result during the migration window. Paginated requests are clamped to 1–100 items (default 50 when only &#x60;cursor&#x60; is supplied). &#x60;items&#x60; is canonical; &#x60;artifacts&#x60; is a deprecated same-value alias.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListTrashRouteV0DrivesDriveIdTrashGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
  } satisfies ListTrashRouteV0DrivesDriveIdTrashGetRequest;

  try {
    const data = await api.listTrashRouteV0DrivesDriveIdTrashGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **driveId** | `string` |  | [Defaults to `undefined`] |
| **cursor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**TrashOut**](TrashOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The cursor is malformed (&#x60;BAD_CURSOR&#x60;). |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No matching authenticated drive exists. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## loginAuthLoginGet

> loginAuthLoginGet(returnTo)

Login

Begin a WorkOS sign-in flow.  Mints a pre-login state cookie (binds the OAuth flow to this browser — defense-in-depth against login-CSRF), signs a state payload, and redirects to AuthKit. The hosted AuthKit page lets the user pick Google OAuth, Microsoft OAuth, magic-link, password, or passkey; we don\&#39;t care which — they all funnel back to /auth/callback with a &#x60;code&#x60; we exchange in D2.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { LoginAuthLoginGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string (optional)
    returnTo: returnTo_example,
  } satisfies LoginAuthLoginGetRequest;

  try {
    const data = await api.loginAuthLoginGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **returnTo** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Redirect to the canonical or authentication URL. |  * Location - Redirect target. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## logoutAuthLogoutPost

> logoutAuthLogoutPost(csrf)

Logout

Terminate both the local session AND the upstream WorkOS session.  Without the WorkOS-side termination, the next &#x60;/auth/login&#x60; flow silently re-authenticates the user through AuthKit\&#39;s still-valid session cookie on &#x60;api.workos.com&#x60; — \&quot;Sign out\&quot; feels broken and a shared-browser user can\&#39;t switch accounts. The recommended pattern (per https://workos.com/docs/authkit/sessions) is to redirect to the WorkOS logout endpoint with the &#x60;sid&#x60; we stashed during the callback; WorkOS clears its own session and returns the browser to our &#x60;return_to&#x60;.  Failure modes handled:   * No &#x60;workos_session_id&#x60; in the session (legacy v2 cookie issued     before this slice landed): fall back to local-only logout. The     upstream session lingers but the user\&#39;s local state is cleared     — same UX as before this slice; cookie rotation on next sign-in     eventually overwrites it.   * SDK raises during &#x60;get_logout_url&#x60;: pure string formatting at     WorkOS\&#39;s end, so the only realistic failure is a misconfigured     WorkOS dashboard (no Sign-out redirect registered). We catch     and fall back to local-only logout rather than 500ing — the     user clicked \&quot;Sign out\&quot;, they should land somewhere, not on an     error page.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { LogoutAuthLogoutPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    csrf: csrf_example,
  } satisfies LogoutAuthLogoutPostRequest;

  try {
    const data = await api.logoutAuthLogoutPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Redirect to the canonical or authentication URL. |  * Location - Redirect target. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The browser CSRF check failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## meUsageV0DrivesMeUsageGet

> DriveUsageOut meUsageV0DrivesMeUsageGet()

Current-period usage + caps for the authenticated drive

Unified view of every metered dimension: storage (snapshot), writes (current hour), indexing ops + retrieval queries (current calendar month UTC). Each row carries &#x60;used&#x60; and &#x60;limit&#x60;; &#x60;limit: 0&#x60; means unlimited (the v0 free-tier default for the two monthly counters). Reads are de-throttled — there is no hourly read budget; the monthly read count appears under &#x60;ops_this_month.reads&#x60;.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { MeUsageV0DrivesMeUsageGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  try {
    const data = await api.meUsageV0DrivesMeUsageGet();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**DriveUsageOut**](DriveUsageOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## meV0DrivesMeGet

> DriveReadOut meV0DrivesMeGet()

Me

Drive overview for the authenticated bearer token.  Wire-protocol preservation (WorkOS integration §6): the &#x60;email&#x60; field is preserved in the response shape; its meaning is now \&quot;the drive\&#39;s owner\&#39;s email\&quot; (via &#x60;drives.owner_user_id&#x60; → &#x60;users.email&#x60;, joined in &#x60;auth.resolve_drive&#x60;). For solo signups this equals v0 behavior — the email the user signed up with. Returns null if the owner has been hard-purged. &#x60;organization_id&#x60; is a new additive field, as are &#x60;metageneration&#x60; / &#x60;etag&#x60; (also emitted as the &#x60;ETag&#x60; header).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { MeV0DrivesMeGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  try {
    const data = await api.meV0DrivesMeGet();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**DriveReadOut**](DriveReadOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## moveArtifactRouteV0ArtifactsArtIdMovePost

> ArtifactOut moveArtifactRouteV0ArtifactsArtIdMovePost(artId, artifactMoveIn, xAgentdriveActor, ifMatch)

Rename / move an artifact to a new path

Canonical artifact move/rename, keyed by the stable &#x60;art_…&#x60; ID (the artifact analogue of &#x60;POST /v0/folders/{fld_id}/move&#x60;). Moves the artifact to a new &#x60;path&#x60; on the same drive; ID, version history, source refs, labels, metadata, and the underlying CAS blob are all preserved — only &#x60;path&#x60; and &#x60;updated_at&#x60; change, and the move does NOT bump &#x60;version_number&#x60;.  The row UPDATE and the emitted &#x60;artifact.renamed&#x60; event commit in a SINGLE transaction — a failure leaves the artifact fully unchanged.  Returns 409 PATH_CONFLICT if the target &#x60;path&#x60; is already taken; 404 ARTIFACT_NOT_FOUND for an unknown id; 403 WIKI_RESERVED for a &#x60;_wiki/&#x60; / &#x60;_compiled/&#x60; target. Honors &#x60;If-Match&#x60; (→ 412 PRECONDITION_FAILED). Use &#x60;X-AgentDrive-Actor&#x60; to attach attribution to the emitted &#x60;artifact.renamed&#x60; event.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { MoveArtifactRouteV0ArtifactsArtIdMovePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
    // ArtifactMoveIn
    artifactMoveIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies MoveArtifactRouteV0ArtifactsArtIdMovePostRequest;

  try {
    const data = await api.moveArtifactRouteV0ArtifactsArtIdMovePost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |
| **artifactMoveIn** | [ArtifactMoveIn](ArtifactMoveIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No such artifact exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The destination path is already occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## moveFolderByIdV0FoldersFldIdMovePost

> FolderOut moveFolderByIdV0FoldersFldIdMovePost(fldId, folderMoveIn, xAgentdriveActor, ifMatch)

Rename / move a folder by stable ID (cascade descendants)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { MoveFolderByIdV0FoldersFldIdMovePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    fldId: fldId_example,
    // FolderMoveIn
    folderMoveIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies MoveFolderByIdV0FoldersFldIdMovePostRequest;

  try {
    const data = await api.moveFolderByIdV0FoldersFldIdMovePost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fldId** | `string` |  | [Defaults to `undefined`] |
| **folderMoveIn** | [FolderMoveIn](FolderMoveIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The destination path is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The destination path is already occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## moveFolderByPathV0FoldersPathMovePost

> FolderOut moveFolderByPathV0FoldersPathMovePost(path, folderMoveIn, xAgentdriveActor, ifMatch)

Rename / move a folder (cascade-update descendants)

Move the folder identified by URL path to the body\&#39;s &#x60;path&#x60;. All descendant folders + artifacts are path-prefix-updated in the same transaction. The folder\&#39;s &#x60;fld_*&#x60; ID stays stable.  Returns 409 &#x60;FOLDER_PATH_CONFLICT&#x60; if the destination prefix collides with a live folder or artifact path.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { MoveFolderByPathV0FoldersPathMovePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    path: path_example,
    // FolderMoveIn
    folderMoveIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies MoveFolderByPathV0FoldersPathMovePostRequest;

  try {
    const data = await api.moveFolderByPathV0FoldersPathMovePost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | `string` |  | [Defaults to `undefined`] |
| **folderMoveIn** | [FolderMoveIn](FolderMoveIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The source or destination path is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The source folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The destination path is already occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## patchArtifactRouteV0ArtifactsArtIdPatch

> ArtifactOut patchArtifactRouteV0ArtifactsArtIdPatch(artId, artifactPatchIn, xAgentdriveActor, ifMatch)

Edit artifact metadata (labels / metadata / source)

Metadata-only JSON-merge-patch update of a single artifact, keyed by its stable &#x60;art_…&#x60; ID. Every field in the body is optional; a field that is **omitted** is left unchanged, a field that is **present** is applied — with an explicit &#x60;null&#x60; / &#x60;[]&#x60; / &#x60;{}&#x60; meaning \&quot;clear\&quot;. This mirrors the MCP &#x60;set_metadata&#x60; tool.  Editable fields:   * &#x60;labels&#x60; — replace the label set (&#x60;[]&#x60;/&#x60;null&#x60; clears).   * &#x60;metadata&#x60; — replace the free-form metadata object (&#x60;{}&#x60;/&#x60;null&#x60; clears).   * &#x60;source&#x60; — replace provenance refs (&#x60;null&#x60; clears).  **To move/rename an artifact, use &#x60;POST /v0/artifacts/{art_id}/move&#x60;** — PATCH no longer accepts &#x60;path&#x60;. The body is &#x60;extra&#x3D;\&quot;forbid\&quot;&#x60;, so a stray field (notably a legacy &#x60;path&#x60;) is rejected with 422 rather than silently ignored.  Metadata edits do NOT create a new content version (no &#x60;version_number&#x60; / generation bump, no &#x60;artifact_versions&#x60; row) but DO bump the artifact\&#39;s &#x60;metageneration&#x60; and &#x60;updated_at&#x60;.  Returns 400 BAD_LABELS / BAD_SOURCE for invalid metadata; 404 ARTIFACT_NOT_FOUND for an unknown id. Honors &#x60;If-Match&#x60;, which takes the composite ETag &#x60;\&quot;&lt;art_id&gt;.&lt;generation&gt;.&lt;metageneration&gt;\&quot;&#x60; and is compared as a whole tuple: ANY concurrent content **or** metadata change (a bumped generation OR metageneration) → 412 PRECONDITION_FAILED. There is no last-writer-wins gap for metadata-only edits. Use &#x60;X-AgentDrive-Actor&#x60; to attach attribution to the emitted &#x60;artifact.metadata_updated&#x60; event.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PatchArtifactRouteV0ArtifactsArtIdPatchRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
    // ArtifactPatchIn
    artifactPatchIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies PatchArtifactRouteV0ArtifactsArtIdPatchRequest;

  try {
    const data = await api.patchArtifactRouteV0ArtifactsArtIdPatch(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |
| **artifactPatchIn** | [ArtifactPatchIn](ArtifactPatchIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The labels or source metadata are invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No such live artifact exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## patchFolderByIdV0FoldersFldIdPatch

> FolderOut patchFolderByIdV0FoldersFldIdPatch(fldId, folderPatchIn, xAgentdriveActor, ifMatch)

Update folder metadata by stable ID

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PatchFolderByIdV0FoldersFldIdPatchRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    fldId: fldId_example,
    // FolderPatchIn
    folderPatchIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies PatchFolderByIdV0FoldersFldIdPatchRequest;

  try {
    const data = await api.patchFolderByIdV0FoldersFldIdPatch(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fldId** | `string` |  | [Defaults to `undefined`] |
| **folderPatchIn** | [FolderPatchIn](FolderPatchIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The folder update is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## patchFolderByPathV0FoldersPathPatch

> FolderOut patchFolderByPathV0FoldersPathPatch(path, folderPatchIn, xAgentdriveActor, ifMatch)

Update folder metadata by path

Partial update — field absence leaves the value unchanged; explicit &#x60;null&#x60; clears the field. Use the by-id endpoint (slice 2) when you need stable addressing across renames.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PatchFolderByPathV0FoldersPathPatchRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    path: path_example,
    // FolderPatchIn
    folderPatchIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies PatchFolderByPathV0FoldersPathPatchRequest;

  try {
    const data = await api.patchFolderByPathV0FoldersPathPatch(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | `string` |  | [Defaults to `undefined`] |
| **folderPatchIn** | [FolderPatchIn](FolderPatchIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The folder update is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## patchGrantRouteV0GrantsGrnIdPatch

> GrantOut patchGrantRouteV0GrantsGrnIdPatch(grnId, grantPatchIn, xAgentdriveActor)

Update a grant\&#39;s role and/or expiry (requires can_manage)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PatchGrantRouteV0GrantsGrnIdPatchRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    grnId: grnId_example,
    // GrantPatchIn
    grantPatchIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
  } satisfies PatchGrantRouteV0GrantsGrnIdPatchRequest;

  try {
    const data = await api.patchGrantRouteV0GrantsGrnIdPatch(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **grnId** | `string` |  | [Defaults to `undefined`] |
| **grantPatchIn** | [GrantPatchIn](GrantPatchIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The grant update or expiry is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The grant does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## postDescribeV0QueryDescribePost

> DatasetDescriptionOut postDescribeV0QueryDescribePost(describeIn)

Describe a dataset\&#39;s column schema

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PostDescribeV0QueryDescribePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // DescribeIn
    describeIn: ...,
  } satisfies PostDescribeV0QueryDescribePostRequest;

  try {
    const data = await api.postDescribeV0QueryDescribePost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **describeIn** | [DescribeIn](DescribeIn.md) |  | |

### Return type

[**DatasetDescriptionOut**](DatasetDescriptionOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The referenced dataset is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | The configured query engine is unavailable. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## postFeedbackV0FeedbackPost

> FeedbackCreateOut postFeedbackV0FeedbackPost()

Post Feedback

File feedback. Body: &#x60;{kind, title, body, contact?, attachments?: [art_id, ...]}&#x60; — attachments are snapshotted from this drive\&#39;s artifacts at submit time.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PostFeedbackV0FeedbackPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  try {
    const data = await api.postFeedbackV0FeedbackPost();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**FeedbackCreateOut**](FeedbackCreateOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The feedback body or attachment list is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | An attached artifact does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## postLookupValuesV0QueryLookupValuesPost

> LookupValuesOut postLookupValuesV0QueryLookupValuesPost(lookupValuesIn)

List distinct values of a dataset column

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PostLookupValuesV0QueryLookupValuesPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // LookupValuesIn
    lookupValuesIn: ...,
  } satisfies PostLookupValuesV0QueryLookupValuesPostRequest;

  try {
    const data = await api.postLookupValuesV0QueryLookupValuesPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **lookupValuesIn** | [LookupValuesIn](LookupValuesIn.md) |  | |

### Return type

[**LookupValuesOut**](LookupValuesOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The dataset, column, or limit is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **402** | The current plan does not permit this query. |  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | The configured query engine is unavailable. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## postQueryV0QueryPost

> ResponsePostQueryV0QueryPost postQueryV0QueryPost(queryIn)

Run a read-only SQL query over authorized datasets

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PostQueryV0QueryPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // QueryIn
    queryIn: ...,
  } satisfies PostQueryV0QueryPostRequest;

  try {
    const data = await api.postQueryV0QueryPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **queryIn** | [QueryIn](QueryIn.md) |  | |

### Return type

[**ResponsePostQueryV0QueryPost**](ResponsePostQueryV0QueryPost.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The SQL or referenced dataset is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **402** | The current plan does not permit this query. |  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **503** | The configured query engine is unavailable. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## putArtifactV0ArtifactsPathPut

> ArtifactOut putArtifactV0ArtifactsPathPut(path, contentType, xAgentdriveLabels, xAgentdriveMetadata, xAgentdriveSource, xAgentdriveActor, xAgentdriveChangeSummary, xAgentdriveChecksum, contentMd5, ifMatch, ifNoneMatch)

Upload (or overwrite) an artifact

Upload an artifact at the given path. The path is treated as the artifact\&#39;s location in the drive — re-uploading the same path overwrites in place (idempotent). Returns 201 when the artifact is created (no prior live artifact at the path), 200 on overwrite — mirroring &#x60;PUT /v0/folders/{path}&#x60;.  **Limits:** request body must not exceed **50 MB**. Path must be non-empty, ≤256 chars, only &#x60;[A-Za-z0-9_./-]&#x60;, no &#x60;..&#x60; segments, no leading/trailing slash. Per-token write rate limit: 100/hour.  **Optional headers.** Each preserves the existing artifact\&#39;s value when omitted on an overwrite, and takes the create-default on a new path; send the header to replace it: - &#x60;X-AgentDrive-Labels&#x60;: comma-separated labels (e.g. &#x60;draft,report&#x60;); an empty value clears them. Each: lowercase &#x60;[a-z0-9_-]+&#x60;, ≤64 chars; ≤16 labels per artifact. - &#x60;X-AgentDrive-Metadata&#x60;: JSON object of agent-attached fields. - &#x60;X-AgentDrive-Source&#x60;: JSON &#x60;{\&quot;refs\&quot;: [...]}&#x60; source provenance (present, including &#x60;{\&quot;refs\&quot;: []}&#x60;, replaces). - &#x60;X-AgentDrive-Actor&#x60;: caller-supplied actor name (≤64 chars) for event-log attribution. Untrusted; never used for authz.  **Preconditions.** &#x60;If-Match: \&quot;&lt;id&gt;.&lt;gen&gt;.&lt;metagen&gt;\&quot;&#x60; makes the write conditional on the current composite ETag (→ 412 PRECONDITION_FAILED). &#x60;If-None-Match: *&#x60; is create-only: it succeeds only if no live artifact occupies the path (→ 412 CREATE_CONFLICT if one does). The two are mutually exclusive (→ 400 BAD_PRECONDITION).  **Integrity (optional).** &#x60;X-AgentDrive-Checksum: &lt;algo&gt;:&lt;value&gt;&#x60; (&#x60;sha256:&lt;hex&gt;&#x60; or &#x60;crc32c:&lt;base64&gt;&#x60;) or the standard &#x60;Content-MD5&#x60; (base64 MD5) is verified against the received bytes before they land (→ 400 CHECKSUM_MISMATCH on mismatch); no artifact is created on failure.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PutArtifactV0ArtifactsPathPutRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    path: path_example,
    // string (optional)
    contentType: contentType_example,
    // string (optional)
    xAgentdriveLabels: xAgentdriveLabels_example,
    // string (optional)
    xAgentdriveMetadata: xAgentdriveMetadata_example,
    // string (optional)
    xAgentdriveSource: xAgentdriveSource_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    xAgentdriveChangeSummary: xAgentdriveChangeSummary_example,
    // string (optional)
    xAgentdriveChecksum: xAgentdriveChecksum_example,
    // string (optional)
    contentMd5: contentMd5_example,
    // string (optional)
    ifMatch: ifMatch_example,
    // string (optional)
    ifNoneMatch: ifNoneMatch_example,
  } satisfies PutArtifactV0ArtifactsPathPutRequest;

  try {
    const data = await api.putArtifactV0ArtifactsPathPut(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | `string` |  | [Defaults to `undefined`] |
| **contentType** | `string` |  | [Optional] [Defaults to `&#39;application/octet-stream&#39;`] |
| **xAgentdriveLabels** | `string` |  | [Optional] [Defaults to `undefined`] |
| **xAgentdriveMetadata** | `string` |  | [Optional] [Defaults to `undefined`] |
| **xAgentdriveSource** | `string` |  | [Optional] [Defaults to `undefined`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **xAgentdriveChangeSummary** | `string` |  | [Optional] [Defaults to `undefined`] |
| **xAgentdriveChecksum** | `string` |  | [Optional] [Defaults to `undefined`] |
| **contentMd5** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifNoneMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **201** | Artifact created at a previously unused path. |  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The path, metadata, source, or conditional headers are invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The path is occupied and overwrite semantics do not permit replacement. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **413** | The artifact or resulting drive storage exceeds its limit. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## putProjectV0ProjectsFldIdPut

> CompileProjectOut putProjectV0ProjectsFldIdPut(fldId, projectConfigIn)

Set a project\&#39;s compile config (entrypoint/engine/auto_compile)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PutProjectV0ProjectsFldIdPutRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    fldId: fldId_example,
    // ProjectConfigIn
    projectConfigIn: ...,
  } satisfies PutProjectV0ProjectsFldIdPutRequest;

  try {
    const data = await api.putProjectV0ProjectsFldIdPut(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fldId** | `string` |  | [Defaults to `undefined`] |
| **projectConfigIn** | [ProjectConfigIn](ProjectConfigIn.md) |  | |

### Return type

[**CompileProjectOut**](CompileProjectOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The compile engine or entrypoint is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The project folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## redeemShareSShareKeyGet

> ShareRedeemOut redeemShareSShareKeyGet(shareKey)

Redeem Share

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RedeemShareSShareKeyGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    shareKey: shareKey_example,
  } satisfies RedeemShareSShareKeyGetRequest;

  try {
    const data = await api.redeemShareSShareKeyGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **shareKey** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ShareRedeemOut**](ShareRedeemOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | JSON capability response or browser password form. |  * X-Request-Id - Request correlation identifier. <br>  |
| **302** | Browser redemption succeeded; continue to the canonical URL. |  * Location - Redirect target. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | A password is required or the supplied password is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The share is invalid, expired, or no longer authorized. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## redeemShareWithPasswordSShareKeyPost

> ShareRedeemOut redeemShareWithPasswordSShareKeyPost(shareKey, password)

Redeem Share With Password

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RedeemShareWithPasswordSShareKeyPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    shareKey: shareKey_example,
    // string (optional)
    password: password_example,
  } satisfies RedeemShareWithPasswordSShareKeyPostRequest;

  try {
    const data = await api.redeemShareWithPasswordSShareKeyPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **shareKey** | `string` |  | [Defaults to `undefined`] |
| **password** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |

### Return type

[**ShareRedeemOut**](ShareRedeemOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | JSON capability response or browser password form. |  * X-Request-Id - Request correlation identifier. <br>  |
| **302** | Browser redemption succeeded; continue to the canonical URL. |  * Location - Redirect target. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | A password is required or the supplied password is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The share is invalid, expired, or no longer authorized. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## restoreArtifactV0ArtifactsArtIdRestorePost

> ArtifactOut restoreArtifactV0ArtifactsArtIdRestorePost(artId, rename, overwrite, xAgentdriveActor, ifMatch)

Restore a soft-deleted artifact

Clear &#x60;deleted_at&#x60; + &#x60;purge_at&#x60; on a soft-deleted artifact. Available only while the artifact is in trash (i.e. before the GC cleanup cron purges it). Returns 404 if the artifact is live or already hard-deleted; 409 PATH_CONFLICT if its path is now occupied by another live artifact. The 409 payload includes a &#x60;restore_options&#x60; block with &#x60;rename_to&#x60; and &#x60;force_overwrite&#x60; URLs the caller can follow to resolve the conflict — see deletion-design.md §5.4.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RestoreArtifactV0ArtifactsArtIdRestorePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
    // string | Restore at this path instead of the original. Soft-deletes the live occupant at the original path with audit `metadata.cause=\'restore_conflict_rename\'`. Mutually exclusive with `overwrite`. (optional)
    rename: rename_example,
    // boolean | Soft-delete the live occupant at the original path and restore there. Audit `metadata.cause=\'restore_conflict_overwrite\'`. Mutually exclusive with `rename`. (optional)
    overwrite: true,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies RestoreArtifactV0ArtifactsArtIdRestorePostRequest;

  try {
    const data = await api.restoreArtifactV0ArtifactsArtIdRestorePost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |
| **rename** | `string` | Restore at this path instead of the original. Soft-deletes the live occupant at the original path with audit &#x60;metadata.cause&#x3D;\&#39;restore_conflict_rename\&#39;&#x60;. Mutually exclusive with &#x60;overwrite&#x60;. | [Optional] [Defaults to `undefined`] |
| **overwrite** | `boolean` | Soft-delete the live occupant at the original path and restore there. Audit &#x60;metadata.cause&#x3D;\&#39;restore_conflict_overwrite\&#39;&#x60;. Mutually exclusive with &#x60;rename&#x60;. | [Optional] [Defaults to `false`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No restorable artifact exists with this ID. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The original or requested restore path is occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## restoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost

> ArtifactOut restoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost(artId, versionNumber, xAgentdriveActor, ifMatch)

Restore a previous version as a new head version

Roll the artifact forward to the content of version &#x60;version_number&#x60; by creating a **new head version** with identical bytes. History is preserved — this never rewrites or deletes past versions. The prior version\&#39;s content-addressed blob is reused, so no bytes are re-uploaded. A change summary of &#x60;Restored version N&#x60; is recorded on the new version; &#x60;X-AgentDrive-Actor&#x60; attributes it.  Restoring a version whose content already matches the current head (including the head itself) is a **no-op**: it returns the current artifact unchanged, with no new version created.  Honors &#x60;If-Match&#x60; on the current head (roll forward only if the head is unchanged → 412 PRECONDITION_FAILED).  Errors: &#x60;404 ARTIFACT_NOT_FOUND&#x60;, &#x60;404 VERSION_NOT_FOUND&#x60;, and &#x60;410 VERSION_PRUNED&#x60; when the version existed but its bytes were retained out of existence.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    artId: artId_example,
    // number
    versionNumber: 56,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePostRequest;

  try {
    const data = await api.restoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |
| **versionNumber** | `number` |  | [Defaults to `undefined`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The artifact or version does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **410** | The requested version was pruned by retention. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## restoreDriveRouteV0DrivesDriveIdRestorePost

> DriveRestoreOut restoreDriveRouteV0DrivesDriveIdRestorePost(driveId, xAgentdriveActor, ifMatch)

Restore a soft-deleted drive

Clear &#x60;deleted_at&#x60; + &#x60;purge_at&#x60; on a soft-deleted drive. Soft-deleted child artifacts get their retention window rebased to the drive-restore moment (see deletion-design.md §5.2). Available only while the drive is in trash. Returns 404 if the drive is live or already hard-deleted.  **Optimistic concurrency:** send &#x60;If-Match&#x60; with the trashed drive\&#39;s composite ETag (&#x60;\&quot;&lt;drv_id&gt;.0.&lt;metageneration&gt;\&quot;&#x60;, e.g. from the delete response\&#39;s &#x60;ETag&#x60; header) to make the restore conditional — a stale token returns 412 PRECONDITION_FAILED. A restore WITHOUT an &#x60;If-Match&#x60; precondition is last-writer-wins.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RestoreDriveRouteV0DrivesDriveIdRestorePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies RestoreDriveRouteV0DrivesDriveIdRestorePostRequest;

  try {
    const data = await api.restoreDriveRouteV0DrivesDriveIdRestorePost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **driveId** | `string` |  | [Defaults to `undefined`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DriveRestoreOut**](DriveRestoreOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The drive does not exist or is not in trash. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The drive cannot be restored into its current workspace state. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | If-Match does not match the current drive. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## restoreFolderByIdV0FoldersFldIdRestorePost

> FolderRestoreOut restoreFolderByIdV0FoldersFldIdRestorePost(fldId, xAgentdriveActor, ifMatch)

Restore a soft-deleted folder (cascade)

Mirrors &#x60;POST /v0/artifacts/{art_id}/restore&#x60; for folders: clear &#x60;deleted_at&#x60; + &#x60;purge_at&#x60; on a soft-deleted folder AND exactly the descendants soft-deleted in the same cascade (descendants trashed separately keep their trash state; restore those individually — the per-artifact restore remains for cherry-picking). Available only while the folder is in trash; returns 404 if it is live or already hard-purged.  Returns 409 &#x60;PATH_CONFLICT&#x60; when a live folder/artifact now occupies a path this restore would reinstate (&#x60;colliding_path&#x60; + &#x60;kind&#x60; identify it). Unlike artifact restore there are NO &#x60;rename&#x60;/&#x60;overwrite&#x60; escape hatches — the whole cascade aborts; free the colliding path (or cherry-pick artifacts) and retry.  &#x60;If-Match&#x60; (the trashed folder\&#39;s composite ETag) makes the restore conditional → 412 PRECONDITION_FAILED on a stale token; omitted, the restore is last-writer-wins.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RestoreFolderByIdV0FoldersFldIdRestorePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    fldId: fldId_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
  } satisfies RestoreFolderByIdV0FoldersFldIdRestorePostRequest;

  try {
    const data = await api.restoreFolderByIdV0FoldersFldIdRestorePost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fldId** | `string` |  | [Defaults to `undefined`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderRestoreOut**](FolderRestoreOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | No restorable folder exists with this ID. |  * X-Request-Id - Request correlation identifier. <br>  |
| **409** | The restore destination is already occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
| **412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## rotateShareRouteV0SharesShrIdRotatePost

> ShareMintOut rotateShareRouteV0SharesShrIdRotatePost(shrId, xAgentdriveActor)

Revoke + reissue a share link\&#39;s key (requires can_share)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RotateShareRouteV0SharesShrIdRotatePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    shrId: shrId_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
  } satisfies RotateShareRouteV0SharesShrIdRotatePostRequest;

  try {
    const data = await api.rotateShareRouteV0SharesShrIdRotatePost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **shrId** | `string` |  | [Defaults to `undefined`] |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ShareMintOut**](ShareMintOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The replacement password is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The share does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## searchV0SearchGet

> SearchPage searchV0SearchGet(q, label, fileType, prefix, updatedAfter, updatedBefore, limit)

Full-text search over artifacts in the drive

Lexical (not semantic) full-text search powered by Postgres &#x60;websearch_to_tsquery&#x60;. Results are ranked by &#x60;ts_rank&#x60; over a weighted tsvector (path &gt; content &gt; metadata &gt; labels).  **Supported query syntax:** - Words: &#x60;kangaroo&#x60; (English stemming) - Phrases: &#x60;\&quot;exact phrase\&quot;&#x60; - Negation: &#x60;kangaroo -secret&#x60; - AND (implicit): &#x60;kangaroo secret&#x60; - OR: &#x60;kangaroo OR koala&#x60; - Paths &amp; filenames: &#x60;reports/q3-summary.md&#x60; or &#x60;q3-summary.md&#x60; match by their path words (&#x60;/ . _ -&#x60; are word boundaries)  **Not supported (v0):** - Semantic / embedding similarity - PDF and image content (only the path + metadata are searchable) - Non-English stemming - Fuzzy matching, regex - Boolean operator parentheses  **Filters:** &#x60;label&#x60; (repeatable, AND), &#x60;file_type&#x60; (enum), &#x60;prefix&#x60; (path prefix), &#x60;updated_after&#x60; / &#x60;updated_before&#x60; (RFC 3339 timestamps, inclusive bounds on &#x60;updated_at&#x60;).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { SearchV0SearchGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DefaultApi(config);

  const body = {
    // string
    q: q_example,
    // Array<string> (optional)
    label: ...,
    // string (optional)
    fileType: fileType_example,
    // string (optional)
    prefix: prefix_example,
    // Date (optional)
    updatedAfter: 2013-10-20T19:20:30+01:00,
    // Date (optional)
    updatedBefore: 2013-10-20T19:20:30+01:00,
    // number (optional)
    limit: 56,
  } satisfies SearchV0SearchGetRequest;

  try {
    const data = await api.searchV0SearchGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **q** | `string` |  | [Defaults to `undefined`] |
| **label** | `Array<string>` |  | [Optional] |
| **fileType** | `string` |  | [Optional] [Defaults to `undefined`] |
| **prefix** | `string` |  | [Optional] [Defaults to `undefined`] |
| **updatedAfter** | `Date` |  | [Optional] [Defaults to `undefined`] |
| **updatedBefore** | `Date` |  | [Optional] [Defaults to `undefined`] |
| **limit** | `number` |  | [Optional] [Defaults to `20`] |

### Return type

[**SearchPage**](SearchPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **400** | The search query or filter is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
| **401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
| **429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## viewArtifactHeadAArtIdHeadGet

> ArtifactHeadOut viewArtifactHeadAArtIdHeadGet(artId)

View Artifact Head

Return &#x60;{\&quot;version\&quot;: &lt;head version_number&gt;}&#x60; for a readable artifact.  Auth mirrors the permalink/viewer: the owner, or an &#x60;anyone:viewer&#x60; grant (a published artifact), reads. Two deliberate differences from the HTML viewer:    * Never redirect to login. A poll is a background &#x60;fetch&#x60;, not a     navigation — an HTML login page would be a useless body and a     same-origin redirect the client can\&#39;t act on. Anonymous callers     on a private/absent artifact get a flat 404.   * \&quot;Doesn\&#39;t exist\&quot; and \&quot;exists but not readable\&quot; collapse to the     same 404, so an anonymous poller can\&#39;t use this as an existence     oracle (matches the permalink/viewer leak guard).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ViewArtifactHeadAArtIdHeadGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
  } satisfies ViewArtifactHeadAArtIdHeadGetRequest;

  try {
    const data = await api.viewArtifactHeadAArtIdHeadGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ArtifactHeadOut**](ArtifactHeadOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## viewArtifactVersionVArtIdVersionGet

> Blob viewArtifactVersionVArtIdVersionGet(artId, version, raw, download)

View Artifact Version

Render version &#x60;version&#x60; of an artifact, read-only.  Version history is owner-only. The drive-blind &#x60;can_read&#x60; gate still provides the same sign-in-or-404 masking as &#x60;/a/{art_id}&#x60;, but readable non-owners cannot browse snapshots. A pruned or never-existed version renders a friendly unavailable state, never a 500. &#x60;?raw&#x3D;1&#x60; / &#x60;?download&#x3D;1&#x60; stream the version\&#39;s bytes (powering the bar\&#39;s Raw / Download buttons) with the same sandbox+nosniff headers as the head raw path.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ViewArtifactVersionVArtIdVersionGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // number
    version: 56,
    // number (optional)
    raw: 56,
    // number (optional)
    download: 56,
  } satisfies ViewArtifactVersionVArtIdVersionGetRequest;

  try {
    const data = await api.viewArtifactVersionVArtIdVersionGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |
| **version** | `number` |  | [Defaults to `undefined`] |
| **raw** | `number` |  | [Optional] [Defaults to `0`] |
| **download** | `number` |  | [Optional] [Defaults to `0`] |

### Return type

**Blob**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/octet-stream`, `text/html`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rendered HTML or raw artifact bytes. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## viewFileDriveIdPathGet

> Blob viewFileDriveIdPathGet(driveId, path, raw, download)

View File

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ViewFileDriveIdPathGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    driveId: driveId_example,
    // string
    path: path_example,
    // number (optional)
    raw: 56,
    // number (optional)
    download: 56,
  } satisfies ViewFileDriveIdPathGetRequest;

  try {
    const data = await api.viewFileDriveIdPathGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **driveId** | `string` |  | [Defaults to `undefined`] |
| **path** | `string` |  | [Defaults to `undefined`] |
| **raw** | `number` |  | [Optional] [Defaults to `0`] |
| **download** | `number` |  | [Optional] [Defaults to `0`] |

### Return type

**Blob**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/octet-stream`, `text/html`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rendered HTML or raw artifact bytes. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## viewPermalinkArtifactAArtIdGet

> viewPermalinkArtifactAArtIdGet(artId)

View Permalink Artifact

Resolve a stable artifact ID to its path-URL and 302 there.  Auth model matches the path URL: public artifacts redirect for anyone; private artifacts redirect only for the owner. Non-owners on private artifacts get 404 — same response as \&quot;doesn\&#39;t exist\&quot;, so the ID\&#39;s existence isn\&#39;t leaked. The forwarded query-param allowlist is &#x60;raw&#x60;, &#x60;download&#x60; (see _PERMALINK_FORWARDED_PARAMS).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ViewPermalinkArtifactAArtIdGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
  } satisfies ViewPermalinkArtifactAArtIdGetRequest;

  try {
    const data = await api.viewPermalinkArtifactAArtIdGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **artId** | `string` |  | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Redirect to the canonical or authentication URL. |  * Location - Redirect target. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The artifact does not exist or is not readable. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## viewPermalinkFolderFFldIdGet

> viewPermalinkFolderFFldIdGet(fldId)

View Permalink Folder

Resolve a stable folder ID to its current path-URL and 302.  Auth model mirrors the artifact permalink: public folder &#x3D; anon OK; private folder &#x3D; owner only, otherwise 404 (no existence leak). \&quot;Public\&quot; is an &#x60;anyone:viewer&#x60; grant on the &#x60;fld_*&#x60; id resolved through &#x60;can_read&#x60; (§4.4); folders carry no visibility flag of their own.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ViewPermalinkFolderFFldIdGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
  } satisfies ViewPermalinkFolderFFldIdGetRequest;

  try {
    const data = await api.viewPermalinkFolderFFldIdGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fldId** | `string` |  | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Redirect to the canonical or authentication URL. |  * Location - Redirect target. <br>  * X-Request-Id - Request correlation identifier. <br>  |
| **404** | The folder does not exist or is not readable. |  * X-Request-Id - Request correlation identifier. <br>  |
| **422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
