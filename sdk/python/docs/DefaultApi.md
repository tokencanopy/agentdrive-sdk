# agentdrive_sdk.DefaultApi

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_upload_v0_uploads_upload_id_delete**](DefaultApi.md#abort_upload_v0_uploads_upload_id_delete) | **DELETE** /v0/uploads/{upload_id} | Abort a large (direct-to-GCS) upload session
[**accept_invitation_invitations_token_get**](DefaultApi.md#accept_invitation_invitations_token_get) | **GET** /invitations/{token} | Accept Invitation
[**activity_feed_activity_get**](DefaultApi.md#activity_feed_activity_get) | **GET** /activity | Activity Feed
[**add_grant_web_share_rid_grant_post**](DefaultApi.md#add_grant_web_share_rid_grant_post) | **POST** /web/share/{rid}/grant | Add Grant
[**artifact_detail_preview_preview_artifact_detail_get**](DefaultApi.md#artifact_detail_preview_preview_artifact_detail_get) | **GET** /preview/artifact-detail | Artifact Detail Preview
[**begin_upload_v0_uploads_post**](DefaultApi.md#begin_upload_v0_uploads_post) | **POST** /v0/uploads | Begin a large (direct-to-GCS) upload
[**callback_auth_callback_get**](DefaultApi.md#callback_auth_callback_get) | **GET** /auth/callback | Callback
[**cancel_job_v0_jobs_job_id_cancel_post**](DefaultApi.md#cancel_job_v0_jobs_job_id_cancel_post) | **POST** /v0/jobs/{job_id}/cancel | Cancel a queued/running job
[**collection_detail_collections_slug_get**](DefaultApi.md#collection_detail_collections_slug_get) | **GET** /collections/{slug} | Collection Detail
[**commit_upload_v0_uploads_upload_id_commit_post**](DefaultApi.md#commit_upload_v0_uploads_upload_id_commit_post) | **POST** /v0/uploads/{upload_id}/commit | Commit a large (direct-to-GCS) upload
[**connectors_page_connectors_get**](DefaultApi.md#connectors_page_connectors_get) | **GET** /connectors | Connectors Page
[**copy_artifact_route_v0_artifacts_art_id_copy_post**](DefaultApi.md#copy_artifact_route_v0_artifacts_art_id_copy_post) | **POST** /v0/artifacts/{art_id}/copy | Duplicate an artifact to a new path (CAS-shared, new ID)
[**copy_folder_by_id_v0_folders_fld_id_copy_post**](DefaultApi.md#copy_folder_by_id_v0_folders_fld_id_copy_post) | **POST** /v0/folders/{fld_id}/copy | Duplicate a folder subtree to a new path (CAS-shared, new IDs)
[**create_drive_key_web_web_drives_drive_id_keys_create_post**](DefaultApi.md#create_drive_key_web_web_drives_drive_id_keys_create_post) | **POST** /web/drives/{drive_id}/keys/create | Create Drive Key Web
[**create_drive_web_web_drives_post**](DefaultApi.md#create_drive_web_web_drives_post) | **POST** /web/drives | Create Drive Web
[**create_folder_by_path_v0_folders_path_put**](DefaultApi.md#create_folder_by_path_v0_folders_path_put) | **PUT** /v0/folders/{path} | Create a folder (idempotent)
[**create_grant_route_v0_grants_post**](DefaultApi.md#create_grant_route_v0_grants_post) | **POST** /v0/grants | Create (or fetch) a per-principal grant on a resource
[**create_key_web_keys_create_post**](DefaultApi.md#create_key_web_keys_create_post) | **POST** /web/keys/create | Create Key
[**create_link_web_share_rid_link_post**](DefaultApi.md#create_link_web_share_rid_link_post) | **POST** /web/share/{rid}/link | Create Link
[**create_share_route_v0_shares_post**](DefaultApi.md#create_share_route_v0_shares_post) | **POST** /v0/shares | Mint a share link (returns the share_key once)
[**create_user_token_web_tokens_create_post**](DefaultApi.md#create_user_token_web_tokens_create_post) | **POST** /web/tokens/create | Create User Token
[**create_workspace_web_web_workspaces_post**](DefaultApi.md#create_workspace_web_web_workspaces_post) | **POST** /web/workspaces | Create Workspace Web
[**danger_zone_old_dashboard_danger_get**](DefaultApi.md#danger_zone_old_dashboard_danger_get) | **GET** /dashboard/danger | Danger Zone Old
[**danger_zone_settings_danger_get**](DefaultApi.md#danger_zone_settings_danger_get) | **GET** /settings/danger | Danger Zone
[**dashboard_dashboard_get**](DefaultApi.md#dashboard_dashboard_get) | **GET** /dashboard | Dashboard
[**delete_account_web_account_delete_post**](DefaultApi.md#delete_account_web_account_delete_post) | **POST** /web/account/delete | Delete Account
[**delete_artifact_by_id_route_v0_artifacts_art_id_delete**](DefaultApi.md#delete_artifact_by_id_route_v0_artifacts_art_id_delete) | **DELETE** /v0/artifacts/{art_id} | Soft-delete an artifact by its stable ID
[**delete_artifact_v0_artifacts_path_delete**](DefaultApi.md#delete_artifact_v0_artifacts_path_delete) | **DELETE** /v0/artifacts/{path} | Delete Artifact
[**delete_drive_route_v0_drives_drive_id_delete**](DefaultApi.md#delete_drive_route_v0_drives_drive_id_delete) | **DELETE** /v0/drives/{drive_id} | Soft-delete a drive
[**delete_drive_web_web_drives_drive_id_delete_post**](DefaultApi.md#delete_drive_web_web_drives_drive_id_delete_post) | **POST** /web/drives/{drive_id}/delete | Delete Drive Web
[**delete_folder_by_id_v0_folders_fld_id_delete**](DefaultApi.md#delete_folder_by_id_v0_folders_fld_id_delete) | **DELETE** /v0/folders/{fld_id} | Soft-delete a folder by stable ID (cascade with ?recursive&#x3D;true)
[**delete_folder_by_path_v0_folders_path_delete**](DefaultApi.md#delete_folder_by_path_v0_folders_path_delete) | **DELETE** /v0/folders/{path} | Soft-delete a folder (cascade with ?recursive&#x3D;true)
[**delete_grant_route_v0_grants_grn_id_delete**](DefaultApi.md#delete_grant_route_v0_grants_grn_id_delete) | **DELETE** /v0/grants/{grn_id} | Revoke a grant (can_manage, or self-revoke own grant)
[**delete_share_route_v0_shares_shr_id_delete**](DefaultApi.md#delete_share_route_v0_shares_shr_id_delete) | **DELETE** /v0/shares/{shr_id} | Revoke a share link (requires can_manage)
[**delete_workspace_web_web_workspaces_org_id_delete_post**](DefaultApi.md#delete_workspace_web_web_workspaces_org_id_delete_post) | **POST** /web/workspaces/{org_id}/delete | Delete Workspace Web
[**download_artifact_by_id_v0_artifacts_art_id_download_get**](DefaultApi.md#download_artifact_by_id_v0_artifacts_art_id_download_get) | **GET** /v0/artifacts/{art_id}/download | Stream the artifact bytes by stable ID (never rendered HTML)
[**download_artifact_by_path_v0_artifacts_path_download_get**](DefaultApi.md#download_artifact_by_path_v0_artifacts_path_download_get) | **GET** /v0/artifacts/{path}/download | Stream the artifact bytes by path (never rendered HTML)
[**download_artifact_version_v0_artifacts_art_id_versions_version_number_download_get**](DefaultApi.md#download_artifact_version_v0_artifacts_art_id_versions_version_number_download_get) | **GET** /v0/artifacts/{art_id}/versions/{version_number}/download | Stream bytes for a specific version (machine surface)
[**download_url_by_id_v0_artifacts_art_id_download_url_get**](DefaultApi.md#download_url_by_id_v0_artifacts_art_id_download_url_get) | **GET** /v0/artifacts/{art_id}/download-url | Signed direct-from-GCS download URL by stable ID
[**download_url_by_path_v0_artifacts_path_download_url_get**](DefaultApi.md#download_url_by_path_v0_artifacts_path_download_url_get) | **GET** /v0/artifacts/{path}/download-url | Signed direct-from-GCS download URL by path
[**download_url_version_v0_artifacts_art_id_versions_version_number_download_url_get**](DefaultApi.md#download_url_version_v0_artifacts_art_id_versions_version_number_download_url_get) | **GET** /v0/artifacts/{art_id}/versions/{version_number}/download-url | Signed direct-from-GCS download URL for a specific version
[**edit_artifact_a_art_id_edit_get**](DefaultApi.md#edit_artifact_a_art_id_edit_get) | **GET** /a/{art_id}/edit | Edit Artifact
[**enqueue_job_v0_projects_fld_id_jobs_post**](DefaultApi.md#enqueue_job_v0_projects_fld_id_jobs_post) | **POST** /v0/projects/{fld_id}/jobs | Enqueue a compile job for a project (folder)
[**extension_start_auth_extension_start_get**](DefaultApi.md#extension_start_auth_extension_start_get) | **GET** /auth/extension/start | Extension Start
[**feedback_form_feedback_get**](DefaultApi.md#feedback_form_feedback_get) | **GET** /feedback | Feedback Form
[**feedback_submit_feedback_post**](DefaultApi.md#feedback_submit_feedback_post) | **POST** /feedback | Feedback Submit
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
[**get_share_state_web_share_rid_get**](DefaultApi.md#get_share_state_web_share_rid_get) | **GET** /web/share/{rid} | Get Share State
[**get_upload_status_v0_uploads_upload_id_get**](DefaultApi.md#get_upload_status_v0_uploads_upload_id_get) | **GET** /v0/uploads/{upload_id} | Get the status of a large (direct-to-GCS) upload session
[**health_health_get**](DefaultApi.md#health_health_get) | **GET** /health | Health
[**invite_member_web_web_members_invite_post**](DefaultApi.md#invite_member_web_web_members_invite_post) | **POST** /web/members/invite | Invite Member Web
[**list_artifact_versions_v0_artifacts_art_id_versions_get**](DefaultApi.md#list_artifact_versions_v0_artifacts_art_id_versions_get) | **GET** /v0/artifacts/{art_id}/versions | List versions of an artifact, newest first
[**list_artifacts_v0_artifacts_get**](DefaultApi.md#list_artifacts_v0_artifacts_get) | **GET** /v0/artifacts | List artifacts in the drive
[**list_events_route_v0_events_get**](DefaultApi.md#list_events_route_v0_events_get) | **GET** /v0/events | Read the append-only event log for the authenticated drive
[**list_grants_route_v0_grants_get**](DefaultApi.md#list_grants_route_v0_grants_get) | **GET** /v0/grants | List live grants on a resource (requires can_manage)
[**list_project_jobs_v0_projects_fld_id_jobs_get**](DefaultApi.md#list_project_jobs_v0_projects_fld_id_jobs_get) | **GET** /v0/projects/{fld_id}/jobs | List a project&#39;s jobs
[**list_shares_route_v0_shares_get**](DefaultApi.md#list_shares_route_v0_shares_get) | **GET** /v0/shares | List live share links on a resource (requires can_manage)
[**list_trash_route_v0_drives_drive_id_trash_get**](DefaultApi.md#list_trash_route_v0_drives_drive_id_trash_get) | **GET** /v0/drives/{drive_id}/trash | List the authenticated drive&#39;s trash
[**login_auth_login_get**](DefaultApi.md#login_auth_login_get) | **GET** /auth/login | Login
[**logout_auth_logout_post**](DefaultApi.md#logout_auth_logout_post) | **POST** /auth/logout | Logout
[**marketing_get**](DefaultApi.md#marketing_get) | **GET** / | Marketing
[**marketplace_browse_marketplace_get**](DefaultApi.md#marketplace_browse_marketplace_get) | **GET** /marketplace | Marketplace Browse
[**marketplace_detail_marketplace_slug_get**](DefaultApi.md#marketplace_detail_marketplace_slug_get) | **GET** /marketplace/{slug} | Marketplace Detail
[**me_usage_v0_drives_me_usage_get**](DefaultApi.md#me_usage_v0_drives_me_usage_get) | **GET** /v0/drives/me/usage | Current-period usage + caps for the authenticated drive
[**me_v0_drives_me_get**](DefaultApi.md#me_v0_drives_me_get) | **GET** /v0/drives/me | Me
[**move_artifact_route_v0_artifacts_art_id_move_post**](DefaultApi.md#move_artifact_route_v0_artifacts_art_id_move_post) | **POST** /v0/artifacts/{art_id}/move | Rename / move an artifact to a new path
[**move_folder_by_id_v0_folders_fld_id_move_post**](DefaultApi.md#move_folder_by_id_v0_folders_fld_id_move_post) | **POST** /v0/folders/{fld_id}/move | Rename / move a folder by stable ID (cascade descendants)
[**move_folder_by_path_v0_folders_path_move_post**](DefaultApi.md#move_folder_by_path_v0_folders_path_move_post) | **POST** /v0/folders/{path}/move | Rename / move a folder (cascade-update descendants)
[**oauth_disconnect_web_oauth_disconnect_post**](DefaultApi.md#oauth_disconnect_web_oauth_disconnect_post) | **POST** /web/oauth/disconnect | Oauth Disconnect
[**patch_artifact_route_v0_artifacts_art_id_patch**](DefaultApi.md#patch_artifact_route_v0_artifacts_art_id_patch) | **PATCH** /v0/artifacts/{art_id} | Edit artifact metadata (labels / metadata / source)
[**patch_folder_by_id_v0_folders_fld_id_patch**](DefaultApi.md#patch_folder_by_id_v0_folders_fld_id_patch) | **PATCH** /v0/folders/{fld_id} | Update folder metadata by stable ID
[**patch_folder_by_path_v0_folders_path_patch**](DefaultApi.md#patch_folder_by_path_v0_folders_path_patch) | **PATCH** /v0/folders/{path} | Update folder metadata by path
[**patch_grant_route_v0_grants_grn_id_patch**](DefaultApi.md#patch_grant_route_v0_grants_grn_id_patch) | **PATCH** /v0/grants/{grn_id} | Update a grant&#39;s role and/or expiry (requires can_manage)
[**post_describe_v0_query_describe_post**](DefaultApi.md#post_describe_v0_query_describe_post) | **POST** /v0/query/describe | Describe a dataset&#39;s column schema
[**post_feedback_v0_feedback_post**](DefaultApi.md#post_feedback_v0_feedback_post) | **POST** /v0/feedback | Post Feedback
[**post_lookup_values_v0_query_lookup_values_post**](DefaultApi.md#post_lookup_values_v0_query_lookup_values_post) | **POST** /v0/query/lookup-values | List distinct values of a dataset column
[**post_query_v0_query_post**](DefaultApi.md#post_query_v0_query_post) | **POST** /v0/query | Run a read-only SQL query over authorized datasets
[**privacy_page_privacy_get**](DefaultApi.md#privacy_page_privacy_get) | **GET** /privacy | Privacy Page
[**project_preview_page_f_fld_id_preview_get**](DefaultApi.md#project_preview_page_f_fld_id_preview_get) | **GET** /f/{fld_id}/preview | Project Preview Page
[**publisher_profile_publishers_handle_get**](DefaultApi.md#publisher_profile_publishers_handle_get) | **GET** /publishers/{handle} | Publisher Profile
[**put_artifact_v0_artifacts_path_put**](DefaultApi.md#put_artifact_v0_artifacts_path_put) | **PUT** /v0/artifacts/{path} | Upload (or overwrite) an artifact
[**put_project_v0_projects_fld_id_put**](DefaultApi.md#put_project_v0_projects_fld_id_put) | **PUT** /v0/projects/{fld_id} | Set a project&#39;s compile config (entrypoint/engine/auto_compile)
[**recovery_new_account_auth_recovery_new_account_post**](DefaultApi.md#recovery_new_account_auth_recovery_new_account_post) | **POST** /auth/recovery/new-account | Recovery New Account
[**recovery_new_account_expired_auth_recovery_new_account_expired_get**](DefaultApi.md#recovery_new_account_expired_auth_recovery_new_account_expired_get) | **GET** /auth/recovery/new-account-expired | Recovery New Account Expired
[**recovery_page_auth_recovery_get**](DefaultApi.md#recovery_page_auth_recovery_get) | **GET** /auth/recovery | Recovery Page
[**recovery_restore_auth_recovery_restore_post**](DefaultApi.md#recovery_restore_auth_recovery_restore_post) | **POST** /auth/recovery/restore | Recovery Restore
[**redeem_share_s_share_key_get**](DefaultApi.md#redeem_share_s_share_key_get) | **GET** /s/{share_key} | Redeem Share
[**redeem_share_with_password_s_share_key_post**](DefaultApi.md#redeem_share_with_password_s_share_key_post) | **POST** /s/{share_key} | Redeem Share With Password
[**remove_member_web_web_members_target_user_id_remove_post**](DefaultApi.md#remove_member_web_web_members_target_user_id_remove_post) | **POST** /web/members/{target_user_id}/remove | Remove Member Web
[**rename_drive_web_web_drives_drive_id_rename_post**](DefaultApi.md#rename_drive_web_web_drives_drive_id_rename_post) | **POST** /web/drives/{drive_id}/rename | Rename Drive Web
[**rename_workspace_web_web_workspaces_org_id_rename_post**](DefaultApi.md#rename_workspace_web_web_workspaces_org_id_rename_post) | **POST** /web/workspaces/{org_id}/rename | Rename Workspace Web
[**resend_invitation_web_web_invitations_invitation_id_resend_post**](DefaultApi.md#resend_invitation_web_web_invitations_invitation_id_resend_post) | **POST** /web/invitations/{invitation_id}/resend | Resend Invitation Web
[**restore_artifact_v0_artifacts_art_id_restore_post**](DefaultApi.md#restore_artifact_v0_artifacts_art_id_restore_post) | **POST** /v0/artifacts/{art_id}/restore | Restore a soft-deleted artifact
[**restore_artifact_version_v0_artifacts_art_id_versions_version_number_restore_post**](DefaultApi.md#restore_artifact_version_v0_artifacts_art_id_versions_version_number_restore_post) | **POST** /v0/artifacts/{art_id}/versions/{version_number}/restore | Restore a previous version as a new head version
[**restore_drive_route_v0_drives_drive_id_restore_post**](DefaultApi.md#restore_drive_route_v0_drives_drive_id_restore_post) | **POST** /v0/drives/{drive_id}/restore | Restore a soft-deleted drive
[**restore_folder_by_id_v0_folders_fld_id_restore_post**](DefaultApi.md#restore_folder_by_id_v0_folders_fld_id_restore_post) | **POST** /v0/folders/{fld_id}/restore | Restore a soft-deleted folder (cascade)
[**revoke_grant_web_share_rid_grant_grn_id_revoke_post**](DefaultApi.md#revoke_grant_web_share_rid_grant_grn_id_revoke_post) | **POST** /web/share/{rid}/grant/{grn_id}/revoke | Revoke Grant
[**revoke_invitation_web_web_invitations_invitation_id_revoke_post**](DefaultApi.md#revoke_invitation_web_web_invitations_invitation_id_revoke_post) | **POST** /web/invitations/{invitation_id}/revoke | Revoke Invitation Web
[**revoke_key_web_keys_revoke_post**](DefaultApi.md#revoke_key_web_keys_revoke_post) | **POST** /web/keys/revoke | Revoke Key
[**revoke_link_web_share_rid_link_shr_id_revoke_post**](DefaultApi.md#revoke_link_web_share_rid_link_shr_id_revoke_post) | **POST** /web/share/{rid}/link/{shr_id}/revoke | Revoke Link
[**revoke_user_token_web_tokens_revoke_post**](DefaultApi.md#revoke_user_token_web_tokens_revoke_post) | **POST** /web/tokens/revoke | Revoke User Token
[**rotate_share_route_v0_shares_shr_id_rotate_post**](DefaultApi.md#rotate_share_route_v0_shares_shr_id_rotate_post) | **POST** /v0/shares/{shr_id}/rotate | Revoke + reissue a share link&#39;s key (requires can_share)
[**search_v0_search_get**](DefaultApi.md#search_v0_search_get) | **GET** /v0/search | Full-text search over artifacts in the drive
[**set_member_role_web_web_members_target_user_id_role_post**](DefaultApi.md#set_member_role_web_web_members_target_user_id_role_post) | **POST** /web/members/{target_user_id}/role | Set Member Role Web
[**set_public_web_share_rid_public_post**](DefaultApi.md#set_public_web_share_rid_public_post) | **POST** /web/share/{rid}/public | Set Public
[**set_seal_web_share_rid_seal_post**](DefaultApi.md#set_seal_web_share_rid_seal_post) | **POST** /web/share/{rid}/seal | Set Seal
[**settings_account_settings_get**](DefaultApi.md#settings_account_settings_get) | **GET** /settings | Settings Account
[**settings_api_keys_settings_api_keys_get**](DefaultApi.md#settings_api_keys_settings_api_keys_get) | **GET** /settings/api-keys | Settings Api Keys
[**settings_quickstart_settings_quickstart_get**](DefaultApi.md#settings_quickstart_settings_quickstart_get) | **GET** /settings/quickstart | Settings Quickstart
[**settings_workspace_settings_workspace_get**](DefaultApi.md#settings_workspace_settings_workspace_get) | **GET** /settings/workspace | Settings Workspace
[**shared_files_shared_get**](DefaultApi.md#shared_files_shared_get) | **GET** /shared | Shared Files
[**switch_drive_web_switch_post**](DefaultApi.md#switch_drive_web_switch_post) | **POST** /web/switch | Switch Drive
[**terms_page_terms_get**](DefaultApi.md#terms_page_terms_get) | **GET** /terms | Terms Page
[**toggle_indexing_web_account_indexing_post**](DefaultApi.md#toggle_indexing_web_account_indexing_post) | **POST** /web/account/indexing | Toggle Indexing
[**trash_web_trash_get**](DefaultApi.md#trash_web_trash_get) | **GET** /web/trash | Trash
[**view_artifact_head_a_art_id_head_get**](DefaultApi.md#view_artifact_head_a_art_id_head_get) | **GET** /a/{art_id}/head | View Artifact Head
[**view_artifact_version_v_art_id_version_get**](DefaultApi.md#view_artifact_version_v_art_id_version_get) | **GET** /v/{art_id}/{version} | View Artifact Version
[**view_file_drive_id_path_get**](DefaultApi.md#view_file_drive_id_path_get) | **GET** /{drive_id}/{path} | View File
[**view_permalink_artifact_a_art_id_get**](DefaultApi.md#view_permalink_artifact_a_art_id_get) | **GET** /a/{art_id} | View Permalink Artifact
[**view_permalink_folder_f_fld_id_get**](DefaultApi.md#view_permalink_folder_f_fld_id_get) | **GET** /f/{fld_id} | View Permalink Folder
[**web_artifact_indexed_web_artifacts_indexed_get**](DefaultApi.md#web_artifact_indexed_web_artifacts_indexed_get) | **GET** /web/artifacts/indexed | Web Artifact Indexed
[**web_copy_artifact_web_artifacts_copy_post**](DefaultApi.md#web_copy_artifact_web_artifacts_copy_post) | **POST** /web/artifacts/copy | Web Copy Artifact
[**web_delete_artifact_op_web_artifacts_delete_post**](DefaultApi.md#web_delete_artifact_op_web_artifacts_delete_post) | **POST** /web/artifacts/delete | Web Delete Artifact Op
[**web_delete_artifact_web_artifacts_path_delete**](DefaultApi.md#web_delete_artifact_web_artifacts_path_delete) | **DELETE** /web/artifacts/{path} | Web Delete Artifact
[**web_delete_folder_web_folders_delete_post**](DefaultApi.md#web_delete_folder_web_folders_delete_post) | **POST** /web/folders/delete | Web Delete Folder
[**web_move_folder_web_folders_move_post**](DefaultApi.md#web_move_folder_web_folders_move_post) | **POST** /web/folders/move | Web Move Folder
[**web_new_folder_web_folders_new_post**](DefaultApi.md#web_new_folder_web_folders_new_post) | **POST** /web/folders/new | Web New Folder
[**web_project_compile_web_projects_fld_id_compile_post**](DefaultApi.md#web_project_compile_web_projects_fld_id_compile_post) | **POST** /web/projects/{fld_id}/compile | Web Project Compile
[**web_project_files_web_projects_fld_id_files_get**](DefaultApi.md#web_project_files_web_projects_fld_id_files_get) | **GET** /web/projects/{fld_id}/files | Web Project Files
[**web_project_preview_web_projects_fld_id_preview_get**](DefaultApi.md#web_project_preview_web_projects_fld_id_preview_get) | **GET** /web/projects/{fld_id}/preview | Web Project Preview
[**web_put_artifact_web_artifacts_path_put**](DefaultApi.md#web_put_artifact_web_artifacts_path_put) | **PUT** /web/artifacts/{path} | Web Put Artifact
[**web_rename_artifact_web_artifacts_rename_post**](DefaultApi.md#web_rename_artifact_web_artifacts_rename_post) | **POST** /web/artifacts/rename | Web Rename Artifact
[**web_restore_artifact_web_artifacts_restore_post**](DefaultApi.md#web_restore_artifact_web_artifacts_restore_post) | **POST** /web/artifacts/restore | Web Restore Artifact
[**web_restore_folder_web_folders_restore_post**](DefaultApi.md#web_restore_folder_web_folders_restore_post) | **POST** /web/folders/restore | Web Restore Folder
[**web_set_metadata_web_set_post**](DefaultApi.md#web_set_metadata_web_set_post) | **POST** /web/set | Web Set Metadata
[**web_upload_web_upload_post**](DefaultApi.md#web_upload_web_upload_post) | **POST** /web/upload | Web Upload
[**webhooks_page_webhooks_get**](DefaultApi.md#webhooks_page_webhooks_get) | **GET** /webhooks | Webhooks Page
[**welcome_welcome_get**](DefaultApi.md#welcome_welcome_get) | **GET** /welcome | Welcome


# **abort_upload_v0_uploads_upload_id_delete**
> UploadAbortOut abort_upload_v0_uploads_upload_id_delete(upload_id, authorization=authorization)

Abort a large (direct-to-GCS) upload session

Release an open upload session: return its reserved quota to the drive and mark it aborted. Idempotent — aborting an already-aborted or already-expired session succeeds with `released_bytes: 0`. A committed session cannot be aborted (409 ALREADY_COMMITTED). No write budget is charged — this frees resources rather than consuming them.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    upload_id = 'upload_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Abort a large (direct-to-GCS) upload session
        api_response = api_instance.abort_upload_v0_uploads_upload_id_delete(upload_id, authorization=authorization)
        print("The response of DefaultApi->abort_upload_v0_uploads_upload_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->abort_upload_v0_uploads_upload_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**UploadAbortOut**](UploadAbortOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | No such upload for this drive |  -  |
**409** | Upload already committed — cannot abort |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accept_invitation_invitations_token_get**
> str accept_invitation_invitations_token_get(token)

Accept Invitation

Accept a workspace invitation (workspaces-design §4.4). Top-level
route — deliberately OFF the reserved single-letter prefixes
(`/a /f /s /v /_`).

If the visitor isn't signed in, bounce through `/auth/login` with a
same-origin `return_to` back here (the login flow validates return_to,
so the path is safe). Once signed in, validate + accept:
  * email mismatch / expired / revoked / unknown → friendly error page,
  * success → join the workspace, set it active, land on the dashboard.

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
    token = 'token_example' # str | 

    try:
        # Accept Invitation
        api_response = api_instance.accept_invitation_invitations_token_get(token)
        print("The response of DefaultApi->accept_invitation_invitations_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->accept_invitation_invitations_token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_feed_activity_get**
> str activity_feed_activity_get()

Activity Feed

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

    try:
        # Activity Feed
        api_response = api_instance.activity_feed_activity_get()
        print("The response of DefaultApi->activity_feed_activity_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->activity_feed_activity_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_grant_web_share_rid_grant_post**
> object add_grant_web_share_rid_grant_post(rid, grant_in, x_csrf_token=x_csrf_token)

Add Grant

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.grant_in import GrantIn
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
    rid = 'rid_example' # str | 
    grant_in = agentdrive_sdk.GrantIn() # GrantIn | 
    x_csrf_token = 'x_csrf_token_example' # str |  (optional)

    try:
        # Add Grant
        api_response = api_instance.add_grant_web_share_rid_grant_post(rid, grant_in, x_csrf_token=x_csrf_token)
        print("The response of DefaultApi->add_grant_web_share_rid_grant_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_grant_web_share_rid_grant_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**|  | 
 **grant_in** | [**GrantIn**](GrantIn.md)|  | 
 **x_csrf_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifact_detail_preview_preview_artifact_detail_get**
> str artifact_detail_preview_preview_artifact_detail_get()

Artifact Detail Preview

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

    try:
        # Artifact Detail Preview
        api_response = api_instance.artifact_detail_preview_preview_artifact_detail_get()
        print("The response of DefaultApi->artifact_detail_preview_preview_artifact_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->artifact_detail_preview_preview_artifact_detail_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_upload_v0_uploads_post**
> UploadBeginOut begin_upload_v0_uploads_post(upload_begin_in, authorization=authorization)

Begin a large (direct-to-GCS) upload

Reserve quota and open a resumable upload session for a file larger than the buffered-upload limit. Returns a `upload_url` to PUT the raw bytes to DIRECTLY (no Authorization header — the URL is the credential), then call `/v0/uploads/{upload_id}/commit`. All artifact decisions (path, labels, metadata, source, if_match) are frozen here.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    upload_begin_in = agentdrive_sdk.UploadBeginIn() # UploadBeginIn | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Begin a large (direct-to-GCS) upload
        api_response = api_instance.begin_upload_v0_uploads_post(upload_begin_in, authorization=authorization)
        print("The response of DefaultApi->begin_upload_v0_uploads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->begin_upload_v0_uploads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_begin_in** | [**UploadBeginIn**](UploadBeginIn.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**UploadBeginOut**](UploadBeginOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid path / labels / metadata / source |  -  |
**403** | Path reserved for the system (WIKI_RESERVED) |  -  |
**413** | size_bytes exceeds the drive&#39;s per-artifact cap, or drive storage quota would be exceeded |  -  |
**429** | Drive&#39;s per-hour write budget exhausted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **callback_auth_callback_get**
> object callback_auth_callback_get(code=code, state=state, error=error)

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

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_job_v0_jobs_job_id_cancel_post**
> object cancel_job_v0_jobs_job_id_cancel_post(job_id, authorization=authorization)

Cancel a queued/running job

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
    job_id = 'job_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Cancel a queued/running job
        api_response = api_instance.cancel_job_v0_jobs_job_id_cancel_post(job_id, authorization=authorization)
        print("The response of DefaultApi->cancel_job_v0_jobs_job_id_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_job_v0_jobs_job_id_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collection_detail_collections_slug_get**
> str collection_detail_collections_slug_get(slug)

Collection Detail

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
    slug = 'slug_example' # str | 

    try:
        # Collection Detail
        api_response = api_instance.collection_detail_collections_slug_get(slug)
        print("The response of DefaultApi->collection_detail_collections_slug_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->collection_detail_collections_slug_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commit_upload_v0_uploads_upload_id_commit_post**
> ArtifactOut commit_upload_v0_uploads_upload_id_commit_post(upload_id, authorization=authorization)

Commit a large (direct-to-GCS) upload

Finalize the upload begun at `/v0/uploads`: AgentDrive verifies the object that landed in GCS (size + checksum) and creates the artifact. Idempotent — a retry after a successful commit returns the same artifact. The write budget is charged here (begin is free metadata).

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    upload_id = 'upload_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Commit a large (direct-to-GCS) upload
        api_response = api_instance.commit_upload_v0_uploads_upload_id_commit_post(upload_id, authorization=authorization)
        print("The response of DefaultApi->commit_upload_v0_uploads_upload_id_commit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->commit_upload_v0_uploads_upload_id_commit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | No such upload for this drive |  -  |
**409** | Uploaded object size !&#x3D; declared size_bytes |  -  |
**410** | Upload session expired |  -  |
**412** | If-Match precondition failed / create-only conflict |  -  |
**429** | Drive&#39;s per-hour write budget exhausted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_page_connectors_get**
> str connectors_page_connectors_get()

Connectors Page

Connectors landing — Google Drive, Notion, etc. Each connector pipes
its files into a virtual folder at the drive root (`gdrive/`, `notion/`)
so the indexer can build wiki pages across all of an org's knowledge.
No backend in v0; cards read from `mock/data.py`.

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

    try:
        # Connectors Page
        api_response = api_instance.connectors_page_connectors_get()
        print("The response of DefaultApi->connectors_page_connectors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->connectors_page_connectors_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_artifact_route_v0_artifacts_art_id_copy_post**
> ArtifactOut copy_artifact_route_v0_artifacts_art_id_copy_post(art_id, copy_in, x_agentdrive_actor=x_agentdrive_actor, if_none_match=if_none_match, authorization=authorization)

Duplicate an artifact to a new path (CAS-shared, new ID)

Create a new artifact at `path` whose bytes are identical to the source artifact's. The copy reuses the source's CAS object (zero new storage) but gets a fresh `art_…` ID, a fresh version 1, and — by default — `source.refs = [{type: 'artifact', id: '<source>'}]` so provenance is preserved.

Quota: the copy's `size_bytes` is added to the drive's `storage_bytes` even though physical bytes are shared.

Source-version pin: pass `from_generation` in the body to require the source's current content generation (`version_number`) to equal it (→ 412 SOURCE_VERSION_MISMATCH); a concurrent source *metadata* edit does NOT fail the copy. Destination create-only: `If-None-Match: *` returns 412 CREATE_CONFLICT (instead of 409 PATH_CONFLICT) when the target path is occupied.

Returns 409 PATH_CONFLICT if the target path is already taken; 413 STORAGE_QUOTA_EXCEEDED if the copy would push the drive over its limit.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str | 
    copy_in = agentdrive_sdk.CopyIn() # CopyIn | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_none_match = 'if_none_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Duplicate an artifact to a new path (CAS-shared, new ID)
        api_response = api_instance.copy_artifact_route_v0_artifacts_art_id_copy_post(art_id, copy_in, x_agentdrive_actor=x_agentdrive_actor, if_none_match=if_none_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_folder_by_id_v0_folders_fld_id_copy_post**
> FolderCopyOut copy_folder_by_id_v0_folders_fld_id_copy_post(fld_id, folder_copy_in, x_agentdrive_actor=x_agentdrive_actor, if_none_match=if_none_match, authorization=authorization)

Duplicate a folder subtree to a new path (CAS-shared, new IDs)

Clone the folder identified by URL id — and every descendant folder + artifact — under the body's `path` (canonical, trailing slash). Each copied artifact reuses the source's CAS object (zero new storage) but gets a fresh `art_…` ID, a fresh version 1, and `source.refs = [{type: 'artifact', id: '<source>'}]` provenance. The new folder gets a fresh `fld_…` ID and the source's description.

The entire subtree is copied in a SINGLE transaction — either every row lands or none does.

Quota: each copy's `size_bytes` counts against the drive's `storage_bytes` even though physical bytes are shared.

Source-version pin: pass `from_metageneration` in the body to require the source folder's current `metageneration` to equal it (→ 412 SOURCE_VERSION_MISMATCH). Destination create-only: `If-None-Match: *` returns 412 CREATE_CONFLICT (instead of 409 FOLDER_PATH_CONFLICT) when the destination folder is occupied.

Returns 409 `FOLDER_PATH_CONFLICT` if the destination collides with a live folder or artifact; 400 `FOLDER_PATH_INVALID` if `path` is non-canonical; 413 `SUBTREE_TOO_LARGE` if the source holds more than 5000 artifacts; 413 `STORAGE_QUOTA_EXCEEDED` if the copy would push the drive over its limit.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str | 
    folder_copy_in = agentdrive_sdk.FolderCopyIn() # FolderCopyIn | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_none_match = 'if_none_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Duplicate a folder subtree to a new path (CAS-shared, new IDs)
        api_response = api_instance.copy_folder_by_id_v0_folders_fld_id_copy_post(fld_id, folder_copy_in, x_agentdrive_actor=x_agentdrive_actor, if_none_match=if_none_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**FolderCopyOut**](FolderCopyOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drive_key_web_web_drives_drive_id_keys_create_post**
> object create_drive_key_web_web_drives_drive_id_keys_create_post(drive_id, csrf, label=label)

Create Drive Key Web

Mint a new `ad_live_` key for a specific owned drive + reveal once
(workspaces-design §5.6). Manager-only (no-leak no-op otherwise).

The per-drive twin of `/web/keys/create` (which acts on the active
drive). Pins the target drive active so the reveal on the api-keys
tab shows the key for the drive the user just minted on.

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
    csrf = 'csrf_example' # str | 
    label = '' # str |  (optional) (default to '')

    try:
        # Create Drive Key Web
        api_response = api_instance.create_drive_key_web_web_drives_drive_id_keys_create_post(drive_id, csrf, label=label)
        print("The response of DefaultApi->create_drive_key_web_web_drives_drive_id_keys_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_drive_key_web_web_drives_drive_id_keys_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **csrf** | **str**|  | 
 **label** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drive_web_web_drives_post**
> object create_drive_web_web_drives_post(name, csrf)

Create Drive Web

Create a drive in the active workspace + reveal its key once
(workspaces-design §4.5, §5.6).

The web (session+CSRF) twin of `POST /v0/drives`. Any MEMBER of the
active workspace may create a drive; the creator becomes its owner.
The new drive's `ad_live_` key is shown ONCE via the same
`reveal_key`-in-session mechanism the api-keys tab consumes; we also
pin the new drive as active and land on the api-keys tab so the user
sees the reveal.

Authorization is by `current_user` + membership, NOT `current_drive`
(workspaces-design §4.3 empty state): a freshly-invited member owns 0
drives, so `current_drive` is None for them — yet this is exactly the
"create your first drive" moment that MUST work. Gating on a pre-existing
drive would dead-end the web onboarding path. Membership + the per-member
cap are the real guards; both hold whether or not the user already owns a
drive.

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
    name = 'name_example' # str | 
    csrf = 'csrf_example' # str | 

    try:
        # Create Drive Web
        api_response = api_instance.create_drive_web_web_drives_post(name, csrf)
        print("The response of DefaultApi->create_drive_web_web_drives_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_drive_web_web_drives_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder_by_path_v0_folders_path_put**
> FolderOut create_folder_by_path_v0_folders_path_put(path, x_agentdrive_actor=x_agentdrive_actor, if_none_match=if_none_match, authorization=authorization, folder_create_in=folder_create_in)

Create a folder (idempotent)

Create a folder at the URL path. Idempotent create-at-known-URI (mirrors `PUT /v0/artifacts/{path}`) — a second call for the same live path returns the existing row unchanged (metadata updates require PATCH). Returns 201 on create, 200 when the folder already exists.

Send `If-None-Match: *` to make it strictly create-only: an existing folder then returns 412 CREATE_CONFLICT instead of the idempotent 200.

Returns 409 `FOLDER_PATH_CONFLICT` if a live artifact occupies the file form of the path (e.g. mkdir `/foo/` when an artifact lives at `/foo`).

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_none_match = 'if_none_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    folder_create_in = agentdrive_sdk.FolderCreateIn() # FolderCreateIn |  (optional)

    try:
        # Create a folder (idempotent)
        api_response = api_instance.create_folder_by_path_v0_folders_path_put(path, x_agentdrive_actor=x_agentdrive_actor, if_none_match=if_none_match, authorization=authorization, folder_create_in=folder_create_in)
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
 **authorization** | **str**|  | [optional] 
 **folder_create_in** | [**FolderCreateIn**](FolderCreateIn.md)|  | [optional] 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_grant_route_v0_grants_post**
> GrantOut create_grant_route_v0_grants_post(grant_create_in, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)

Create (or fetch) a per-principal grant on a resource

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    grant_create_in = agentdrive_sdk.GrantCreateIn() # GrantCreateIn | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Create (or fetch) a per-principal grant on a resource
        api_response = api_instance.create_grant_route_v0_grants_post(grant_create_in, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_key_web_keys_create_post**
> object create_key_web_keys_create_post(csrf, label=label)

Create Key

Mint a new `ad_live_` key for the active drive (reveal-once).

A drive may hold several keys — this appends one rather than replacing.
Management gate (workspaces-v2 §4.4): personal → owner, team → admin.
Without it a team MEMBER (who now reaches the shared drive) could mint a
shared key. No-leak redirect on non-manage.

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
    label = '' # str |  (optional) (default to '')

    try:
        # Create Key
        api_response = api_instance.create_key_web_keys_create_post(csrf, label=label)
        print("The response of DefaultApi->create_key_web_keys_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_key_web_keys_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **str**|  | 
 **label** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_link_web_share_rid_link_post**
> object create_link_web_share_rid_link_post(rid, link_in, x_csrf_token=x_csrf_token)

Create Link

Mint a viewer share link. Returns the fresh state PLUS `minted` with the
raw `share_key` + url — the ONLY response that carries the key. Artifacts
only (v1: folder share links are not supported).

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.link_in import LinkIn
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
    rid = 'rid_example' # str | 
    link_in = agentdrive_sdk.LinkIn() # LinkIn | 
    x_csrf_token = 'x_csrf_token_example' # str |  (optional)

    try:
        # Create Link
        api_response = api_instance.create_link_web_share_rid_link_post(rid, link_in, x_csrf_token=x_csrf_token)
        print("The response of DefaultApi->create_link_web_share_rid_link_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_link_web_share_rid_link_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**|  | 
 **link_in** | [**LinkIn**](LinkIn.md)|  | 
 **x_csrf_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_share_route_v0_shares_post**
> ShareMintOut create_share_route_v0_shares_post(share_create_in, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)

Mint a share link (returns the share_key once)

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    share_create_in = agentdrive_sdk.ShareCreateIn() # ShareCreateIn | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Mint a share link (returns the share_key once)
        api_response = api_instance.create_share_route_v0_shares_post(share_create_in, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**ShareMintOut**](ShareMintOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_token_web_tokens_create_post**
> object create_user_token_web_tokens_create_post(csrf, label=label, scope=scope)

Create User Token

Mint an `ad_user_` user-identity token (workspaces-design §5.2, §5.6).

**Web-only minting**: the bootstrap chicken-and-egg is solved here,
and a leaked token must not be able to mint persistent siblings — so
this path exists only behind the browser session + CSRF, never over
the `/v0/` API.

The raw token is shown ONCE via `reveal_token` in the session, then
consumed on the next GET of the api-keys tab.

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
    label = '' # str |  (optional) (default to '')
    scope = 'full' # str |  (optional) (default to 'full')

    try:
        # Create User Token
        api_response = api_instance.create_user_token_web_tokens_create_post(csrf, label=label, scope=scope)
        print("The response of DefaultApi->create_user_token_web_tokens_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_user_token_web_tokens_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **str**|  | 
 **label** | **str**|  | [optional] [default to &#39;&#39;]
 **scope** | **str**|  | [optional] [default to &#39;full&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace_web_web_workspaces_post**
> object create_workspace_web_web_workspaces_post(name, csrf)

Create Workspace Web

Create a new workspace, set it active, reveal its starter key once
(workspaces-design §4.7).

The web (session+CSRF) twin of `POST /v0/workspaces`. A user may
administer up to their plan's number of TEAM workspaces
(`core.entitlements.can_create_workspace`, tier-governed — workspaces-v2
§4.6); a blocked create bounces to the dashboard with a limit-reached
affordance (`?err=workspace_limit`). On success the new workspace + its starter
drive become active and we land on the api-keys tab so the user sees the
one-time key reveal.

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
    name = 'name_example' # str | 
    csrf = 'csrf_example' # str | 

    try:
        # Create Workspace Web
        api_response = api_instance.create_workspace_web_web_workspaces_post(name, csrf)
        print("The response of DefaultApi->create_workspace_web_web_workspaces_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_workspace_web_web_workspaces_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **danger_zone_old_dashboard_danger_get**
> object danger_zone_old_dashboard_danger_get()

Danger Zone Old

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

    try:
        # Danger Zone Old
        api_response = api_instance.danger_zone_old_dashboard_danger_get()
        print("The response of DefaultApi->danger_zone_old_dashboard_danger_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->danger_zone_old_dashboard_danger_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **danger_zone_settings_danger_get**
> str danger_zone_settings_danger_get()

Danger Zone

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

    try:
        # Danger Zone
        api_response = api_instance.danger_zone_settings_danger_get()
        print("The response of DefaultApi->danger_zone_settings_danger_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->danger_zone_settings_danger_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_dashboard_get**
> str dashboard_dashboard_get(q=q, path=path, wiki=wiki, type=type, label=label, after=after, before=before, view=view, sort=sort, dir=dir)

Dashboard

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
    q = '' # str |  (optional) (default to '')
    path = '' # str |  (optional) (default to '')
    wiki = 0 # int |  (optional) (default to 0)
    type = '' # str |  (optional) (default to '')
    label = ['label_example'] # List[str] |  (optional)
    after = '' # str |  (optional) (default to '')
    before = '' # str |  (optional) (default to '')
    view = '' # str |  (optional) (default to '')
    sort = '' # str |  (optional) (default to '')
    dir = '' # str |  (optional) (default to '')

    try:
        # Dashboard
        api_response = api_instance.dashboard_dashboard_get(q=q, path=path, wiki=wiki, type=type, label=label, after=after, before=before, view=view, sort=sort, dir=dir)
        print("The response of DefaultApi->dashboard_dashboard_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->dashboard_dashboard_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] [default to &#39;&#39;]
 **path** | **str**|  | [optional] [default to &#39;&#39;]
 **wiki** | **int**|  | [optional] [default to 0]
 **type** | **str**|  | [optional] [default to &#39;&#39;]
 **label** | [**List[str]**](str.md)|  | [optional] 
 **after** | **str**|  | [optional] [default to &#39;&#39;]
 **before** | **str**|  | [optional] [default to &#39;&#39;]
 **view** | **str**|  | [optional] [default to &#39;&#39;]
 **sort** | **str**|  | [optional] [default to &#39;&#39;]
 **dir** | **str**|  | [optional] [default to &#39;&#39;]

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_web_account_delete_post**
> object delete_account_web_account_delete_post(confirm, csrf)

Delete Account

Soft-delete the user + their solo workspace + drive.

v1 semantics (solo orgs): deleting the account also deletes the
workspace and its data under one aligned retention window, after
which everything is hard-purged. "Delete my account" means "delete
everything mine," matching Notion / Linear / Slack consumer-tier
semantics. Membership-transfer for shared orgs lands in v1.5+.

The response routes through the auth provider's logout so the
upstream session is cleared before the user returns, preventing a
silent re-authentication that would re-provision the just-deleted
account. Falls back to a local-only redirect when there is no
upstream session to clear.

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
    confirm = 'confirm_example' # str | 
    csrf = 'csrf_example' # str | 

    try:
        # Delete Account
        api_response = api_instance.delete_account_web_account_delete_post(confirm, csrf)
        print("The response of DefaultApi->delete_account_web_account_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_account_web_account_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirm** | **str**|  | 
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact_by_id_route_v0_artifacts_art_id_delete**
> object delete_artifact_by_id_route_v0_artifacts_art_id_delete(art_id, if_match=if_match, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)

Soft-delete an artifact by its stable ID

Soft-delete the artifact with this `art_…` ID. Same semantics + response shape as the path-based `DELETE /v0/artifacts/{path}` (reversible until the GC cron hard-deletes at `purge_at`; `restore_url` points at the by-id restore), but keys on the immutable id so a concurrent rename can't change the target.

Returns 404 ARTIFACT_NOT_FOUND if no live artifact has this id; 403 WIKI_RESERVED for `_wiki/` artifacts (system-managed); 412 if `If-Match` doesn't match the current version. Declared before the `{path:path}` family so the id convertor wins for DELETEs.

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
    if_match = 'if_match_example' # str |  (optional)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Soft-delete an artifact by its stable ID
        api_response = api_instance.delete_artifact_by_id_route_v0_artifacts_art_id_delete(art_id, if_match=if_match, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact_v0_artifacts_path_delete**
> ArtifactDeleteOut delete_artifact_v0_artifacts_path_delete(path, if_match=if_match, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)

Delete Artifact

Soft-delete the artifact at the given path.

A delete WITHOUT an `If-Match` precondition is last-writer-wins and will
silently remove a concurrently-modified artifact.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str | 
    if_match = 'if_match_example' # str |  (optional)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Delete Artifact
        api_response = api_instance.delete_artifact_v0_artifacts_path_delete(path, if_match=if_match, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**ArtifactDeleteOut**](ArtifactDeleteOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_drive_route_v0_drives_drive_id_delete**
> DriveDeleteOut delete_drive_route_v0_drives_drive_id_delete(drive_id, confirm=confirm, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

Soft-delete a drive

Mark the drive for cleanup. All tenant data (artifacts, versions, wiki, embeddings, events) is hidden via the `live_*` views and CASCADE-removed by the GC cleanup cron at `purge_at`. Restore via `POST /v0/drives/{id}/restore` while the row is still in trash. The path-param `drive_id` MUST match the authenticated drive.

Accepts either an `ad_live_` per-drive key (deletes that key's drive) or an `ad_user_` user token selecting an owned drive (workspaces-design §5.3); a `read`-scope user token is rejected with 403 `INSUFFICIENT_SCOPE`. **Guard (§8):** a workspace must retain at least one live drive — deleting the workspace's last live drive returns 409 `LAST_DRIVE`.

**Explicit confirmation required:** pass `?confirm=DELETE` or the request is rejected with 400 `CONFIRM_REQUIRED`. Tenant-level deletion is the largest-blast-radius operation on the API; the static token forces a deliberate act (soft-delete still gives a restore window on top).

**Optimistic concurrency:** send `If-Match` with the drive's composite ETag (`"<drv_id>.0.<metageneration>"`, from a drive read) to make the delete conditional — a stale token returns 412 PRECONDITION_FAILED. A delete WITHOUT an `If-Match` precondition is last-writer-wins and will silently trash a concurrently-modified drive.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    drive_id = 'drive_id_example' # str | 
    confirm = 'confirm_example' # str |  (optional)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Soft-delete a drive
        api_response = api_instance.delete_drive_route_v0_drives_drive_id_delete(drive_id, confirm=confirm, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**DriveDeleteOut**](DriveDeleteOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_drive_web_web_drives_drive_id_delete_post**
> object delete_drive_web_web_drives_drive_id_delete_post(drive_id, csrf)

Delete Drive Web

Soft-delete a drive the caller owns, with the last-drive guard
(workspaces-design §8). Owner-only (no-leak no-op otherwise).

Guard: blocks deleting the workspace's LAST live drive — a member must
always land somewhere. On a successful delete of the *active* drive,
we drop the pin so `current_drive` falls back to the user's next
oldest owned drive.

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
    csrf = 'csrf_example' # str | 

    try:
        # Delete Drive Web
        api_response = api_instance.delete_drive_web_web_drives_drive_id_delete_post(drive_id, csrf)
        print("The response of DefaultApi->delete_drive_web_web_drives_drive_id_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_drive_web_web_drives_drive_id_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder_by_id_v0_folders_fld_id_delete**
> FolderDeleteOut delete_folder_by_id_v0_folders_fld_id_delete(fld_id, recursive=recursive, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

Soft-delete a folder by stable ID (cascade with ?recursive=true)

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str | 
    recursive = False # bool |  (optional) (default to False)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Soft-delete a folder by stable ID (cascade with ?recursive=true)
        api_response = api_instance.delete_folder_by_id_v0_folders_fld_id_delete(fld_id, recursive=recursive, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**FolderDeleteOut**](FolderDeleteOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder_by_path_v0_folders_path_delete**
> FolderDeleteOut delete_folder_by_path_v0_folders_path_delete(path, recursive=recursive, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

Soft-delete a folder (cascade with ?recursive=true)

Soft-delete the folder. Refuses if the folder has live descendants unless `?recursive=true` is set, in which case ALL descendant folders + artifacts are soft-deleted in the same transaction.

Returns 409 `FOLDER_RECURSIVE_REQUIRED` (with descendant counts in `colliding_path`) when recursion is needed but the flag isn't set. Retention window is frozen on `purge_at` per deletion-design.md §5.1; mid-retention tier changes don't shift it.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str | 
    recursive = False # bool |  (optional) (default to False)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Soft-delete a folder (cascade with ?recursive=true)
        api_response = api_instance.delete_folder_by_path_v0_folders_path_delete(path, recursive=recursive, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**FolderDeleteOut**](FolderDeleteOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_grant_route_v0_grants_grn_id_delete**
> RevokeOut delete_grant_route_v0_grants_grn_id_delete(grn_id, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)

Revoke a grant (can_manage, or self-revoke own grant)

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    grn_id = 'grn_id_example' # str | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Revoke a grant (can_manage, or self-revoke own grant)
        api_response = api_instance.delete_grant_route_v0_grants_grn_id_delete(grn_id, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**RevokeOut**](RevokeOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_share_route_v0_shares_shr_id_delete**
> RevokeOut delete_share_route_v0_shares_shr_id_delete(shr_id, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)

Revoke a share link (requires can_manage)

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    shr_id = 'shr_id_example' # str | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Revoke a share link (requires can_manage)
        api_response = api_instance.delete_share_route_v0_shares_shr_id_delete(shr_id, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**RevokeOut**](RevokeOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_web_web_workspaces_org_id_delete_post**
> object delete_workspace_web_web_workspaces_org_id_delete_post(org_id, csrf, confirm=confirm)

Delete Workspace Web

Explicit delete-workspace path (workspaces-design §4.4): a sole admin
who can't leave (members remain) may instead destroy the workspace —
cascade soft-delete the org + all its live drives.

Admin-gated against the PATH org (not just the session) so a stale
cookie can't redirect the cascade. A non-admin is a no-leak no-op.

**Typed confirmation required** (parallel to `delete_account`'s
`confirm == "DELETE"`): this cascade soft-deletes the WHOLE workspace
plus every member's drives in it, so a single mis-clicked CSRF POST must
not be able to trigger it. The caller must type either the literal
`DELETE` or the exact workspace name; anything else bounces with no
cascade. (Restricting to sole-admin is a separate product question,
flagged to the user — not changed here.)

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
    org_id = 'org_id_example' # str | 
    csrf = 'csrf_example' # str | 
    confirm = '' # str |  (optional) (default to '')

    try:
        # Delete Workspace Web
        api_response = api_instance.delete_workspace_web_web_workspaces_org_id_delete_post(org_id, csrf, confirm=confirm)
        print("The response of DefaultApi->delete_workspace_web_web_workspaces_org_id_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_workspace_web_web_workspaces_org_id_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **csrf** | **str**|  | 
 **confirm** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_artifact_by_id_v0_artifacts_art_id_download_get**
> object download_artifact_by_id_v0_artifacts_art_id_download_get(art_id, authorization=authorization)

Stream the artifact bytes by stable ID (never rendered HTML)

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
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Stream the artifact bytes by stable ID (never rendered HTML)
        api_response = api_instance.download_artifact_by_id_v0_artifacts_art_id_download_get(art_id, authorization=authorization)
        print("The response of DefaultApi->download_artifact_by_id_v0_artifacts_art_id_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_artifact_by_id_v0_artifacts_art_id_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_artifact_by_path_v0_artifacts_path_download_get**
> object download_artifact_by_path_v0_artifacts_path_download_get(path, authorization=authorization)

Stream the artifact bytes by path (never rendered HTML)

Same bytes-only machine surface as `/{art_id}/download` but resolves the artifact by path, so callers don't have to resolve path→id first. Applies the identical CSP `sandbox` + `nosniff` posture (never serves HTML inline as active content).

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
    path = 'path_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Stream the artifact bytes by path (never rendered HTML)
        api_response = api_instance.download_artifact_by_path_v0_artifacts_path_download_get(path, authorization=authorization)
        print("The response of DefaultApi->download_artifact_by_path_v0_artifacts_path_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_artifact_by_path_v0_artifacts_path_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_artifact_version_v0_artifacts_art_id_versions_version_number_download_get**
> object download_artifact_version_v0_artifacts_art_id_versions_version_number_download_get(art_id, version_number, authorization=authorization)

Stream bytes for a specific version (machine surface)

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
    version_number = 56 # int | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Stream bytes for a specific version (machine surface)
        api_response = api_instance.download_artifact_version_v0_artifacts_art_id_versions_version_number_download_get(art_id, version_number, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_url_by_id_v0_artifacts_art_id_download_url_get**
> DownloadUrlOut download_url_by_id_v0_artifacts_art_id_download_url_get(art_id, authorization=authorization)

Signed direct-from-GCS download URL by stable ID

Returns a URL for the artifact's bytes. For large artifacts (>= the signed-download threshold) when signing is available, it's a short-lived **signed GCS URL** the client fetches directly (`direct:true`, `expires_at` set); otherwise the **proxy** `/download` URL (`direct:false`). Treat the URL as opaque. large-download-design.md §5.1.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Signed direct-from-GCS download URL by stable ID
        api_response = api_instance.download_url_by_id_v0_artifacts_art_id_download_url_get(art_id, authorization=authorization)
        print("The response of DefaultApi->download_url_by_id_v0_artifacts_art_id_download_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_url_by_id_v0_artifacts_art_id_download_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_url_by_path_v0_artifacts_path_download_url_get**
> DownloadUrlOut download_url_by_path_v0_artifacts_path_download_url_get(path, authorization=authorization)

Signed direct-from-GCS download URL by path

Same as `/{art_id}/download-url` but resolves the artifact by path. The returned proxy URL (when `direct:false`) still points at the by-id `/download` endpoint. large-download-design.md §5.1.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Signed direct-from-GCS download URL by path
        api_response = api_instance.download_url_by_path_v0_artifacts_path_download_url_get(path, authorization=authorization)
        print("The response of DefaultApi->download_url_by_path_v0_artifacts_path_download_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_url_by_path_v0_artifacts_path_download_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_url_version_v0_artifacts_art_id_versions_version_number_download_url_get**
> DownloadUrlOut download_url_version_v0_artifacts_art_id_versions_version_number_download_url_get(art_id, version_number, authorization=authorization)

Signed direct-from-GCS download URL for a specific version

Same as `/{art_id}/download-url` but for a specific version's bytes (`direct:true` signed GCS URL when large + signing available, else the proxy `/versions/{n}/download` URL). large-download-design.md §5.1.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str | 
    version_number = 56 # int | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Signed direct-from-GCS download URL for a specific version
        api_response = api_instance.download_url_version_v0_artifacts_art_id_versions_version_number_download_url_get(art_id, version_number, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_artifact_a_art_id_edit_get**
> str edit_artifact_a_art_id_edit_get(art_id)

Edit Artifact

SnipIt annotation editor for an image artifact.

URL pattern mirrors the artifact permalink (`/a/{art_id}` → viewer;
`/a/{art_id}/edit` → editor). FastAPI matches the more-specific
`/edit` path before `/a/{art_id}` so there's no collision.

Owner-only: requires a signed-in session cookie AND the artifact
must belong to the user's currently-active drive. Non-owners and
anonymous viewers redirect to /auth/login with this URL as
`return_to` so they land back here after sign-in.

Renders an editor shell — the editor JS owns all behavior (load
the PNG, draw annotations on a canvas overlay, auto-save via
`PUT /web/artifacts/{path}` with cookie auth). v0 supports image
artifacts only; non-image art_ids redirect to the canonical
viewer URL.

Pairs with the SnipIt Chrome extension: after auto-upload finishes
the extension's SW navigates the tab to this URL, so the user's
URL bar shows the real `agentdrive.run/a/<art_id>/edit` instead
of a chrome-extension://... page. Editing on the web app side
also means the same flow is reachable from the dashboard ("Edit
this clip") without the extension installed.

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
        # Edit Artifact
        api_response = api_instance.edit_artifact_a_art_id_edit_get(art_id)
        print("The response of DefaultApi->edit_artifact_a_art_id_edit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edit_artifact_a_art_id_edit_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enqueue_job_v0_projects_fld_id_jobs_post**
> object enqueue_job_v0_projects_fld_id_jobs_post(fld_id, compile_job_in, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)

Enqueue a compile job for a project (folder)

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.compile_job_in import CompileJobIn
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
    compile_job_in = agentdrive_sdk.CompileJobIn() # CompileJobIn | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Enqueue a compile job for a project (folder)
        api_response = api_instance.enqueue_job_v0_projects_fld_id_jobs_post(fld_id, compile_job_in, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extension_start_auth_extension_start_get**
> object extension_start_auth_extension_start_get(ext_id=ext_id)

Extension Start

Begin a WorkOS sign-in flow on behalf of a Chrome extension.

Stamps `for=ext` + `ext_id` into the signed OAuth state so the
callback handler knows to render the extension handoff page
instead of setting a session cookie.

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
        api_response = api_instance.extension_start_auth_extension_start_get(ext_id=ext_id)
        print("The response of DefaultApi->extension_start_auth_extension_start_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->extension_start_auth_extension_start_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ext_id** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feedback_form_feedback_get**
> str feedback_form_feedback_get()

Feedback Form

Render the feedback form. Auth-required.

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

    try:
        # Feedback Form
        api_response = api_instance.feedback_form_feedback_get()
        print("The response of DefaultApi->feedback_form_feedback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->feedback_form_feedback_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feedback_submit_feedback_post**
> object feedback_submit_feedback_post(csrf, category=category, title=title, message=message, contact=contact, attachments=attachments)

Feedback Submit

Validate, charge the feedback budget, insert the ticket,
redirect with a flash.

Validation runs BEFORE the quota charge so users get clear field
errors without burning budget. The ticket insert is LLM-free and
GitHub-free (§5.2) — the triage lane picks it up on its next tick.

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
    category = '' # str |  (optional) (default to '')
    title = '' # str |  (optional) (default to '')
    message = '' # str |  (optional) (default to '')
    contact = '' # str |  (optional) (default to '')
    attachments = None # List[bytes] |  (optional)

    try:
        # Feedback Submit
        api_response = api_instance.feedback_submit_feedback_post(csrf, category=category, title=title, message=message, contact=contact, attachments=attachments)
        print("The response of DefaultApi->feedback_submit_feedback_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->feedback_submit_feedback_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **str**|  | 
 **category** | **str**|  | [optional] [default to &#39;&#39;]
 **title** | **str**|  | [optional] [default to &#39;&#39;]
 **message** | **str**|  | [optional] [default to &#39;&#39;]
 **contact** | **str**|  | [optional] [default to &#39;&#39;]
 **attachments** | **List[bytes]**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_v0_find_get**
> FindPage find_v0_find_get(q, mode=mode, label=label, file_type=file_type, prefix=prefix, modality=modality, updated_after=updated_after, updated_before=updated_before, limit=limit, authorization=authorization)

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

**Embedding availability:** when `GEMINI_API_KEY` is not configured, `mode=semantic` returns 500; `mode=hybrid` logs a warning and falls back to lexical-only; `mode=lexical` is unaffected.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    q = 'q_example' # str | 
    mode = hybrid # str |  (optional) (default to hybrid)
    label = ['label_example'] # List[str] |  (optional)
    file_type = 'file_type_example' # str |  (optional)
    prefix = 'prefix_example' # str |  (optional)
    modality = ['modality_example'] # List[Optional[str]] |  (optional)
    updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 20 # int |  (optional) (default to 20)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Hybrid passage retrieval over the full file body
        api_response = api_instance.find_v0_find_get(q, mode=mode, label=label, file_type=file_type, prefix=prefix, modality=modality, updated_after=updated_after, updated_before=updated_before, limit=limit, authorization=authorization)
        print("The response of DefaultApi->find_v0_find_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->find_v0_find_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | 
 **mode** | **str**|  | [optional] [default to hybrid]
 **label** | [**List[str]**](str.md)|  | [optional] 
 **file_type** | **str**|  | [optional] 
 **prefix** | **str**|  | [optional] 
 **modality** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **updated_after** | **datetime**|  | [optional] 
 **updated_before** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **authorization** | **str**|  | [optional] 

### Return type

[**FindPage**](FindPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_by_id_meta_v0_artifacts_art_id_meta_get**
> ArtifactOut get_artifact_by_id_meta_v0_artifacts_art_id_meta_get(art_id, authorization=authorization)

Artifact metadata by stable ID (same shape as path /meta)

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Artifact metadata by stable ID (same shape as path /meta)
        api_response = api_instance.get_artifact_by_id_meta_v0_artifacts_art_id_meta_get(art_id, authorization=authorization)
        print("The response of DefaultApi->get_artifact_by_id_meta_v0_artifacts_art_id_meta_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_artifact_by_id_meta_v0_artifacts_art_id_meta_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_by_id_v0_artifacts_art_id_get**
> ArtifactOut get_artifact_by_id_v0_artifacts_art_id_get(art_id, authorization=authorization)

Canonical lookup of an artifact by its stable ID

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Canonical lookup of an artifact by its stable ID
        api_response = api_instance.get_artifact_by_id_v0_artifacts_art_id_get(art_id, authorization=authorization)
        print("The response of DefaultApi->get_artifact_by_id_v0_artifacts_art_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_artifact_by_id_v0_artifacts_art_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_meta_v0_artifacts_path_meta_get**
> ArtifactOut get_artifact_meta_v0_artifacts_path_meta_get(path, authorization=authorization)

Get Artifact Meta

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Artifact Meta
        api_response = api_instance.get_artifact_meta_v0_artifacts_path_meta_get(path, authorization=authorization)
        print("The response of DefaultApi->get_artifact_meta_v0_artifacts_path_meta_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_artifact_meta_v0_artifacts_path_meta_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_version_v0_artifacts_art_id_versions_version_number_get**
> VersionOut get_artifact_version_v0_artifacts_art_id_versions_version_number_get(art_id, version_number, authorization=authorization)

Metadata for a specific version of an artifact

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str | 
    version_number = 56 # int | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Metadata for a specific version of an artifact
        api_response = api_instance.get_artifact_version_v0_artifacts_art_id_versions_version_number_get(art_id, version_number, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**VersionOut**](VersionOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drive_route_v0_drives_drive_id_get**
> object get_drive_route_v0_drives_drive_id_get(drive_id, authorization=authorization)

Drive overview by id (same shape as /drives/me)

Identical to `GET /v0/drives/me` — the by-id singleton so `Location`-style URLs and scripted clients can address the drive canonically. The path-param `drive_id` MUST match the authenticated drive (mirrors the delete/trash routes' no-leak 404). Emits the drive's composite `ETag` header (`"<drv_id>.0.<metageneration>"`).

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
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Drive overview by id (same shape as /drives/me)
        api_response = api_instance.get_drive_route_v0_drives_drive_id_get(drive_id, authorization=authorization)
        print("The response of DefaultApi->get_drive_route_v0_drives_drive_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_drive_route_v0_drives_drive_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feedback_status_v0_feedback_fbk_id_get**
> FeedbackStatusOut get_feedback_status_v0_feedback_fbk_id_get(fbk_id, authorization=authorization)

Get Feedback Status

Lifecycle status of feedback THIS drive filed. Foreign tickets
read as 404 — indistinguishable from absent.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fbk_id = 'fbk_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Feedback Status
        api_response = api_instance.get_feedback_status_v0_feedback_fbk_id_get(fbk_id, authorization=authorization)
        print("The response of DefaultApi->get_feedback_status_v0_feedback_fbk_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_feedback_status_v0_feedback_fbk_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fbk_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**FeedbackStatusOut**](FeedbackStatusOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_id_meta_v0_folders_fld_id_meta_get**
> FolderOut get_folder_by_id_meta_v0_folders_fld_id_meta_get(fld_id, authorization=authorization)

Folder metadata by stable ID (same shape as the bare id route)

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Folder metadata by stable ID (same shape as the bare id route)
        api_response = api_instance.get_folder_by_id_meta_v0_folders_fld_id_meta_get(fld_id, authorization=authorization)
        print("The response of DefaultApi->get_folder_by_id_meta_v0_folders_fld_id_meta_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_folder_by_id_meta_v0_folders_fld_id_meta_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_id_v0_folders_fld_id_get**
> FolderOut get_folder_by_id_v0_folders_fld_id_get(fld_id, authorization=authorization)

Canonical lookup of a folder by its stable ID

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Canonical lookup of a folder by its stable ID
        api_response = api_instance.get_folder_by_id_v0_folders_fld_id_get(fld_id, authorization=authorization)
        print("The response of DefaultApi->get_folder_by_id_v0_folders_fld_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_folder_by_id_v0_folders_fld_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_path_meta_v0_folders_path_meta_get**
> FolderOut get_folder_by_path_meta_v0_folders_path_meta_get(path, authorization=authorization)

Folder metadata by path (same shape as the bare path route)

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Folder metadata by path (same shape as the bare path route)
        api_response = api_instance.get_folder_by_path_meta_v0_folders_path_meta_get(path, authorization=authorization)
        print("The response of DefaultApi->get_folder_by_path_meta_v0_folders_path_meta_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_folder_by_path_meta_v0_folders_path_meta_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_path_v0_folders_path_get**
> FolderOut get_folder_by_path_v0_folders_path_get(path, authorization=authorization)

Read folder metadata by path

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Read folder metadata by path
        api_response = api_instance.get_folder_by_path_v0_folders_path_get(path, authorization=authorization)
        print("The response of DefaultApi->get_folder_by_path_v0_folders_path_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_folder_by_path_v0_folders_path_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grant_route_v0_grants_grn_id_get**
> GrantOut get_grant_route_v0_grants_grn_id_get(grn_id, authorization=authorization)

Read a single grant (can_manage, or the grant's own principal)

The `Location` target of `POST /v0/grants`. Authorization mirrors
DELETE: `can_manage` on the granted resource, or the caller IS the
grant's own principal (a grantee may read — like revoke — their own
grant). A revoked grant reads as 404 (same no-leak shape as a
foreign/absent id); DELETE stays idempotent on it.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    grn_id = 'grn_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Read a single grant (can_manage, or the grant's own principal)
        api_response = api_instance.get_grant_route_v0_grants_grn_id_get(grn_id, authorization=authorization)
        print("The response of DefaultApi->get_grant_route_v0_grants_grn_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_grant_route_v0_grants_grn_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grn_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_logs_v0_jobs_job_id_logs_get**
> object get_job_logs_v0_jobs_job_id_logs_get(job_id, authorization=authorization)

Raw compile log (text/plain)

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
    job_id = 'job_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Raw compile log (text/plain)
        api_response = api_instance.get_job_logs_v0_jobs_job_id_logs_get(job_id, authorization=authorization)
        print("The response of DefaultApi->get_job_logs_v0_jobs_job_id_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_job_logs_v0_jobs_job_id_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_v0_jobs_job_id_get**
> object get_job_v0_jobs_job_id_get(job_id, authorization=authorization)

Poll a job

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
    job_id = 'job_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Poll a job
        api_response = api_instance.get_job_v0_jobs_job_id_get(job_id, authorization=authorization)
        print("The response of DefaultApi->get_job_v0_jobs_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_job_v0_jobs_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_v0_projects_fld_id_get**
> object get_project_v0_projects_fld_id_get(fld_id, authorization=authorization)

Get a project's compile config

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
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get a project's compile config
        api_response = api_instance.get_project_v0_projects_fld_id_get(fld_id, authorization=authorization)
        print("The response of DefaultApi->get_project_v0_projects_fld_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_v0_projects_fld_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_share_route_v0_shares_shr_id_get**
> ShareOut get_share_route_v0_shares_shr_id_get(shr_id, authorization=authorization)

Read a single share link's metadata (requires can_manage)

The `Location` target of `POST /v0/shares`. Metadata ONLY —
`ShareOut` never carries the raw `share_key`/URL (returned exactly
once at mint/rotate, §4.5). Authorization mirrors DELETE:
`can_manage` on the shared resource. A revoked share reads as 404
(same no-leak shape as a foreign/absent id).

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    shr_id = 'shr_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Read a single share link's metadata (requires can_manage)
        api_response = api_instance.get_share_route_v0_shares_shr_id_get(shr_id, authorization=authorization)
        print("The response of DefaultApi->get_share_route_v0_shares_shr_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_share_route_v0_shares_shr_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shr_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**ShareOut**](ShareOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_share_state_web_share_rid_get**
> object get_share_state_web_share_rid_get(rid)

Get Share State

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
    rid = 'rid_example' # str | 

    try:
        # Get Share State
        api_response = api_instance.get_share_state_web_share_rid_get(rid)
        print("The response of DefaultApi->get_share_state_web_share_rid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_share_state_web_share_rid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_status_v0_uploads_upload_id_get**
> UploadStatusOut get_upload_status_v0_uploads_upload_id_get(upload_id, authorization=authorization)

Get the status of a large (direct-to-GCS) upload session

Report the live state of an upload session begun at `/v0/uploads`. `state` is derived: `initiated` (open — PUT the bytes then commit), `committed` (artifact created), `aborted` (released via DELETE), or `expired` (past `expires_at` without a commit). Read-only; charges the read budget.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    upload_id = 'upload_id_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get the status of a large (direct-to-GCS) upload session
        api_response = api_instance.get_upload_status_v0_uploads_upload_id_get(upload_id, authorization=authorization)
        print("The response of DefaultApi->get_upload_status_v0_uploads_upload_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_upload_status_v0_uploads_upload_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**UploadStatusOut**](UploadStatusOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | No such upload for this drive |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_health_get**
> object health_health_get()

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

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_member_web_web_members_invite_post**
> object invite_member_web_web_members_invite_post(email, csrf, role=role, workspace_name=workspace_name)

Invite Member Web

Admin invites a person by email (workspaces-design §4.4). Sends the
invite email via the e2a lane. Admin-only; a non-admin is bounced.

Rename-on-first-invite (workspaces-design §4.6): a single-member workspace
still carries its onboarding default name. The invite form offers an
optional `workspace_name` — a LIGHT prompt, not a gate. If non-empty, we
rename the workspace in the SAME submit (before sending) so teammates land
in a named workspace, not "Someone's Drive".

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
    email = 'email_example' # str | 
    csrf = 'csrf_example' # str | 
    role = 'member' # str |  (optional) (default to 'member')
    workspace_name = '' # str |  (optional) (default to '')

    try:
        # Invite Member Web
        api_response = api_instance.invite_member_web_web_members_invite_post(email, csrf, role=role, workspace_name=workspace_name)
        print("The response of DefaultApi->invite_member_web_web_members_invite_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->invite_member_web_web_members_invite_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **csrf** | **str**|  | 
 **role** | **str**|  | [optional] [default to &#39;member&#39;]
 **workspace_name** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_artifact_versions_v0_artifacts_art_id_versions_get**
> VersionPage list_artifact_versions_v0_artifacts_art_id_versions_get(art_id, cursor=cursor, limit=limit, authorization=authorization)

List versions of an artifact, newest first

Returns versions in descending `version_number` order. Cursor pagination via `?cursor=<token>`; `next_cursor` is non-null when the page is full and more older versions may exist.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str | 
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List versions of an artifact, newest first
        api_response = api_instance.list_artifact_versions_v0_artifacts_art_id_versions_get(art_id, cursor=cursor, limit=limit, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**VersionPage**](VersionPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_artifacts_v0_artifacts_get**
> Page list_artifacts_v0_artifacts_get(prefix=prefix, label=label, file_type=file_type, cursor=cursor, limit=limit, authorization=authorization)

List artifacts in the drive

Returns artifacts sorted by path. Filter by `prefix`, `label` (repeatable + AND-combined), and `file_type`.

**Cursor pagination:** when more results exist, the response carries `next_cursor`. Pass it back as `?cursor=<token>` to fetch the next page. `next_cursor` is `null` on the final page. Filters MUST stay consistent across pages — the cursor encodes only the keyset position, not the filter set, so the client is responsible for re-sending the same filter on each page.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    prefix = '' # str |  (optional) (default to '')
    label = ['label_example'] # List[Optional[str]] |  (optional)
    file_type = 'file_type_example' # str |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List artifacts in the drive
        api_response = api_instance.list_artifacts_v0_artifacts_get(prefix=prefix, label=label, file_type=file_type, cursor=cursor, limit=limit, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_events_route_v0_events_get**
> EventPage list_events_route_v0_events_get(art_id=art_id, action=action, since=since, before=before, cursor=cursor, limit=limit, authorization=authorization)

Read the append-only event log for the authenticated drive

Returns events newest-first. Filters compose with AND.

**Cursor pagination:** pass the oldest event's `created_at` from the previous page as `before` to fetch the next page back in time. Combine `since` + `before` to bound a window.

### Example


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
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Read the append-only event log for the authenticated drive
        api_response = api_instance.list_events_route_v0_events_get(art_id=art_id, action=action, since=since, before=before, cursor=cursor, limit=limit, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**EventPage**](EventPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_grants_route_v0_grants_get**
> GrantList list_grants_route_v0_grants_get(resource, cursor=cursor, limit=limit, authorization=authorization)

List live grants on a resource (requires can_manage)

**Cursor pagination:** when more results exist, the response carries `next_cursor`. Pass it back as `?cursor=<token>` to fetch the next page; `null` means the listing is complete. `limit` is clamped to [1, 100] (default 50), never rejected. The `resource` filter must be re-sent on every page — the cursor encodes only the keyset position.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    resource = 'resource_example' # str | art_*/fld_* id or a path
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List live grants on a resource (requires can_manage)
        api_response = api_instance.list_grants_route_v0_grants_get(resource, cursor=cursor, limit=limit, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**GrantList**](GrantList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_jobs_v0_projects_fld_id_jobs_get**
> object list_project_jobs_v0_projects_fld_id_jobs_get(fld_id, status=status, limit=limit, authorization=authorization)

List a project's jobs

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
    status = 'status_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List a project's jobs
        api_response = api_instance.list_project_jobs_v0_projects_fld_id_jobs_get(fld_id, status=status, limit=limit, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shares_route_v0_shares_get**
> ShareList list_shares_route_v0_shares_get(resource, cursor=cursor, limit=limit, authorization=authorization)

List live share links on a resource (requires can_manage)

**Cursor pagination:** when more results exist, the response carries `next_cursor`. Pass it back as `?cursor=<token>` to fetch the next page; `null` means the listing is complete. `limit` is clamped to [1, 100] (default 50), never rejected. The `resource` filter must be re-sent on every page — the cursor encodes only the keyset position.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    resource = 'resource_example' # str | art_*/fld_* id or a path
    cursor = 'cursor_example' # str |  (optional)
    limit = 56 # int |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List live share links on a resource (requires can_manage)
        api_response = api_instance.list_shares_route_v0_shares_get(resource, cursor=cursor, limit=limit, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**ShareList**](ShareList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trash_route_v0_drives_drive_id_trash_get**
> object list_trash_route_v0_drives_drive_id_trash_get(drive_id, authorization=authorization)

List the authenticated drive's trash

Returns soft-deleted artifacts on the drive plus the drive's own soft-delete state (if applicable). The path-param `drive_id` MUST match the authenticated drive.

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
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List the authenticated drive's trash
        api_response = api_instance.list_trash_route_v0_drives_drive_id_trash_get(drive_id, authorization=authorization)
        print("The response of DefaultApi->list_trash_route_v0_drives_drive_id_trash_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_trash_route_v0_drives_drive_id_trash_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_auth_login_get**
> object login_auth_login_get(return_to=return_to)

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
        api_response = api_instance.login_auth_login_get(return_to=return_to)
        print("The response of DefaultApi->login_auth_login_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->login_auth_login_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_to** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_auth_logout_post**
> object logout_auth_logout_post(csrf)

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
        api_response = api_instance.logout_auth_logout_post(csrf)
        print("The response of DefaultApi->logout_auth_logout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->logout_auth_logout_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketing_get**
> str marketing_get()

Marketing

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

    try:
        # Marketing
        api_response = api_instance.marketing_get()
        print("The response of DefaultApi->marketing_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketing_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_browse_marketplace_get**
> str marketplace_browse_marketplace_get()

Marketplace Browse

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

    try:
        # Marketplace Browse
        api_response = api_instance.marketplace_browse_marketplace_get()
        print("The response of DefaultApi->marketplace_browse_marketplace_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_browse_marketplace_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_detail_marketplace_slug_get**
> str marketplace_detail_marketplace_slug_get(slug)

Marketplace Detail

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
    slug = 'slug_example' # str | 

    try:
        # Marketplace Detail
        api_response = api_instance.marketplace_detail_marketplace_slug_get(slug)
        print("The response of DefaultApi->marketplace_detail_marketplace_slug_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->marketplace_detail_marketplace_slug_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_usage_v0_drives_me_usage_get**
> object me_usage_v0_drives_me_usage_get(authorization=authorization)

Current-period usage + caps for the authenticated drive

Unified view of every metered dimension: storage (snapshot), writes (current hour), indexing ops + retrieval queries (current calendar month UTC). Each row carries `used` and `limit`; `limit: 0` means unlimited (the v0 free-tier default for the two monthly counters). Reads are de-throttled — there is no hourly read budget; the monthly read count appears under `ops_this_month.reads`.

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
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Current-period usage + caps for the authenticated drive
        api_response = api_instance.me_usage_v0_drives_me_usage_get(authorization=authorization)
        print("The response of DefaultApi->me_usage_v0_drives_me_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->me_usage_v0_drives_me_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_v0_drives_me_get**
> object me_v0_drives_me_get(authorization=authorization)

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
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Me
        api_response = api_instance.me_v0_drives_me_get(authorization=authorization)
        print("The response of DefaultApi->me_v0_drives_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->me_v0_drives_me_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_artifact_route_v0_artifacts_art_id_move_post**
> ArtifactOut move_artifact_route_v0_artifacts_art_id_move_post(art_id, artifact_move_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

Rename / move an artifact to a new path

Canonical artifact move/rename, keyed by the stable `art_…` ID (the artifact analogue of `POST /v0/folders/{fld_id}/move`). Moves the artifact to a new `path` on the same drive; ID, version history, source refs, labels, metadata, and the underlying CAS blob are all preserved — only `path` and `updated_at` change, and the move does NOT bump `version_number`.

The row UPDATE and the emitted `artifact.renamed` event commit in a SINGLE transaction — a failure leaves the artifact fully unchanged.

Returns 409 PATH_CONFLICT if the target `path` is already taken; 404 ARTIFACT_NOT_FOUND for an unknown id; 403 WIKI_RESERVED for a `_wiki/` / `_compiled/` target. Honors `If-Match` (→ 412 PRECONDITION_FAILED). Use `X-AgentDrive-Actor` to attach attribution to the emitted `artifact.renamed` event.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str | 
    artifact_move_in = agentdrive_sdk.ArtifactMoveIn() # ArtifactMoveIn | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Rename / move an artifact to a new path
        api_response = api_instance.move_artifact_route_v0_artifacts_art_id_move_post(art_id, artifact_move_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder_by_id_v0_folders_fld_id_move_post**
> FolderOut move_folder_by_id_v0_folders_fld_id_move_post(fld_id, folder_move_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

Rename / move a folder by stable ID (cascade descendants)

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str | 
    folder_move_in = agentdrive_sdk.FolderMoveIn() # FolderMoveIn | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Rename / move a folder by stable ID (cascade descendants)
        api_response = api_instance.move_folder_by_id_v0_folders_fld_id_move_post(fld_id, folder_move_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder_by_path_v0_folders_path_move_post**
> FolderOut move_folder_by_path_v0_folders_path_move_post(path, folder_move_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

Rename / move a folder (cascade-update descendants)

Move the folder identified by URL path to the body's `path`. All descendant folders + artifacts are path-prefix-updated in the same transaction. The folder's `fld_*` ID stays stable.

Returns 409 `FOLDER_PATH_CONFLICT` if the destination prefix collides with a live folder or artifact path.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str | 
    folder_move_in = agentdrive_sdk.FolderMoveIn() # FolderMoveIn | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Rename / move a folder (cascade-update descendants)
        api_response = api_instance.move_folder_by_path_v0_folders_path_move_post(path, folder_move_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_disconnect_web_oauth_disconnect_post**
> object oauth_disconnect_web_oauth_disconnect_post(chain_id, csrf)

Oauth Disconnect

Disconnect one MCP client: revoke its whole rotation chain
(mcp-oauth-design §4.8). Ownership is checked against the chain's
user_id — the form value is attacker-controllable.

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
    chain_id = 'chain_id_example' # str | 
    csrf = 'csrf_example' # str | 

    try:
        # Oauth Disconnect
        api_response = api_instance.oauth_disconnect_web_oauth_disconnect_post(chain_id, csrf)
        print("The response of DefaultApi->oauth_disconnect_web_oauth_disconnect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->oauth_disconnect_web_oauth_disconnect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**|  | 
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_artifact_route_v0_artifacts_art_id_patch**
> ArtifactOut patch_artifact_route_v0_artifacts_art_id_patch(art_id, artifact_patch_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str | 
    artifact_patch_in = agentdrive_sdk.ArtifactPatchIn() # ArtifactPatchIn | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Edit artifact metadata (labels / metadata / source)
        api_response = api_instance.patch_artifact_route_v0_artifacts_art_id_patch(art_id, artifact_patch_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_folder_by_id_v0_folders_fld_id_patch**
> FolderOut patch_folder_by_id_v0_folders_fld_id_patch(fld_id, folder_patch_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

Update folder metadata by stable ID

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str | 
    folder_patch_in = agentdrive_sdk.FolderPatchIn() # FolderPatchIn | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Update folder metadata by stable ID
        api_response = api_instance.patch_folder_by_id_v0_folders_fld_id_patch(fld_id, folder_patch_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_folder_by_path_v0_folders_path_patch**
> FolderOut patch_folder_by_path_v0_folders_path_patch(path, folder_patch_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

Update folder metadata by path

Partial update — field absence leaves the value unchanged; explicit `null` clears the field. Use the by-id endpoint (slice 2) when you need stable addressing across renames.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    path = 'path_example' # str | 
    folder_patch_in = agentdrive_sdk.FolderPatchIn() # FolderPatchIn | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Update folder metadata by path
        api_response = api_instance.patch_folder_by_path_v0_folders_path_patch(path, folder_patch_in, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_grant_route_v0_grants_grn_id_patch**
> GrantOut patch_grant_route_v0_grants_grn_id_patch(grn_id, grant_patch_in, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)

Update a grant's role and/or expiry (requires can_manage)

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    grn_id = 'grn_id_example' # str | 
    grant_patch_in = agentdrive_sdk.GrantPatchIn() # GrantPatchIn | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Update a grant's role and/or expiry (requires can_manage)
        api_response = api_instance.patch_grant_route_v0_grants_grn_id_patch(grn_id, grant_patch_in, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_describe_v0_query_describe_post**
> object post_describe_v0_query_describe_post(describe_in, authorization=authorization)

Describe a dataset's column schema

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.describe_in import DescribeIn
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
    describe_in = agentdrive_sdk.DescribeIn() # DescribeIn | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Describe a dataset's column schema
        api_response = api_instance.post_describe_v0_query_describe_post(describe_in, authorization=authorization)
        print("The response of DefaultApi->post_describe_v0_query_describe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_describe_v0_query_describe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describe_in** | [**DescribeIn**](DescribeIn.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feedback_v0_feedback_post**
> object post_feedback_v0_feedback_post(authorization=authorization)

Post Feedback

File feedback. Body: `{kind, title, body, contact?,
attachments?: [art_id, ...]}` — attachments are snapshotted from
this drive's artifacts at submit time.

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
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Post Feedback
        api_response = api_instance.post_feedback_v0_feedback_post(authorization=authorization)
        print("The response of DefaultApi->post_feedback_v0_feedback_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_feedback_v0_feedback_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lookup_values_v0_query_lookup_values_post**
> object post_lookup_values_v0_query_lookup_values_post(lookup_values_in, authorization=authorization)

List distinct values of a dataset column

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.lookup_values_in import LookupValuesIn
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
    lookup_values_in = agentdrive_sdk.LookupValuesIn() # LookupValuesIn | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List distinct values of a dataset column
        api_response = api_instance.post_lookup_values_v0_query_lookup_values_post(lookup_values_in, authorization=authorization)
        print("The response of DefaultApi->post_lookup_values_v0_query_lookup_values_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_lookup_values_v0_query_lookup_values_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookup_values_in** | [**LookupValuesIn**](LookupValuesIn.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_query_v0_query_post**
> object post_query_v0_query_post(query_in, authorization=authorization)

Run a read-only SQL query over authorized datasets

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.query_in import QueryIn
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
    query_in = agentdrive_sdk.QueryIn() # QueryIn | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Run a read-only SQL query over authorized datasets
        api_response = api_instance.post_query_v0_query_post(query_in, authorization=authorization)
        print("The response of DefaultApi->post_query_v0_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_query_v0_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_in** | [**QueryIn**](QueryIn.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **privacy_page_privacy_get**
> str privacy_page_privacy_get()

Privacy Page

Public privacy & data-handling disclosure. Linked from the marketing
footer and the per-drive privacy settings card. Public — same disclosure
for every visitor; no per-drive personalization.

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

    try:
        # Privacy Page
        api_response = api_instance.privacy_page_privacy_get()
        print("The response of DefaultApi->privacy_page_privacy_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->privacy_page_privacy_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_preview_page_f_fld_id_preview_get**
> str project_preview_page_f_fld_id_preview_get(fld_id)

Project Preview Page

Live PDF preview for a project folder (latex-live-preview-design.md).

URL mirrors the folder permalink (`/f/{fld_id}` → dashboard;
`/f/{fld_id}/preview` → live preview) and the editor (`/a/{art_id}/edit`).
Owner-only focused viewer: the page polls `/web/projects/{fld_id}/preview`
and re-renders the compiled PDF in place (PDF.js) as the agent recompiles.
Anonymous / non-owner → bounce through login with this URL as return_to.
The page renders an empty shell; preview.js owns all behavior.

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
        # Project Preview Page
        api_response = api_instance.project_preview_page_f_fld_id_preview_get(fld_id)
        print("The response of DefaultApi->project_preview_page_f_fld_id_preview_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->project_preview_page_f_fld_id_preview_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publisher_profile_publishers_handle_get**
> str publisher_profile_publishers_handle_get(handle)

Publisher Profile

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
    handle = 'handle_example' # str | 

    try:
        # Publisher Profile
        api_response = api_instance.publisher_profile_publishers_handle_get(handle)
        print("The response of DefaultApi->publisher_profile_publishers_handle_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->publisher_profile_publishers_handle_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_artifact_v0_artifacts_path_put**
> ArtifactOut put_artifact_v0_artifacts_path_put(path, content_type=content_type, x_agentdrive_labels=x_agentdrive_labels, x_agentdrive_metadata=x_agentdrive_metadata, x_agentdrive_source=x_agentdrive_source, x_agentdrive_actor=x_agentdrive_actor, x_agentdrive_change_summary=x_agentdrive_change_summary, x_agentdrive_checksum=x_agentdrive_checksum, content_md5=content_md5, if_match=if_match, if_none_match=if_none_match, authorization=authorization)

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
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Upload (or overwrite) an artifact
        api_response = api_instance.put_artifact_v0_artifacts_path_put(path, content_type=content_type, x_agentdrive_labels=x_agentdrive_labels, x_agentdrive_metadata=x_agentdrive_metadata, x_agentdrive_source=x_agentdrive_source, x_agentdrive_actor=x_agentdrive_actor, x_agentdrive_change_summary=x_agentdrive_change_summary, x_agentdrive_checksum=x_agentdrive_checksum, content_md5=content_md5, if_match=if_match, if_none_match=if_none_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_v0_projects_fld_id_put**
> object put_project_v0_projects_fld_id_put(fld_id, project_config_in, authorization=authorization)

Set a project's compile config (entrypoint/engine/auto_compile)

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.project_config_in import ProjectConfigIn
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
    project_config_in = agentdrive_sdk.ProjectConfigIn() # ProjectConfigIn | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Set a project's compile config (entrypoint/engine/auto_compile)
        api_response = api_instance.put_project_v0_projects_fld_id_put(fld_id, project_config_in, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recovery_new_account_auth_recovery_new_account_post**
> object recovery_new_account_auth_recovery_new_account_post(csrf, claim=claim)

Recovery New Account

Start fresh under the same identity.

Provisions a new user / org / drive; the soft-deleted record stays
in trash until garbage-collected. Lands on /welcome so the user sees
the freshly-minted API key once.

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
    claim = 'bind' # str |  (optional) (default to 'bind')

    try:
        # Recovery New Account
        api_response = api_instance.recovery_new_account_auth_recovery_new_account_post(csrf, claim=claim)
        print("The response of DefaultApi->recovery_new_account_auth_recovery_new_account_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->recovery_new_account_auth_recovery_new_account_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **str**|  | 
 **claim** | **str**|  | [optional] [default to &#39;bind&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recovery_new_account_expired_auth_recovery_new_account_expired_get**
> object recovery_new_account_expired_auth_recovery_new_account_expired_get()

Recovery New Account Expired

Friendly landing for the rare race where the soft-deleted row
has been hard-purged between callback and recovery-page render.
Clears the recovery cookie (only when one is present) and tells
the user to retry — fresh sign-in will JIT-provision cleanly
since no soft-deleted record blocks it any more.

Gated on `pending_recovery` so a normal signed-in user who
navigates here directly doesn't get their session wiped. Without
a pending payload there's nothing to expire; bounce home.

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

    try:
        # Recovery New Account Expired
        api_response = api_instance.recovery_new_account_expired_auth_recovery_new_account_expired_get()
        print("The response of DefaultApi->recovery_new_account_expired_auth_recovery_new_account_expired_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->recovery_new_account_expired_auth_recovery_new_account_expired_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recovery_page_auth_recovery_get**
> object recovery_page_auth_recovery_get()

Recovery Page

Show the recover-or-start-fresh decision. Requires a valid
`pending_recovery` payload — direct hits without one bounce to
/auth/login (the recovery state is only meaningful inside the
callback → recovery → resolve chain).

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

    try:
        # Recovery Page
        api_response = api_instance.recovery_page_auth_recovery_get()
        print("The response of DefaultApi->recovery_page_auth_recovery_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->recovery_page_auth_recovery_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recovery_restore_auth_recovery_restore_post**
> object recovery_restore_auth_recovery_restore_post(csrf)

Recovery Restore

Recover the soft-deleted account. Undelete cascade runs in
`onboarding.recover_account`; on success we set the normal
session and bounce to /dashboard. If the retention window has
lapsed between page-render and POST (the GC raced us), surface
the same "expired" redirect so the user lands somewhere
actionable.

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
        # Recovery Restore
        api_response = api_instance.recovery_restore_auth_recovery_restore_post(csrf)
        print("The response of DefaultApi->recovery_restore_auth_recovery_restore_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->recovery_restore_auth_recovery_restore_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_share_s_share_key_get**
> object redeem_share_s_share_key_get(share_key)

Redeem Share

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

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_share_with_password_s_share_key_post**
> object redeem_share_with_password_s_share_key_post(share_key, password=password)

Redeem Share With Password

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

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_member_web_web_members_target_user_id_remove_post**
> object remove_member_web_web_members_target_user_id_remove_post(target_user_id, csrf, organization_id=organization_id)

Remove Member Web

Remove a member (admin) or self-leave (any member). Soft-deletes the
member's owned drives in that workspace (workspaces-design §4.4). The
sole-admin-with-members case is blocked (promote-or-delete).

Org scoping: defaults to the session's active workspace. The "Your
workspaces" list passes an explicit `organization_id` so a user can
Leave a NON-active workspace too — authorized against THAT org's
standing (self-leave for any member there; admin to remove others).
A forged/non-member org id is a no-leak forbidden.

Auth: gates on `current_user` + per-org standing, NOT `current_drive`
(a driveless member of the target workspace must still be able to
leave it). Attribution uses the user's email.

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
    target_user_id = 'target_user_id_example' # str | 
    csrf = 'csrf_example' # str | 
    organization_id = '' # str |  (optional) (default to '')

    try:
        # Remove Member Web
        api_response = api_instance.remove_member_web_web_members_target_user_id_remove_post(target_user_id, csrf, organization_id=organization_id)
        print("The response of DefaultApi->remove_member_web_web_members_target_user_id_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->remove_member_web_web_members_target_user_id_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_user_id** | **str**|  | 
 **csrf** | **str**|  | 
 **organization_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_drive_web_web_drives_drive_id_rename_post**
> object rename_drive_web_web_drives_drive_id_rename_post(drive_id, name, csrf)

Rename Drive Web

Rename a drive the caller owns (workspaces-design §4.5).

Owner-only: `drives.get_owned_drive` returns None for a peer-owned /
forged / soft-deleted id, which we treat as a silent no-op (no-leak)
and bounce back to the dashboard.

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
    name = 'name_example' # str | 
    csrf = 'csrf_example' # str | 

    try:
        # Rename Drive Web
        api_response = api_instance.rename_drive_web_web_drives_drive_id_rename_post(drive_id, name, csrf)
        print("The response of DefaultApi->rename_drive_web_web_drives_drive_id_rename_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rename_drive_web_web_drives_drive_id_rename_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drive_id** | **str**|  | 
 **name** | **str**|  | 
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_workspace_web_web_workspaces_org_id_rename_post**
> object rename_workspace_web_web_workspaces_org_id_rename_post(org_id, name, csrf)

Rename Workspace Web

Rename a workspace the caller administers (workspaces-design §4.6).

Admin-gated against the PATH org (not just the session) so a stale cookie
can't redirect the rename. A non-admin / non-member is a no-leak no-op.

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
    org_id = 'org_id_example' # str | 
    name = 'name_example' # str | 
    csrf = 'csrf_example' # str | 

    try:
        # Rename Workspace Web
        api_response = api_instance.rename_workspace_web_web_workspaces_org_id_rename_post(org_id, name, csrf)
        print("The response of DefaultApi->rename_workspace_web_web_workspaces_org_id_rename_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rename_workspace_web_web_workspaces_org_id_rename_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **name** | **str**|  | 
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_invitation_web_web_invitations_invitation_id_resend_post**
> object resend_invitation_web_web_invitations_invitation_id_resend_post(invitation_id, csrf)

Resend Invitation Web

Admin re-mints + re-emails a pending invite (workspaces-design §8).

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
    invitation_id = 'invitation_id_example' # str | 
    csrf = 'csrf_example' # str | 

    try:
        # Resend Invitation Web
        api_response = api_instance.resend_invitation_web_web_invitations_invitation_id_resend_post(invitation_id, csrf)
        print("The response of DefaultApi->resend_invitation_web_web_invitations_invitation_id_resend_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->resend_invitation_web_web_invitations_invitation_id_resend_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**|  | 
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_artifact_v0_artifacts_art_id_restore_post**
> ArtifactOut restore_artifact_v0_artifacts_art_id_restore_post(art_id, rename=rename, overwrite=overwrite, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

Restore a soft-deleted artifact

Clear `deleted_at` + `purge_at` on a soft-deleted artifact. Available only while the artifact is in trash (i.e. before the GC cleanup cron purges it). Returns 404 if the artifact is live or already hard-deleted; 409 PATH_CONFLICT if its path is now occupied by another live artifact. The 409 payload includes a `restore_options` block with `rename_to` and `force_overwrite` URLs the caller can follow to resolve the conflict — see deletion-design.md §5.4.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str | 
    rename = 'rename_example' # str | Restore at this path instead of the original. Soft-deletes the live occupant at the original path with audit `metadata.cause='restore_conflict_rename'`. Mutually exclusive with `overwrite`. (optional)
    overwrite = False # bool | Soft-delete the live occupant at the original path and restore there. Audit `metadata.cause='restore_conflict_overwrite'`. Mutually exclusive with `rename`. (optional) (default to False)
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Restore a soft-deleted artifact
        api_response = api_instance.restore_artifact_v0_artifacts_art_id_restore_post(art_id, rename=rename, overwrite=overwrite, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_artifact_version_v0_artifacts_art_id_versions_version_number_restore_post**
> ArtifactOut restore_artifact_version_v0_artifacts_art_id_versions_version_number_restore_post(art_id, version_number, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

Restore a previous version as a new head version

Roll the artifact forward to the content of version `version_number` by creating a **new head version** with identical bytes. History is preserved — this never rewrites or deletes past versions. The prior version's content-addressed blob is reused, so no bytes are re-uploaded. A change summary of `Restored version N` is recorded on the new version; `X-AgentDrive-Actor` attributes it.

Restoring a version whose content already matches the current head (including the head itself) is a **no-op**: it returns the current artifact unchanged, with no new version created.

Honors `If-Match` on the current head (roll forward only if the head is unchanged → 412 PRECONDITION_FAILED).

Errors: `404 ARTIFACT_NOT_FOUND`, `404 VERSION_NOT_FOUND`, and `410 VERSION_PRUNED` when the version existed but its bytes were retained out of existence.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    art_id = 'art_id_example' # str | 
    version_number = 56 # int | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Restore a previous version as a new head version
        api_response = api_instance.restore_artifact_version_v0_artifacts_art_id_versions_version_number_restore_post(art_id, version_number, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_drive_route_v0_drives_drive_id_restore_post**
> object restore_drive_route_v0_drives_drive_id_restore_post(drive_id, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

Restore a soft-deleted drive

Clear `deleted_at` + `purge_at` on a soft-deleted drive. Soft-deleted child artifacts get their retention window rebased to the drive-restore moment (see deletion-design.md §5.2). Available only while the drive is in trash. Returns 404 if the drive is live or already hard-deleted.

**Optimistic concurrency:** send `If-Match` with the trashed drive's composite ETag (`"<drv_id>.0.<metageneration>"`, e.g. from the delete response's `ETag` header) to make the restore conditional — a stale token returns 412 PRECONDITION_FAILED. A restore WITHOUT an `If-Match` precondition is last-writer-wins.

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
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Restore a soft-deleted drive
        api_response = api_instance.restore_drive_route_v0_drives_drive_id_restore_post(drive_id, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_folder_by_id_v0_folders_fld_id_restore_post**
> FolderRestoreOut restore_folder_by_id_v0_folders_fld_id_restore_post(fld_id, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)

Restore a soft-deleted folder (cascade)

Mirrors `POST /v0/artifacts/{art_id}/restore` for folders: clear `deleted_at` + `purge_at` on a soft-deleted folder AND exactly the descendants soft-deleted in the same cascade (descendants trashed separately keep their trash state; restore those individually — the per-artifact restore remains for cherry-picking). Available only while the folder is in trash; returns 404 if it is live or already hard-purged.

Returns 409 `PATH_CONFLICT` when a live folder/artifact now occupies a path this restore would reinstate (`colliding_path` + `kind` identify it). Unlike artifact restore there are NO `rename`/`overwrite` escape hatches — the whole cascade aborts; free the colliding path (or cherry-pick artifacts) and retry.

`If-Match` (the trashed folder's composite ETag) makes the restore conditional → 412 PRECONDITION_FAILED on a stale token; omitted, the restore is last-writer-wins.

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    fld_id = 'fld_id_example' # str | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    if_match = 'if_match_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Restore a soft-deleted folder (cascade)
        api_response = api_instance.restore_folder_by_id_v0_folders_fld_id_restore_post(fld_id, x_agentdrive_actor=x_agentdrive_actor, if_match=if_match, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**FolderRestoreOut**](FolderRestoreOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_grant_web_share_rid_grant_grn_id_revoke_post**
> object revoke_grant_web_share_rid_grant_grn_id_revoke_post(rid, grn_id, x_csrf_token=x_csrf_token)

Revoke Grant

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
    rid = 'rid_example' # str | 
    grn_id = 'grn_id_example' # str | 
    x_csrf_token = 'x_csrf_token_example' # str |  (optional)

    try:
        # Revoke Grant
        api_response = api_instance.revoke_grant_web_share_rid_grant_grn_id_revoke_post(rid, grn_id, x_csrf_token=x_csrf_token)
        print("The response of DefaultApi->revoke_grant_web_share_rid_grant_grn_id_revoke_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->revoke_grant_web_share_rid_grant_grn_id_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**|  | 
 **grn_id** | **str**|  | 
 **x_csrf_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_invitation_web_web_invitations_invitation_id_revoke_post**
> object revoke_invitation_web_web_invitations_invitation_id_revoke_post(invitation_id, csrf)

Revoke Invitation Web

Admin revokes a pending invite (org-scoped, no-leak).

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
    invitation_id = 'invitation_id_example' # str | 
    csrf = 'csrf_example' # str | 

    try:
        # Revoke Invitation Web
        api_response = api_instance.revoke_invitation_web_web_invitations_invitation_id_revoke_post(invitation_id, csrf)
        print("The response of DefaultApi->revoke_invitation_web_web_invitations_invitation_id_revoke_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->revoke_invitation_web_web_invitations_invitation_id_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**|  | 
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_key_web_keys_revoke_post**
> object revoke_key_web_keys_revoke_post(key_id, csrf)

Revoke Key

Revoke one of the active drive's `ad_live_` keys.

Management gate (workspaces-v2 §4.4): revoking a shared drive's key is
admin-for-team / owner-for-personal — a mere member must not revoke a key
out from under the team. `drive_keys.revoke` is additionally scoped by
drive_id, so the form's `key_id` can't reach another drive's key.

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
    key_id = 'key_id_example' # str | 
    csrf = 'csrf_example' # str | 

    try:
        # Revoke Key
        api_response = api_instance.revoke_key_web_keys_revoke_post(key_id, csrf)
        print("The response of DefaultApi->revoke_key_web_keys_revoke_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->revoke_key_web_keys_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_link_web_share_rid_link_shr_id_revoke_post**
> object revoke_link_web_share_rid_link_shr_id_revoke_post(rid, shr_id, x_csrf_token=x_csrf_token)

Revoke Link

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
    rid = 'rid_example' # str | 
    shr_id = 'shr_id_example' # str | 
    x_csrf_token = 'x_csrf_token_example' # str |  (optional)

    try:
        # Revoke Link
        api_response = api_instance.revoke_link_web_share_rid_link_shr_id_revoke_post(rid, shr_id, x_csrf_token=x_csrf_token)
        print("The response of DefaultApi->revoke_link_web_share_rid_link_shr_id_revoke_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->revoke_link_web_share_rid_link_shr_id_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**|  | 
 **shr_id** | **str**|  | 
 **x_csrf_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_user_token_web_tokens_revoke_post**
> object revoke_user_token_web_tokens_revoke_post(token_id, csrf)

Revoke User Token

Revoke one of the caller's `ad_user_` tokens.

Ownership is enforced inside `user_tokens.revoke(token_id, user_id)`
— the form's `token_id` is attacker-controllable, so we never revoke
by id alone. A non-matching id is a silent no-op (same redirect).

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
    token_id = 'token_id_example' # str | 
    csrf = 'csrf_example' # str | 

    try:
        # Revoke User Token
        api_response = api_instance.revoke_user_token_web_tokens_revoke_post(token_id, csrf)
        print("The response of DefaultApi->revoke_user_token_web_tokens_revoke_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->revoke_user_token_web_tokens_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**|  | 
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_share_route_v0_shares_shr_id_rotate_post**
> ShareMintOut rotate_share_route_v0_shares_shr_id_rotate_post(shr_id, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)

Revoke + reissue a share link's key (requires can_share)

### Example


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


# Enter a context with an instance of the API client
with agentdrive_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentdrive_sdk.DefaultApi(api_client)
    shr_id = 'shr_id_example' # str | 
    x_agentdrive_actor = 'x_agentdrive_actor_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Revoke + reissue a share link's key (requires can_share)
        api_response = api_instance.rotate_share_route_v0_shares_shr_id_rotate_post(shr_id, x_agentdrive_actor=x_agentdrive_actor, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**ShareMintOut**](ShareMintOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_v0_search_get**
> SearchPage search_v0_search_get(q, label=label, file_type=file_type, prefix=prefix, updated_after=updated_after, updated_before=updated_before, limit=limit, authorization=authorization)

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
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Full-text search over artifacts in the drive
        api_response = api_instance.search_v0_search_get(q, label=label, file_type=file_type, prefix=prefix, updated_after=updated_after, updated_before=updated_before, limit=limit, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**SearchPage**](SearchPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_member_role_web_web_members_target_user_id_role_post**
> object set_member_role_web_web_members_target_user_id_role_post(target_user_id, role, csrf)

Set Member Role Web

Admin promotes/demotes a member. Last-admin demote is blocked
(workspaces-design §4.4).

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
    target_user_id = 'target_user_id_example' # str | 
    role = 'role_example' # str | 
    csrf = 'csrf_example' # str | 

    try:
        # Set Member Role Web
        api_response = api_instance.set_member_role_web_web_members_target_user_id_role_post(target_user_id, role, csrf)
        print("The response of DefaultApi->set_member_role_web_web_members_target_user_id_role_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_member_role_web_web_members_target_user_id_role_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_user_id** | **str**|  | 
 **role** | **str**|  | 
 **csrf** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_public_web_share_rid_public_post**
> object set_public_web_share_rid_public_post(rid, public_in, x_csrf_token=x_csrf_token)

Set Public

Toggle world-readable: create (idempotent) or revoke the `anyone:viewer`
grant. On a folder this cascades to the subtree (the response carries the
blast-radius the UI confirmed).

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.public_in import PublicIn
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
    rid = 'rid_example' # str | 
    public_in = agentdrive_sdk.PublicIn() # PublicIn | 
    x_csrf_token = 'x_csrf_token_example' # str |  (optional)

    try:
        # Set Public
        api_response = api_instance.set_public_web_share_rid_public_post(rid, public_in, x_csrf_token=x_csrf_token)
        print("The response of DefaultApi->set_public_web_share_rid_public_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_public_web_share_rid_public_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**|  | 
 **public_in** | [**PublicIn**](PublicIn.md)|  | 
 **x_csrf_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_seal_web_share_rid_seal_post**
> object set_seal_web_share_rid_seal_post(rid, seal_in, x_csrf_token=x_csrf_token)

Set Seal

Set the limited-access seal (`inherit_grants`). `false` makes the
resource ignore grants inherited from ancestor folders (§4.6/§4.11).
Gated on `can_manage` (changing who can reach the resource).

### Example


```python
import agentdrive_sdk
from agentdrive_sdk.models.seal_in import SealIn
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
    rid = 'rid_example' # str | 
    seal_in = agentdrive_sdk.SealIn() # SealIn | 
    x_csrf_token = 'x_csrf_token_example' # str |  (optional)

    try:
        # Set Seal
        api_response = api_instance.set_seal_web_share_rid_seal_post(rid, seal_in, x_csrf_token=x_csrf_token)
        print("The response of DefaultApi->set_seal_web_share_rid_seal_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_seal_web_share_rid_seal_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**|  | 
 **seal_in** | [**SealIn**](SealIn.md)|  | 
 **x_csrf_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_account_settings_get**
> str settings_account_settings_get()

Settings Account

Default settings landing — Account info + Usage + Danger zone.

Usage folded in here (was a standalone `/settings/usage` tab): the
same meter data is fetched via `_usage_context` and rendered as a
section on this page.

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

    try:
        # Settings Account
        api_response = api_instance.settings_account_settings_get()
        print("The response of DefaultApi->settings_account_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->settings_account_settings_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_api_keys_settings_api_keys_get**
> str settings_api_keys_settings_api_keys_get()

Settings Api Keys

API key tab. Also where `reveal_key` is rendered once after a key is
minted; the reveal is consumed (removed from session) on first read.

Surfaces two credential classes (workspaces-design §5.6):
  * the drive's `ad_live_` per-drive keys (`drive_keys.list_for_drive`) —
    a drive may hold several, each created/revoked individually.
  * the user's `ad_user_` identity tokens (`user_tokens`, mint/list/
    revoke). Minting reveals the raw token once via the same
    `reveal_key`-in-session mechanism as the drive keys.

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

    try:
        # Settings Api Keys
        api_response = api_instance.settings_api_keys_settings_api_keys_get()
        print("The response of DefaultApi->settings_api_keys_settings_api_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->settings_api_keys_settings_api_keys_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_quickstart_settings_quickstart_get**
> str settings_quickstart_settings_quickstart_get()

Settings Quickstart

Quickstart tab — the single connect-and-use surface, consolidating the
former Skill + MCP-setup tabs. Hero is the copy-paste bootstrap prompt
(for terminal-less agents); the `claude mcp add` one-liner is second (for
Claude Code). Connected clients fold into a collapsible section below.

The full tool reference lives at `/agentdrive.md` (rendered from
`skills/SKILL.md`); the bootstrap prompt points the agent there rather
than inlining it here, keeping the tab drift-free.

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

    try:
        # Settings Quickstart
        api_response = api_instance.settings_quickstart_settings_quickstart_get()
        print("The response of DefaultApi->settings_quickstart_settings_quickstart_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->settings_quickstart_settings_quickstart_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_workspace_settings_workspace_get**
> str settings_workspace_settings_workspace_get()

Settings Workspace

Standalone workspace settings page (decision O4): members list +
pending invites + invite form + role change + remove.

Admin-gated for the management actions; a member sees the roster but no
management controls (the template hides them unless `is_admin`). The
active workspace is the session's `active_organization_id`.

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

    try:
        # Settings Workspace
        api_response = api_instance.settings_workspace_settings_workspace_get()
        print("The response of DefaultApi->settings_workspace_settings_workspace_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->settings_workspace_settings_workspace_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shared_files_shared_get**
> str shared_files_shared_get()

Shared Files

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

    try:
        # Shared Files
        api_response = api_instance.shared_files_shared_get()
        print("The response of DefaultApi->shared_files_shared_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->shared_files_shared_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_drive_web_switch_post**
> object switch_drive_web_switch_post(csrf, drive_id=drive_id, organization_id=organization_id)

Switch Drive

Switch the active workspace (and drive) — workspace-first
(workspaces-design §4.3).

Two modes, mirroring the Linear/Slack/GitHub "switch by workspace"
model:

  * **Workspace switch** (`organization_id`): membership-check the
    target org for the user; on success set it active and pin the
    user's OLDEST owned live drive there (deterministic), or None if
    they own none — in which case the dashboard's
    `resolve_driveless_member` renders the "create your first drive"
    empty state for that workspace.
  * **Drive switch** (`drive_id`): validate the user OWNS the posted
    drive (and is a live member of its workspace) via
    `drives_svc.user_owns_drive`, then set both org + drive active.
    Lets a multi-drive workspace pick a specific drive. If BOTH are
    posted, the explicit `drive_id` wins (subject to its own check).

Both forms are no-leak: a forged / peer-owned / non-member target
fails its check and is treated identically to "no such target"
(303 back to /dashboard without mutating the session — no leak, no
error oracle).

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
    drive_id = '' # str |  (optional) (default to '')
    organization_id = '' # str |  (optional) (default to '')

    try:
        # Switch Drive
        api_response = api_instance.switch_drive_web_switch_post(csrf, drive_id=drive_id, organization_id=organization_id)
        print("The response of DefaultApi->switch_drive_web_switch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->switch_drive_web_switch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **str**|  | 
 **drive_id** | **str**|  | [optional] [default to &#39;&#39;]
 **organization_id** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_page_terms_get**
> str terms_page_terms_get()

Terms Page

Public beta terms of service. Linked from the marketing footer.

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

    try:
        # Terms Page
        api_response = api_instance.terms_page_terms_get()
        print("The response of DefaultApi->terms_page_terms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->terms_page_terms_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_indexing_web_account_indexing_post**
> object toggle_indexing_web_account_indexing_post(csrf, enabled=enabled)

Toggle Indexing

Flip the per-drive `indexing_enabled` flag (privacy opt-out for
sending file content to Gemini). Checkbox semantics: a checked HTML
`<input type=checkbox name=enabled value=on>` POSTs `enabled=on`;
unchecked posts NO `enabled` field at all, which Form(default='')
surfaces as the empty string.

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
    enabled = '' # str |  (optional) (default to '')

    try:
        # Toggle Indexing
        api_response = api_instance.toggle_indexing_web_account_indexing_post(csrf, enabled=enabled)
        print("The response of DefaultApi->toggle_indexing_web_account_indexing_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->toggle_indexing_web_account_indexing_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **str**|  | 
 **enabled** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trash_web_trash_get**
> str trash_web_trash_get()

Trash

Drive-wide Trash: soft-deleted artifacts + folder roots, each with
a Restore action. Restore wiring lives in web/file_ops.py.

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

    try:
        # Trash
        api_response = api_instance.trash_web_trash_get()
        print("The response of DefaultApi->trash_web_trash_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->trash_web_trash_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_artifact_head_a_art_id_head_get**
> object view_artifact_head_a_art_id_head_get(art_id)

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

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_artifact_version_v_art_id_version_get**
> object view_artifact_version_v_art_id_version_get(art_id, version, raw=raw, download=download)

View Artifact Version

Render version `version` of an artifact, read-only.

Authorization is byte-for-byte identical to viewing the artifact via
`/a/{art_id}`: the same drive-blind `can_read` gate runs, so a viewer
who can see the artifact can see its versions, and one who cannot gets
the identical sign-in-or-404 response (no existence leak). A pruned or
never-existed version renders a friendly unavailable state, never a 500.
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

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_file_drive_id_path_get**
> object view_file_drive_id_path_get(drive_id, path, raw=raw, download=download)

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

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_permalink_artifact_a_art_id_get**
> object view_permalink_artifact_a_art_id_get(art_id)

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
        api_response = api_instance.view_permalink_artifact_a_art_id_get(art_id)
        print("The response of DefaultApi->view_permalink_artifact_a_art_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->view_permalink_artifact_a_art_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_permalink_folder_f_fld_id_get**
> object view_permalink_folder_f_fld_id_get(fld_id)

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
        api_response = api_instance.view_permalink_folder_f_fld_id_get(fld_id)
        print("The response of DefaultApi->view_permalink_folder_f_fld_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->view_permalink_folder_f_fld_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_artifact_indexed_web_artifacts_indexed_get**
> object web_artifact_indexed_web_artifacts_indexed_get(path)

Web Artifact Indexed

Session-auth companion to `/v0/artifacts/{path}/meta` used by the
wiki-banner poller in the browser. The poller runs in any logged-in
owner's tab; the v0 endpoint requires Bearer auth and was therefore
dead for browser owners (the banner spinner never resolved).

Returns `{indexed_at, has_index}` so the poller can detect when the
extraction finishes and reload the page. 401 if not signed in (anon
viewer); 404 if the path doesn't exist in the caller's drive.

Rate limit is generous (120/min) because the banner polls every 5s and
a user might leave multiple tabs open. Per-IP keying so one abusive
client doesn't starve out concurrent legit polls from other users.

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
    path = 'path_example' # str | 

    try:
        # Web Artifact Indexed
        api_response = api_instance.web_artifact_indexed_web_artifacts_indexed_get(path)
        print("The response of DefaultApi->web_artifact_indexed_web_artifacts_indexed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_artifact_indexed_web_artifacts_indexed_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_copy_artifact_web_artifacts_copy_post**
> object web_copy_artifact_web_artifacts_copy_post(art_id, new_path, csrf, return_to=return_to)

Web Copy Artifact

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
    new_path = 'new_path_example' # str | 
    csrf = 'csrf_example' # str | 
    return_to = '/dashboard' # str |  (optional) (default to '/dashboard')

    try:
        # Web Copy Artifact
        api_response = api_instance.web_copy_artifact_web_artifacts_copy_post(art_id, new_path, csrf, return_to=return_to)
        print("The response of DefaultApi->web_copy_artifact_web_artifacts_copy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_copy_artifact_web_artifacts_copy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  | 
 **new_path** | **str**|  | 
 **csrf** | **str**|  | 
 **return_to** | **str**|  | [optional] [default to &#39;/dashboard&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_delete_artifact_op_web_artifacts_delete_post**
> object web_delete_artifact_op_web_artifacts_delete_post(path, csrf, return_to=return_to)

Web Delete Artifact Op

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
    path = 'path_example' # str | 
    csrf = 'csrf_example' # str | 
    return_to = '/dashboard' # str |  (optional) (default to '/dashboard')

    try:
        # Web Delete Artifact Op
        api_response = api_instance.web_delete_artifact_op_web_artifacts_delete_post(path, csrf, return_to=return_to)
        print("The response of DefaultApi->web_delete_artifact_op_web_artifacts_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_delete_artifact_op_web_artifacts_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **csrf** | **str**|  | 
 **return_to** | **str**|  | [optional] [default to &#39;/dashboard&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_delete_artifact_web_artifacts_path_delete**
> object web_delete_artifact_web_artifacts_path_delete(path, x_csrf_token=x_csrf_token)

Web Delete Artifact

Cookie-authed delete used by the editor's Discard button
(`/a/{art_id}/edit`): if the user isn't happy with a capture, they
delete it right there instead of round-tripping through the
dashboard. The bearer-authed `DELETE /v0/artifacts/{path}` won't
accept a cookie-only session, hence this `/web/...` alias — the
same split as the autosave PUT above.

Mirrors the v0 DELETE's guards: CSRF header (cross-site fetch
can't forge the token), write-quota consumption, and reserved
`_wiki/` namespace rejection. Soft-delete semantics are identical
too — the artifact lands in trash and is restorable until the GC
cron purges it at `purge_at`, so a misclick through the confirm
dialog is recoverable. `If-Match` is deliberately not supported:
the editor is the only intended caller and always deletes
whatever is current.

Note: `restore_url` in the response points at the bearer-authed
v0 endpoint, which this cookie-only caller can't hit — it's kept
for shape parity with the v0 DELETE and is informational here
(a future web trash UI would need a `/web/...` restore alias).

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
    path = 'path_example' # str | 
    x_csrf_token = 'x_csrf_token_example' # str |  (optional)

    try:
        # Web Delete Artifact
        api_response = api_instance.web_delete_artifact_web_artifacts_path_delete(path, x_csrf_token=x_csrf_token)
        print("The response of DefaultApi->web_delete_artifact_web_artifacts_path_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_delete_artifact_web_artifacts_path_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **x_csrf_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_delete_folder_web_folders_delete_post**
> object web_delete_folder_web_folders_delete_post(fld_id, csrf, recursive=recursive, return_to=return_to)

Web Delete Folder

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
    csrf = 'csrf_example' # str | 
    recursive = '' # str |  (optional) (default to '')
    return_to = '/dashboard' # str |  (optional) (default to '/dashboard')

    try:
        # Web Delete Folder
        api_response = api_instance.web_delete_folder_web_folders_delete_post(fld_id, csrf, recursive=recursive, return_to=return_to)
        print("The response of DefaultApi->web_delete_folder_web_folders_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_delete_folder_web_folders_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  | 
 **csrf** | **str**|  | 
 **recursive** | **str**|  | [optional] [default to &#39;&#39;]
 **return_to** | **str**|  | [optional] [default to &#39;/dashboard&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_move_folder_web_folders_move_post**
> object web_move_folder_web_folders_move_post(fld_id, new_path, csrf, return_to=return_to)

Web Move Folder

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
    new_path = 'new_path_example' # str | 
    csrf = 'csrf_example' # str | 
    return_to = '/dashboard' # str |  (optional) (default to '/dashboard')

    try:
        # Web Move Folder
        api_response = api_instance.web_move_folder_web_folders_move_post(fld_id, new_path, csrf, return_to=return_to)
        print("The response of DefaultApi->web_move_folder_web_folders_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_move_folder_web_folders_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  | 
 **new_path** | **str**|  | 
 **csrf** | **str**|  | 
 **return_to** | **str**|  | [optional] [default to &#39;/dashboard&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_new_folder_web_folders_new_post**
> object web_new_folder_web_folders_new_post(name, csrf, parent=parent, return_to=return_to)

Web New Folder

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
    name = 'name_example' # str | 
    csrf = 'csrf_example' # str | 
    parent = '' # str |  (optional) (default to '')
    return_to = '/dashboard' # str |  (optional) (default to '/dashboard')

    try:
        # Web New Folder
        api_response = api_instance.web_new_folder_web_folders_new_post(name, csrf, parent=parent, return_to=return_to)
        print("The response of DefaultApi->web_new_folder_web_folders_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_new_folder_web_folders_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **csrf** | **str**|  | 
 **parent** | **str**|  | [optional] [default to &#39;&#39;]
 **return_to** | **str**|  | [optional] [default to &#39;/dashboard&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_project_compile_web_projects_fld_id_compile_post**
> object web_project_compile_web_projects_fld_id_compile_post(fld_id, csrf, engine=engine, entrypoint=entrypoint)

Web Project Compile

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
    csrf = 'csrf_example' # str | 
    engine = '' # str |  (optional) (default to '')
    entrypoint = '' # str |  (optional) (default to '')

    try:
        # Web Project Compile
        api_response = api_instance.web_project_compile_web_projects_fld_id_compile_post(fld_id, csrf, engine=engine, entrypoint=entrypoint)
        print("The response of DefaultApi->web_project_compile_web_projects_fld_id_compile_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_project_compile_web_projects_fld_id_compile_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  | 
 **csrf** | **str**|  | 
 **engine** | **str**|  | [optional] [default to &#39;&#39;]
 **entrypoint** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_project_files_web_projects_fld_id_files_get**
> object web_project_files_web_projects_fld_id_files_get(fld_id)

Web Project Files

Cookie-authed file tree + read-only source manifest for the LaTeX
workspace (handoff §3). Same auth contract as the preview poll (401 /
404-not-403). Source bytes themselves stream from `/a/{art_id}?raw=1`
(owner session authorizes private files) — this endpoint only lists.

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
        # Web Project Files
        api_response = api_instance.web_project_files_web_projects_fld_id_files_get(fld_id)
        print("The response of DefaultApi->web_project_files_web_projects_fld_id_files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_project_files_web_projects_fld_id_files_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_project_preview_web_projects_fld_id_preview_get**
> object web_project_preview_web_projects_fld_id_preview_get(fld_id)

Web Project Preview

Session-auth poll for the live PDF preview page (latex-live-preview-
design.md §4.2). The browser uses the session cookie (the `/v0` jobs API
is Bearer-only), so this is the cookie-authed companion. Returns the
current compile status + the last successful PDF + diagnostics so the page
updates in place. 401 if not signed in; 404 (not 403) if the folder isn't
in the caller's drive, to avoid existence leakage.

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
        # Web Project Preview
        api_response = api_instance.web_project_preview_web_projects_fld_id_preview_get(fld_id)
        print("The response of DefaultApi->web_project_preview_web_projects_fld_id_preview_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_project_preview_web_projects_fld_id_preview_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_put_artifact_web_artifacts_path_put**
> object web_put_artifact_web_artifacts_path_put(path, x_csrf_token=x_csrf_token)

Web Put Artifact

Cookie-authed write of an image artifact. Used by the SnipIt web
editor (`/a/{art_id}/edit`) for autosave; the bearer-authed
`PUT /v0/artifacts/{path}` won't accept a cookie-only session.

Owner-only; the path is checked against the signed-in user's drive.
Accepts `image/*` (SnipIt editor autosave) and `application/pdf` (the
PDF viewer's annotation save) only — refuses everything else so the
editor can't smuggle markdown/HTML or anything else through this surface.
Mirrors every guard the v0 PUT enforces — write quota, reserved
`_wiki/` namespace rejection, per-tier max-bytes cap (both
`Content-Length` short-circuit and post-body length check) — so
a logged-in user can't bypass quota or write into the wiki by
routing autosaves through this endpoint instead of the v0 API.
CSRF is checked via the `X-CSRF-Token` header (see
`csrf.require_csrf_header`); the editor reads the token from the
`<meta name="csrf-token">` tag rendered into the edit page.
Rate-limited per-IP/user at the same cadence the editor's 1.5s
autosave can sustain without flagging abuse.

Cross-workspace (design §4.3): the editor page is reached by a stable-id
URL that may name a drive outside the session's active workspace, so the
write must target the RESOURCE's drive, not the active one. The editor
sends the resolved drive in an `X-Drive-Id` header; we authorize ownership
of THAT drive via `resolve_owned_drive` (it returns None for a forged /
unowned id → 401, never a write). Absent header ⇒ fall back to
`current_drive` (pre-fast-follow behavior; a cached old client still works,
only without the cross-workspace fix).

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
    path = 'path_example' # str | 
    x_csrf_token = 'x_csrf_token_example' # str |  (optional)

    try:
        # Web Put Artifact
        api_response = api_instance.web_put_artifact_web_artifacts_path_put(path, x_csrf_token=x_csrf_token)
        print("The response of DefaultApi->web_put_artifact_web_artifacts_path_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_put_artifact_web_artifacts_path_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **x_csrf_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_rename_artifact_web_artifacts_rename_post**
> object web_rename_artifact_web_artifacts_rename_post(art_id, new_path, csrf, return_to=return_to)

Web Rename Artifact

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
    new_path = 'new_path_example' # str | 
    csrf = 'csrf_example' # str | 
    return_to = '/dashboard' # str |  (optional) (default to '/dashboard')

    try:
        # Web Rename Artifact
        api_response = api_instance.web_rename_artifact_web_artifacts_rename_post(art_id, new_path, csrf, return_to=return_to)
        print("The response of DefaultApi->web_rename_artifact_web_artifacts_rename_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_rename_artifact_web_artifacts_rename_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  | 
 **new_path** | **str**|  | 
 **csrf** | **str**|  | 
 **return_to** | **str**|  | [optional] [default to &#39;/dashboard&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_restore_artifact_web_artifacts_restore_post**
> object web_restore_artifact_web_artifacts_restore_post(art_id, csrf, return_to=return_to)

Web Restore Artifact

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
    csrf = 'csrf_example' # str | 
    return_to = '/web/trash' # str |  (optional) (default to '/web/trash')

    try:
        # Web Restore Artifact
        api_response = api_instance.web_restore_artifact_web_artifacts_restore_post(art_id, csrf, return_to=return_to)
        print("The response of DefaultApi->web_restore_artifact_web_artifacts_restore_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_restore_artifact_web_artifacts_restore_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **art_id** | **str**|  | 
 **csrf** | **str**|  | 
 **return_to** | **str**|  | [optional] [default to &#39;/web/trash&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_restore_folder_web_folders_restore_post**
> object web_restore_folder_web_folders_restore_post(fld_id, csrf, return_to=return_to)

Web Restore Folder

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
    csrf = 'csrf_example' # str | 
    return_to = '/web/trash' # str |  (optional) (default to '/web/trash')

    try:
        # Web Restore Folder
        api_response = api_instance.web_restore_folder_web_folders_restore_post(fld_id, csrf, return_to=return_to)
        print("The response of DefaultApi->web_restore_folder_web_folders_restore_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_restore_folder_web_folders_restore_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fld_id** | **str**|  | 
 **csrf** | **str**|  | 
 **return_to** | **str**|  | [optional] [default to &#39;/web/trash&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_set_metadata_web_set_post**
> object web_set_metadata_web_set_post(target, csrf, description=description, return_to=return_to)

Web Set Metadata

Folder description edit (target = `fld_<id>`).

"Public/private" is no longer a folder/artifact flag — access is
expressed through grants (permission-sharing-design §4.4), so this
endpoint only edits folder descriptions. Artifact targets are
rejected; publishing an artifact is the dedicated grant/`publish`
flow, not a metadata toggle.

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
    target = 'target_example' # str | 
    csrf = 'csrf_example' # str | 
    description = '' # str |  (optional) (default to '')
    return_to = '/dashboard' # str |  (optional) (default to '/dashboard')

    try:
        # Web Set Metadata
        api_response = api_instance.web_set_metadata_web_set_post(target, csrf, description=description, return_to=return_to)
        print("The response of DefaultApi->web_set_metadata_web_set_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_set_metadata_web_set_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**|  | 
 **csrf** | **str**|  | 
 **description** | **str**|  | [optional] [default to &#39;&#39;]
 **return_to** | **str**|  | [optional] [default to &#39;/dashboard&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_upload_web_upload_post**
> object web_upload_web_upload_post(file, csrf, dest_dir=dest_dir, return_to=return_to)

Web Upload

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
    file = None # bytes | 
    csrf = 'csrf_example' # str | 
    dest_dir = '' # str |  (optional) (default to '')
    return_to = '/dashboard' # str |  (optional) (default to '/dashboard')

    try:
        # Web Upload
        api_response = api_instance.web_upload_web_upload_post(file, csrf, dest_dir=dest_dir, return_to=return_to)
        print("The response of DefaultApi->web_upload_web_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->web_upload_web_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**|  | 
 **csrf** | **str**|  | 
 **dest_dir** | **str**|  | [optional] [default to &#39;&#39;]
 **return_to** | **str**|  | [optional] [default to &#39;/dashboard&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_page_webhooks_get**
> str webhooks_page_webhooks_get()

Webhooks Page

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

    try:
        # Webhooks Page
        api_response = api_instance.webhooks_page_webhooks_get()
        print("The response of DefaultApi->webhooks_page_webhooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->webhooks_page_webhooks_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **welcome_welcome_get**
> str welcome_welcome_get()

Welcome

Show the three-step welcome screen and consume `reveal_key`.

Auth-required. If no key is in the session, redirect onward to
`/dashboard` (the user has already saved theirs, or is a
returning visitor who arrived here by typing the URL).

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

    try:
        # Welcome
        api_response = api_instance.welcome_welcome_get()
        print("The response of DefaultApi->welcome_welcome_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->welcome_welcome_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

