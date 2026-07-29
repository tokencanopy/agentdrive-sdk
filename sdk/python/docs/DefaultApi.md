# agentdrive_sdk.DefaultApi

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_upload_v0_uploads_upload_id_delete**](DefaultApi.md#abort_upload_v0_uploads_upload_id_delete) | **DELETE** /v0/uploads/{upload_id} | Abort a large (direct-to-GCS) upload session
[**begin_upload_v0_uploads_post**](DefaultApi.md#begin_upload_v0_uploads_post) | **POST** /v0/uploads | Begin a large (direct-to-GCS) upload
[**callback_auth_callback_get**](DefaultApi.md#callback_auth_callback_get) | **GET** /auth/callback | Callback
[**cancel_job_v0_jobs_job_id_cancel_post**](DefaultApi.md#cancel_job_v0_jobs_job_id_cancel_post) | **POST** /v0/jobs/{job_id}/cancel | Cancel a queued/running job
[**commit_upload_v0_uploads_upload_id_commit_post**](DefaultApi.md#commit_upload_v0_uploads_upload_id_commit_post) | **POST** /v0/uploads/{upload_id}/commit | Commit a large (direct-to-GCS) upload
[**copy_artifact_route_v0_artifacts_art_id_copy_post**](DefaultApi.md#copy_artifact_route_v0_artifacts_art_id_copy_post) | **POST** /v0/artifacts/{art_id}/copy | Duplicate an artifact to a new path (CAS-shared, new ID)
[**copy_folder_by_id_v0_folders_fld_id_copy_post**](DefaultApi.md#copy_folder_by_id_v0_folders_fld_id_copy_post) | **POST** /v0/folders/{fld_id}/copy | Duplicate a folder subtree to a new path (CAS-shared, new IDs)
[**create_folder_by_path_v0_folders_path_put**](DefaultApi.md#create_folder_by_path_v0_folders_path_put) | **PUT** /v0/folders/{path} | Create a folder (idempotent)
[**create_grant_route_v0_grants_post**](DefaultApi.md#create_grant_route_v0_grants_post) | **POST** /v0/grants | Create (or fetch) a per-principal grant on a resource
[**create_share_route_v0_shares_post**](DefaultApi.md#create_share_route_v0_shares_post) | **POST** /v0/shares | Mint a share link (returns the share_key once)
[**delete_artifact_by_id_route_v0_artifacts_art_id_delete**](DefaultApi.md#delete_artifact_by_id_route_v0_artifacts_art_id_delete) | **DELETE** /v0/artifacts/{art_id} | Soft-delete an artifact by its stable ID
[**delete_artifact_v0_artifacts_path_delete**](DefaultApi.md#delete_artifact_v0_artifacts_path_delete) | **DELETE** /v0/artifacts/{path} | Delete Artifact
[**delete_drive_route_v0_drives_drive_id_delete**](DefaultApi.md#delete_drive_route_v0_drives_drive_id_delete) | **DELETE** /v0/drives/{drive_id} | Soft-delete a drive
[**delete_folder_by_id_v0_folders_fld_id_delete**](DefaultApi.md#delete_folder_by_id_v0_folders_fld_id_delete) | **DELETE** /v0/folders/{fld_id} | Soft-delete a folder by stable ID (cascade with ?recursive&#x3D;true)
[**delete_folder_by_path_v0_folders_path_delete**](DefaultApi.md#delete_folder_by_path_v0_folders_path_delete) | **DELETE** /v0/folders/{path} | Soft-delete a folder (cascade with ?recursive&#x3D;true)
[**delete_grant_route_v0_grants_grn_id_delete**](DefaultApi.md#delete_grant_route_v0_grants_grn_id_delete) | **DELETE** /v0/grants/{grn_id} | Revoke a grant (can_manage, or self-revoke own grant)
[**delete_share_route_v0_shares_shr_id_delete**](DefaultApi.md#delete_share_route_v0_shares_shr_id_delete) | **DELETE** /v0/shares/{shr_id} | Revoke a share link (requires can_manage)
[**download_artifact_by_id_v0_artifacts_art_id_download_get**](DefaultApi.md#download_artifact_by_id_v0_artifacts_art_id_download_get) | **GET** /v0/artifacts/{art_id}/download | Stream the artifact bytes by stable ID (never rendered HTML)
[**download_artifact_by_path_v0_artifacts_path_download_get**](DefaultApi.md#download_artifact_by_path_v0_artifacts_path_download_get) | **GET** /v0/artifacts/{path}/download | Stream the artifact bytes by path (never rendered HTML)
[**download_artifact_version_v0_artifacts_art_id_versions_version_number_download_get**](DefaultApi.md#download_artifact_version_v0_artifacts_art_id_versions_version_number_download_get) | **GET** /v0/artifacts/{art_id}/versions/{version_number}/download | Stream bytes for a specific version (machine surface)
[**download_url_by_id_v0_artifacts_art_id_download_url_get**](DefaultApi.md#download_url_by_id_v0_artifacts_art_id_download_url_get) | **GET** /v0/artifacts/{art_id}/download-url | Signed direct-from-GCS download URL by stable ID
[**download_url_by_path_v0_artifacts_path_download_url_get**](DefaultApi.md#download_url_by_path_v0_artifacts_path_download_url_get) | **GET** /v0/artifacts/{path}/download-url | Signed direct-from-GCS download URL by path
[**download_url_version_v0_artifacts_art_id_versions_version_number_download_url_get**](DefaultApi.md#download_url_version_v0_artifacts_art_id_versions_version_number_download_url_get) | **GET** /v0/artifacts/{art_id}/versions/{version_number}/download-url | Signed direct-from-GCS download URL for a specific version
[**enqueue_job_v0_projects_fld_id_jobs_post**](DefaultApi.md#enqueue_job_v0_projects_fld_id_jobs_post) | **POST** /v0/projects/{fld_id}/jobs | Enqueue a compile job for a project (folder)
[**extension_start_auth_extension_start_get**](DefaultApi.md#extension_start_auth_extension_start_get) | **GET** /auth/extension/start | Extension Start
[**find_v0_find_get**](DefaultApi.md#find_v0_find_get) | **GET** /v0/find | Hybrid passage retrieval over the full file body
[**get_artifact_by_id_meta_v0_artifacts_art_id_meta_get**](DefaultApi.md#get_artifact_by_id_meta_v0_artifacts_art_id_meta_get) | **GET** /v0/artifacts/{art_id}/meta | Artifact metadata by stable ID (same shape as path /meta)
[**get_artifact_by_id_v0_artifacts_art_id_get**](DefaultApi.md#get_artifact_by_id_v0_artifacts_art_id_get) | **GET** /v0/artifacts/{art_id} | Canonical lookup of an artifact by its stable ID
[**get_artifact_meta_v0_artifacts_path_meta_get**](DefaultApi.md#get_artifact_meta_v0_artifacts_path_meta_get) | **GET** /v0/artifacts/{path}/meta | Get Artifact Meta
[**get_artifact_version_v0_artifacts_art_id_versions_version_number_get**](DefaultApi.md#get_artifact_version_v0_artifacts_art_id_versions_version_number_get) | **GET** /v0/artifacts/{art_id}/versions/{version_number} | Metadata for a specific version of an artifact
[**get_drive_route_v0_drives_drive_id_get**](DefaultApi.md#get_drive_route_v0_drives_drive_id_get) | **GET** /v0/drives/{drive_id} | Drive overview by id (same shape as /drives/me)
[**get_feedback_status_v0_feedback_fbk_id_get**](DefaultApi.md#get_feedback_status_v0_feedback_fbk_id_get) | **GET** /v0/feedback/{fbk_id} | Get Feedback Status
[**get_folder_by_id_meta_v0_folders_fld_id_meta_get**](DefaultApi.md#get_folder_by_id_meta_v0_folders_fld_id_meta_get) | **GET** /v0/folders/{fld_id}/meta | Folder metadata by stable ID (same shape as the bare id route)
[**get_folder_by_id_v0_folders_fld_id_get**](DefaultApi.md#get_folder_by_id_v0_folders_fld_id_get) | **GET** /v0/folders/{fld_id} | Canonical lookup of a folder by its stable ID
[**get_folder_by_path_meta_v0_folders_path_meta_get**](DefaultApi.md#get_folder_by_path_meta_v0_folders_path_meta_get) | **GET** /v0/folders/{path}/meta | Folder metadata by path (same shape as the bare path route)
[**get_folder_by_path_v0_folders_path_get**](DefaultApi.md#get_folder_by_path_v0_folders_path_get) | **GET** /v0/folders/{path} | Read folder metadata by path
[**get_grant_route_v0_grants_grn_id_get**](DefaultApi.md#get_grant_route_v0_grants_grn_id_get) | **GET** /v0/grants/{grn_id} | Read a single grant (can_manage, or the grant&#39;s own principal)
[**get_job_logs_v0_jobs_job_id_logs_get**](DefaultApi.md#get_job_logs_v0_jobs_job_id_logs_get) | **GET** /v0/jobs/{job_id}/logs | Raw compile log (text/plain)
[**get_job_v0_jobs_job_id_get**](DefaultApi.md#get_job_v0_jobs_job_id_get) | **GET** /v0/jobs/{job_id} | Poll a job
[**get_project_v0_projects_fld_id_get**](DefaultApi.md#get_project_v0_projects_fld_id_get) | **GET** /v0/projects/{fld_id} | Get a project&#39;s compile config
[**get_share_route_v0_shares_shr_id_get**](DefaultApi.md#get_share_route_v0_shares_shr_id_get) | **GET** /v0/shares/{shr_id} | Read a single share link&#39;s metadata (requires can_manage)
[**get_upload_status_v0_uploads_upload_id_get**](DefaultApi.md#get_upload_status_v0_uploads_upload_id_get) | **GET** /v0/uploads/{upload_id} | Get the status of a large (direct-to-GCS) upload session
[**health_health_get**](DefaultApi.md#health_health_get) | **GET** /health | Health
[**list_artifact_versions_v0_artifacts_art_id_versions_get**](DefaultApi.md#list_artifact_versions_v0_artifacts_art_id_versions_get) | **GET** /v0/artifacts/{art_id}/versions | List versions of an artifact, newest first
[**list_artifacts_v0_artifacts_get**](DefaultApi.md#list_artifacts_v0_artifacts_get) | **GET** /v0/artifacts | List artifacts in the drive
[**list_events_route_v0_events_get**](DefaultApi.md#list_events_route_v0_events_get) | **GET** /v0/events | Read the append-only event log for the authenticated drive
[**list_grants_route_v0_grants_get**](DefaultApi.md#list_grants_route_v0_grants_get) | **GET** /v0/grants | List live grants on a resource (requires can_manage)
[**list_project_jobs_v0_projects_fld_id_jobs_get**](DefaultApi.md#list_project_jobs_v0_projects_fld_id_jobs_get) | **GET** /v0/projects/{fld_id}/jobs | List a project&#39;s jobs
[**list_shares_route_v0_shares_get**](DefaultApi.md#list_shares_route_v0_shares_get) | **GET** /v0/shares | List live share links on a resource (requires can_manage)
[**list_trash_route_v0_drives_drive_id_trash_get**](DefaultApi.md#list_trash_route_v0_drives_drive_id_trash_get) | **GET** /v0/drives/{drive_id}/trash | List the authenticated drive&#39;s trash
[**login_auth_login_get**](DefaultApi.md#login_auth_login_get) | **GET** /auth/login | Login
[**logout_auth_logout_post**](DefaultApi.md#logout_auth_logout_post) | **POST** /auth/logout | Logout
[**me_usage_v0_drives_me_usage_get**](DefaultApi.md#me_usage_v0_drives_me_usage_get) | **GET** /v0/drives/me/usage | Current-period usage + caps for the authenticated drive
[**me_v0_drives_me_get**](DefaultApi.md#me_v0_drives_me_get) | **GET** /v0/drives/me | Me
[**move_artifact_route_v0_artifacts_art_id_move_post**](DefaultApi.md#move_artifact_route_v0_artifacts_art_id_move_post) | **POST** /v0/artifacts/{art_id}/move | Rename / move an artifact to a new path
[**move_folder_by_id_v0_folders_fld_id_move_post**](DefaultApi.md#move_folder_by_id_v0_folders_fld_id_move_post) | **POST** /v0/folders/{fld_id}/move | Rename / move a folder by stable ID (cascade descendants)
[**move_folder_by_path_v0_folders_path_move_post**](DefaultApi.md#move_folder_by_path_v0_folders_path_move_post) | **POST** /v0/folders/{path}/move | Rename / move a folder (cascade-update descendants)
[**patch_artifact_route_v0_artifacts_art_id_patch**](DefaultApi.md#patch_artifact_route_v0_artifacts_art_id_patch) | **PATCH** /v0/artifacts/{art_id} | Edit artifact metadata (labels / metadata / source)
[**patch_folder_by_id_v0_folders_fld_id_patch**](DefaultApi.md#patch_folder_by_id_v0_folders_fld_id_patch) | **PATCH** /v0/folders/{fld_id} | Update folder metadata by stable ID
[**patch_folder_by_path_v0_folders_path_patch**](DefaultApi.md#patch_folder_by_path_v0_folders_path_patch) | **PATCH** /v0/folders/{path} | Update folder metadata by path
[**patch_grant_route_v0_grants_grn_id_patch**](DefaultApi.md#patch_grant_route_v0_grants_grn_id_patch) | **PATCH** /v0/grants/{grn_id} | Update a grant&#39;s role and/or expiry (requires can_manage)
[**post_describe_v0_query_describe_post**](DefaultApi.md#post_describe_v0_query_describe_post) | **POST** /v0/query/describe | Describe a dataset&#39;s column schema
[**post_feedback_v0_feedback_post**](DefaultApi.md#post_feedback_v0_feedback_post) | **POST** /v0/feedback | Post Feedback
[**post_lookup_values_v0_query_lookup_values_post**](DefaultApi.md#post_lookup_values_v0_query_lookup_values_post) | **POST** /v0/query/lookup-values | List distinct values of a dataset column
[**post_query_v0_query_post**](DefaultApi.md#post_query_v0_query_post) | **POST** /v0/query | Run a read-only SQL query over authorized datasets
[**put_artifact_v0_artifacts_path_put**](DefaultApi.md#put_artifact_v0_artifacts_path_put) | **PUT** /v0/artifacts/{path} | Upload (or overwrite) an artifact
[**put_project_v0_projects_fld_id_put**](DefaultApi.md#put_project_v0_projects_fld_id_put) | **PUT** /v0/projects/{fld_id} | Set a project&#39;s compile config (entrypoint/engine/auto_compile)
[**redeem_share_s_share_key_get**](DefaultApi.md#redeem_share_s_share_key_get) | **GET** /s/{share_key} | Redeem Share
[**redeem_share_with_password_s_share_key_post**](DefaultApi.md#redeem_share_with_password_s_share_key_post) | **POST** /s/{share_key} | Redeem Share With Password
[**restore_artifact_v0_artifacts_art_id_restore_post**](DefaultApi.md#restore_artifact_v0_artifacts_art_id_restore_post) | **POST** /v0/artifacts/{art_id}/restore | Restore a soft-deleted artifact
[**restore_artifact_version_v0_artifacts_art_id_versions_version_number_restore_post**](DefaultApi.md#restore_artifact_version_v0_artifacts_art_id_versions_version_number_restore_post) | **POST** /v0/artifacts/{art_id}/versions/{version_number}/restore | Restore a previous version as a new head version
[**restore_drive_route_v0_drives_drive_id_restore_post**](DefaultApi.md#restore_drive_route_v0_drives_drive_id_restore_post) | **POST** /v0/drives/{drive_id}/restore | Restore a soft-deleted drive
[**restore_folder_by_id_v0_folders_fld_id_restore_post**](DefaultApi.md#restore_folder_by_id_v0_folders_fld_id_restore_post) | **POST** /v0/folders/{fld_id}/restore | Restore a soft-deleted folder (cascade)
[**rotate_share_route_v0_shares_shr_id_rotate_post**](DefaultApi.md#rotate_share_route_v0_shares_shr_id_rotate_post) | **POST** /v0/shares/{shr_id}/rotate | Revoke + reissue a share link&#39;s key (requires can_share)
[**search_v0_search_get**](DefaultApi.md#search_v0_search_get) | **GET** /v0/search | Full-text search over artifacts in the drive
[**view_artifact_head_a_art_id_head_get**](DefaultApi.md#view_artifact_head_a_art_id_head_get) | **GET** /a/{art_id}/head | View Artifact Head
[**view_artifact_version_v_art_id_version_get**](DefaultApi.md#view_artifact_version_v_art_id_version_get) | **GET** /v/{art_id}/{version} | View Artifact Version
[**view_file_drive_id_path_get**](DefaultApi.md#view_file_drive_id_path_get) | **GET** /{drive_id}/{path} | View File
[**view_permalink_artifact_a_art_id_get**](DefaultApi.md#view_permalink_artifact_a_art_id_get) | **GET** /a/{art_id} | View Permalink Artifact
[**view_permalink_folder_f_fld_id_get**](DefaultApi.md#view_permalink_folder_f_fld_id_get) | **GET** /f/{fld_id} | View Permalink Folder


# **abort_upload_v0_uploads_upload_id_delete**
> UploadAbortOut abort_upload_v0_uploads_upload_id_delete(upload_id)

Abort a large (direct-to-GCS) upload session

Release an open upload session: return its reserved quota to the drive and mark it aborted. Idempotent — aborting an already-aborted or already-expired session succeeds with `released_bytes: 0`. A committed session cannot be aborted (409 ALREADY_COMMITTED). No write budget is charged — this frees resources rather than consuming them.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.upload_abort_out import UploadAbortOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    upload_id = 'upload_id_example' # str |

    try:
        # Abort a large (direct-to-GCS) upload session
        api_response = api_instance.abort_upload_v0_uploads_upload_id_delete(upload_id)
        print("The response of DefaultApi->abort_upload_v0_uploads_upload_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->abort_upload_v0_uploads_upload_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  |

### Return type

[**UploadAbortOut**](UploadAbortOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No such upload for this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | Upload already committed and cannot be aborted. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_upload_v0_uploads_post**
> UploadBeginOut begin_upload_v0_uploads_post(upload_begin_in)

Begin a large (direct-to-GCS) upload

Reserve quota and open a resumable upload session for a file larger than the buffered-upload limit. Returns a `upload_url` to PUT the raw bytes to DIRECTLY (no Authorization header — the URL is the credential), then call `/v0/uploads/{upload_id}/commit`. All artifact decisions (path, labels, metadata, source, if_match) are frozen here.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.upload_begin_in import UploadBeginIn
from agentdrive_sdk.models.upload_begin_out import UploadBeginOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    upload_begin_in = agentdrive_sdk.UploadBeginIn() # UploadBeginIn |

    try:
        # Begin a large (direct-to-GCS) upload
        api_response = api_instance.begin_upload_v0_uploads_post(upload_begin_in)
        print("The response of DefaultApi->begin_upload_v0_uploads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->begin_upload_v0_uploads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_begin_in** | [**UploadBeginIn**](UploadBeginIn.md)|  |

### Return type

[**UploadBeginOut**](UploadBeginOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | Invalid path, labels, metadata, or source. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | Path reserved for the system (WIKI_RESERVED). |  * X-Request-Id - Request correlation identifier. <br>  |
**413** | size_bytes exceeds the per-artifact cap or storage quota. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Drive&#39;s per-hour write budget exhausted. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **callback_auth_callback_get**
> str callback_auth_callback_get(code=code, state=state, error=error)

Callback

Complete a sign-in.

Handles the auth provider's OAuth callback and shapes failures into
user-readable errors:
  * an invalid or expired login flow — LOGIN_FLOW_INVALID (400);
  * an invalid or already-used authorization code — AUTH_CODE_INVALID (400);
  * the upstream auth provider being unavailable — WORKOS_UNAVAILABLE (502),
    returned with Retry-After.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    code = 'code_example' # str |  (optional)
    state = 'state_example' # str |  (optional)
    error = 'error_example' # str |  (optional)

    try:
        # Callback
        api_response = api_instance.callback_auth_callback_get(code=code, state=state, error=error)
        print("The response of DefaultApi->callback_auth_callback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->callback_auth_callback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional]
 **state** | **str**|  | [optional]
 **error** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Extension authentication handoff page. |  * X-Request-Id - Request correlation identifier. <br>  |
**302** | Redirect to the canonical or authentication URL. |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The login flow or authorization code is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | Account recovery is required or the Hub principal conflicts with the existing account link. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**502** | The upstream identity provider is temporarily unavailable. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**503** | Extension authentication is temporarily disabled. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_job_v0_jobs_job_id_cancel_post**
> CompileJobOut cancel_job_v0_jobs_job_id_cancel_post(job_id)

Cancel a queued/running job

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.compile_job_out import CompileJobOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    job_id = 'job_id_example' # str |

    try:
        # Cancel a queued/running job
        api_response = api_instance.cancel_job_v0_jobs_job_id_cancel_post(job_id)
        print("The response of DefaultApi->cancel_job_v0_jobs_job_id_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_job_v0_jobs_job_id_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  |

### Return type

[**CompileJobOut**](CompileJobOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No such compile job exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commit_upload_v0_uploads_upload_id_commit_post**
> ArtifactOut commit_upload_v0_uploads_upload_id_commit_post(upload_id)

Commit a large (direct-to-GCS) upload

Finalize the upload begun at `/v0/uploads`: AgentDrive verifies the object that landed in GCS (size + checksum) and creates the artifact. Idempotent — a retry after a successful commit returns the same artifact. The write budget is charged when the upload session is created; commit retries are not charged again.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    upload_id = 'upload_id_example' # str |

    try:
        # Commit a large (direct-to-GCS) upload
        api_response = api_instance.commit_upload_v0_uploads_upload_id_commit_post(upload_id)
        print("The response of DefaultApi->commit_upload_v0_uploads_upload_id_commit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->commit_upload_v0_uploads_upload_id_commit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No such upload for this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | Uploaded object size differs from declared size_bytes. |  * X-Request-Id - Request correlation identifier. <br>  |
**410** | Upload session expired. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | If-Match precondition failed or create-only conflict. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**413** | Committing the upload would exceed the storage quota. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | Drive&#39;s per-hour write budget exhausted. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_artifact_route_v0_artifacts_art_id_copy_post**
> ArtifactOut copy_artifact_route_v0_artifacts_art_id_copy_post(art_id, copy_in, x_agentdrive_actor=x_agentdrive_actor, if_none_match=if_none_match)

Duplicate an artifact to a new path (CAS-shared, new ID)

Create a new artifact at `path` whose bytes are identical to the source artifact's. The copy reuses the source's CAS object (zero new storage) but gets a fresh `art_…` ID, a fresh version 1, and — by default — `source.refs = [{type: 'artifact', id: '<source>'}]` so provenance is preserved.

Quota: the copy's `size_bytes` is added to the drive's `storage_bytes` even though physical bytes are shared.

Source-version pin: pass `from_generation` in the body to require the source's current content generation (`version_number`) to equal it (→ 412 SOURCE_VERSION_MISMATCH); a concurrent source *metadata* edit does NOT fail the copy. Destination create-only: `If-None-Match: *` returns 412 CREATE_CONFLICT (instead of 409 PATH_CONFLICT) when the target path is occupied.

Returns 409 PATH_CONFLICT if the target path is already taken; 413 STORAGE_QUOTA_EXCEEDED if the copy would push the drive over its limit.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
from agentdrive_sdk.models.copy_in import CopyIn
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |
    copy_in = agentdrive_sdk.CopyIn() # CopyIn |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_none_match = 'if_none_match_example' # str |  (optional)

    try:
        # Duplicate an artifact to a new path (CAS-shared, new ID)
        api_response = api_instance.copy_artifact_route_v0_artifacts_art_id_copy_post(art_id, copy_in, x_agentdrive_actor=x_agentdrive_actor, if_none_match=if_none_match)
        print("The response of DefaultApi->copy_artifact_route_v0_artifacts_art_id_copy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->copy_artifact_route_v0_artifacts_art_id_copy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |
 **copy_in** | [**CopyIn**](CopyIn.md)|  |
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_none_match** | **str**|  | [optional]

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The destination path or source metadata is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The source artifact does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The destination path is already occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**413** | The copy would exceed the drive storage limit. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_folder_by_id_v0_folders_fld_id_copy_post**
> FolderCopyOut copy_folder_by_id_v0_folders_fld_id_copy_post(fld_id, folder_copy_in, x_agentdrive_actor=x_agentdrive_actor, if_none_match=if_none_match)

Duplicate a folder subtree to a new path (CAS-shared, new IDs)

Clone the folder identified by URL id — and every descendant folder + artifact — under the body's `path` (canonical, trailing slash). Each copied artifact reuses the source's CAS object (zero new storage) but gets a fresh `art_…` ID, a fresh version 1, and `source.refs = [{type: 'artifact', id: '<source>'}]` provenance. The new folder gets a fresh `fld_…` ID and the source's description.

The entire subtree is copied in a SINGLE transaction — either every row lands or none does.

Quota: each copy's `size_bytes` counts against the drive's `storage_bytes` even though physical bytes are shared.

Source-version pin: pass `from_metageneration` in the body to require the source folder's current `metageneration` to equal it (→ 412 SOURCE_VERSION_MISMATCH). Destination create-only: `If-None-Match: *` returns 412 CREATE_CONFLICT (instead of 409 FOLDER_PATH_CONFLICT) when the destination folder is occupied.

Returns 409 `FOLDER_PATH_CONFLICT` if the destination collides with a live folder or artifact; 400 `FOLDER_PATH_INVALID` if `path` is non-canonical; 413 `SUBTREE_TOO_LARGE` if the source holds more than 5000 artifacts; 413 `STORAGE_QUOTA_EXCEEDED` if the copy would push the drive over its limit.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_copy_in import FolderCopyIn
from agentdrive_sdk.models.folder_copy_out import FolderCopyOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str |
    folder_copy_in = agentdrive_sdk.FolderCopyIn() # FolderCopyIn |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_none_match = 'if_none_match_example' # str |  (optional)

    try:
        # Duplicate a folder subtree to a new path (CAS-shared, new IDs)
        api_response = api_instance.copy_folder_by_id_v0_folders_fld_id_copy_post(fld_id, folder_copy_in, x_agentdrive_actor=x_agentdrive_actor, if_none_match=if_none_match)
        print("The response of DefaultApi->copy_folder_by_id_v0_folders_fld_id_copy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->copy_folder_by_id_v0_folders_fld_id_copy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  |
 **folder_copy_in** | [**FolderCopyIn**](FolderCopyIn.md)|  |
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_none_match** | **str**|  | [optional]

### Return type

[**FolderCopyOut**](FolderCopyOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The destination path is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The destination path is already occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**413** | The copied subtree would exceed the drive storage limit. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder_by_path_v0_folders_path_put**
> FolderOut create_folder_by_path_v0_folders_path_put(path, x_agentdrive_actor=x_agentdrive_actor, if_none_match=if_none_match, folder_create_in=folder_create_in)

Create a folder (idempotent)

Create a folder at the URL path. Idempotent create-at-known-URI (mirrors `PUT /v0/artifacts/{path}`) — a second call for the same live path returns the existing row unchanged (metadata updates require PATCH). Returns 201 on create, 200 when the folder already exists.

Send `If-None-Match: *` to make it strictly create-only: an existing folder then returns 412 CREATE_CONFLICT instead of the idempotent 200.

Returns 409 `FOLDER_PATH_CONFLICT` if a live artifact occupies the file form of the path (e.g. mkdir `/foo/` when an artifact lives at `/foo`).

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_create_in import FolderCreateIn
from agentdrive_sdk.models.folder_out import FolderOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_none_match = 'if_none_match_example' # str |  (optional)
    folder_create_in = agentdrive_sdk.FolderCreateIn() # FolderCreateIn |  (optional)

    try:
        # Create a folder (idempotent)
        api_response = api_instance.create_folder_by_path_v0_folders_path_put(path, x_agentdrive_actor=x_agentdrive_actor, if_none_match=if_none_match, folder_create_in=folder_create_in)
        print("The response of DefaultApi->create_folder_by_path_v0_folders_path_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_folder_by_path_v0_folders_path_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_none_match** | **str**|  | [optional]
 **folder_create_in** | [**FolderCreateIn**](FolderCreateIn.md)|  | [optional]

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The existing folder was returned unchanged. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**201** | Successful Response |  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The folder path is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The folder conflicts with an existing path. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_grant_route_v0_grants_post**
> GrantOut create_grant_route_v0_grants_post(grant_create_in, x_agentdrive_actor=x_agentdrive_actor)

Create (or fetch) a per-principal grant on a resource

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.grant_create_in import GrantCreateIn
from agentdrive_sdk.models.grant_out import GrantOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    grant_create_in = agentdrive_sdk.GrantCreateIn() # GrantCreateIn |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)

    try:
        # Create (or fetch) a per-principal grant on a resource
        api_response = api_instance.create_grant_route_v0_grants_post(grant_create_in, x_agentdrive_actor=x_agentdrive_actor)
        print("The response of DefaultApi->create_grant_route_v0_grants_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_grant_route_v0_grants_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_create_in** | [**GrantCreateIn**](GrantCreateIn.md)|  |
 **x_agentdrive_actor** | **str**|  | [optional]

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The grant or expiry is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The target resource does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_share_route_v0_shares_post**
> ShareMintOut create_share_route_v0_shares_post(share_create_in, x_agentdrive_actor=x_agentdrive_actor)

Mint a share link (returns the share_key once)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.share_create_in import ShareCreateIn
from agentdrive_sdk.models.share_mint_out import ShareMintOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    share_create_in = agentdrive_sdk.ShareCreateIn() # ShareCreateIn |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)

    try:
        # Mint a share link (returns the share_key once)
        api_response = api_instance.create_share_route_v0_shares_post(share_create_in, x_agentdrive_actor=x_agentdrive_actor)
        print("The response of DefaultApi->create_share_route_v0_shares_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_share_route_v0_shares_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_create_in** | [**ShareCreateIn**](ShareCreateIn.md)|  |
 **x_agentdrive_actor** | **str**|  | [optional]

### Return type

[**ShareMintOut**](ShareMintOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The share settings or expiry are invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The target resource does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact_by_id_route_v0_artifacts_art_id_delete**
> ArtifactDeleteOut delete_artifact_by_id_route_v0_artifacts_art_id_delete(art_id, if_match=if_match, x_agentdrive_actor=x_agentdrive_actor)

Soft-delete an artifact by its stable ID

Soft-delete the artifact with this `art_…` ID. Same semantics + response shape as the path-based `DELETE /v0/artifacts/{path}` (reversible until the GC cron hard-deletes at `purge_at`; `restore_url` points at the by-id restore), but keys on the immutable id so a concurrent rename can't change the target.

Returns 404 ARTIFACT_NOT_FOUND if no live artifact has this id; 403 WIKI_RESERVED for `_wiki/` artifacts (system-managed); 412 if `If-Match` doesn't match the current version. Declared before the `{path:path}` family so the id convertor wins for DELETEs.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_delete_out import ArtifactDeleteOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |
    if_match = 'if_match_example' # str |  (optional)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)

    try:
        # Soft-delete an artifact by its stable ID
        api_response = api_instance.delete_artifact_by_id_route_v0_artifacts_art_id_delete(art_id, if_match=if_match, x_agentdrive_actor=x_agentdrive_actor)
        print("The response of DefaultApi->delete_artifact_by_id_route_v0_artifacts_art_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_artifact_by_id_route_v0_artifacts_art_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |
 **if_match** | **str**|  | [optional]
 **x_agentdrive_actor** | **str**|  | [optional]

### Return type

[**ArtifactDeleteOut**](ArtifactDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No live artifact with this ID exists. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | If-Match does not match the current artifact. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact_v0_artifacts_path_delete**
> ArtifactDeleteOut delete_artifact_v0_artifacts_path_delete(path, if_match=if_match, x_agentdrive_actor=x_agentdrive_actor)

Delete Artifact

Soft-delete the artifact at the given path.

A delete WITHOUT an `If-Match` precondition is last-writer-wins and will
silently remove a concurrently-modified artifact.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_delete_out import ArtifactDeleteOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str |
    if_match = 'if_match_example' # str |  (optional)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)

    try:
        # Delete Artifact
        api_response = api_instance.delete_artifact_v0_artifacts_path_delete(path, if_match=if_match, x_agentdrive_actor=x_agentdrive_actor)
        print("The response of DefaultApi->delete_artifact_v0_artifacts_path_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_artifact_v0_artifacts_path_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |
 **if_match** | **str**|  | [optional]
 **x_agentdrive_actor** | **str**|  | [optional]

### Return type

[**ArtifactDeleteOut**](ArtifactDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No such live artifact exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_drive_route_v0_drives_drive_id_delete**
> DriveDeleteOut delete_drive_route_v0_drives_drive_id_delete(drive_id, confirm=confirm, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Soft-delete a drive

Mark the drive for cleanup. All tenant data (artifacts, versions, wiki, embeddings, events) is hidden via the `live_*` views and CASCADE-removed by the GC cleanup cron at `purge_at`. Restore via `POST /v0/drives/{id}/restore` while the row is still in trash. The path-param `drive_id` MUST match the authenticated drive.

Accepts either an `ad_live_` per-drive key (deletes that key's drive) or an `ad_user_` user token selecting an owned drive (workspaces-design §5.3); a `read`-scope user token is rejected with 403 `INSUFFICIENT_SCOPE`. **Guard (§8):** a workspace must retain at least one live drive — deleting the workspace's last live drive returns 409 `LAST_DRIVE`.

**Explicit confirmation required:** pass `?confirm=DELETE` or the request is rejected with 400 `CONFIRM_REQUIRED`. Tenant-level deletion is the largest-blast-radius operation on the API; the static token forces a deliberate act (soft-delete still gives a restore window on top).

**Optimistic concurrency:** send `If-Match` with the drive's composite ETag (`"<drv_id>.0.<metageneration>"`, from a drive read) to make the delete conditional — a stale token returns 412 PRECONDITION_FAILED. A delete WITHOUT an `If-Match` precondition is last-writer-wins and will silently trash a concurrently-modified drive.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.drive_delete_out import DriveDeleteOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    drive_id = 'drive_id_example' # str |
    confirm = 'confirm_example' # str |  (optional)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Soft-delete a drive
        api_response = api_instance.delete_drive_route_v0_drives_drive_id_delete(drive_id, confirm=confirm, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->delete_drive_route_v0_drives_drive_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_drive_route_v0_drives_drive_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |
 **confirm** | **str**|  | [optional]
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**DriveDeleteOut**](DriveDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The explicit DELETE confirmation is missing. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No such drive exists for this principal. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The workspace must retain at least one live drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder_by_id_v0_folders_fld_id_delete**
> FolderDeleteOut delete_folder_by_id_v0_folders_fld_id_delete(fld_id, recursive=recursive, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Soft-delete a folder by stable ID (cascade with ?recursive=true)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_delete_out import FolderDeleteOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str |
    recursive = False # bool |  (optional) (default to False)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Soft-delete a folder by stable ID (cascade with ?recursive=true)
        api_response = api_instance.delete_folder_by_id_v0_folders_fld_id_delete(fld_id, recursive=recursive, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->delete_folder_by_id_v0_folders_fld_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_folder_by_id_v0_folders_fld_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  |
 **recursive** | **bool**|  | [optional] [default to False]
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**FolderDeleteOut**](FolderDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder_by_path_v0_folders_path_delete**
> FolderDeleteOut delete_folder_by_path_v0_folders_path_delete(path, recursive=recursive, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Soft-delete a folder (cascade with ?recursive=true)

Soft-delete the folder. Refuses if the folder has live descendants unless `?recursive=true` is set, in which case ALL descendant folders + artifacts are soft-deleted in the same transaction.

Returns 409 `FOLDER_RECURSIVE_REQUIRED` (with descendant counts in `colliding_path`) when recursion is needed but the flag isn't set. Retention window is frozen on `purge_at` per deletion-design.md §5.1; mid-retention tier changes don't shift it.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_delete_out import FolderDeleteOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str |
    recursive = False # bool |  (optional) (default to False)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Soft-delete a folder (cascade with ?recursive=true)
        api_response = api_instance.delete_folder_by_path_v0_folders_path_delete(path, recursive=recursive, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->delete_folder_by_path_v0_folders_path_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_folder_by_path_v0_folders_path_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |
 **recursive** | **bool**|  | [optional] [default to False]
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**FolderDeleteOut**](FolderDeleteOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_grant_route_v0_grants_grn_id_delete**
> RevokeOut delete_grant_route_v0_grants_grn_id_delete(grn_id, x_agentdrive_actor=x_agentdrive_actor)

Revoke a grant (can_manage, or self-revoke own grant)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.revoke_out import RevokeOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    grn_id = 'grn_id_example' # str |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)

    try:
        # Revoke a grant (can_manage, or self-revoke own grant)
        api_response = api_instance.delete_grant_route_v0_grants_grn_id_delete(grn_id, x_agentdrive_actor=x_agentdrive_actor)
        print("The response of DefaultApi->delete_grant_route_v0_grants_grn_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_grant_route_v0_grants_grn_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grn_id** | **str**|  |
 **x_agentdrive_actor** | **str**|  | [optional]

### Return type

[**RevokeOut**](RevokeOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The grant does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_share_route_v0_shares_shr_id_delete**
> RevokeOut delete_share_route_v0_shares_shr_id_delete(shr_id, x_agentdrive_actor=x_agentdrive_actor)

Revoke a share link (requires can_manage)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.revoke_out import RevokeOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    shr_id = 'shr_id_example' # str |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)

    try:
        # Revoke a share link (requires can_manage)
        api_response = api_instance.delete_share_route_v0_shares_shr_id_delete(shr_id, x_agentdrive_actor=x_agentdrive_actor)
        print("The response of DefaultApi->delete_share_route_v0_shares_shr_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_share_route_v0_shares_shr_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shr_id** | **str**|  |
 **x_agentdrive_actor** | **str**|  | [optional]

### Return type

[**RevokeOut**](RevokeOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The share does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_artifact_by_id_v0_artifacts_art_id_download_get**
> bytes download_artifact_by_id_v0_artifacts_art_id_download_get(art_id)

Stream the artifact bytes by stable ID (never rendered HTML)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |

    try:
        # Stream the artifact bytes by stable ID (never rendered HTML)
        api_response = api_instance.download_artifact_by_id_v0_artifacts_art_id_download_get(art_id)
        print("The response of DefaultApi->download_artifact_by_id_v0_artifacts_art_id_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_artifact_by_id_v0_artifacts_art_id_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |

### Return type

**bytes**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw artifact bytes. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No live artifact with this ID exists. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_artifact_by_path_v0_artifacts_path_download_get**
> bytes download_artifact_by_path_v0_artifacts_path_download_get(path)

Stream the artifact bytes by path (never rendered HTML)

Same bytes-only machine surface as `/{art_id}/download` but resolves the artifact by path, so callers don't have to resolve path→id first. Applies the identical CSP `sandbox` + `nosniff` posture (never serves HTML inline as active content).

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str |

    try:
        # Stream the artifact bytes by path (never rendered HTML)
        api_response = api_instance.download_artifact_by_path_v0_artifacts_path_download_get(path)
        print("The response of DefaultApi->download_artifact_by_path_v0_artifacts_path_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_artifact_by_path_v0_artifacts_path_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |

### Return type

**bytes**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw artifact bytes. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No live artifact exists at this path. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_artifact_version_v0_artifacts_art_id_versions_version_number_download_get**
> bytes download_artifact_version_v0_artifacts_art_id_versions_version_number_download_get(art_id, version_number)

Stream bytes for a specific version (machine surface)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |
    version_number = 56 # int |

    try:
        # Stream bytes for a specific version (machine surface)
        api_response = api_instance.download_artifact_version_v0_artifacts_art_id_versions_version_number_download_get(art_id, version_number)
        print("The response of DefaultApi->download_artifact_version_v0_artifacts_art_id_versions_version_number_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_artifact_version_v0_artifacts_art_id_versions_version_number_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |
 **version_number** | **int**|  |

### Return type

**bytes**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw artifact bytes. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The artifact or version does not exist. |  * X-Request-Id - Request correlation identifier. <br>  |
**410** | The requested version has been pruned. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_url_by_id_v0_artifacts_art_id_download_url_get**
> DownloadUrlOut download_url_by_id_v0_artifacts_art_id_download_url_get(art_id)

Signed direct-from-GCS download URL by stable ID

Returns a URL for the artifact's bytes. For large artifacts (>= the signed-download threshold) when signing is available, it's a short-lived **signed GCS URL** the client fetches directly (`direct:true`, `expires_at` set); otherwise the **proxy** `/download` URL (`direct:false`). Treat the URL as opaque. large-download-design.md §5.1.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.download_url_out import DownloadUrlOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |

    try:
        # Signed direct-from-GCS download URL by stable ID
        api_response = api_instance.download_url_by_id_v0_artifacts_art_id_download_url_get(art_id)
        print("The response of DefaultApi->download_url_by_id_v0_artifacts_art_id_download_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_url_by_id_v0_artifacts_art_id_download_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The artifact does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_url_by_path_v0_artifacts_path_download_url_get**
> DownloadUrlOut download_url_by_path_v0_artifacts_path_download_url_get(path)

Signed direct-from-GCS download URL by path

Same as `/{art_id}/download-url` but resolves the artifact by path. The returned proxy URL (when `direct:false`) still points at the by-id `/download` endpoint. large-download-design.md §5.1.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.download_url_out import DownloadUrlOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str |

    try:
        # Signed direct-from-GCS download URL by path
        api_response = api_instance.download_url_by_path_v0_artifacts_path_download_url_get(path)
        print("The response of DefaultApi->download_url_by_path_v0_artifacts_path_download_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_url_by_path_v0_artifacts_path_download_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The artifact does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_url_version_v0_artifacts_art_id_versions_version_number_download_url_get**
> DownloadUrlOut download_url_version_v0_artifacts_art_id_versions_version_number_download_url_get(art_id, version_number)

Signed direct-from-GCS download URL for a specific version

Same as `/{art_id}/download-url` but for a specific version's bytes (`direct:true` signed GCS URL when large + signing available, else the proxy `/versions/{n}/download` URL). large-download-design.md §5.1.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.download_url_out import DownloadUrlOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |
    version_number = 56 # int |

    try:
        # Signed direct-from-GCS download URL for a specific version
        api_response = api_instance.download_url_version_v0_artifacts_art_id_versions_version_number_download_url_get(art_id, version_number)
        print("The response of DefaultApi->download_url_version_v0_artifacts_art_id_versions_version_number_download_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_url_version_v0_artifacts_art_id_versions_version_number_download_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |
 **version_number** | **int**|  |

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The artifact or version does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**410** | The requested version was pruned by retention. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enqueue_job_v0_projects_fld_id_jobs_post**
> CompileJobOut enqueue_job_v0_projects_fld_id_jobs_post(fld_id, compile_job_in, x_agentdrive_actor=x_agentdrive_actor)

Enqueue a compile job for a project (folder)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.compile_job_in import CompileJobIn
from agentdrive_sdk.models.compile_job_out import CompileJobOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str |
    compile_job_in = agentdrive_sdk.CompileJobIn() # CompileJobIn |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)

    try:
        # Enqueue a compile job for a project (folder)
        api_response = api_instance.enqueue_job_v0_projects_fld_id_jobs_post(fld_id, compile_job_in, x_agentdrive_actor=x_agentdrive_actor)
        print("The response of DefaultApi->enqueue_job_v0_projects_fld_id_jobs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->enqueue_job_v0_projects_fld_id_jobs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  |
 **compile_job_in** | [**CompileJobIn**](CompileJobIn.md)|  |
 **x_agentdrive_actor** | **str**|  | [optional]

### Return type

[**CompileJobOut**](CompileJobOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**202** | Compile accepted and queued or running. |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The task, engine, entrypoint, or project is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**402** | The current plan does not permit this compile. |  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The project folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**413** | The compile project exceeds an input or storage limit. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extension_start_auth_extension_start_get**
> extension_start_auth_extension_start_get(ext_id=ext_id)

Extension Start

Begin a sign-in flow on behalf of a Chrome extension.

Provider follows AUTH_MODE (WorkOS AuthKit or the TokenCanopy hub),
exactly like /auth/login. Stamps `for=ext` + `ext_id` into the
signed OAuth state so the callback handler knows to render the
extension handoff page instead of setting a session cookie.

Three short-circuits, all surface as actionable errors:
  * EXTENSION_AUTH_DISABLED (503): kill switch flipped off.
  * UNKNOWN_EXTENSION (400): `ext_id` not on the allow-list.
  * Missing `ext_id` query string (400 INVALID_REQUEST).

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    ext_id = 'ext_id_example' # str |  (optional)

    try:
        # Extension Start
        api_instance.extension_start_auth_extension_start_get(ext_id=ext_id)
    except Exception as e:
        print("Exception when calling DefaultApi->extension_start_auth_extension_start_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ext_id** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the canonical or authentication URL. |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The extension ID is missing or not allowed. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**503** | Extension authentication is temporarily disabled. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_v0_find_get**
> FindPage find_v0_find_get(q, mode=mode, label=label, file_type=file_type, prefix=prefix, modality=modality, updated_after=updated_after, updated_before=updated_before, limit=limit)

Hybrid passage retrieval over the full file body

Passage-level chunk RAG over `embed_chunks`. Lexical (`chunk_tsv`, GIN) + semantic (HNSW over `embedding`) are run in parallel and fused via Reciprocal Rank Fusion (k=60). Unlike `/v0/search`, which only sees the first ~16 KB preview of each artifact, `/v0/find` reaches the full file body.

**Modes:**
- `hybrid` (default) — lexical + semantic, RRF-fused.
- `lexical` — `chunk_tsv` only. Best for exact tokens, identifiers, code snippets.
- `semantic` — embedding only. Best for conceptual queries where the surface terms differ from the query phrasing.

**Granularity:** results are passages, not files. A long document with multiple matching regions returns multiple hits with distinct `ord` values; consecutive `ord`s overlap by ~400 tokens. Dedupe by `art_id` if you want one row per file.

**Span citations:** `char_start`/`char_end` for text & code, `page_start`/`page_end` for PDFs, `time_start_ms`/`time_end_ms` for audio & video. Only the modality-relevant pair is populated.

**Filters:** `label`, `file_type`, `prefix`, `modality` (repeatable), `updated_after` / `updated_before` (RFC 3339 timestamps, inclusive bounds on `updated_at`, applied to both legs).

**Wiki coverage:** `/v0/find` excludes `_wiki/` paths by default and — importantly — does NOT cover them even when the caller passes `prefix=_wiki/...`. Wiki pages are not embedded by the pipeline (they're system-generated output, not user input), so `embed_chunks` has no rows for them and the join returns empty. Use `wiki_search` (or `list`/`grep` with a `_wiki/` prefix) for the wiki layer.

**Embedding availability:** when `GEMINI_API_KEY` is not configured, `mode=semantic` returns 503; `mode=hybrid` logs a warning and falls back to lexical-only; `mode=lexical` is unaffected.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.find_page import FindPage
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    q = 'q_example' # str |
    mode = 'hybrid' # str |  (optional) (default to 'hybrid')
    label = ['label_example'] # List[str] |  (optional)
    file_type = 'file_type_example' # str |  (optional)
    prefix = 'prefix_example' # str |  (optional)
    modality = ['modality_example'] # List[Optional[str]] |  (optional)
    updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # Hybrid passage retrieval over the full file body
        api_response = api_instance.find_v0_find_get(q, mode=mode, label=label, file_type=file_type, prefix=prefix, modality=modality, updated_after=updated_after, updated_before=updated_before, limit=limit)
        print("The response of DefaultApi->find_v0_find_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->find_v0_find_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  |
 **mode** | **str**|  | [optional] [default to &#39;hybrid&#39;]
 **label** | [**List[str]**](str.md)|  | [optional]
 **file_type** | **str**|  | [optional]
 **prefix** | **str**|  | [optional]
 **modality** | [**List[Optional[str]]**](str.md)|  | [optional]
 **updated_after** | **datetime**|  | [optional]
 **updated_before** | **datetime**|  | [optional]
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**FindPage**](FindPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**503** | Semantic embeddings are unavailable; use lexical or hybrid mode. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_by_id_meta_v0_artifacts_art_id_meta_get**
> ArtifactOut get_artifact_by_id_meta_v0_artifacts_art_id_meta_get(art_id)

Artifact metadata by stable ID (same shape as path /meta)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |

    try:
        # Artifact metadata by stable ID (same shape as path /meta)
        api_response = api_instance.get_artifact_by_id_meta_v0_artifacts_art_id_meta_get(art_id)
        print("The response of DefaultApi->get_artifact_by_id_meta_v0_artifacts_art_id_meta_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_artifact_by_id_meta_v0_artifacts_art_id_meta_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No such artifact exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_by_id_v0_artifacts_art_id_get**
> ArtifactOut get_artifact_by_id_v0_artifacts_art_id_get(art_id)

Canonical lookup of an artifact by its stable ID

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |

    try:
        # Canonical lookup of an artifact by its stable ID
        api_response = api_instance.get_artifact_by_id_v0_artifacts_art_id_get(art_id)
        print("The response of DefaultApi->get_artifact_by_id_v0_artifacts_art_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_artifact_by_id_v0_artifacts_art_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No such artifact exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_meta_v0_artifacts_path_meta_get**
> ArtifactOut get_artifact_meta_v0_artifacts_path_meta_get(path)

Get Artifact Meta

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str |

    try:
        # Get Artifact Meta
        api_response = api_instance.get_artifact_meta_v0_artifacts_path_meta_get(path)
        print("The response of DefaultApi->get_artifact_meta_v0_artifacts_path_meta_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_artifact_meta_v0_artifacts_path_meta_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The artifact does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_version_v0_artifacts_art_id_versions_version_number_get**
> VersionOut get_artifact_version_v0_artifacts_art_id_versions_version_number_get(art_id, version_number)

Metadata for a specific version of an artifact

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.version_out import VersionOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |
    version_number = 56 # int |

    try:
        # Metadata for a specific version of an artifact
        api_response = api_instance.get_artifact_version_v0_artifacts_art_id_versions_version_number_get(art_id, version_number)
        print("The response of DefaultApi->get_artifact_version_v0_artifacts_art_id_versions_version_number_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_artifact_version_v0_artifacts_art_id_versions_version_number_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |
 **version_number** | **int**|  |

### Return type

[**VersionOut**](VersionOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The artifact or version does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**410** | The requested version was pruned by retention. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drive_route_v0_drives_drive_id_get**
> DriveReadOut get_drive_route_v0_drives_drive_id_get(drive_id)

Drive overview by id (same shape as /drives/me)

Identical to `GET /v0/drives/me` — the by-id singleton so `Location`-style URLs and scripted clients can address the drive canonically. The path-param `drive_id` MUST match the authenticated drive (mirrors the delete/trash routes' no-leak 404). Emits the drive's composite `ETag` header (`"<drv_id>.0.<metageneration>"`).

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.drive_read_out import DriveReadOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    drive_id = 'drive_id_example' # str |

    try:
        # Drive overview by id (same shape as /drives/me)
        api_response = api_instance.get_drive_route_v0_drives_drive_id_get(drive_id)
        print("The response of DefaultApi->get_drive_route_v0_drives_drive_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_drive_route_v0_drives_drive_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |

### Return type

[**DriveReadOut**](DriveReadOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No matching authenticated drive exists. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feedback_status_v0_feedback_fbk_id_get**
> FeedbackStatusOut get_feedback_status_v0_feedback_fbk_id_get(fbk_id)

Get Feedback Status

Lifecycle status of feedback THIS drive filed. Foreign tickets
read as 404 — indistinguishable from absent.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.feedback_status_out import FeedbackStatusOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fbk_id = 'fbk_id_example' # str |

    try:
        # Get Feedback Status
        api_response = api_instance.get_feedback_status_v0_feedback_fbk_id_get(fbk_id)
        print("The response of DefaultApi->get_feedback_status_v0_feedback_fbk_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_feedback_status_v0_feedback_fbk_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fbk_id** | **str**|  |

### Return type

[**FeedbackStatusOut**](FeedbackStatusOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The feedback ticket does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_id_meta_v0_folders_fld_id_meta_get**
> FolderOut get_folder_by_id_meta_v0_folders_fld_id_meta_get(fld_id)

Folder metadata by stable ID (same shape as the bare id route)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_out import FolderOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str |

    try:
        # Folder metadata by stable ID (same shape as the bare id route)
        api_response = api_instance.get_folder_by_id_meta_v0_folders_fld_id_meta_get(fld_id)
        print("The response of DefaultApi->get_folder_by_id_meta_v0_folders_fld_id_meta_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_folder_by_id_meta_v0_folders_fld_id_meta_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_id_v0_folders_fld_id_get**
> FolderOut get_folder_by_id_v0_folders_fld_id_get(fld_id)

Canonical lookup of a folder by its stable ID

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_out import FolderOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str |

    try:
        # Canonical lookup of a folder by its stable ID
        api_response = api_instance.get_folder_by_id_v0_folders_fld_id_get(fld_id)
        print("The response of DefaultApi->get_folder_by_id_v0_folders_fld_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_folder_by_id_v0_folders_fld_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_path_meta_v0_folders_path_meta_get**
> FolderOut get_folder_by_path_meta_v0_folders_path_meta_get(path)

Folder metadata by path (same shape as the bare path route)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_out import FolderOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str |

    try:
        # Folder metadata by path (same shape as the bare path route)
        api_response = api_instance.get_folder_by_path_meta_v0_folders_path_meta_get(path)
        print("The response of DefaultApi->get_folder_by_path_meta_v0_folders_path_meta_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_folder_by_path_meta_v0_folders_path_meta_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_path_v0_folders_path_get**
> FolderOut get_folder_by_path_v0_folders_path_get(path)

Read folder metadata by path

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_out import FolderOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str |

    try:
        # Read folder metadata by path
        api_response = api_instance.get_folder_by_path_v0_folders_path_get(path)
        print("The response of DefaultApi->get_folder_by_path_v0_folders_path_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_folder_by_path_v0_folders_path_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**304** | The current entity tag or modification date matched. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grant_route_v0_grants_grn_id_get**
> GrantOut get_grant_route_v0_grants_grn_id_get(grn_id)

Read a single grant (can_manage, or the grant's own principal)

The `Location` target of `POST /v0/grants`. Authorization mirrors
DELETE: `can_manage` on the granted resource, or the caller IS the
grant's own principal (a grantee may read — like revoke — their own
grant). A revoked grant reads as 404 (same no-leak shape as a
foreign/absent id); DELETE stays idempotent on it.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.grant_out import GrantOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    grn_id = 'grn_id_example' # str |

    try:
        # Read a single grant (can_manage, or the grant's own principal)
        api_response = api_instance.get_grant_route_v0_grants_grn_id_get(grn_id)
        print("The response of DefaultApi->get_grant_route_v0_grants_grn_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_grant_route_v0_grants_grn_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grn_id** | **str**|  |

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The grant does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_logs_v0_jobs_job_id_logs_get**
> str get_job_logs_v0_jobs_job_id_logs_get(job_id)

Raw compile log (text/plain)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    job_id = 'job_id_example' # str |

    try:
        # Raw compile log (text/plain)
        api_response = api_instance.get_job_logs_v0_jobs_job_id_logs_get(job_id)
        print("The response of DefaultApi->get_job_logs_v0_jobs_job_id_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_job_logs_v0_jobs_job_id_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  |

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw compile log. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The job or its captured log does not exist. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_v0_jobs_job_id_get**
> CompileJobOut get_job_v0_jobs_job_id_get(job_id)

Poll a job

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.compile_job_out import CompileJobOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    job_id = 'job_id_example' # str |

    try:
        # Poll a job
        api_response = api_instance.get_job_v0_jobs_job_id_get(job_id)
        print("The response of DefaultApi->get_job_v0_jobs_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_job_v0_jobs_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  |

### Return type

[**CompileJobOut**](CompileJobOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No such compile job exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_v0_projects_fld_id_get**
> CompileProjectOut get_project_v0_projects_fld_id_get(fld_id)

Get a project's compile config

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.compile_project_out import CompileProjectOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str |

    try:
        # Get a project's compile config
        api_response = api_instance.get_project_v0_projects_fld_id_get(fld_id)
        print("The response of DefaultApi->get_project_v0_projects_fld_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_v0_projects_fld_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  |

### Return type

[**CompileProjectOut**](CompileProjectOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The project folder does not exist or has no compile configuration. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_share_route_v0_shares_shr_id_get**
> ShareOut get_share_route_v0_shares_shr_id_get(shr_id)

Read a single share link's metadata (requires can_manage)

The `Location` target of `POST /v0/shares`. Metadata ONLY —
`ShareOut` never carries the raw `share_key`/URL (returned exactly
once at mint/rotate, §4.5). Authorization mirrors DELETE:
`can_manage` on the shared resource. A revoked share reads as 404
(same no-leak shape as a foreign/absent id).

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.share_out import ShareOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    shr_id = 'shr_id_example' # str |

    try:
        # Read a single share link's metadata (requires can_manage)
        api_response = api_instance.get_share_route_v0_shares_shr_id_get(shr_id)
        print("The response of DefaultApi->get_share_route_v0_shares_shr_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_share_route_v0_shares_shr_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shr_id** | **str**|  |

### Return type

[**ShareOut**](ShareOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The share does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_status_v0_uploads_upload_id_get**
> UploadStatusOut get_upload_status_v0_uploads_upload_id_get(upload_id)

Get the status of a large (direct-to-GCS) upload session

Report the live state of an upload session begun at `/v0/uploads`. `state` is derived: `initiated` (open — PUT the bytes then commit), `committed` (artifact created), `aborted` (released via DELETE), or `expired` (past `expires_at` without a commit). Read-only; charges the read budget.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.upload_status_out import UploadStatusOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    upload_id = 'upload_id_example' # str |

    try:
        # Get the status of a large (direct-to-GCS) upload session
        api_response = api_instance.get_upload_status_v0_uploads_upload_id_get(upload_id)
        print("The response of DefaultApi->get_upload_status_v0_uploads_upload_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_upload_status_v0_uploads_upload_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  |

### Return type

[**UploadStatusOut**](UploadStatusOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No such upload for this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_health_get**
> HealthOut health_health_get()

Health

Liveness + DB-reachability probe. Used by Cloud Run / k8s healthchecks
and any uptime monitor. Returns 200 only if the DB pool can serve a
trivial query; 503 otherwise so the orchestrator can pull the instance
out of rotation.

NOTE: route is `/health`, NOT `/healthz`. Google's edge infrastructure
intercepts `/healthz` (legacy kubernetes-reserved path) and returns a
generic 404 before traffic reaches Cloud Run — discovered the hard way
during the first prod deploy. Don't rename back.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.health_out import HealthOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)

    try:
        # Health
        api_response = api_instance.health_health_get()
        print("The response of DefaultApi->health_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthOut**](HealthOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**503** | The database reachability probe failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_artifact_versions_v0_artifacts_art_id_versions_get**
> VersionPage list_artifact_versions_v0_artifacts_art_id_versions_get(art_id, cursor=cursor, limit=limit)

List versions of an artifact, newest first

Returns versions in descending `version_number` order. Cursor pagination via `?cursor=<token>`; `next_cursor` is non-null when the page is full and more older versions may exist.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.version_page import VersionPage
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List versions of an artifact, newest first
        api_response = api_instance.list_artifact_versions_v0_artifacts_art_id_versions_get(art_id, cursor=cursor, limit=limit)
        print("The response of DefaultApi->list_artifact_versions_v0_artifacts_art_id_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_artifact_versions_v0_artifacts_art_id_versions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**VersionPage**](VersionPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The pagination cursor is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The artifact does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_artifacts_v0_artifacts_get**
> Page list_artifacts_v0_artifacts_get(prefix=prefix, label=label, file_type=file_type, cursor=cursor, limit=limit)

List artifacts in the drive

Returns artifacts sorted by path. Filter by `prefix`, `label` (repeatable + AND-combined), and `file_type`.

**Cursor pagination:** when more results exist, the response carries `next_cursor`. Pass it back as `?cursor=<token>` to fetch the next page. `next_cursor` is `null` on the final page. Filters MUST stay consistent across pages — the cursor encodes only the keyset position, not the filter set, so the client is responsible for re-sending the same filter on each page.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.page import Page
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    prefix = '' # str |  (optional) (default to '')
    label = ['label_example'] # List[Optional[str]] |  (optional)
    file_type = 'file_type_example' # str |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List artifacts in the drive
        api_response = api_instance.list_artifacts_v0_artifacts_get(prefix=prefix, label=label, file_type=file_type, cursor=cursor, limit=limit)
        print("The response of DefaultApi->list_artifacts_v0_artifacts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_artifacts_v0_artifacts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**|  | [optional] [default to &#39;&#39;]
 **label** | [**List[Optional[str]]**](str.md)|  | [optional]
 **file_type** | **str**|  | [optional]
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**Page**](Page.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The pagination cursor is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_events_route_v0_events_get**
> EventPage list_events_route_v0_events_get(art_id=art_id, action=action, since=since, before=before, cursor=cursor, limit=limit)

Read the append-only event log for the authenticated drive

Returns events newest-first. Filters compose with AND.

**Cursor pagination:** pass the oldest event's `created_at` from the previous page as `before` to fetch the next page back in time. Combine `since` + `before` to bound a window.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.event_page import EventPage
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |  (optional)
    action = 'action_example' # str |  (optional)
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # Read the append-only event log for the authenticated drive
        api_response = api_instance.list_events_route_v0_events_get(art_id=art_id, action=action, since=since, before=before, cursor=cursor, limit=limit)
        print("The response of DefaultApi->list_events_route_v0_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_events_route_v0_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  | [optional]
 **action** | **str**|  | [optional]
 **since** | **datetime**|  | [optional]
 **before** | **datetime**|  | [optional]
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**EventPage**](EventPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The pagination cursor is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_grants_route_v0_grants_get**
> GrantList list_grants_route_v0_grants_get(resource, cursor=cursor, limit=limit)

List live grants on a resource (requires can_manage)

**Cursor pagination:** when more results exist, the response carries `next_cursor`. Pass it back as `?cursor=<token>` to fetch the next page; `null` means the listing is complete. `limit` is clamped to [1, 100] (default 50), never rejected. The `resource` filter must be re-sent on every page — the cursor encodes only the keyset position.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.grant_list import GrantList
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    resource = 'resource_example' # str | art_*/fld_* id or a path
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List live grants on a resource (requires can_manage)
        api_response = api_instance.list_grants_route_v0_grants_get(resource, cursor=cursor, limit=limit)
        print("The response of DefaultApi->list_grants_route_v0_grants_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_grants_route_v0_grants_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| art_*/fld_* id or a path |
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**GrantList**](GrantList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The cursor or resource reference is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The target resource does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_jobs_v0_projects_fld_id_jobs_get**
> CompileJobListOut list_project_jobs_v0_projects_fld_id_jobs_get(fld_id, status=status, limit=limit, cursor=cursor)

List a project's jobs

List compile jobs newest first in stable `(created_at, job_id)` descending order. Pass a non-null `next_cursor` back as `cursor` to continue; malformed cursors return `400 BAD_CURSOR`. The cursor contains only the keyset position, so a `status` filter must be re-sent unchanged on every page. `limit` retains its existing default of 50 and validated range of 1 through 200.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.compile_job_list_out import CompileJobListOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str |
    status = 'status_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    cursor = 'cursor_example' # str |  (optional)

    try:
        # List a project's jobs
        api_response = api_instance.list_project_jobs_v0_projects_fld_id_jobs_get(fld_id, status=status, limit=limit, cursor=cursor)
        print("The response of DefaultApi->list_project_jobs_v0_projects_fld_id_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_project_jobs_v0_projects_fld_id_jobs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  |
 **status** | **str**|  | [optional]
 **limit** | **int**|  | [optional] [default to 50]
 **cursor** | **str**|  | [optional]

### Return type

[**CompileJobListOut**](CompileJobListOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The status filter is invalid, or the cursor is malformed (&#x60;BAD_CURSOR&#x60;). |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The project folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shares_route_v0_shares_get**
> ShareList list_shares_route_v0_shares_get(resource, cursor=cursor, limit=limit)

List live share links on a resource (requires can_manage)

**Cursor pagination:** when more results exist, the response carries `next_cursor`. Pass it back as `?cursor=<token>` to fetch the next page; `null` means the listing is complete. `limit` is clamped to [1, 100] (default 50), never rejected. The `resource` filter must be re-sent on every page — the cursor encodes only the keyset position.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.share_list import ShareList
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    resource = 'resource_example' # str | art_*/fld_* id or a path
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List live share links on a resource (requires can_manage)
        api_response = api_instance.list_shares_route_v0_shares_get(resource, cursor=cursor, limit=limit)
        print("The response of DefaultApi->list_shares_route_v0_shares_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_shares_route_v0_shares_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| art_*/fld_* id or a path |
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**ShareList**](ShareList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The cursor or resource reference is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The target resource does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trash_route_v0_drives_drive_id_trash_get**
> TrashOut list_trash_route_v0_drives_drive_id_trash_get(drive_id, cursor=cursor, limit=limit)

List the authenticated drive's trash

Returns soft-deleted artifacts on the drive plus the drive's own soft-delete state (if applicable). The path-param `drive_id` MUST match the authenticated drive.

**Compatibility window:** `limit` or `cursor` opts into cursor pagination. Unadorned requests retain the legacy complete result during the migration window. Paginated requests are clamped to 1–100 items (default 50 when only `cursor` is supplied). `items` is canonical; `artifacts` is a deprecated same-value alias.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.trash_out import TrashOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    drive_id = 'drive_id_example' # str |
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List the authenticated drive's trash
        api_response = api_instance.list_trash_route_v0_drives_drive_id_trash_get(drive_id, cursor=cursor, limit=limit)
        print("The response of DefaultApi->list_trash_route_v0_drives_drive_id_trash_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_trash_route_v0_drives_drive_id_trash_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**TrashOut**](TrashOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The cursor is malformed (&#x60;BAD_CURSOR&#x60;). |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No matching authenticated drive exists. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_auth_login_get**
> login_auth_login_get(return_to=return_to)

Login

Begin a WorkOS sign-in flow.

Mints a pre-login state cookie (binds the OAuth flow to this
browser — defense-in-depth against login-CSRF), signs a state
payload, and redirects to AuthKit. The hosted AuthKit page lets
the user pick Google OAuth, Microsoft OAuth, magic-link,
password, or passkey; we don't care which — they all funnel
back to /auth/callback with a `code` we exchange in D2.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    return_to = 'return_to_example' # str |  (optional)

    try:
        # Login
        api_instance.login_auth_login_get(return_to=return_to)
    except Exception as e:
        print("Exception when calling DefaultApi->login_auth_login_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_to** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the canonical or authentication URL. |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_auth_logout_post**
> logout_auth_logout_post(csrf)

Logout

Terminate both the local session AND the upstream WorkOS session.

Without the WorkOS-side termination, the next `/auth/login` flow
silently re-authenticates the user through AuthKit's still-valid
session cookie on `api.workos.com` — "Sign out" feels broken and
a shared-browser user can't switch accounts. The recommended
pattern (per https://workos.com/docs/authkit/sessions) is to
redirect to the WorkOS logout endpoint with the `sid` we stashed
during the callback; WorkOS clears its own session and returns
the browser to our `return_to`.

Failure modes handled:
  * No `workos_session_id` in the session (legacy v2 cookie issued
    before this slice landed): fall back to local-only logout. The
    upstream session lingers but the user's local state is cleared
    — same UX as before this slice; cookie rotation on next sign-in
    eventually overwrites it.
  * SDK raises during `get_logout_url`: pure string formatting at
    WorkOS's end, so the only realistic failure is a misconfigured
    WorkOS dashboard (no Sign-out redirect registered). We catch
    and fall back to local-only logout rather than 500ing — the
    user clicked "Sign out", they should land somewhere, not on an
    error page.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    csrf = 'csrf_example' # str |

    try:
        # Logout
        api_instance.logout_auth_logout_post(csrf)
    except Exception as e:
        print("Exception when calling DefaultApi->logout_auth_logout_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the canonical or authentication URL. |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The browser CSRF check failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_usage_v0_drives_me_usage_get**
> DriveUsageOut me_usage_v0_drives_me_usage_get()

Current-period usage + caps for the authenticated drive

Unified view of every metered dimension: storage (snapshot), writes (current hour), indexing ops + retrieval queries (current calendar month UTC). Each row carries `used` and `limit`; `limit: 0` means unlimited (the v0 free-tier default for the two monthly counters). Reads are de-throttled — there is no hourly read budget; the monthly read count appears under `ops_this_month.reads`.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.drive_usage_out import DriveUsageOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)

    try:
        # Current-period usage + caps for the authenticated drive
        api_response = api_instance.me_usage_v0_drives_me_usage_get()
        print("The response of DefaultApi->me_usage_v0_drives_me_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->me_usage_v0_drives_me_usage_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DriveUsageOut**](DriveUsageOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_v0_drives_me_get**
> DriveReadOut me_v0_drives_me_get()

Me

Drive overview for the authenticated bearer token.

Wire-protocol preservation (WorkOS integration §6): the `email` field
is preserved in the response shape; its meaning is now "the drive's
owner's email" (via `drives.owner_user_id` → `users.email`, joined
in `auth.resolve_drive`). For solo signups this equals v0 behavior —
the email the user signed up with. Returns null if the owner has
been hard-purged. `organization_id` is a new additive field, as are
`metageneration` / `etag` (also emitted as the `ETag` header).

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.drive_read_out import DriveReadOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)

    try:
        # Me
        api_response = api_instance.me_v0_drives_me_get()
        print("The response of DefaultApi->me_v0_drives_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->me_v0_drives_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DriveReadOut**](DriveReadOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_artifact_route_v0_artifacts_art_id_move_post**
> ArtifactOut move_artifact_route_v0_artifacts_art_id_move_post(art_id, artifact_move_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Rename / move an artifact to a new path

Canonical artifact move/rename, keyed by the stable `art_…` ID (the artifact analogue of `POST /v0/folders/{fld_id}/move`). Moves the artifact to a new `path` on the same drive; ID, version history, source refs, labels, metadata, and the underlying CAS blob are all preserved — only `path` and `updated_at` change, and the move does NOT bump `version_number`.

The row UPDATE and the emitted `artifact.renamed` event commit in a SINGLE transaction — a failure leaves the artifact fully unchanged.

Returns 409 PATH_CONFLICT if the target `path` is already taken; 404 ARTIFACT_NOT_FOUND for an unknown id; 403 WIKI_RESERVED for a `_wiki/` / `_compiled/` target. Honors `If-Match` (→ 412 PRECONDITION_FAILED). Use `X-AgentDrive-Actor` to attach attribution to the emitted `artifact.renamed` event.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_move_in import ArtifactMoveIn
from agentdrive_sdk.models.artifact_out import ArtifactOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |
    artifact_move_in = agentdrive_sdk.ArtifactMoveIn() # ArtifactMoveIn |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Rename / move an artifact to a new path
        api_response = api_instance.move_artifact_route_v0_artifacts_art_id_move_post(art_id, artifact_move_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->move_artifact_route_v0_artifacts_art_id_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->move_artifact_route_v0_artifacts_art_id_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |
 **artifact_move_in** | [**ArtifactMoveIn**](ArtifactMoveIn.md)|  |
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No such artifact exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The destination path is already occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder_by_id_v0_folders_fld_id_move_post**
> FolderOut move_folder_by_id_v0_folders_fld_id_move_post(fld_id, folder_move_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Rename / move a folder by stable ID (cascade descendants)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_move_in import FolderMoveIn
from agentdrive_sdk.models.folder_out import FolderOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str |
    folder_move_in = agentdrive_sdk.FolderMoveIn() # FolderMoveIn |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Rename / move a folder by stable ID (cascade descendants)
        api_response = api_instance.move_folder_by_id_v0_folders_fld_id_move_post(fld_id, folder_move_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->move_folder_by_id_v0_folders_fld_id_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->move_folder_by_id_v0_folders_fld_id_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  |
 **folder_move_in** | [**FolderMoveIn**](FolderMoveIn.md)|  |
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The destination path is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The destination path is already occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder_by_path_v0_folders_path_move_post**
> FolderOut move_folder_by_path_v0_folders_path_move_post(path, folder_move_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Rename / move a folder (cascade-update descendants)

Move the folder identified by URL path to the body's `path`. All descendant folders + artifacts are path-prefix-updated in the same transaction. The folder's `fld_*` ID stays stable.

Returns 409 `FOLDER_PATH_CONFLICT` if the destination prefix collides with a live folder or artifact path.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_move_in import FolderMoveIn
from agentdrive_sdk.models.folder_out import FolderOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str |
    folder_move_in = agentdrive_sdk.FolderMoveIn() # FolderMoveIn |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Rename / move a folder (cascade-update descendants)
        api_response = api_instance.move_folder_by_path_v0_folders_path_move_post(path, folder_move_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->move_folder_by_path_v0_folders_path_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->move_folder_by_path_v0_folders_path_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |
 **folder_move_in** | [**FolderMoveIn**](FolderMoveIn.md)|  |
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The source or destination path is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The source folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The destination path is already occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_artifact_route_v0_artifacts_art_id_patch**
> ArtifactOut patch_artifact_route_v0_artifacts_art_id_patch(art_id, artifact_patch_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Edit artifact metadata (labels / metadata / source)

Metadata-only JSON-merge-patch update of a single artifact, keyed by its stable `art_…` ID. Every field in the body is optional; a field that is **omitted** is left unchanged, a field that is **present** is applied — with an explicit `null` / `[]` / `{}` meaning "clear". This mirrors the MCP `set_metadata` tool.

Editable fields:
  * `labels` — replace the label set (`[]`/`null` clears).
  * `metadata` — replace the free-form metadata object (`{}`/`null` clears).
  * `source` — replace provenance refs (`null` clears).

**To move/rename an artifact, use `POST /v0/artifacts/{art_id}/move`** — PATCH no longer accepts `path`. The body is `extra="forbid"`, so a stray field (notably a legacy `path`) is rejected with 422 rather than silently ignored.

Metadata edits do NOT create a new content version (no `version_number` / generation bump, no `artifact_versions` row) but DO bump the artifact's `metageneration` and `updated_at`.

Returns 400 BAD_LABELS / BAD_SOURCE for invalid metadata; 404 ARTIFACT_NOT_FOUND for an unknown id. Honors `If-Match`, which takes the composite ETag `"<art_id>.<generation>.<metageneration>"` and is compared as a whole tuple: ANY concurrent content **or** metadata change (a bumped generation OR metageneration) → 412 PRECONDITION_FAILED. There is no last-writer-wins gap for metadata-only edits. Use `X-AgentDrive-Actor` to attach attribution to the emitted `artifact.metadata_updated` event.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
from agentdrive_sdk.models.artifact_patch_in import ArtifactPatchIn
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |
    artifact_patch_in = agentdrive_sdk.ArtifactPatchIn() # ArtifactPatchIn |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Edit artifact metadata (labels / metadata / source)
        api_response = api_instance.patch_artifact_route_v0_artifacts_art_id_patch(art_id, artifact_patch_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->patch_artifact_route_v0_artifacts_art_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patch_artifact_route_v0_artifacts_art_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |
 **artifact_patch_in** | [**ArtifactPatchIn**](ArtifactPatchIn.md)|  |
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The labels or source metadata are invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No such live artifact exists in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_folder_by_id_v0_folders_fld_id_patch**
> FolderOut patch_folder_by_id_v0_folders_fld_id_patch(fld_id, folder_patch_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Update folder metadata by stable ID

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_out import FolderOut
from agentdrive_sdk.models.folder_patch_in import FolderPatchIn
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str |
    folder_patch_in = agentdrive_sdk.FolderPatchIn() # FolderPatchIn |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Update folder metadata by stable ID
        api_response = api_instance.patch_folder_by_id_v0_folders_fld_id_patch(fld_id, folder_patch_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->patch_folder_by_id_v0_folders_fld_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patch_folder_by_id_v0_folders_fld_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  |
 **folder_patch_in** | [**FolderPatchIn**](FolderPatchIn.md)|  |
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The folder update is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_folder_by_path_v0_folders_path_patch**
> FolderOut patch_folder_by_path_v0_folders_path_patch(path, folder_patch_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Update folder metadata by path

Partial update — field absence leaves the value unchanged; explicit `null` clears the field. Use the by-id endpoint (slice 2) when you need stable addressing across renames.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_out import FolderOut
from agentdrive_sdk.models.folder_patch_in import FolderPatchIn
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str |
    folder_patch_in = agentdrive_sdk.FolderPatchIn() # FolderPatchIn |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Update folder metadata by path
        api_response = api_instance.patch_folder_by_path_v0_folders_path_patch(path, folder_patch_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->patch_folder_by_path_v0_folders_path_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patch_folder_by_path_v0_folders_path_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |
 **folder_patch_in** | [**FolderPatchIn**](FolderPatchIn.md)|  |
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The folder update is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_grant_route_v0_grants_grn_id_patch**
> GrantOut patch_grant_route_v0_grants_grn_id_patch(grn_id, grant_patch_in, x_agentdrive_actor=x_agentdrive_actor)

Update a grant's role and/or expiry (requires can_manage)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.grant_out import GrantOut
from agentdrive_sdk.models.grant_patch_in import GrantPatchIn
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    grn_id = 'grn_id_example' # str |
    grant_patch_in = agentdrive_sdk.GrantPatchIn() # GrantPatchIn |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)

    try:
        # Update a grant's role and/or expiry (requires can_manage)
        api_response = api_instance.patch_grant_route_v0_grants_grn_id_patch(grn_id, grant_patch_in, x_agentdrive_actor=x_agentdrive_actor)
        print("The response of DefaultApi->patch_grant_route_v0_grants_grn_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patch_grant_route_v0_grants_grn_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grn_id** | **str**|  |
 **grant_patch_in** | [**GrantPatchIn**](GrantPatchIn.md)|  |
 **x_agentdrive_actor** | **str**|  | [optional]

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The grant update or expiry is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The grant does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_describe_v0_query_describe_post**
> DatasetDescriptionOut post_describe_v0_query_describe_post(describe_in)

Describe a dataset's column schema

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.dataset_description_out import DatasetDescriptionOut
from agentdrive_sdk.models.describe_in import DescribeIn
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    describe_in = agentdrive_sdk.DescribeIn() # DescribeIn |

    try:
        # Describe a dataset's column schema
        api_response = api_instance.post_describe_v0_query_describe_post(describe_in)
        print("The response of DefaultApi->post_describe_v0_query_describe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_describe_v0_query_describe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_in** | [**DescribeIn**](DescribeIn.md)|  |

### Return type

[**DatasetDescriptionOut**](DatasetDescriptionOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The referenced dataset is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**503** | The configured query engine is unavailable. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feedback_v0_feedback_post**
> FeedbackCreateOut post_feedback_v0_feedback_post()

Post Feedback

File feedback. Body: `{kind, title, body, contact?,
attachments?: [art_id, ...]}` — attachments are snapshotted from
this drive's artifacts at submit time.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.feedback_create_out import FeedbackCreateOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)

    try:
        # Post Feedback
        api_response = api_instance.post_feedback_v0_feedback_post()
        print("The response of DefaultApi->post_feedback_v0_feedback_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_feedback_v0_feedback_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FeedbackCreateOut**](FeedbackCreateOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The feedback body or attachment list is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | An attached artifact does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lookup_values_v0_query_lookup_values_post**
> LookupValuesOut post_lookup_values_v0_query_lookup_values_post(lookup_values_in)

List distinct values of a dataset column

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.lookup_values_in import LookupValuesIn
from agentdrive_sdk.models.lookup_values_out import LookupValuesOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    lookup_values_in = agentdrive_sdk.LookupValuesIn() # LookupValuesIn |

    try:
        # List distinct values of a dataset column
        api_response = api_instance.post_lookup_values_v0_query_lookup_values_post(lookup_values_in)
        print("The response of DefaultApi->post_lookup_values_v0_query_lookup_values_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_lookup_values_v0_query_lookup_values_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookup_values_in** | [**LookupValuesIn**](LookupValuesIn.md)|  |

### Return type

[**LookupValuesOut**](LookupValuesOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The dataset, column, or limit is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**402** | The current plan does not permit this query. |  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**503** | The configured query engine is unavailable. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_query_v0_query_post**
> ResponsePostQueryV0QueryPost post_query_v0_query_post(query_in)

Run a read-only SQL query over authorized datasets

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.query_in import QueryIn
from agentdrive_sdk.models.response_post_query_v0_query_post import ResponsePostQueryV0QueryPost
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    query_in = agentdrive_sdk.QueryIn() # QueryIn |

    try:
        # Run a read-only SQL query over authorized datasets
        api_response = api_instance.post_query_v0_query_post(query_in)
        print("The response of DefaultApi->post_query_v0_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_query_v0_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_in** | [**QueryIn**](QueryIn.md)|  |

### Return type

[**ResponsePostQueryV0QueryPost**](ResponsePostQueryV0QueryPost.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The SQL or referenced dataset is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**402** | The current plan does not permit this query. |  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**503** | The configured query engine is unavailable. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_artifact_v0_artifacts_path_put**
> ArtifactOut put_artifact_v0_artifacts_path_put(path, content_type=content_type, x_agentdrive_labels=x_agentdrive_labels, x_agentdrive_metadata=x_agentdrive_metadata, x_agentdrive_source=x_agentdrive_source, x_agentdrive_actor=x_agentdrive_actor, x_agentdrive_change_summary=x_agentdrive_change_summary, x_agentdrive_checksum=x_agentdrive_checksum, content_md5=content_md5, if_match=if_match, if_none_match=if_none_match)

Upload (or overwrite) an artifact

Upload an artifact at the given path. The path is treated as the artifact's location in the drive — re-uploading the same path overwrites in place (idempotent). Returns 201 when the artifact is created (no prior live artifact at the path), 200 on overwrite — mirroring `PUT /v0/folders/{path}`.

**Limits:** request body must not exceed **50 MB**. Path must be non-empty, ≤256 chars, only `[A-Za-z0-9_./-]`, no `..` segments, no leading/trailing slash. Per-token write rate limit: 100/hour.

**Optional headers.** Each preserves the existing artifact's value when omitted on an overwrite, and takes the create-default on a new path; send the header to replace it:
- `X-AgentDrive-Labels`: comma-separated labels (e.g. `draft,report`); an empty value clears them. Each: lowercase `[a-z0-9_-]+`, ≤64 chars; ≤16 labels per artifact.
- `X-AgentDrive-Metadata`: JSON object of agent-attached fields.
- `X-AgentDrive-Source`: JSON `{"refs": [...]}` source provenance (present, including `{"refs": []}`, replaces).
- `X-AgentDrive-Actor`: caller-supplied actor name (≤64 chars) for event-log attribution. Untrusted; never used for authz.

**Preconditions.** `If-Match: "<id>.<gen>.<metagen>"` makes the write conditional on the current composite ETag (→ 412 PRECONDITION_FAILED). `If-None-Match: *` is create-only: it succeeds only if no live artifact occupies the path (→ 412 CREATE_CONFLICT if one does). The two are mutually exclusive (→ 400 BAD_PRECONDITION).

**Integrity (optional).** `X-AgentDrive-Checksum: <algo>:<value>` (`sha256:<hex>` or `crc32c:<base64>`) or the standard `Content-MD5` (base64 MD5) is verified against the received bytes before they land (→ 400 CHECKSUM_MISMATCH on mismatch); no artifact is created on failure.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str |
    content_type = 'application/octet-stream' # str |  (optional) (default to 'application/octet-stream')
    x_agentdrive_labels = 'x_agentdrive_labels_example' # str |  (optional)
    x_agentdrive_metadata = 'x_agentdrive_metadata_example' # str |  (optional)
    x_agentdrive_source = 'x_agentdrive_source_example' # str |  (optional)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    x_agentdrive_change_summary = 'x_agentdrive_change_summary_example' # str |  (optional)
    x_agentdrive_checksum = 'x_agentdrive_checksum_example' # str |  (optional)
    content_md5 = 'content_md5_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    if_none_match = 'if_none_match_example' # str |  (optional)

    try:
        # Upload (or overwrite) an artifact
        api_response = api_instance.put_artifact_v0_artifacts_path_put(path, content_type=content_type, x_agentdrive_labels=x_agentdrive_labels, x_agentdrive_metadata=x_agentdrive_metadata, x_agentdrive_source=x_agentdrive_source, x_agentdrive_actor=x_agentdrive_actor, x_agentdrive_change_summary=x_agentdrive_change_summary, x_agentdrive_checksum=x_agentdrive_checksum, content_md5=content_md5, if_match=if_match, if_none_match=if_none_match)
        print("The response of DefaultApi->put_artifact_v0_artifacts_path_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->put_artifact_v0_artifacts_path_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  |
 **content_type** | **str**|  | [optional] [default to &#39;application/octet-stream&#39;]
 **x_agentdrive_labels** | **str**|  | [optional]
 **x_agentdrive_metadata** | **str**|  | [optional]
 **x_agentdrive_source** | **str**|  | [optional]
 **x_agentdrive_actor** | **str**|  | [optional]
 **x_agentdrive_change_summary** | **str**|  | [optional]
 **x_agentdrive_checksum** | **str**|  | [optional]
 **content_md5** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]
 **if_none_match** | **str**|  | [optional]

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**201** | Artifact created at a previously unused path. |  * ETag - Current strong entity tag. <br>  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The path, metadata, source, or conditional headers are invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The path is occupied and overwrite semantics do not permit replacement. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**413** | The artifact or resulting drive storage exceeds its limit. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_v0_projects_fld_id_put**
> CompileProjectOut put_project_v0_projects_fld_id_put(fld_id, project_config_in)

Set a project's compile config (entrypoint/engine/auto_compile)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.compile_project_out import CompileProjectOut
from agentdrive_sdk.models.project_config_in import ProjectConfigIn
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str |
    project_config_in = agentdrive_sdk.ProjectConfigIn() # ProjectConfigIn |

    try:
        # Set a project's compile config (entrypoint/engine/auto_compile)
        api_response = api_instance.put_project_v0_projects_fld_id_put(fld_id, project_config_in)
        print("The response of DefaultApi->put_project_v0_projects_fld_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->put_project_v0_projects_fld_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  |
 **project_config_in** | [**ProjectConfigIn**](ProjectConfigIn.md)|  |

### Return type

[**CompileProjectOut**](CompileProjectOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The compile engine or entrypoint is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The project folder does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_share_s_share_key_get**
> ShareRedeemOut redeem_share_s_share_key_get(share_key)

Redeem Share

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.share_redeem_out import ShareRedeemOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    share_key = 'share_key_example' # str |

    try:
        # Redeem Share
        api_response = api_instance.redeem_share_s_share_key_get(share_key)
        print("The response of DefaultApi->redeem_share_s_share_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->redeem_share_s_share_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_key** | **str**|  |

### Return type

[**ShareRedeemOut**](ShareRedeemOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON capability response or browser password form. |  * X-Request-Id - Request correlation identifier. <br>  |
**302** | Browser redemption succeeded; continue to the canonical URL. |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | A password is required or the supplied password is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The share is invalid, expired, or no longer authorized. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_share_with_password_s_share_key_post**
> ShareRedeemOut redeem_share_with_password_s_share_key_post(share_key, password=password)

Redeem Share With Password

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.share_redeem_out import ShareRedeemOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    share_key = 'share_key_example' # str |
    password = '' # str |  (optional) (default to '')

    try:
        # Redeem Share With Password
        api_response = api_instance.redeem_share_with_password_s_share_key_post(share_key, password=password)
        print("The response of DefaultApi->redeem_share_with_password_s_share_key_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->redeem_share_with_password_s_share_key_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_key** | **str**|  |
 **password** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**ShareRedeemOut**](ShareRedeemOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON capability response or browser password form. |  * X-Request-Id - Request correlation identifier. <br>  |
**302** | Browser redemption succeeded; continue to the canonical URL. |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | A password is required or the supplied password is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The share is invalid, expired, or no longer authorized. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_artifact_v0_artifacts_art_id_restore_post**
> ArtifactOut restore_artifact_v0_artifacts_art_id_restore_post(art_id, rename=rename, overwrite=overwrite, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Restore a soft-deleted artifact

Clear `deleted_at` + `purge_at` on a soft-deleted artifact. Available only while the artifact is in trash (i.e. before the GC cleanup cron purges it). Returns 404 if the artifact is live or already hard-deleted; 409 PATH_CONFLICT if its path is now occupied by another live artifact. The 409 payload includes a `restore_options` block with `rename_to` and `force_overwrite` URLs the caller can follow to resolve the conflict — see deletion-design.md §5.4.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |
    rename = 'rename_example' # str | Restore at this path instead of the original. Soft-deletes the live occupant at the original path with audit `metadata.cause='restore_conflict_rename'`. Mutually exclusive with `overwrite`. (optional)
    overwrite = False # bool | Soft-delete the live occupant at the original path and restore there. Audit `metadata.cause='restore_conflict_overwrite'`. Mutually exclusive with `rename`. (optional) (default to False)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Restore a soft-deleted artifact
        api_response = api_instance.restore_artifact_v0_artifacts_art_id_restore_post(art_id, rename=rename, overwrite=overwrite, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->restore_artifact_v0_artifacts_art_id_restore_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->restore_artifact_v0_artifacts_art_id_restore_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |
 **rename** | **str**| Restore at this path instead of the original. Soft-deletes the live occupant at the original path with audit &#x60;metadata.cause&#x3D;&#39;restore_conflict_rename&#39;&#x60;. Mutually exclusive with &#x60;overwrite&#x60;. | [optional]
 **overwrite** | **bool**| Soft-delete the live occupant at the original path and restore there. Audit &#x60;metadata.cause&#x3D;&#39;restore_conflict_overwrite&#39;&#x60;. Mutually exclusive with &#x60;rename&#x60;. | [optional] [default to False]
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No restorable artifact exists with this ID. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The original or requested restore path is occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_artifact_version_v0_artifacts_art_id_versions_version_number_restore_post**
> ArtifactOut restore_artifact_version_v0_artifacts_art_id_versions_version_number_restore_post(art_id, version_number, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Restore a previous version as a new head version

Roll the artifact forward to the content of version `version_number` by creating a **new head version** with identical bytes. History is preserved — this never rewrites or deletes past versions. The prior version's content-addressed blob is reused, so no bytes are re-uploaded. A change summary of `Restored version N` is recorded on the new version; `X-AgentDrive-Actor` attributes it.

Restoring a version whose content already matches the current head (including the head itself) is a **no-op**: it returns the current artifact unchanged, with no new version created.

Honors `If-Match` on the current head (roll forward only if the head is unchanged → 412 PRECONDITION_FAILED).

Errors: `404 ARTIFACT_NOT_FOUND`, `404 VERSION_NOT_FOUND`, and `410 VERSION_PRUNED` when the version existed but its bytes were retained out of existence.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_out import ArtifactOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |
    version_number = 56 # int |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Restore a previous version as a new head version
        api_response = api_instance.restore_artifact_version_v0_artifacts_art_id_versions_version_number_restore_post(art_id, version_number, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->restore_artifact_version_v0_artifacts_art_id_versions_version_number_restore_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->restore_artifact_version_v0_artifacts_art_id_versions_version_number_restore_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |
 **version_number** | **int**|  |
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The artifact or version does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**410** | The requested version was pruned by retention. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_drive_route_v0_drives_drive_id_restore_post**
> DriveRestoreOut restore_drive_route_v0_drives_drive_id_restore_post(drive_id, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Restore a soft-deleted drive

Clear `deleted_at` + `purge_at` on a soft-deleted drive. Soft-deleted child artifacts get their retention window rebased to the drive-restore moment (see deletion-design.md §5.2). Available only while the drive is in trash. Returns 404 if the drive is live or already hard-deleted.

**Optimistic concurrency:** send `If-Match` with the trashed drive's composite ETag (`"<drv_id>.0.<metageneration>"`, e.g. from the delete response's `ETag` header) to make the restore conditional — a stale token returns 412 PRECONDITION_FAILED. A restore WITHOUT an `If-Match` precondition is last-writer-wins.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.drive_restore_out import DriveRestoreOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    drive_id = 'drive_id_example' # str |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Restore a soft-deleted drive
        api_response = api_instance.restore_drive_route_v0_drives_drive_id_restore_post(drive_id, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->restore_drive_route_v0_drives_drive_id_restore_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->restore_drive_route_v0_drives_drive_id_restore_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**DriveRestoreOut**](DriveRestoreOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The drive does not exist or is not in trash. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The drive cannot be restored into its current workspace state. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | If-Match does not match the current drive. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_folder_by_id_v0_folders_fld_id_restore_post**
> FolderRestoreOut restore_folder_by_id_v0_folders_fld_id_restore_post(fld_id, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)

Restore a soft-deleted folder (cascade)

Mirrors `POST /v0/artifacts/{art_id}/restore` for folders: clear `deleted_at` + `purge_at` on a soft-deleted folder AND exactly the descendants soft-deleted in the same cascade (descendants trashed separately keep their trash state; restore those individually — the per-artifact restore remains for cherry-picking). Available only while the folder is in trash; returns 404 if it is live or already hard-purged.

Returns 409 `PATH_CONFLICT` when a live folder/artifact now occupies a path this restore would reinstate (`colliding_path` + `kind` identify it). Unlike artifact restore there are NO `rename`/`overwrite` escape hatches — the whole cascade aborts; free the colliding path (or cherry-pick artifacts) and retry.

`If-Match` (the trashed folder's composite ETag) makes the restore conditional → 412 PRECONDITION_FAILED on a stale token; omitted, the restore is last-writer-wins.

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.folder_restore_out import FolderRestoreOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)

    try:
        # Restore a soft-deleted folder (cascade)
        api_response = api_instance.restore_folder_by_id_v0_folders_fld_id_restore_post(fld_id, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match)
        print("The response of DefaultApi->restore_folder_by_id_v0_folders_fld_id_restore_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->restore_folder_by_id_v0_folders_fld_id_restore_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  |
 **x_agentdrive_actor** | **str**|  | [optional]
 **if_match** | **str**|  | [optional]

### Return type

[**FolderRestoreOut**](FolderRestoreOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | No restorable folder exists with this ID. |  * X-Request-Id - Request correlation identifier. <br>  |
**409** | The restore destination is already occupied. |  * X-Request-Id - Request correlation identifier. <br>  |
**412** | A request precondition did not match. |  * ETag - Current strong entity tag. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_share_route_v0_shares_shr_id_rotate_post**
> ShareMintOut rotate_share_route_v0_shares_shr_id_rotate_post(shr_id, x_agentdrive_actor=x_agentdrive_actor)

Revoke + reissue a share link's key (requires can_share)

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.share_mint_out import ShareMintOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    shr_id = 'shr_id_example' # str |
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)

    try:
        # Revoke + reissue a share link's key (requires can_share)
        api_response = api_instance.rotate_share_route_v0_shares_shr_id_rotate_post(shr_id, x_agentdrive_actor=x_agentdrive_actor)
        print("The response of DefaultApi->rotate_share_route_v0_shares_shr_id_rotate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rotate_share_route_v0_shares_shr_id_rotate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shr_id** | **str**|  |
 **x_agentdrive_actor** | **str**|  | [optional]

### Return type

[**ShareMintOut**](ShareMintOut.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The replacement password is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The share does not exist in this drive. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_v0_search_get**
> SearchPage search_v0_search_get(q, label=label, file_type=file_type, prefix=prefix, updated_after=updated_after, updated_before=updated_before, limit=limit)

Full-text search over artifacts in the drive

Lexical (not semantic) full-text search powered by Postgres `websearch_to_tsquery`. Results are ranked by `ts_rank` over a weighted tsvector (path > content > metadata > labels).

**Supported query syntax:**
- Words: `kangaroo` (English stemming)
- Phrases: `"exact phrase"`
- Negation: `kangaroo -secret`
- AND (implicit): `kangaroo secret`
- OR: `kangaroo OR koala`
- Paths & filenames: `reports/q3-summary.md` or `q3-summary.md` match by their path words (`/ . _ -` are word boundaries)

**Not supported (v0):**
- Semantic / embedding similarity
- PDF and image content (only the path + metadata are searchable)
- Non-English stemming
- Fuzzy matching, regex
- Boolean operator parentheses

**Filters:** `label` (repeatable, AND), `file_type` (enum), `prefix` (path prefix), `updated_after` / `updated_before` (RFC 3339 timestamps, inclusive bounds on `updated_at`).

### Example

* Bearer (ad_live_ | ad_user_ | JWT) Authentication (BearerAuth):

```python
import agentdrive_sdk
from agentdrive_sdk.models.search_page import SearchPage
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ad_live_ | ad_user_ | JWT): BearerAuth
configuration = agentdrive_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    q = 'q_example' # str |
    label = ['label_example'] # List[str] |  (optional)
    file_type = 'file_type_example' # str |  (optional)
    prefix = 'prefix_example' # str |  (optional)
    updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # Full-text search over artifacts in the drive
        api_response = api_instance.search_v0_search_get(q, label=label, file_type=file_type, prefix=prefix, updated_after=updated_after, updated_before=updated_before, limit=limit)
        print("The response of DefaultApi->search_v0_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_v0_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  |
 **label** | [**List[str]**](str.md)|  | [optional]
 **file_type** | **str**|  | [optional]
 **prefix** | **str**|  | [optional]
 **updated_after** | **datetime**|  | [optional]
 **updated_before** | **datetime**|  | [optional]
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**SearchPage**](SearchPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**400** | The search query or filter is invalid. |  * X-Request-Id - Request correlation identifier. <br>  |
**401** | Bearer credential is missing or invalid. |  * WWW-Authenticate - RFC 6750 bearer authentication challenge. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**403** | The authenticated principal is not allowed to perform this operation. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |
**429** | A request, operation, or quota rate limit was exceeded. |  * Retry-After - Seconds until the caller should retry. <br>  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_artifact_head_a_art_id_head_get**
> ArtifactHeadOut view_artifact_head_a_art_id_head_get(art_id)

View Artifact Head

Return `{"version": <head version_number>}` for a readable artifact.

Auth mirrors the permalink/viewer: the owner, or an `anyone:viewer`
grant (a published artifact), reads. Two deliberate differences from
the HTML viewer:

  * Never redirect to login. A poll is a background `fetch`, not a
    navigation — an HTML login page would be a useless body and a
    same-origin redirect the client can't act on. Anonymous callers
    on a private/absent artifact get a flat 404.
  * "Doesn't exist" and "exists but not readable" collapse to the
    same 404, so an anonymous poller can't use this as an existence
    oracle (matches the permalink/viewer leak guard).

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.artifact_head_out import ArtifactHeadOut
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |

    try:
        # View Artifact Head
        api_response = api_instance.view_artifact_head_a_art_id_head_get(art_id)
        print("The response of DefaultApi->view_artifact_head_a_art_id_head_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->view_artifact_head_a_art_id_head_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |

### Return type

[**ArtifactHeadOut**](ArtifactHeadOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_artifact_version_v_art_id_version_get**
> bytes view_artifact_version_v_art_id_version_get(art_id, version, raw=raw, download=download)

View Artifact Version

Render version `version` of an artifact, read-only.

Version history is owner-only. The drive-blind `can_read` gate still
provides the same sign-in-or-404 masking as `/a/{art_id}`, but readable
non-owners cannot browse snapshots. A pruned or never-existed version
renders a friendly unavailable state, never a 500.
`?raw=1` / `?download=1` stream the version's bytes (powering the bar's
Raw / Download buttons) with the same sandbox+nosniff headers as the
head raw path.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |
    version = 56 # int |
    raw = 0 # int |  (optional) (default to 0)
    download = 0 # int |  (optional) (default to 0)

    try:
        # View Artifact Version
        api_response = api_instance.view_artifact_version_v_art_id_version_get(art_id, version, raw=raw, download=download)
        print("The response of DefaultApi->view_artifact_version_v_art_id_version_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->view_artifact_version_v_art_id_version_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |
 **version** | **int**|  |
 **raw** | **int**|  | [optional] [default to 0]
 **download** | **int**|  | [optional] [default to 0]

### Return type

**bytes**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rendered HTML or raw artifact bytes. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_file_drive_id_path_get**
> bytes view_file_drive_id_path_get(drive_id, path, raw=raw, download=download)

View File

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    drive_id = 'drive_id_example' # str |
    path = 'path_example' # str |
    raw = 0 # int |  (optional) (default to 0)
    download = 0 # int |  (optional) (default to 0)

    try:
        # View File
        api_response = api_instance.view_file_drive_id_path_get(drive_id, path, raw=raw, download=download)
        print("The response of DefaultApi->view_file_drive_id_path_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->view_file_drive_id_path_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  |
 **path** | **str**|  |
 **raw** | **int**|  | [optional] [default to 0]
 **download** | **int**|  | [optional] [default to 0]

### Return type

**bytes**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/html, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rendered HTML or raw artifact bytes. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_permalink_artifact_a_art_id_get**
> view_permalink_artifact_a_art_id_get(art_id)

View Permalink Artifact

Resolve a stable artifact ID to its path-URL and 302 there.

Auth model matches the path URL: public artifacts redirect for
anyone; private artifacts redirect only for the owner. Non-owners
on private artifacts get 404 — same response as "doesn't exist",
so the ID's existence isn't leaked. The forwarded query-param
allowlist is `raw`, `download` (see _PERMALINK_FORWARDED_PARAMS).

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str |

    try:
        # View Permalink Artifact
        api_instance.view_permalink_artifact_a_art_id_get(art_id)
    except Exception as e:
        print("Exception when calling DefaultApi->view_permalink_artifact_a_art_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the canonical or authentication URL. |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The artifact does not exist or is not readable. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_permalink_folder_f_fld_id_get**
> view_permalink_folder_f_fld_id_get(fld_id)

View Permalink Folder

Resolve a stable folder ID to its current path-URL and 302.

Auth model mirrors the artifact permalink: public folder = anon
OK; private folder = owner only, otherwise 404 (no existence
leak). "Public" is an `anyone:viewer` grant on the `fld_*` id
resolved through `can_read` (§4.4); folders carry no visibility
flag of their own.

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agentdrive.run
# See configuration.py for a list of all supported configuration parameters.
configuration = agentdrive_sdk.Configuration(
    host = "https://api.agentdrive.run"
)


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str |

    try:
        # View Permalink Folder
        api_instance.view_permalink_folder_f_fld_id_get(fld_id)
    except Exception as e:
        print("Exception when calling DefaultApi->view_permalink_folder_f_fld_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the canonical or authentication URL. |  * Location - Canonical URL of the created resource. <br>  * X-Request-Id - Request correlation identifier. <br>  |
**404** | The folder does not exist or is not readable. |  * X-Request-Id - Request correlation identifier. <br>  |
**422** | Request validation failed. |  * X-Request-Id - Request correlation identifier. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
