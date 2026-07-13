# \DefaultAPI

All URIs are relative to *https://api.agentdrive.run*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AbortUploadV0UploadsUploadIdDelete**](DefaultAPI.md#AbortUploadV0UploadsUploadIdDelete) | **Delete** /v0/uploads/{upload_id} | Abort a large (direct-to-GCS) upload session
[**AcceptInvitationInvitationsTokenGet**](DefaultAPI.md#AcceptInvitationInvitationsTokenGet) | **Get** /invitations/{token} | Accept Invitation
[**ActivityFeedActivityGet**](DefaultAPI.md#ActivityFeedActivityGet) | **Get** /activity | Activity Feed
[**AddGrantWebShareRidGrantPost**](DefaultAPI.md#AddGrantWebShareRidGrantPost) | **Post** /web/share/{rid}/grant | Add Grant
[**ArtifactDetailPreviewPreviewArtifactDetailGet**](DefaultAPI.md#ArtifactDetailPreviewPreviewArtifactDetailGet) | **Get** /preview/artifact-detail | Artifact Detail Preview
[**BeginUploadV0UploadsPost**](DefaultAPI.md#BeginUploadV0UploadsPost) | **Post** /v0/uploads | Begin a large (direct-to-GCS) upload
[**CallbackAuthCallbackGet**](DefaultAPI.md#CallbackAuthCallbackGet) | **Get** /auth/callback | Callback
[**CancelJobV0JobsJobIdCancelPost**](DefaultAPI.md#CancelJobV0JobsJobIdCancelPost) | **Post** /v0/jobs/{job_id}/cancel | Cancel a queued/running job
[**CollectionDetailCollectionsSlugGet**](DefaultAPI.md#CollectionDetailCollectionsSlugGet) | **Get** /collections/{slug} | Collection Detail
[**CommitUploadV0UploadsUploadIdCommitPost**](DefaultAPI.md#CommitUploadV0UploadsUploadIdCommitPost) | **Post** /v0/uploads/{upload_id}/commit | Commit a large (direct-to-GCS) upload
[**ConnectorsPageConnectorsGet**](DefaultAPI.md#ConnectorsPageConnectorsGet) | **Get** /connectors | Connectors Page
[**CopyArtifactRouteV0ArtifactsArtIdCopyPost**](DefaultAPI.md#CopyArtifactRouteV0ArtifactsArtIdCopyPost) | **Post** /v0/artifacts/{art_id}/copy | Duplicate an artifact to a new path (CAS-shared, new ID)
[**CopyFolderByIdV0FoldersFldIdCopyPost**](DefaultAPI.md#CopyFolderByIdV0FoldersFldIdCopyPost) | **Post** /v0/folders/{fld_id}/copy | Duplicate a folder subtree to a new path (CAS-shared, new IDs)
[**CreateDriveKeyWebWebDrivesDriveIdKeysCreatePost**](DefaultAPI.md#CreateDriveKeyWebWebDrivesDriveIdKeysCreatePost) | **Post** /web/drives/{drive_id}/keys/create | Create Drive Key Web
[**CreateDriveWebWebDrivesPost**](DefaultAPI.md#CreateDriveWebWebDrivesPost) | **Post** /web/drives | Create Drive Web
[**CreateFolderByPathV0FoldersPathPut**](DefaultAPI.md#CreateFolderByPathV0FoldersPathPut) | **Put** /v0/folders/{path} | Create a folder (idempotent)
[**CreateGrantRouteV0GrantsPost**](DefaultAPI.md#CreateGrantRouteV0GrantsPost) | **Post** /v0/grants | Create (or fetch) a per-principal grant on a resource
[**CreateKeyWebKeysCreatePost**](DefaultAPI.md#CreateKeyWebKeysCreatePost) | **Post** /web/keys/create | Create Key
[**CreateLinkWebShareRidLinkPost**](DefaultAPI.md#CreateLinkWebShareRidLinkPost) | **Post** /web/share/{rid}/link | Create Link
[**CreateShareRouteV0SharesPost**](DefaultAPI.md#CreateShareRouteV0SharesPost) | **Post** /v0/shares | Mint a share link (returns the share_key once)
[**CreateUserTokenWebTokensCreatePost**](DefaultAPI.md#CreateUserTokenWebTokensCreatePost) | **Post** /web/tokens/create | Create User Token
[**CreateWorkspaceWebWebWorkspacesPost**](DefaultAPI.md#CreateWorkspaceWebWebWorkspacesPost) | **Post** /web/workspaces | Create Workspace Web
[**DangerZoneOldDashboardDangerGet**](DefaultAPI.md#DangerZoneOldDashboardDangerGet) | **Get** /dashboard/danger | Danger Zone Old
[**DangerZoneSettingsDangerGet**](DefaultAPI.md#DangerZoneSettingsDangerGet) | **Get** /settings/danger | Danger Zone
[**DashboardDashboardGet**](DefaultAPI.md#DashboardDashboardGet) | **Get** /dashboard | Dashboard
[**DeleteAccountWebAccountDeletePost**](DefaultAPI.md#DeleteAccountWebAccountDeletePost) | **Post** /web/account/delete | Delete Account
[**DeleteArtifactByIdRouteV0ArtifactsArtIdDelete**](DefaultAPI.md#DeleteArtifactByIdRouteV0ArtifactsArtIdDelete) | **Delete** /v0/artifacts/{art_id} | Soft-delete an artifact by its stable ID
[**DeleteArtifactV0ArtifactsPathDelete**](DefaultAPI.md#DeleteArtifactV0ArtifactsPathDelete) | **Delete** /v0/artifacts/{path} | Delete Artifact
[**DeleteDriveRouteV0DrivesDriveIdDelete**](DefaultAPI.md#DeleteDriveRouteV0DrivesDriveIdDelete) | **Delete** /v0/drives/{drive_id} | Soft-delete a drive
[**DeleteDriveWebWebDrivesDriveIdDeletePost**](DefaultAPI.md#DeleteDriveWebWebDrivesDriveIdDeletePost) | **Post** /web/drives/{drive_id}/delete | Delete Drive Web
[**DeleteFolderByIdV0FoldersFldIdDelete**](DefaultAPI.md#DeleteFolderByIdV0FoldersFldIdDelete) | **Delete** /v0/folders/{fld_id} | Soft-delete a folder by stable ID (cascade with ?recursive&#x3D;true)
[**DeleteFolderByPathV0FoldersPathDelete**](DefaultAPI.md#DeleteFolderByPathV0FoldersPathDelete) | **Delete** /v0/folders/{path} | Soft-delete a folder (cascade with ?recursive&#x3D;true)
[**DeleteGrantRouteV0GrantsGrnIdDelete**](DefaultAPI.md#DeleteGrantRouteV0GrantsGrnIdDelete) | **Delete** /v0/grants/{grn_id} | Revoke a grant (can_manage, or self-revoke own grant)
[**DeleteShareRouteV0SharesShrIdDelete**](DefaultAPI.md#DeleteShareRouteV0SharesShrIdDelete) | **Delete** /v0/shares/{shr_id} | Revoke a share link (requires can_manage)
[**DeleteWorkspaceWebWebWorkspacesOrgIdDeletePost**](DefaultAPI.md#DeleteWorkspaceWebWebWorkspacesOrgIdDeletePost) | **Post** /web/workspaces/{org_id}/delete | Delete Workspace Web
[**DownloadArtifactByIdV0ArtifactsArtIdDownloadGet**](DefaultAPI.md#DownloadArtifactByIdV0ArtifactsArtIdDownloadGet) | **Get** /v0/artifacts/{art_id}/download | Stream the artifact bytes by stable ID (never rendered HTML)
[**DownloadArtifactByPathV0ArtifactsPathDownloadGet**](DefaultAPI.md#DownloadArtifactByPathV0ArtifactsPathDownloadGet) | **Get** /v0/artifacts/{path}/download | Stream the artifact bytes by path (never rendered HTML)
[**DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet**](DefaultAPI.md#DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet) | **Get** /v0/artifacts/{art_id}/versions/{version_number}/download | Stream bytes for a specific version (machine surface)
[**DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet**](DefaultAPI.md#DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet) | **Get** /v0/artifacts/{art_id}/download-url | Signed direct-from-GCS download URL by stable ID
[**DownloadUrlByPathV0ArtifactsPathDownloadUrlGet**](DefaultAPI.md#DownloadUrlByPathV0ArtifactsPathDownloadUrlGet) | **Get** /v0/artifacts/{path}/download-url | Signed direct-from-GCS download URL by path
[**DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet**](DefaultAPI.md#DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet) | **Get** /v0/artifacts/{art_id}/versions/{version_number}/download-url | Signed direct-from-GCS download URL for a specific version
[**EditArtifactAArtIdEditGet**](DefaultAPI.md#EditArtifactAArtIdEditGet) | **Get** /a/{art_id}/edit | Edit Artifact
[**EnqueueJobV0ProjectsFldIdJobsPost**](DefaultAPI.md#EnqueueJobV0ProjectsFldIdJobsPost) | **Post** /v0/projects/{fld_id}/jobs | Enqueue a compile job for a project (folder)
[**ExtensionStartAuthExtensionStartGet**](DefaultAPI.md#ExtensionStartAuthExtensionStartGet) | **Get** /auth/extension/start | Extension Start
[**FeedbackFormFeedbackGet**](DefaultAPI.md#FeedbackFormFeedbackGet) | **Get** /feedback | Feedback Form
[**FeedbackSubmitFeedbackPost**](DefaultAPI.md#FeedbackSubmitFeedbackPost) | **Post** /feedback | Feedback Submit
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
[**GetShareStateWebShareRidGet**](DefaultAPI.md#GetShareStateWebShareRidGet) | **Get** /web/share/{rid} | Get Share State
[**GetUploadStatusV0UploadsUploadIdGet**](DefaultAPI.md#GetUploadStatusV0UploadsUploadIdGet) | **Get** /v0/uploads/{upload_id} | Get the status of a large (direct-to-GCS) upload session
[**HealthHealthGet**](DefaultAPI.md#HealthHealthGet) | **Get** /health | Health
[**InviteMemberWebWebMembersInvitePost**](DefaultAPI.md#InviteMemberWebWebMembersInvitePost) | **Post** /web/members/invite | Invite Member Web
[**ListArtifactVersionsV0ArtifactsArtIdVersionsGet**](DefaultAPI.md#ListArtifactVersionsV0ArtifactsArtIdVersionsGet) | **Get** /v0/artifacts/{art_id}/versions | List versions of an artifact, newest first
[**ListArtifactsV0ArtifactsGet**](DefaultAPI.md#ListArtifactsV0ArtifactsGet) | **Get** /v0/artifacts | List artifacts in the drive
[**ListEventsRouteV0EventsGet**](DefaultAPI.md#ListEventsRouteV0EventsGet) | **Get** /v0/events | Read the append-only event log for the authenticated drive
[**ListGrantsRouteV0GrantsGet**](DefaultAPI.md#ListGrantsRouteV0GrantsGet) | **Get** /v0/grants | List live grants on a resource (requires can_manage)
[**ListProjectJobsV0ProjectsFldIdJobsGet**](DefaultAPI.md#ListProjectJobsV0ProjectsFldIdJobsGet) | **Get** /v0/projects/{fld_id}/jobs | List a project&#39;s jobs
[**ListSharesRouteV0SharesGet**](DefaultAPI.md#ListSharesRouteV0SharesGet) | **Get** /v0/shares | List live share links on a resource (requires can_manage)
[**ListTrashRouteV0DrivesDriveIdTrashGet**](DefaultAPI.md#ListTrashRouteV0DrivesDriveIdTrashGet) | **Get** /v0/drives/{drive_id}/trash | List the authenticated drive&#39;s trash
[**LoginAuthLoginGet**](DefaultAPI.md#LoginAuthLoginGet) | **Get** /auth/login | Login
[**LogoutAuthLogoutPost**](DefaultAPI.md#LogoutAuthLogoutPost) | **Post** /auth/logout | Logout
[**MarketingGet**](DefaultAPI.md#MarketingGet) | **Get** / | Marketing
[**MarketplaceBrowseMarketplaceGet**](DefaultAPI.md#MarketplaceBrowseMarketplaceGet) | **Get** /marketplace | Marketplace Browse
[**MarketplaceDetailMarketplaceSlugGet**](DefaultAPI.md#MarketplaceDetailMarketplaceSlugGet) | **Get** /marketplace/{slug} | Marketplace Detail
[**MeUsageV0DrivesMeUsageGet**](DefaultAPI.md#MeUsageV0DrivesMeUsageGet) | **Get** /v0/drives/me/usage | Current-period usage + caps for the authenticated drive
[**MeV0DrivesMeGet**](DefaultAPI.md#MeV0DrivesMeGet) | **Get** /v0/drives/me | Me
[**MoveArtifactRouteV0ArtifactsArtIdMovePost**](DefaultAPI.md#MoveArtifactRouteV0ArtifactsArtIdMovePost) | **Post** /v0/artifacts/{art_id}/move | Rename / move an artifact to a new path
[**MoveFolderByIdV0FoldersFldIdMovePost**](DefaultAPI.md#MoveFolderByIdV0FoldersFldIdMovePost) | **Post** /v0/folders/{fld_id}/move | Rename / move a folder by stable ID (cascade descendants)
[**MoveFolderByPathV0FoldersPathMovePost**](DefaultAPI.md#MoveFolderByPathV0FoldersPathMovePost) | **Post** /v0/folders/{path}/move | Rename / move a folder (cascade-update descendants)
[**OauthDisconnectWebOauthDisconnectPost**](DefaultAPI.md#OauthDisconnectWebOauthDisconnectPost) | **Post** /web/oauth/disconnect | Oauth Disconnect
[**PatchArtifactRouteV0ArtifactsArtIdPatch**](DefaultAPI.md#PatchArtifactRouteV0ArtifactsArtIdPatch) | **Patch** /v0/artifacts/{art_id} | Edit artifact metadata (labels / metadata / source)
[**PatchFolderByIdV0FoldersFldIdPatch**](DefaultAPI.md#PatchFolderByIdV0FoldersFldIdPatch) | **Patch** /v0/folders/{fld_id} | Update folder metadata by stable ID
[**PatchFolderByPathV0FoldersPathPatch**](DefaultAPI.md#PatchFolderByPathV0FoldersPathPatch) | **Patch** /v0/folders/{path} | Update folder metadata by path
[**PatchGrantRouteV0GrantsGrnIdPatch**](DefaultAPI.md#PatchGrantRouteV0GrantsGrnIdPatch) | **Patch** /v0/grants/{grn_id} | Update a grant&#39;s role and/or expiry (requires can_manage)
[**PostDescribeV0QueryDescribePost**](DefaultAPI.md#PostDescribeV0QueryDescribePost) | **Post** /v0/query/describe | Describe a dataset&#39;s column schema
[**PostFeedbackV0FeedbackPost**](DefaultAPI.md#PostFeedbackV0FeedbackPost) | **Post** /v0/feedback | Post Feedback
[**PostLookupValuesV0QueryLookupValuesPost**](DefaultAPI.md#PostLookupValuesV0QueryLookupValuesPost) | **Post** /v0/query/lookup-values | List distinct values of a dataset column
[**PostQueryV0QueryPost**](DefaultAPI.md#PostQueryV0QueryPost) | **Post** /v0/query | Run a read-only SQL query over authorized datasets
[**PrivacyPagePrivacyGet**](DefaultAPI.md#PrivacyPagePrivacyGet) | **Get** /privacy | Privacy Page
[**ProjectPreviewPageFFldIdPreviewGet**](DefaultAPI.md#ProjectPreviewPageFFldIdPreviewGet) | **Get** /f/{fld_id}/preview | Project Preview Page
[**PublisherProfilePublishersHandleGet**](DefaultAPI.md#PublisherProfilePublishersHandleGet) | **Get** /publishers/{handle} | Publisher Profile
[**PutArtifactV0ArtifactsPathPut**](DefaultAPI.md#PutArtifactV0ArtifactsPathPut) | **Put** /v0/artifacts/{path} | Upload (or overwrite) an artifact
[**PutProjectV0ProjectsFldIdPut**](DefaultAPI.md#PutProjectV0ProjectsFldIdPut) | **Put** /v0/projects/{fld_id} | Set a project&#39;s compile config (entrypoint/engine/auto_compile)
[**RecoveryNewAccountAuthRecoveryNewAccountPost**](DefaultAPI.md#RecoveryNewAccountAuthRecoveryNewAccountPost) | **Post** /auth/recovery/new-account | Recovery New Account
[**RecoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGet**](DefaultAPI.md#RecoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGet) | **Get** /auth/recovery/new-account-expired | Recovery New Account Expired
[**RecoveryPageAuthRecoveryGet**](DefaultAPI.md#RecoveryPageAuthRecoveryGet) | **Get** /auth/recovery | Recovery Page
[**RecoveryRestoreAuthRecoveryRestorePost**](DefaultAPI.md#RecoveryRestoreAuthRecoveryRestorePost) | **Post** /auth/recovery/restore | Recovery Restore
[**RedeemShareSShareKeyGet**](DefaultAPI.md#RedeemShareSShareKeyGet) | **Get** /s/{share_key} | Redeem Share
[**RedeemShareWithPasswordSShareKeyPost**](DefaultAPI.md#RedeemShareWithPasswordSShareKeyPost) | **Post** /s/{share_key} | Redeem Share With Password
[**RemoveMemberWebWebMembersTargetUserIdRemovePost**](DefaultAPI.md#RemoveMemberWebWebMembersTargetUserIdRemovePost) | **Post** /web/members/{target_user_id}/remove | Remove Member Web
[**RenameDriveWebWebDrivesDriveIdRenamePost**](DefaultAPI.md#RenameDriveWebWebDrivesDriveIdRenamePost) | **Post** /web/drives/{drive_id}/rename | Rename Drive Web
[**RenameWorkspaceWebWebWorkspacesOrgIdRenamePost**](DefaultAPI.md#RenameWorkspaceWebWebWorkspacesOrgIdRenamePost) | **Post** /web/workspaces/{org_id}/rename | Rename Workspace Web
[**ResendInvitationWebWebInvitationsInvitationIdResendPost**](DefaultAPI.md#ResendInvitationWebWebInvitationsInvitationIdResendPost) | **Post** /web/invitations/{invitation_id}/resend | Resend Invitation Web
[**RestoreArtifactV0ArtifactsArtIdRestorePost**](DefaultAPI.md#RestoreArtifactV0ArtifactsArtIdRestorePost) | **Post** /v0/artifacts/{art_id}/restore | Restore a soft-deleted artifact
[**RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost**](DefaultAPI.md#RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost) | **Post** /v0/artifacts/{art_id}/versions/{version_number}/restore | Restore a previous version as a new head version
[**RestoreDriveRouteV0DrivesDriveIdRestorePost**](DefaultAPI.md#RestoreDriveRouteV0DrivesDriveIdRestorePost) | **Post** /v0/drives/{drive_id}/restore | Restore a soft-deleted drive
[**RestoreFolderByIdV0FoldersFldIdRestorePost**](DefaultAPI.md#RestoreFolderByIdV0FoldersFldIdRestorePost) | **Post** /v0/folders/{fld_id}/restore | Restore a soft-deleted folder (cascade)
[**RevokeGrantWebShareRidGrantGrnIdRevokePost**](DefaultAPI.md#RevokeGrantWebShareRidGrantGrnIdRevokePost) | **Post** /web/share/{rid}/grant/{grn_id}/revoke | Revoke Grant
[**RevokeInvitationWebWebInvitationsInvitationIdRevokePost**](DefaultAPI.md#RevokeInvitationWebWebInvitationsInvitationIdRevokePost) | **Post** /web/invitations/{invitation_id}/revoke | Revoke Invitation Web
[**RevokeKeyWebKeysRevokePost**](DefaultAPI.md#RevokeKeyWebKeysRevokePost) | **Post** /web/keys/revoke | Revoke Key
[**RevokeLinkWebShareRidLinkShrIdRevokePost**](DefaultAPI.md#RevokeLinkWebShareRidLinkShrIdRevokePost) | **Post** /web/share/{rid}/link/{shr_id}/revoke | Revoke Link
[**RevokeUserTokenWebTokensRevokePost**](DefaultAPI.md#RevokeUserTokenWebTokensRevokePost) | **Post** /web/tokens/revoke | Revoke User Token
[**RotateShareRouteV0SharesShrIdRotatePost**](DefaultAPI.md#RotateShareRouteV0SharesShrIdRotatePost) | **Post** /v0/shares/{shr_id}/rotate | Revoke + reissue a share link&#39;s key (requires can_share)
[**SearchV0SearchGet**](DefaultAPI.md#SearchV0SearchGet) | **Get** /v0/search | Full-text search over artifacts in the drive
[**SetMemberRoleWebWebMembersTargetUserIdRolePost**](DefaultAPI.md#SetMemberRoleWebWebMembersTargetUserIdRolePost) | **Post** /web/members/{target_user_id}/role | Set Member Role Web
[**SetPublicWebShareRidPublicPost**](DefaultAPI.md#SetPublicWebShareRidPublicPost) | **Post** /web/share/{rid}/public | Set Public
[**SetSealWebShareRidSealPost**](DefaultAPI.md#SetSealWebShareRidSealPost) | **Post** /web/share/{rid}/seal | Set Seal
[**SettingsAccountSettingsGet**](DefaultAPI.md#SettingsAccountSettingsGet) | **Get** /settings | Settings Account
[**SettingsApiKeysSettingsApiKeysGet**](DefaultAPI.md#SettingsApiKeysSettingsApiKeysGet) | **Get** /settings/api-keys | Settings Api Keys
[**SettingsQuickstartSettingsQuickstartGet**](DefaultAPI.md#SettingsQuickstartSettingsQuickstartGet) | **Get** /settings/quickstart | Settings Quickstart
[**SettingsWorkspaceSettingsWorkspaceGet**](DefaultAPI.md#SettingsWorkspaceSettingsWorkspaceGet) | **Get** /settings/workspace | Settings Workspace
[**SharedFilesSharedGet**](DefaultAPI.md#SharedFilesSharedGet) | **Get** /shared | Shared Files
[**SwitchDriveWebSwitchPost**](DefaultAPI.md#SwitchDriveWebSwitchPost) | **Post** /web/switch | Switch Drive
[**TermsPageTermsGet**](DefaultAPI.md#TermsPageTermsGet) | **Get** /terms | Terms Page
[**ToggleIndexingWebAccountIndexingPost**](DefaultAPI.md#ToggleIndexingWebAccountIndexingPost) | **Post** /web/account/indexing | Toggle Indexing
[**TrashWebTrashGet**](DefaultAPI.md#TrashWebTrashGet) | **Get** /web/trash | Trash
[**ViewArtifactHeadAArtIdHeadGet**](DefaultAPI.md#ViewArtifactHeadAArtIdHeadGet) | **Get** /a/{art_id}/head | View Artifact Head
[**ViewArtifactVersionVArtIdVersionGet**](DefaultAPI.md#ViewArtifactVersionVArtIdVersionGet) | **Get** /v/{art_id}/{version} | View Artifact Version
[**ViewFileDriveIdPathGet**](DefaultAPI.md#ViewFileDriveIdPathGet) | **Get** /{drive_id}/{path} | View File
[**ViewPermalinkArtifactAArtIdGet**](DefaultAPI.md#ViewPermalinkArtifactAArtIdGet) | **Get** /a/{art_id} | View Permalink Artifact
[**ViewPermalinkFolderFFldIdGet**](DefaultAPI.md#ViewPermalinkFolderFFldIdGet) | **Get** /f/{fld_id} | View Permalink Folder
[**WebArtifactIndexedWebArtifactsIndexedGet**](DefaultAPI.md#WebArtifactIndexedWebArtifactsIndexedGet) | **Get** /web/artifacts/indexed | Web Artifact Indexed
[**WebCopyArtifactWebArtifactsCopyPost**](DefaultAPI.md#WebCopyArtifactWebArtifactsCopyPost) | **Post** /web/artifacts/copy | Web Copy Artifact
[**WebDeleteArtifactOpWebArtifactsDeletePost**](DefaultAPI.md#WebDeleteArtifactOpWebArtifactsDeletePost) | **Post** /web/artifacts/delete | Web Delete Artifact Op
[**WebDeleteArtifactWebArtifactsPathDelete**](DefaultAPI.md#WebDeleteArtifactWebArtifactsPathDelete) | **Delete** /web/artifacts/{path} | Web Delete Artifact
[**WebDeleteFolderWebFoldersDeletePost**](DefaultAPI.md#WebDeleteFolderWebFoldersDeletePost) | **Post** /web/folders/delete | Web Delete Folder
[**WebMoveFolderWebFoldersMovePost**](DefaultAPI.md#WebMoveFolderWebFoldersMovePost) | **Post** /web/folders/move | Web Move Folder
[**WebNewFolderWebFoldersNewPost**](DefaultAPI.md#WebNewFolderWebFoldersNewPost) | **Post** /web/folders/new | Web New Folder
[**WebProjectCompileWebProjectsFldIdCompilePost**](DefaultAPI.md#WebProjectCompileWebProjectsFldIdCompilePost) | **Post** /web/projects/{fld_id}/compile | Web Project Compile
[**WebProjectFilesWebProjectsFldIdFilesGet**](DefaultAPI.md#WebProjectFilesWebProjectsFldIdFilesGet) | **Get** /web/projects/{fld_id}/files | Web Project Files
[**WebProjectPreviewWebProjectsFldIdPreviewGet**](DefaultAPI.md#WebProjectPreviewWebProjectsFldIdPreviewGet) | **Get** /web/projects/{fld_id}/preview | Web Project Preview
[**WebPutArtifactWebArtifactsPathPut**](DefaultAPI.md#WebPutArtifactWebArtifactsPathPut) | **Put** /web/artifacts/{path} | Web Put Artifact
[**WebRenameArtifactWebArtifactsRenamePost**](DefaultAPI.md#WebRenameArtifactWebArtifactsRenamePost) | **Post** /web/artifacts/rename | Web Rename Artifact
[**WebRestoreArtifactWebArtifactsRestorePost**](DefaultAPI.md#WebRestoreArtifactWebArtifactsRestorePost) | **Post** /web/artifacts/restore | Web Restore Artifact
[**WebRestoreFolderWebFoldersRestorePost**](DefaultAPI.md#WebRestoreFolderWebFoldersRestorePost) | **Post** /web/folders/restore | Web Restore Folder
[**WebSetMetadataWebSetPost**](DefaultAPI.md#WebSetMetadataWebSetPost) | **Post** /web/set | Web Set Metadata
[**WebUploadWebUploadPost**](DefaultAPI.md#WebUploadWebUploadPost) | **Post** /web/upload | Web Upload
[**WebhooksPageWebhooksGet**](DefaultAPI.md#WebhooksPageWebhooksGet) | **Get** /webhooks | Webhooks Page
[**WelcomeWelcomeGet**](DefaultAPI.md#WelcomeWelcomeGet) | **Get** /welcome | Welcome



## AbortUploadV0UploadsUploadIdDelete

> UploadAbortOut AbortUploadV0UploadsUploadIdDelete(ctx, uploadId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.AbortUploadV0UploadsUploadIdDelete(context.Background(), uploadId).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**UploadAbortOut**](UploadAbortOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AcceptInvitationInvitationsTokenGet

> string AcceptInvitationInvitationsTokenGet(ctx, token).Execute()

Accept Invitation



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
	token := "token_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.AcceptInvitationInvitationsTokenGet(context.Background(), token).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.AcceptInvitationInvitationsTokenGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AcceptInvitationInvitationsTokenGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.AcceptInvitationInvitationsTokenGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**token** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiAcceptInvitationInvitationsTokenGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


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


## ActivityFeedActivityGet

> string ActivityFeedActivityGet(ctx).Execute()

Activity Feed

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
	resp, r, err := apiClient.DefaultAPI.ActivityFeedActivityGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ActivityFeedActivityGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ActivityFeedActivityGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ActivityFeedActivityGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiActivityFeedActivityGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AddGrantWebShareRidGrantPost

> interface{} AddGrantWebShareRidGrantPost(ctx, rid).GrantIn(grantIn).XCsrfToken(xCsrfToken).Execute()

Add Grant

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
	rid := "rid_example" // string | 
	grantIn := *openapiclient.NewGrantIn("Principal_example") // GrantIn | 
	xCsrfToken := "xCsrfToken_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.AddGrantWebShareRidGrantPost(context.Background(), rid).GrantIn(grantIn).XCsrfToken(xCsrfToken).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.AddGrantWebShareRidGrantPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddGrantWebShareRidGrantPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.AddGrantWebShareRidGrantPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**rid** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddGrantWebShareRidGrantPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **grantIn** | [**GrantIn**](GrantIn.md) |  | 
 **xCsrfToken** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ArtifactDetailPreviewPreviewArtifactDetailGet

> string ArtifactDetailPreviewPreviewArtifactDetailGet(ctx).Execute()

Artifact Detail Preview

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
	resp, r, err := apiClient.DefaultAPI.ArtifactDetailPreviewPreviewArtifactDetailGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ArtifactDetailPreviewPreviewArtifactDetailGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ArtifactDetailPreviewPreviewArtifactDetailGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ArtifactDetailPreviewPreviewArtifactDetailGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiArtifactDetailPreviewPreviewArtifactDetailGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BeginUploadV0UploadsPost

> UploadBeginOut BeginUploadV0UploadsPost(ctx).UploadBeginIn(uploadBeginIn).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.BeginUploadV0UploadsPost(context.Background()).UploadBeginIn(uploadBeginIn).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**UploadBeginOut**](UploadBeginOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CallbackAuthCallbackGet

> interface{} CallbackAuthCallbackGet(ctx).Code(code).State(state).Error_(error_).Execute()

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
	// response from `CallbackAuthCallbackGet`: interface{}
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

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CancelJobV0JobsJobIdCancelPost

> interface{} CancelJobV0JobsJobIdCancelPost(ctx, jobId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CancelJobV0JobsJobIdCancelPost(context.Background(), jobId).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CancelJobV0JobsJobIdCancelPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CancelJobV0JobsJobIdCancelPost`: interface{}
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

 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CollectionDetailCollectionsSlugGet

> string CollectionDetailCollectionsSlugGet(ctx, slug).Execute()

Collection Detail

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
	slug := "slug_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CollectionDetailCollectionsSlugGet(context.Background(), slug).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CollectionDetailCollectionsSlugGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CollectionDetailCollectionsSlugGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CollectionDetailCollectionsSlugGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**slug** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCollectionDetailCollectionsSlugGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


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


## CommitUploadV0UploadsUploadIdCommitPost

> ArtifactOut CommitUploadV0UploadsUploadIdCommitPost(ctx, uploadId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CommitUploadV0UploadsUploadIdCommitPost(context.Background(), uploadId).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ConnectorsPageConnectorsGet

> string ConnectorsPageConnectorsGet(ctx).Execute()

Connectors Page



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
	resp, r, err := apiClient.DefaultAPI.ConnectorsPageConnectorsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ConnectorsPageConnectorsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ConnectorsPageConnectorsGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ConnectorsPageConnectorsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiConnectorsPageConnectorsGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CopyArtifactRouteV0ArtifactsArtIdCopyPost

> ArtifactOut CopyArtifactRouteV0ArtifactsArtIdCopyPost(ctx, artId).CopyIn(copyIn).XAgentdriveActor(xAgentdriveActor).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CopyArtifactRouteV0ArtifactsArtIdCopyPost(context.Background(), artId).CopyIn(copyIn).XAgentdriveActor(xAgentdriveActor).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CopyFolderByIdV0FoldersFldIdCopyPost

> FolderCopyOut CopyFolderByIdV0FoldersFldIdCopyPost(ctx, fldId).FolderCopyIn(folderCopyIn).XAgentdriveActor(xAgentdriveActor).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CopyFolderByIdV0FoldersFldIdCopyPost(context.Background(), fldId).FolderCopyIn(folderCopyIn).XAgentdriveActor(xAgentdriveActor).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**FolderCopyOut**](FolderCopyOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateDriveKeyWebWebDrivesDriveIdKeysCreatePost

> interface{} CreateDriveKeyWebWebDrivesDriveIdKeysCreatePost(ctx, driveId).Csrf(csrf).Label(label).Execute()

Create Drive Key Web



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
	csrf := "csrf_example" // string | 
	label := "label_example" // string |  (optional) (default to "")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CreateDriveKeyWebWebDrivesDriveIdKeysCreatePost(context.Background(), driveId).Csrf(csrf).Label(label).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateDriveKeyWebWebDrivesDriveIdKeysCreatePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateDriveKeyWebWebDrivesDriveIdKeysCreatePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CreateDriveKeyWebWebDrivesDriveIdKeysCreatePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateDriveKeyWebWebDrivesDriveIdKeysCreatePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **csrf** | **string** |  | 
 **label** | **string** |  | [default to &quot;&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateDriveWebWebDrivesPost

> interface{} CreateDriveWebWebDrivesPost(ctx).Name(name).Csrf(csrf).Execute()

Create Drive Web



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
	name := "name_example" // string | 
	csrf := "csrf_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CreateDriveWebWebDrivesPost(context.Background()).Name(name).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateDriveWebWebDrivesPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateDriveWebWebDrivesPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CreateDriveWebWebDrivesPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateDriveWebWebDrivesPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **string** |  | 
 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateFolderByPathV0FoldersPathPut

> FolderOut CreateFolderByPathV0FoldersPathPut(ctx, path).XAgentdriveActor(xAgentdriveActor).IfNoneMatch(ifNoneMatch).Authorization(authorization).FolderCreateIn(folderCreateIn).Execute()

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
	authorization := "authorization_example" // string |  (optional)
	folderCreateIn := *openapiclient.NewFolderCreateIn() // FolderCreateIn |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CreateFolderByPathV0FoldersPathPut(context.Background(), path).XAgentdriveActor(xAgentdriveActor).IfNoneMatch(ifNoneMatch).Authorization(authorization).FolderCreateIn(folderCreateIn).Execute()
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
 **authorization** | **string** |  | 
 **folderCreateIn** | [**FolderCreateIn**](FolderCreateIn.md) |  | 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateGrantRouteV0GrantsPost

> GrantOut CreateGrantRouteV0GrantsPost(ctx).GrantCreateIn(grantCreateIn).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()

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
	grantCreateIn := *openapiclient.NewGrantCreateIn("Resource_example", *openapiclient.NewGrantPrincipalIn("Type_example"), "Role_example") // GrantCreateIn | 
	xAgentdriveActor := "xAgentdriveActor_example" // string |  (optional)
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CreateGrantRouteV0GrantsPost(context.Background()).GrantCreateIn(grantCreateIn).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateKeyWebKeysCreatePost

> interface{} CreateKeyWebKeysCreatePost(ctx).Csrf(csrf).Label(label).Execute()

Create Key



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
	label := "label_example" // string |  (optional) (default to "")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CreateKeyWebKeysCreatePost(context.Background()).Csrf(csrf).Label(label).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateKeyWebKeysCreatePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateKeyWebKeysCreatePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CreateKeyWebKeysCreatePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateKeyWebKeysCreatePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **string** |  | 
 **label** | **string** |  | [default to &quot;&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateLinkWebShareRidLinkPost

> interface{} CreateLinkWebShareRidLinkPost(ctx, rid).LinkIn(linkIn).XCsrfToken(xCsrfToken).Execute()

Create Link



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
	rid := "rid_example" // string | 
	linkIn := *openapiclient.NewLinkIn() // LinkIn | 
	xCsrfToken := "xCsrfToken_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CreateLinkWebShareRidLinkPost(context.Background(), rid).LinkIn(linkIn).XCsrfToken(xCsrfToken).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateLinkWebShareRidLinkPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateLinkWebShareRidLinkPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CreateLinkWebShareRidLinkPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**rid** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateLinkWebShareRidLinkPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **linkIn** | [**LinkIn**](LinkIn.md) |  | 
 **xCsrfToken** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateShareRouteV0SharesPost

> ShareMintOut CreateShareRouteV0SharesPost(ctx).ShareCreateIn(shareCreateIn).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CreateShareRouteV0SharesPost(context.Background()).ShareCreateIn(shareCreateIn).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**ShareMintOut**](ShareMintOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateUserTokenWebTokensCreatePost

> interface{} CreateUserTokenWebTokensCreatePost(ctx).Csrf(csrf).Label(label).Scope(scope).Execute()

Create User Token



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
	label := "label_example" // string |  (optional) (default to "")
	scope := "scope_example" // string |  (optional) (default to "full")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CreateUserTokenWebTokensCreatePost(context.Background()).Csrf(csrf).Label(label).Scope(scope).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateUserTokenWebTokensCreatePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateUserTokenWebTokensCreatePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CreateUserTokenWebTokensCreatePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateUserTokenWebTokensCreatePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **string** |  | 
 **label** | **string** |  | [default to &quot;&quot;]
 **scope** | **string** |  | [default to &quot;full&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateWorkspaceWebWebWorkspacesPost

> interface{} CreateWorkspaceWebWebWorkspacesPost(ctx).Name(name).Csrf(csrf).Execute()

Create Workspace Web



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
	name := "name_example" // string | 
	csrf := "csrf_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.CreateWorkspaceWebWebWorkspacesPost(context.Background()).Name(name).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.CreateWorkspaceWebWebWorkspacesPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateWorkspaceWebWebWorkspacesPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.CreateWorkspaceWebWebWorkspacesPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateWorkspaceWebWebWorkspacesPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **string** |  | 
 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DangerZoneOldDashboardDangerGet

> interface{} DangerZoneOldDashboardDangerGet(ctx).Execute()

Danger Zone Old

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
	resp, r, err := apiClient.DefaultAPI.DangerZoneOldDashboardDangerGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DangerZoneOldDashboardDangerGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DangerZoneOldDashboardDangerGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DangerZoneOldDashboardDangerGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiDangerZoneOldDashboardDangerGetRequest struct via the builder pattern


### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DangerZoneSettingsDangerGet

> string DangerZoneSettingsDangerGet(ctx).Execute()

Danger Zone

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
	resp, r, err := apiClient.DefaultAPI.DangerZoneSettingsDangerGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DangerZoneSettingsDangerGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DangerZoneSettingsDangerGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DangerZoneSettingsDangerGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiDangerZoneSettingsDangerGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DashboardDashboardGet

> string DashboardDashboardGet(ctx).Q(q).Path(path).Wiki(wiki).Type_(type_).Label(label).After(after).Before(before).View(view).Sort(sort).Dir(dir).Execute()

Dashboard

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
	q := "q_example" // string |  (optional) (default to "")
	path := "path_example" // string |  (optional) (default to "")
	wiki := int32(56) // int32 |  (optional) (default to 0)
	type_ := "type__example" // string |  (optional) (default to "")
	label := []string{"Inner_example"} // []string |  (optional)
	after := "after_example" // string |  (optional) (default to "")
	before := "before_example" // string |  (optional) (default to "")
	view := "view_example" // string |  (optional) (default to "")
	sort := "sort_example" // string |  (optional) (default to "")
	dir := "dir_example" // string |  (optional) (default to "")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DashboardDashboardGet(context.Background()).Q(q).Path(path).Wiki(wiki).Type_(type_).Label(label).After(after).Before(before).View(view).Sort(sort).Dir(dir).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DashboardDashboardGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DashboardDashboardGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DashboardDashboardGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDashboardDashboardGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **string** |  | [default to &quot;&quot;]
 **path** | **string** |  | [default to &quot;&quot;]
 **wiki** | **int32** |  | [default to 0]
 **type_** | **string** |  | [default to &quot;&quot;]
 **label** | **[]string** |  | 
 **after** | **string** |  | [default to &quot;&quot;]
 **before** | **string** |  | [default to &quot;&quot;]
 **view** | **string** |  | [default to &quot;&quot;]
 **sort** | **string** |  | [default to &quot;&quot;]
 **dir** | **string** |  | [default to &quot;&quot;]

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


## DeleteAccountWebAccountDeletePost

> interface{} DeleteAccountWebAccountDeletePost(ctx).Confirm(confirm).Csrf(csrf).Execute()

Delete Account



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
	confirm := "confirm_example" // string | 
	csrf := "csrf_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteAccountWebAccountDeletePost(context.Background()).Confirm(confirm).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteAccountWebAccountDeletePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteAccountWebAccountDeletePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DeleteAccountWebAccountDeletePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDeleteAccountWebAccountDeletePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirm** | **string** |  | 
 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteArtifactByIdRouteV0ArtifactsArtIdDelete

> interface{} DeleteArtifactByIdRouteV0ArtifactsArtIdDelete(ctx, artId).IfMatch(ifMatch).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteArtifactByIdRouteV0ArtifactsArtIdDelete(context.Background(), artId).IfMatch(ifMatch).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteArtifactByIdRouteV0ArtifactsArtIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteArtifactByIdRouteV0ArtifactsArtIdDelete`: interface{}
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
 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteArtifactV0ArtifactsPathDelete

> ArtifactDeleteOut DeleteArtifactV0ArtifactsPathDelete(ctx, path).IfMatch(ifMatch).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteArtifactV0ArtifactsPathDelete(context.Background(), path).IfMatch(ifMatch).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**ArtifactDeleteOut**](ArtifactDeleteOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteDriveRouteV0DrivesDriveIdDelete

> DriveDeleteOut DeleteDriveRouteV0DrivesDriveIdDelete(ctx, driveId).Confirm(confirm).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteDriveRouteV0DrivesDriveIdDelete(context.Background(), driveId).Confirm(confirm).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**DriveDeleteOut**](DriveDeleteOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteDriveWebWebDrivesDriveIdDeletePost

> interface{} DeleteDriveWebWebDrivesDriveIdDeletePost(ctx, driveId).Csrf(csrf).Execute()

Delete Drive Web



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
	csrf := "csrf_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteDriveWebWebDrivesDriveIdDeletePost(context.Background(), driveId).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteDriveWebWebDrivesDriveIdDeletePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteDriveWebWebDrivesDriveIdDeletePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DeleteDriveWebWebDrivesDriveIdDeletePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteDriveWebWebDrivesDriveIdDeletePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteFolderByIdV0FoldersFldIdDelete

> FolderDeleteOut DeleteFolderByIdV0FoldersFldIdDelete(ctx, fldId).Recursive(recursive).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteFolderByIdV0FoldersFldIdDelete(context.Background(), fldId).Recursive(recursive).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**FolderDeleteOut**](FolderDeleteOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteFolderByPathV0FoldersPathDelete

> FolderDeleteOut DeleteFolderByPathV0FoldersPathDelete(ctx, path).Recursive(recursive).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteFolderByPathV0FoldersPathDelete(context.Background(), path).Recursive(recursive).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**FolderDeleteOut**](FolderDeleteOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteGrantRouteV0GrantsGrnIdDelete

> RevokeOut DeleteGrantRouteV0GrantsGrnIdDelete(ctx, grnId).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteGrantRouteV0GrantsGrnIdDelete(context.Background(), grnId).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**RevokeOut**](RevokeOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteShareRouteV0SharesShrIdDelete

> RevokeOut DeleteShareRouteV0SharesShrIdDelete(ctx, shrId).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteShareRouteV0SharesShrIdDelete(context.Background(), shrId).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**RevokeOut**](RevokeOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteWorkspaceWebWebWorkspacesOrgIdDeletePost

> interface{} DeleteWorkspaceWebWebWorkspacesOrgIdDeletePost(ctx, orgId).Csrf(csrf).Confirm(confirm).Execute()

Delete Workspace Web



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
	csrf := "csrf_example" // string | 
	confirm := "confirm_example" // string |  (optional) (default to "")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DeleteWorkspaceWebWebWorkspacesOrgIdDeletePost(context.Background(), orgId).Csrf(csrf).Confirm(confirm).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DeleteWorkspaceWebWebWorkspacesOrgIdDeletePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteWorkspaceWebWebWorkspacesOrgIdDeletePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.DeleteWorkspaceWebWebWorkspacesOrgIdDeletePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**orgId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteWorkspaceWebWebWorkspacesOrgIdDeletePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **csrf** | **string** |  | 
 **confirm** | **string** |  | [default to &quot;&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadArtifactByIdV0ArtifactsArtIdDownloadGet

> interface{} DownloadArtifactByIdV0ArtifactsArtIdDownloadGet(ctx, artId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DownloadArtifactByIdV0ArtifactsArtIdDownloadGet(context.Background(), artId).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DownloadArtifactByIdV0ArtifactsArtIdDownloadGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadArtifactByIdV0ArtifactsArtIdDownloadGet`: interface{}
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

 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadArtifactByPathV0ArtifactsPathDownloadGet

> interface{} DownloadArtifactByPathV0ArtifactsPathDownloadGet(ctx, path).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DownloadArtifactByPathV0ArtifactsPathDownloadGet(context.Background(), path).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DownloadArtifactByPathV0ArtifactsPathDownloadGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadArtifactByPathV0ArtifactsPathDownloadGet`: interface{}
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

 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet

> interface{} DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet(ctx, artId, versionNumber).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet(context.Background(), artId, versionNumber).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DownloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet`: interface{}
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


 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet

> DownloadUrlOut DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet(ctx, artId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DownloadUrlByIdV0ArtifactsArtIdDownloadUrlGet(context.Background(), artId).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadUrlByPathV0ArtifactsPathDownloadUrlGet

> DownloadUrlOut DownloadUrlByPathV0ArtifactsPathDownloadUrlGet(ctx, path).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DownloadUrlByPathV0ArtifactsPathDownloadUrlGet(context.Background(), path).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet

> DownloadUrlOut DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet(ctx, artId, versionNumber).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.DownloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet(context.Background(), artId, versionNumber).Authorization(authorization).Execute()
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


 **authorization** | **string** |  | 

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## EditArtifactAArtIdEditGet

> string EditArtifactAArtIdEditGet(ctx, artId).Execute()

Edit Artifact



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
	resp, r, err := apiClient.DefaultAPI.EditArtifactAArtIdEditGet(context.Background(), artId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.EditArtifactAArtIdEditGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `EditArtifactAArtIdEditGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.EditArtifactAArtIdEditGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**artId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiEditArtifactAArtIdEditGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


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


## EnqueueJobV0ProjectsFldIdJobsPost

> interface{} EnqueueJobV0ProjectsFldIdJobsPost(ctx, fldId).CompileJobIn(compileJobIn).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.EnqueueJobV0ProjectsFldIdJobsPost(context.Background(), fldId).CompileJobIn(compileJobIn).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.EnqueueJobV0ProjectsFldIdJobsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `EnqueueJobV0ProjectsFldIdJobsPost`: interface{}
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
 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ExtensionStartAuthExtensionStartGet

> interface{} ExtensionStartAuthExtensionStartGet(ctx).ExtId(extId).Execute()

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
	resp, r, err := apiClient.DefaultAPI.ExtensionStartAuthExtensionStartGet(context.Background()).ExtId(extId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ExtensionStartAuthExtensionStartGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ExtensionStartAuthExtensionStartGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ExtensionStartAuthExtensionStartGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiExtensionStartAuthExtensionStartGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extId** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FeedbackFormFeedbackGet

> string FeedbackFormFeedbackGet(ctx).Execute()

Feedback Form



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
	resp, r, err := apiClient.DefaultAPI.FeedbackFormFeedbackGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.FeedbackFormFeedbackGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FeedbackFormFeedbackGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.FeedbackFormFeedbackGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiFeedbackFormFeedbackGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FeedbackSubmitFeedbackPost

> interface{} FeedbackSubmitFeedbackPost(ctx).Csrf(csrf).Category(category).Title(title).Message(message).Contact(contact).Attachments(attachments).Execute()

Feedback Submit



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
	category := "category_example" // string |  (optional) (default to "")
	title := "title_example" // string |  (optional) (default to "")
	message := "message_example" // string |  (optional) (default to "")
	contact := "contact_example" // string |  (optional) (default to "")
	attachments := []*os.File{"TODO"} // []*os.File |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.FeedbackSubmitFeedbackPost(context.Background()).Csrf(csrf).Category(category).Title(title).Message(message).Contact(contact).Attachments(attachments).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.FeedbackSubmitFeedbackPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FeedbackSubmitFeedbackPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.FeedbackSubmitFeedbackPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiFeedbackSubmitFeedbackPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **string** |  | 
 **category** | **string** |  | [default to &quot;&quot;]
 **title** | **string** |  | [default to &quot;&quot;]
 **message** | **string** |  | [default to &quot;&quot;]
 **contact** | **string** |  | [default to &quot;&quot;]
 **attachments** | **[]*os.File** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## FindV0FindGet

> FindPage FindV0FindGet(ctx).Q(q).Mode(mode).Label(label).FileType(fileType).Prefix(prefix).Modality(modality).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).Limit(limit).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.FindV0FindGet(context.Background()).Q(q).Mode(mode).Label(label).FileType(fileType).Prefix(prefix).Modality(modality).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).Limit(limit).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**FindPage**](FindPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetArtifactByIdMetaV0ArtifactsArtIdMetaGet

> ArtifactOut GetArtifactByIdMetaV0ArtifactsArtIdMetaGet(ctx, artId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetArtifactByIdMetaV0ArtifactsArtIdMetaGet(context.Background(), artId).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetArtifactByIdV0ArtifactsArtIdGet

> ArtifactOut GetArtifactByIdV0ArtifactsArtIdGet(ctx, artId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetArtifactByIdV0ArtifactsArtIdGet(context.Background(), artId).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetArtifactMetaV0ArtifactsPathMetaGet

> ArtifactOut GetArtifactMetaV0ArtifactsPathMetaGet(ctx, path).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetArtifactMetaV0ArtifactsPathMetaGet(context.Background(), path).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet

> VersionOut GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet(ctx, artId, versionNumber).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet(context.Background(), artId, versionNumber).Authorization(authorization).Execute()
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


 **authorization** | **string** |  | 

### Return type

[**VersionOut**](VersionOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDriveRouteV0DrivesDriveIdGet

> interface{} GetDriveRouteV0DrivesDriveIdGet(ctx, driveId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetDriveRouteV0DrivesDriveIdGet(context.Background(), driveId).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetDriveRouteV0DrivesDriveIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetDriveRouteV0DrivesDriveIdGet`: interface{}
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

 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFeedbackStatusV0FeedbackFbkIdGet

> FeedbackStatusOut GetFeedbackStatusV0FeedbackFbkIdGet(ctx, fbkId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetFeedbackStatusV0FeedbackFbkIdGet(context.Background(), fbkId).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**FeedbackStatusOut**](FeedbackStatusOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFolderByIdMetaV0FoldersFldIdMetaGet

> FolderOut GetFolderByIdMetaV0FoldersFldIdMetaGet(ctx, fldId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetFolderByIdMetaV0FoldersFldIdMetaGet(context.Background(), fldId).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFolderByIdV0FoldersFldIdGet

> FolderOut GetFolderByIdV0FoldersFldIdGet(ctx, fldId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetFolderByIdV0FoldersFldIdGet(context.Background(), fldId).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFolderByPathMetaV0FoldersPathMetaGet

> FolderOut GetFolderByPathMetaV0FoldersPathMetaGet(ctx, path).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetFolderByPathMetaV0FoldersPathMetaGet(context.Background(), path).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFolderByPathV0FoldersPathGet

> FolderOut GetFolderByPathV0FoldersPathGet(ctx, path).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetFolderByPathV0FoldersPathGet(context.Background(), path).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetGrantRouteV0GrantsGrnIdGet

> GrantOut GetGrantRouteV0GrantsGrnIdGet(ctx, grnId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetGrantRouteV0GrantsGrnIdGet(context.Background(), grnId).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetJobLogsV0JobsJobIdLogsGet

> interface{} GetJobLogsV0JobsJobIdLogsGet(ctx, jobId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetJobLogsV0JobsJobIdLogsGet(context.Background(), jobId).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetJobLogsV0JobsJobIdLogsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetJobLogsV0JobsJobIdLogsGet`: interface{}
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

 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetJobV0JobsJobIdGet

> interface{} GetJobV0JobsJobIdGet(ctx, jobId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetJobV0JobsJobIdGet(context.Background(), jobId).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetJobV0JobsJobIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetJobV0JobsJobIdGet`: interface{}
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

 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetProjectV0ProjectsFldIdGet

> interface{} GetProjectV0ProjectsFldIdGet(ctx, fldId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetProjectV0ProjectsFldIdGet(context.Background(), fldId).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetProjectV0ProjectsFldIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetProjectV0ProjectsFldIdGet`: interface{}
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

 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetShareRouteV0SharesShrIdGet

> ShareOut GetShareRouteV0SharesShrIdGet(ctx, shrId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetShareRouteV0SharesShrIdGet(context.Background(), shrId).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**ShareOut**](ShareOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetShareStateWebShareRidGet

> interface{} GetShareStateWebShareRidGet(ctx, rid).Execute()

Get Share State

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
	rid := "rid_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetShareStateWebShareRidGet(context.Background(), rid).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.GetShareStateWebShareRidGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetShareStateWebShareRidGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.GetShareStateWebShareRidGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**rid** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetShareStateWebShareRidGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetUploadStatusV0UploadsUploadIdGet

> UploadStatusOut GetUploadStatusV0UploadsUploadIdGet(ctx, uploadId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.GetUploadStatusV0UploadsUploadIdGet(context.Background(), uploadId).Authorization(authorization).Execute()
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

 **authorization** | **string** |  | 

### Return type

[**UploadStatusOut**](UploadStatusOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## HealthHealthGet

> interface{} HealthHealthGet(ctx).Execute()

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
	// response from `HealthHealthGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.HealthHealthGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiHealthHealthGetRequest struct via the builder pattern


### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## InviteMemberWebWebMembersInvitePost

> interface{} InviteMemberWebWebMembersInvitePost(ctx).Email(email).Csrf(csrf).Role(role).WorkspaceName(workspaceName).Execute()

Invite Member Web



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
	email := "email_example" // string | 
	csrf := "csrf_example" // string | 
	role := "role_example" // string |  (optional) (default to "member")
	workspaceName := "workspaceName_example" // string |  (optional) (default to "")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.InviteMemberWebWebMembersInvitePost(context.Background()).Email(email).Csrf(csrf).Role(role).WorkspaceName(workspaceName).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.InviteMemberWebWebMembersInvitePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `InviteMemberWebWebMembersInvitePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.InviteMemberWebWebMembersInvitePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiInviteMemberWebWebMembersInvitePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **string** |  | 
 **csrf** | **string** |  | 
 **role** | **string** |  | [default to &quot;member&quot;]
 **workspaceName** | **string** |  | [default to &quot;&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListArtifactVersionsV0ArtifactsArtIdVersionsGet

> VersionPage ListArtifactVersionsV0ArtifactsArtIdVersionsGet(ctx, artId).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListArtifactVersionsV0ArtifactsArtIdVersionsGet(context.Background(), artId).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**VersionPage**](VersionPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListArtifactsV0ArtifactsGet

> Page ListArtifactsV0ArtifactsGet(ctx).Prefix(prefix).Label(label).FileType(fileType).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListArtifactsV0ArtifactsGet(context.Background()).Prefix(prefix).Label(label).FileType(fileType).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListEventsRouteV0EventsGet

> EventPage ListEventsRouteV0EventsGet(ctx).ArtId(artId).Action(action).Since(since).Before(before).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListEventsRouteV0EventsGet(context.Background()).ArtId(artId).Action(action).Since(since).Before(before).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**EventPage**](EventPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListGrantsRouteV0GrantsGet

> GrantList ListGrantsRouteV0GrantsGet(ctx).Resource(resource).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListGrantsRouteV0GrantsGet(context.Background()).Resource(resource).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**GrantList**](GrantList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListProjectJobsV0ProjectsFldIdJobsGet

> interface{} ListProjectJobsV0ProjectsFldIdJobsGet(ctx, fldId).Status(status).Limit(limit).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListProjectJobsV0ProjectsFldIdJobsGet(context.Background(), fldId).Status(status).Limit(limit).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ListProjectJobsV0ProjectsFldIdJobsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListProjectJobsV0ProjectsFldIdJobsGet`: interface{}
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
 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSharesRouteV0SharesGet

> ShareList ListSharesRouteV0SharesGet(ctx).Resource(resource).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListSharesRouteV0SharesGet(context.Background()).Resource(resource).Cursor(cursor).Limit(limit).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**ShareList**](ShareList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListTrashRouteV0DrivesDriveIdTrashGet

> interface{} ListTrashRouteV0DrivesDriveIdTrashGet(ctx, driveId).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ListTrashRouteV0DrivesDriveIdTrashGet(context.Background(), driveId).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ListTrashRouteV0DrivesDriveIdTrashGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListTrashRouteV0DrivesDriveIdTrashGet`: interface{}
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

 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## LoginAuthLoginGet

> interface{} LoginAuthLoginGet(ctx).ReturnTo(returnTo).Execute()

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
	resp, r, err := apiClient.DefaultAPI.LoginAuthLoginGet(context.Background()).ReturnTo(returnTo).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.LoginAuthLoginGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `LoginAuthLoginGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.LoginAuthLoginGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiLoginAuthLoginGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returnTo** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## LogoutAuthLogoutPost

> interface{} LogoutAuthLogoutPost(ctx).Csrf(csrf).Execute()

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
	resp, r, err := apiClient.DefaultAPI.LogoutAuthLogoutPost(context.Background()).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.LogoutAuthLogoutPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `LogoutAuthLogoutPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.LogoutAuthLogoutPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiLogoutAuthLogoutPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MarketingGet

> string MarketingGet(ctx).Execute()

Marketing

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
	resp, r, err := apiClient.DefaultAPI.MarketingGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.MarketingGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MarketingGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.MarketingGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiMarketingGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MarketplaceBrowseMarketplaceGet

> string MarketplaceBrowseMarketplaceGet(ctx).Execute()

Marketplace Browse

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
	resp, r, err := apiClient.DefaultAPI.MarketplaceBrowseMarketplaceGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.MarketplaceBrowseMarketplaceGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MarketplaceBrowseMarketplaceGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.MarketplaceBrowseMarketplaceGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiMarketplaceBrowseMarketplaceGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MarketplaceDetailMarketplaceSlugGet

> string MarketplaceDetailMarketplaceSlugGet(ctx, slug).Execute()

Marketplace Detail

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
	slug := "slug_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.MarketplaceDetailMarketplaceSlugGet(context.Background(), slug).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.MarketplaceDetailMarketplaceSlugGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MarketplaceDetailMarketplaceSlugGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.MarketplaceDetailMarketplaceSlugGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**slug** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiMarketplaceDetailMarketplaceSlugGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


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


## MeUsageV0DrivesMeUsageGet

> interface{} MeUsageV0DrivesMeUsageGet(ctx).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.MeUsageV0DrivesMeUsageGet(context.Background()).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.MeUsageV0DrivesMeUsageGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MeUsageV0DrivesMeUsageGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.MeUsageV0DrivesMeUsageGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiMeUsageV0DrivesMeUsageGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MeV0DrivesMeGet

> interface{} MeV0DrivesMeGet(ctx).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.MeV0DrivesMeGet(context.Background()).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.MeV0DrivesMeGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MeV0DrivesMeGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.MeV0DrivesMeGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiMeV0DrivesMeGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MoveArtifactRouteV0ArtifactsArtIdMovePost

> ArtifactOut MoveArtifactRouteV0ArtifactsArtIdMovePost(ctx, artId).ArtifactMoveIn(artifactMoveIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.MoveArtifactRouteV0ArtifactsArtIdMovePost(context.Background(), artId).ArtifactMoveIn(artifactMoveIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MoveFolderByIdV0FoldersFldIdMovePost

> FolderOut MoveFolderByIdV0FoldersFldIdMovePost(ctx, fldId).FolderMoveIn(folderMoveIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.MoveFolderByIdV0FoldersFldIdMovePost(context.Background(), fldId).FolderMoveIn(folderMoveIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MoveFolderByPathV0FoldersPathMovePost

> FolderOut MoveFolderByPathV0FoldersPathMovePost(ctx, path).FolderMoveIn(folderMoveIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.MoveFolderByPathV0FoldersPathMovePost(context.Background(), path).FolderMoveIn(folderMoveIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## OauthDisconnectWebOauthDisconnectPost

> interface{} OauthDisconnectWebOauthDisconnectPost(ctx).ChainId(chainId).Csrf(csrf).Execute()

Oauth Disconnect



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
	chainId := "chainId_example" // string | 
	csrf := "csrf_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.OauthDisconnectWebOauthDisconnectPost(context.Background()).ChainId(chainId).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.OauthDisconnectWebOauthDisconnectPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `OauthDisconnectWebOauthDisconnectPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.OauthDisconnectWebOauthDisconnectPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiOauthDisconnectWebOauthDisconnectPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chainId** | **string** |  | 
 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchArtifactRouteV0ArtifactsArtIdPatch

> ArtifactOut PatchArtifactRouteV0ArtifactsArtIdPatch(ctx, artId).ArtifactPatchIn(artifactPatchIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PatchArtifactRouteV0ArtifactsArtIdPatch(context.Background(), artId).ArtifactPatchIn(artifactPatchIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchFolderByIdV0FoldersFldIdPatch

> FolderOut PatchFolderByIdV0FoldersFldIdPatch(ctx, fldId).FolderPatchIn(folderPatchIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PatchFolderByIdV0FoldersFldIdPatch(context.Background(), fldId).FolderPatchIn(folderPatchIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchFolderByPathV0FoldersPathPatch

> FolderOut PatchFolderByPathV0FoldersPathPatch(ctx, path).FolderPatchIn(folderPatchIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PatchFolderByPathV0FoldersPathPatch(context.Background(), path).FolderPatchIn(folderPatchIn).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchGrantRouteV0GrantsGrnIdPatch

> GrantOut PatchGrantRouteV0GrantsGrnIdPatch(ctx, grnId).GrantPatchIn(grantPatchIn).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PatchGrantRouteV0GrantsGrnIdPatch(context.Background(), grnId).GrantPatchIn(grantPatchIn).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PostDescribeV0QueryDescribePost

> interface{} PostDescribeV0QueryDescribePost(ctx).DescribeIn(describeIn).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PostDescribeV0QueryDescribePost(context.Background()).DescribeIn(describeIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PostDescribeV0QueryDescribePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PostDescribeV0QueryDescribePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PostDescribeV0QueryDescribePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPostDescribeV0QueryDescribePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **describeIn** | [**DescribeIn**](DescribeIn.md) |  | 
 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PostFeedbackV0FeedbackPost

> interface{} PostFeedbackV0FeedbackPost(ctx).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PostFeedbackV0FeedbackPost(context.Background()).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PostFeedbackV0FeedbackPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PostFeedbackV0FeedbackPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PostFeedbackV0FeedbackPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPostFeedbackV0FeedbackPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PostLookupValuesV0QueryLookupValuesPost

> interface{} PostLookupValuesV0QueryLookupValuesPost(ctx).LookupValuesIn(lookupValuesIn).Authorization(authorization).Execute()

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
	lookupValuesIn := *openapiclient.NewLookupValuesIn("Dataset_example", "Column_example") // LookupValuesIn | 
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PostLookupValuesV0QueryLookupValuesPost(context.Background()).LookupValuesIn(lookupValuesIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PostLookupValuesV0QueryLookupValuesPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PostLookupValuesV0QueryLookupValuesPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PostLookupValuesV0QueryLookupValuesPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPostLookupValuesV0QueryLookupValuesPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookupValuesIn** | [**LookupValuesIn**](LookupValuesIn.md) |  | 
 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PostQueryV0QueryPost

> interface{} PostQueryV0QueryPost(ctx).QueryIn(queryIn).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PostQueryV0QueryPost(context.Background()).QueryIn(queryIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PostQueryV0QueryPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PostQueryV0QueryPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PostQueryV0QueryPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPostQueryV0QueryPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryIn** | [**QueryIn**](QueryIn.md) |  | 
 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PrivacyPagePrivacyGet

> string PrivacyPagePrivacyGet(ctx).Execute()

Privacy Page



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
	resp, r, err := apiClient.DefaultAPI.PrivacyPagePrivacyGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PrivacyPagePrivacyGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PrivacyPagePrivacyGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PrivacyPagePrivacyGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiPrivacyPagePrivacyGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ProjectPreviewPageFFldIdPreviewGet

> string ProjectPreviewPageFFldIdPreviewGet(ctx, fldId).Execute()

Project Preview Page



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
	resp, r, err := apiClient.DefaultAPI.ProjectPreviewPageFFldIdPreviewGet(context.Background(), fldId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ProjectPreviewPageFFldIdPreviewGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ProjectPreviewPageFFldIdPreviewGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ProjectPreviewPageFFldIdPreviewGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiProjectPreviewPageFFldIdPreviewGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


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


## PublisherProfilePublishersHandleGet

> string PublisherProfilePublishersHandleGet(ctx, handle).Execute()

Publisher Profile

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
	handle := "handle_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PublisherProfilePublishersHandleGet(context.Background(), handle).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PublisherProfilePublishersHandleGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PublisherProfilePublishersHandleGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.PublisherProfilePublishersHandleGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**handle** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiPublisherProfilePublishersHandleGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


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


## PutArtifactV0ArtifactsPathPut

> ArtifactOut PutArtifactV0ArtifactsPathPut(ctx, path).ContentType(contentType).XAgentdriveLabels(xAgentdriveLabels).XAgentdriveMetadata(xAgentdriveMetadata).XAgentdriveSource(xAgentdriveSource).XAgentdriveActor(xAgentdriveActor).XAgentdriveChangeSummary(xAgentdriveChangeSummary).XAgentdriveChecksum(xAgentdriveChecksum).ContentMd5(contentMd5).IfMatch(ifMatch).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PutArtifactV0ArtifactsPathPut(context.Background(), path).ContentType(contentType).XAgentdriveLabels(xAgentdriveLabels).XAgentdriveMetadata(xAgentdriveMetadata).XAgentdriveSource(xAgentdriveSource).XAgentdriveActor(xAgentdriveActor).XAgentdriveChangeSummary(xAgentdriveChangeSummary).XAgentdriveChecksum(xAgentdriveChecksum).ContentMd5(contentMd5).IfMatch(ifMatch).IfNoneMatch(ifNoneMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PutProjectV0ProjectsFldIdPut

> interface{} PutProjectV0ProjectsFldIdPut(ctx, fldId).ProjectConfigIn(projectConfigIn).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.PutProjectV0ProjectsFldIdPut(context.Background(), fldId).ProjectConfigIn(projectConfigIn).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.PutProjectV0ProjectsFldIdPut``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PutProjectV0ProjectsFldIdPut`: interface{}
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
 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RecoveryNewAccountAuthRecoveryNewAccountPost

> interface{} RecoveryNewAccountAuthRecoveryNewAccountPost(ctx).Csrf(csrf).Claim(claim).Execute()

Recovery New Account



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
	claim := "claim_example" // string |  (optional) (default to "bind")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RecoveryNewAccountAuthRecoveryNewAccountPost(context.Background()).Csrf(csrf).Claim(claim).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RecoveryNewAccountAuthRecoveryNewAccountPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RecoveryNewAccountAuthRecoveryNewAccountPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RecoveryNewAccountAuthRecoveryNewAccountPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRecoveryNewAccountAuthRecoveryNewAccountPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **string** |  | 
 **claim** | **string** |  | [default to &quot;bind&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RecoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGet

> interface{} RecoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGet(ctx).Execute()

Recovery New Account Expired



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
	resp, r, err := apiClient.DefaultAPI.RecoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RecoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RecoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RecoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiRecoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGetRequest struct via the builder pattern


### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RecoveryPageAuthRecoveryGet

> interface{} RecoveryPageAuthRecoveryGet(ctx).Execute()

Recovery Page



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
	resp, r, err := apiClient.DefaultAPI.RecoveryPageAuthRecoveryGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RecoveryPageAuthRecoveryGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RecoveryPageAuthRecoveryGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RecoveryPageAuthRecoveryGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiRecoveryPageAuthRecoveryGetRequest struct via the builder pattern


### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RecoveryRestoreAuthRecoveryRestorePost

> interface{} RecoveryRestoreAuthRecoveryRestorePost(ctx).Csrf(csrf).Execute()

Recovery Restore



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
	resp, r, err := apiClient.DefaultAPI.RecoveryRestoreAuthRecoveryRestorePost(context.Background()).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RecoveryRestoreAuthRecoveryRestorePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RecoveryRestoreAuthRecoveryRestorePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RecoveryRestoreAuthRecoveryRestorePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRecoveryRestoreAuthRecoveryRestorePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RedeemShareSShareKeyGet

> interface{} RedeemShareSShareKeyGet(ctx, shareKey).Execute()

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
	// response from `RedeemShareSShareKeyGet`: interface{}
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

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RedeemShareWithPasswordSShareKeyPost

> interface{} RedeemShareWithPasswordSShareKeyPost(ctx, shareKey).Password(password).Execute()

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
	// response from `RedeemShareWithPasswordSShareKeyPost`: interface{}
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

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RemoveMemberWebWebMembersTargetUserIdRemovePost

> interface{} RemoveMemberWebWebMembersTargetUserIdRemovePost(ctx, targetUserId).Csrf(csrf).OrganizationId(organizationId).Execute()

Remove Member Web



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
	targetUserId := "targetUserId_example" // string | 
	csrf := "csrf_example" // string | 
	organizationId := "organizationId_example" // string |  (optional) (default to "")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RemoveMemberWebWebMembersTargetUserIdRemovePost(context.Background(), targetUserId).Csrf(csrf).OrganizationId(organizationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RemoveMemberWebWebMembersTargetUserIdRemovePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RemoveMemberWebWebMembersTargetUserIdRemovePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RemoveMemberWebWebMembersTargetUserIdRemovePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**targetUserId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRemoveMemberWebWebMembersTargetUserIdRemovePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **csrf** | **string** |  | 
 **organizationId** | **string** |  | [default to &quot;&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RenameDriveWebWebDrivesDriveIdRenamePost

> interface{} RenameDriveWebWebDrivesDriveIdRenamePost(ctx, driveId).Name(name).Csrf(csrf).Execute()

Rename Drive Web



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
	name := "name_example" // string | 
	csrf := "csrf_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RenameDriveWebWebDrivesDriveIdRenamePost(context.Background(), driveId).Name(name).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RenameDriveWebWebDrivesDriveIdRenamePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RenameDriveWebWebDrivesDriveIdRenamePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RenameDriveWebWebDrivesDriveIdRenamePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**driveId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRenameDriveWebWebDrivesDriveIdRenamePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **name** | **string** |  | 
 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RenameWorkspaceWebWebWorkspacesOrgIdRenamePost

> interface{} RenameWorkspaceWebWebWorkspacesOrgIdRenamePost(ctx, orgId).Name(name).Csrf(csrf).Execute()

Rename Workspace Web



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
	name := "name_example" // string | 
	csrf := "csrf_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RenameWorkspaceWebWebWorkspacesOrgIdRenamePost(context.Background(), orgId).Name(name).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RenameWorkspaceWebWebWorkspacesOrgIdRenamePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RenameWorkspaceWebWebWorkspacesOrgIdRenamePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RenameWorkspaceWebWebWorkspacesOrgIdRenamePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**orgId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRenameWorkspaceWebWebWorkspacesOrgIdRenamePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **name** | **string** |  | 
 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ResendInvitationWebWebInvitationsInvitationIdResendPost

> interface{} ResendInvitationWebWebInvitationsInvitationIdResendPost(ctx, invitationId).Csrf(csrf).Execute()

Resend Invitation Web



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
	invitationId := "invitationId_example" // string | 
	csrf := "csrf_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ResendInvitationWebWebInvitationsInvitationIdResendPost(context.Background(), invitationId).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ResendInvitationWebWebInvitationsInvitationIdResendPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ResendInvitationWebWebInvitationsInvitationIdResendPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ResendInvitationWebWebInvitationsInvitationIdResendPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**invitationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiResendInvitationWebWebInvitationsInvitationIdResendPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreArtifactV0ArtifactsArtIdRestorePost

> ArtifactOut RestoreArtifactV0ArtifactsArtIdRestorePost(ctx, artId).Rename(rename).Overwrite(overwrite).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RestoreArtifactV0ArtifactsArtIdRestorePost(context.Background(), artId).Rename(rename).Overwrite(overwrite).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost

> ArtifactOut RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost(ctx, artId, versionNumber).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RestoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost(context.Background(), artId, versionNumber).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreDriveRouteV0DrivesDriveIdRestorePost

> interface{} RestoreDriveRouteV0DrivesDriveIdRestorePost(ctx, driveId).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RestoreDriveRouteV0DrivesDriveIdRestorePost(context.Background(), driveId).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RestoreDriveRouteV0DrivesDriveIdRestorePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreDriveRouteV0DrivesDriveIdRestorePost`: interface{}
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
 **authorization** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreFolderByIdV0FoldersFldIdRestorePost

> FolderRestoreOut RestoreFolderByIdV0FoldersFldIdRestorePost(ctx, fldId).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RestoreFolderByIdV0FoldersFldIdRestorePost(context.Background(), fldId).XAgentdriveActor(xAgentdriveActor).IfMatch(ifMatch).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**FolderRestoreOut**](FolderRestoreOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RevokeGrantWebShareRidGrantGrnIdRevokePost

> interface{} RevokeGrantWebShareRidGrantGrnIdRevokePost(ctx, rid, grnId).XCsrfToken(xCsrfToken).Execute()

Revoke Grant

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
	rid := "rid_example" // string | 
	grnId := "grnId_example" // string | 
	xCsrfToken := "xCsrfToken_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RevokeGrantWebShareRidGrantGrnIdRevokePost(context.Background(), rid, grnId).XCsrfToken(xCsrfToken).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RevokeGrantWebShareRidGrantGrnIdRevokePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RevokeGrantWebShareRidGrantGrnIdRevokePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RevokeGrantWebShareRidGrantGrnIdRevokePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**rid** | **string** |  | 
**grnId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRevokeGrantWebShareRidGrantGrnIdRevokePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xCsrfToken** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RevokeInvitationWebWebInvitationsInvitationIdRevokePost

> interface{} RevokeInvitationWebWebInvitationsInvitationIdRevokePost(ctx, invitationId).Csrf(csrf).Execute()

Revoke Invitation Web



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
	invitationId := "invitationId_example" // string | 
	csrf := "csrf_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RevokeInvitationWebWebInvitationsInvitationIdRevokePost(context.Background(), invitationId).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RevokeInvitationWebWebInvitationsInvitationIdRevokePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RevokeInvitationWebWebInvitationsInvitationIdRevokePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RevokeInvitationWebWebInvitationsInvitationIdRevokePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**invitationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRevokeInvitationWebWebInvitationsInvitationIdRevokePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RevokeKeyWebKeysRevokePost

> interface{} RevokeKeyWebKeysRevokePost(ctx).KeyId(keyId).Csrf(csrf).Execute()

Revoke Key



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
	keyId := "keyId_example" // string | 
	csrf := "csrf_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RevokeKeyWebKeysRevokePost(context.Background()).KeyId(keyId).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RevokeKeyWebKeysRevokePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RevokeKeyWebKeysRevokePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RevokeKeyWebKeysRevokePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRevokeKeyWebKeysRevokePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyId** | **string** |  | 
 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RevokeLinkWebShareRidLinkShrIdRevokePost

> interface{} RevokeLinkWebShareRidLinkShrIdRevokePost(ctx, rid, shrId).XCsrfToken(xCsrfToken).Execute()

Revoke Link

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
	rid := "rid_example" // string | 
	shrId := "shrId_example" // string | 
	xCsrfToken := "xCsrfToken_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RevokeLinkWebShareRidLinkShrIdRevokePost(context.Background(), rid, shrId).XCsrfToken(xCsrfToken).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RevokeLinkWebShareRidLinkShrIdRevokePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RevokeLinkWebShareRidLinkShrIdRevokePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RevokeLinkWebShareRidLinkShrIdRevokePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**rid** | **string** |  | 
**shrId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRevokeLinkWebShareRidLinkShrIdRevokePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **xCsrfToken** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RevokeUserTokenWebTokensRevokePost

> interface{} RevokeUserTokenWebTokensRevokePost(ctx).TokenId(tokenId).Csrf(csrf).Execute()

Revoke User Token



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
	tokenId := "tokenId_example" // string | 
	csrf := "csrf_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RevokeUserTokenWebTokensRevokePost(context.Background()).TokenId(tokenId).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.RevokeUserTokenWebTokensRevokePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RevokeUserTokenWebTokensRevokePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.RevokeUserTokenWebTokensRevokePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRevokeUserTokenWebTokensRevokePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenId** | **string** |  | 
 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RotateShareRouteV0SharesShrIdRotatePost

> ShareMintOut RotateShareRouteV0SharesShrIdRotatePost(ctx, shrId).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.RotateShareRouteV0SharesShrIdRotatePost(context.Background(), shrId).XAgentdriveActor(xAgentdriveActor).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**ShareMintOut**](ShareMintOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SearchV0SearchGet

> SearchPage SearchV0SearchGet(ctx).Q(q).Label(label).FileType(fileType).Prefix(prefix).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).Limit(limit).Authorization(authorization).Execute()

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
	authorization := "authorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.SearchV0SearchGet(context.Background()).Q(q).Label(label).FileType(fileType).Prefix(prefix).UpdatedAfter(updatedAfter).UpdatedBefore(updatedBefore).Limit(limit).Authorization(authorization).Execute()
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
 **authorization** | **string** |  | 

### Return type

[**SearchPage**](SearchPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SetMemberRoleWebWebMembersTargetUserIdRolePost

> interface{} SetMemberRoleWebWebMembersTargetUserIdRolePost(ctx, targetUserId).Role(role).Csrf(csrf).Execute()

Set Member Role Web



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
	targetUserId := "targetUserId_example" // string | 
	role := "role_example" // string | 
	csrf := "csrf_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.SetMemberRoleWebWebMembersTargetUserIdRolePost(context.Background(), targetUserId).Role(role).Csrf(csrf).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.SetMemberRoleWebWebMembersTargetUserIdRolePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SetMemberRoleWebWebMembersTargetUserIdRolePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.SetMemberRoleWebWebMembersTargetUserIdRolePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**targetUserId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiSetMemberRoleWebWebMembersTargetUserIdRolePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **role** | **string** |  | 
 **csrf** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SetPublicWebShareRidPublicPost

> interface{} SetPublicWebShareRidPublicPost(ctx, rid).PublicIn(publicIn).XCsrfToken(xCsrfToken).Execute()

Set Public



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
	rid := "rid_example" // string | 
	publicIn := *openapiclient.NewPublicIn(false) // PublicIn | 
	xCsrfToken := "xCsrfToken_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.SetPublicWebShareRidPublicPost(context.Background(), rid).PublicIn(publicIn).XCsrfToken(xCsrfToken).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.SetPublicWebShareRidPublicPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SetPublicWebShareRidPublicPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.SetPublicWebShareRidPublicPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**rid** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiSetPublicWebShareRidPublicPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **publicIn** | [**PublicIn**](PublicIn.md) |  | 
 **xCsrfToken** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SetSealWebShareRidSealPost

> interface{} SetSealWebShareRidSealPost(ctx, rid).SealIn(sealIn).XCsrfToken(xCsrfToken).Execute()

Set Seal



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
	rid := "rid_example" // string | 
	sealIn := *openapiclient.NewSealIn(false) // SealIn | 
	xCsrfToken := "xCsrfToken_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.SetSealWebShareRidSealPost(context.Background(), rid).SealIn(sealIn).XCsrfToken(xCsrfToken).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.SetSealWebShareRidSealPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SetSealWebShareRidSealPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.SetSealWebShareRidSealPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**rid** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiSetSealWebShareRidSealPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **sealIn** | [**SealIn**](SealIn.md) |  | 
 **xCsrfToken** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SettingsAccountSettingsGet

> string SettingsAccountSettingsGet(ctx).Execute()

Settings Account



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
	resp, r, err := apiClient.DefaultAPI.SettingsAccountSettingsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.SettingsAccountSettingsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SettingsAccountSettingsGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.SettingsAccountSettingsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiSettingsAccountSettingsGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SettingsApiKeysSettingsApiKeysGet

> string SettingsApiKeysSettingsApiKeysGet(ctx).Execute()

Settings Api Keys



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
	resp, r, err := apiClient.DefaultAPI.SettingsApiKeysSettingsApiKeysGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.SettingsApiKeysSettingsApiKeysGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SettingsApiKeysSettingsApiKeysGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.SettingsApiKeysSettingsApiKeysGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiSettingsApiKeysSettingsApiKeysGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SettingsQuickstartSettingsQuickstartGet

> string SettingsQuickstartSettingsQuickstartGet(ctx).Execute()

Settings Quickstart



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
	resp, r, err := apiClient.DefaultAPI.SettingsQuickstartSettingsQuickstartGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.SettingsQuickstartSettingsQuickstartGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SettingsQuickstartSettingsQuickstartGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.SettingsQuickstartSettingsQuickstartGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiSettingsQuickstartSettingsQuickstartGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SettingsWorkspaceSettingsWorkspaceGet

> string SettingsWorkspaceSettingsWorkspaceGet(ctx).Execute()

Settings Workspace



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
	resp, r, err := apiClient.DefaultAPI.SettingsWorkspaceSettingsWorkspaceGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.SettingsWorkspaceSettingsWorkspaceGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SettingsWorkspaceSettingsWorkspaceGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.SettingsWorkspaceSettingsWorkspaceGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiSettingsWorkspaceSettingsWorkspaceGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SharedFilesSharedGet

> string SharedFilesSharedGet(ctx).Execute()

Shared Files

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
	resp, r, err := apiClient.DefaultAPI.SharedFilesSharedGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.SharedFilesSharedGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SharedFilesSharedGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.SharedFilesSharedGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiSharedFilesSharedGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SwitchDriveWebSwitchPost

> interface{} SwitchDriveWebSwitchPost(ctx).Csrf(csrf).DriveId(driveId).OrganizationId(organizationId).Execute()

Switch Drive



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
	driveId := "driveId_example" // string |  (optional) (default to "")
	organizationId := "organizationId_example" // string |  (optional) (default to "")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.SwitchDriveWebSwitchPost(context.Background()).Csrf(csrf).DriveId(driveId).OrganizationId(organizationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.SwitchDriveWebSwitchPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SwitchDriveWebSwitchPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.SwitchDriveWebSwitchPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSwitchDriveWebSwitchPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **string** |  | 
 **driveId** | **string** |  | [default to &quot;&quot;]
 **organizationId** | **string** |  | [default to &quot;&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TermsPageTermsGet

> string TermsPageTermsGet(ctx).Execute()

Terms Page



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
	resp, r, err := apiClient.DefaultAPI.TermsPageTermsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.TermsPageTermsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TermsPageTermsGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.TermsPageTermsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiTermsPageTermsGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ToggleIndexingWebAccountIndexingPost

> interface{} ToggleIndexingWebAccountIndexingPost(ctx).Csrf(csrf).Enabled(enabled).Execute()

Toggle Indexing



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
	enabled := "enabled_example" // string |  (optional) (default to "")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.ToggleIndexingWebAccountIndexingPost(context.Background()).Csrf(csrf).Enabled(enabled).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ToggleIndexingWebAccountIndexingPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ToggleIndexingWebAccountIndexingPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ToggleIndexingWebAccountIndexingPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiToggleIndexingWebAccountIndexingPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csrf** | **string** |  | 
 **enabled** | **string** |  | [default to &quot;&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TrashWebTrashGet

> string TrashWebTrashGet(ctx).Execute()

Trash



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
	resp, r, err := apiClient.DefaultAPI.TrashWebTrashGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.TrashWebTrashGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TrashWebTrashGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.TrashWebTrashGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiTrashWebTrashGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ViewArtifactHeadAArtIdHeadGet

> interface{} ViewArtifactHeadAArtIdHeadGet(ctx, artId).Execute()

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
	// response from `ViewArtifactHeadAArtIdHeadGet`: interface{}
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

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ViewArtifactVersionVArtIdVersionGet

> interface{} ViewArtifactVersionVArtIdVersionGet(ctx, artId, version).Raw(raw).Download(download).Execute()

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
	// response from `ViewArtifactVersionVArtIdVersionGet`: interface{}
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

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ViewFileDriveIdPathGet

> interface{} ViewFileDriveIdPathGet(ctx, driveId, path).Raw(raw).Download(download).Execute()

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
	// response from `ViewFileDriveIdPathGet`: interface{}
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

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ViewPermalinkArtifactAArtIdGet

> interface{} ViewPermalinkArtifactAArtIdGet(ctx, artId).Execute()

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
	resp, r, err := apiClient.DefaultAPI.ViewPermalinkArtifactAArtIdGet(context.Background(), artId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ViewPermalinkArtifactAArtIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ViewPermalinkArtifactAArtIdGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ViewPermalinkArtifactAArtIdGet`: %v\n", resp)
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

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ViewPermalinkFolderFFldIdGet

> interface{} ViewPermalinkFolderFFldIdGet(ctx, fldId).Execute()

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
	resp, r, err := apiClient.DefaultAPI.ViewPermalinkFolderFFldIdGet(context.Background(), fldId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.ViewPermalinkFolderFFldIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ViewPermalinkFolderFFldIdGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.ViewPermalinkFolderFFldIdGet`: %v\n", resp)
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

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebArtifactIndexedWebArtifactsIndexedGet

> interface{} WebArtifactIndexedWebArtifactsIndexedGet(ctx).Path(path).Execute()

Web Artifact Indexed



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
	resp, r, err := apiClient.DefaultAPI.WebArtifactIndexedWebArtifactsIndexedGet(context.Background()).Path(path).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebArtifactIndexedWebArtifactsIndexedGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebArtifactIndexedWebArtifactsIndexedGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebArtifactIndexedWebArtifactsIndexedGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebArtifactIndexedWebArtifactsIndexedGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebCopyArtifactWebArtifactsCopyPost

> interface{} WebCopyArtifactWebArtifactsCopyPost(ctx).ArtId(artId).NewPath(newPath).Csrf(csrf).ReturnTo(returnTo).Execute()

Web Copy Artifact

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
	newPath := "newPath_example" // string | 
	csrf := "csrf_example" // string | 
	returnTo := "returnTo_example" // string |  (optional) (default to "/dashboard")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebCopyArtifactWebArtifactsCopyPost(context.Background()).ArtId(artId).NewPath(newPath).Csrf(csrf).ReturnTo(returnTo).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebCopyArtifactWebArtifactsCopyPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebCopyArtifactWebArtifactsCopyPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebCopyArtifactWebArtifactsCopyPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebCopyArtifactWebArtifactsCopyPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artId** | **string** |  | 
 **newPath** | **string** |  | 
 **csrf** | **string** |  | 
 **returnTo** | **string** |  | [default to &quot;/dashboard&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebDeleteArtifactOpWebArtifactsDeletePost

> interface{} WebDeleteArtifactOpWebArtifactsDeletePost(ctx).Path(path).Csrf(csrf).ReturnTo(returnTo).Execute()

Web Delete Artifact Op

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
	csrf := "csrf_example" // string | 
	returnTo := "returnTo_example" // string |  (optional) (default to "/dashboard")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebDeleteArtifactOpWebArtifactsDeletePost(context.Background()).Path(path).Csrf(csrf).ReturnTo(returnTo).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebDeleteArtifactOpWebArtifactsDeletePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebDeleteArtifactOpWebArtifactsDeletePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebDeleteArtifactOpWebArtifactsDeletePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebDeleteArtifactOpWebArtifactsDeletePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **string** |  | 
 **csrf** | **string** |  | 
 **returnTo** | **string** |  | [default to &quot;/dashboard&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebDeleteArtifactWebArtifactsPathDelete

> interface{} WebDeleteArtifactWebArtifactsPathDelete(ctx, path).XCsrfToken(xCsrfToken).Execute()

Web Delete Artifact



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
	xCsrfToken := "xCsrfToken_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebDeleteArtifactWebArtifactsPathDelete(context.Background(), path).XCsrfToken(xCsrfToken).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebDeleteArtifactWebArtifactsPathDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebDeleteArtifactWebArtifactsPathDelete`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebDeleteArtifactWebArtifactsPathDelete`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiWebDeleteArtifactWebArtifactsPathDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xCsrfToken** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebDeleteFolderWebFoldersDeletePost

> interface{} WebDeleteFolderWebFoldersDeletePost(ctx).FldId(fldId).Csrf(csrf).Recursive(recursive).ReturnTo(returnTo).Execute()

Web Delete Folder

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
	csrf := "csrf_example" // string | 
	recursive := "recursive_example" // string |  (optional) (default to "")
	returnTo := "returnTo_example" // string |  (optional) (default to "/dashboard")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebDeleteFolderWebFoldersDeletePost(context.Background()).FldId(fldId).Csrf(csrf).Recursive(recursive).ReturnTo(returnTo).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebDeleteFolderWebFoldersDeletePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebDeleteFolderWebFoldersDeletePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebDeleteFolderWebFoldersDeletePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebDeleteFolderWebFoldersDeletePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fldId** | **string** |  | 
 **csrf** | **string** |  | 
 **recursive** | **string** |  | [default to &quot;&quot;]
 **returnTo** | **string** |  | [default to &quot;/dashboard&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebMoveFolderWebFoldersMovePost

> interface{} WebMoveFolderWebFoldersMovePost(ctx).FldId(fldId).NewPath(newPath).Csrf(csrf).ReturnTo(returnTo).Execute()

Web Move Folder

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
	newPath := "newPath_example" // string | 
	csrf := "csrf_example" // string | 
	returnTo := "returnTo_example" // string |  (optional) (default to "/dashboard")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebMoveFolderWebFoldersMovePost(context.Background()).FldId(fldId).NewPath(newPath).Csrf(csrf).ReturnTo(returnTo).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebMoveFolderWebFoldersMovePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebMoveFolderWebFoldersMovePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebMoveFolderWebFoldersMovePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebMoveFolderWebFoldersMovePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fldId** | **string** |  | 
 **newPath** | **string** |  | 
 **csrf** | **string** |  | 
 **returnTo** | **string** |  | [default to &quot;/dashboard&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebNewFolderWebFoldersNewPost

> interface{} WebNewFolderWebFoldersNewPost(ctx).Name(name).Csrf(csrf).Parent(parent).ReturnTo(returnTo).Execute()

Web New Folder

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
	name := "name_example" // string | 
	csrf := "csrf_example" // string | 
	parent := "parent_example" // string |  (optional) (default to "")
	returnTo := "returnTo_example" // string |  (optional) (default to "/dashboard")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebNewFolderWebFoldersNewPost(context.Background()).Name(name).Csrf(csrf).Parent(parent).ReturnTo(returnTo).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebNewFolderWebFoldersNewPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebNewFolderWebFoldersNewPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebNewFolderWebFoldersNewPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebNewFolderWebFoldersNewPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **string** |  | 
 **csrf** | **string** |  | 
 **parent** | **string** |  | [default to &quot;&quot;]
 **returnTo** | **string** |  | [default to &quot;/dashboard&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebProjectCompileWebProjectsFldIdCompilePost

> interface{} WebProjectCompileWebProjectsFldIdCompilePost(ctx, fldId).Csrf(csrf).Engine(engine).Entrypoint(entrypoint).Execute()

Web Project Compile

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
	csrf := "csrf_example" // string | 
	engine := "engine_example" // string |  (optional) (default to "")
	entrypoint := "entrypoint_example" // string |  (optional) (default to "")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebProjectCompileWebProjectsFldIdCompilePost(context.Background(), fldId).Csrf(csrf).Engine(engine).Entrypoint(entrypoint).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebProjectCompileWebProjectsFldIdCompilePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebProjectCompileWebProjectsFldIdCompilePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebProjectCompileWebProjectsFldIdCompilePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiWebProjectCompileWebProjectsFldIdCompilePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **csrf** | **string** |  | 
 **engine** | **string** |  | [default to &quot;&quot;]
 **entrypoint** | **string** |  | [default to &quot;&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebProjectFilesWebProjectsFldIdFilesGet

> interface{} WebProjectFilesWebProjectsFldIdFilesGet(ctx, fldId).Execute()

Web Project Files



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
	resp, r, err := apiClient.DefaultAPI.WebProjectFilesWebProjectsFldIdFilesGet(context.Background(), fldId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebProjectFilesWebProjectsFldIdFilesGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebProjectFilesWebProjectsFldIdFilesGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebProjectFilesWebProjectsFldIdFilesGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiWebProjectFilesWebProjectsFldIdFilesGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebProjectPreviewWebProjectsFldIdPreviewGet

> interface{} WebProjectPreviewWebProjectsFldIdPreviewGet(ctx, fldId).Execute()

Web Project Preview



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
	resp, r, err := apiClient.DefaultAPI.WebProjectPreviewWebProjectsFldIdPreviewGet(context.Background(), fldId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebProjectPreviewWebProjectsFldIdPreviewGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebProjectPreviewWebProjectsFldIdPreviewGet`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebProjectPreviewWebProjectsFldIdPreviewGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fldId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiWebProjectPreviewWebProjectsFldIdPreviewGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebPutArtifactWebArtifactsPathPut

> interface{} WebPutArtifactWebArtifactsPathPut(ctx, path).XCsrfToken(xCsrfToken).Execute()

Web Put Artifact



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
	xCsrfToken := "xCsrfToken_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebPutArtifactWebArtifactsPathPut(context.Background(), path).XCsrfToken(xCsrfToken).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebPutArtifactWebArtifactsPathPut``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebPutArtifactWebArtifactsPathPut`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebPutArtifactWebArtifactsPathPut`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**path** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiWebPutArtifactWebArtifactsPathPutRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **xCsrfToken** | **string** |  | 

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebRenameArtifactWebArtifactsRenamePost

> interface{} WebRenameArtifactWebArtifactsRenamePost(ctx).ArtId(artId).NewPath(newPath).Csrf(csrf).ReturnTo(returnTo).Execute()

Web Rename Artifact

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
	newPath := "newPath_example" // string | 
	csrf := "csrf_example" // string | 
	returnTo := "returnTo_example" // string |  (optional) (default to "/dashboard")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebRenameArtifactWebArtifactsRenamePost(context.Background()).ArtId(artId).NewPath(newPath).Csrf(csrf).ReturnTo(returnTo).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebRenameArtifactWebArtifactsRenamePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebRenameArtifactWebArtifactsRenamePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebRenameArtifactWebArtifactsRenamePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebRenameArtifactWebArtifactsRenamePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artId** | **string** |  | 
 **newPath** | **string** |  | 
 **csrf** | **string** |  | 
 **returnTo** | **string** |  | [default to &quot;/dashboard&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebRestoreArtifactWebArtifactsRestorePost

> interface{} WebRestoreArtifactWebArtifactsRestorePost(ctx).ArtId(artId).Csrf(csrf).ReturnTo(returnTo).Execute()

Web Restore Artifact

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
	csrf := "csrf_example" // string | 
	returnTo := "returnTo_example" // string |  (optional) (default to "/web/trash")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebRestoreArtifactWebArtifactsRestorePost(context.Background()).ArtId(artId).Csrf(csrf).ReturnTo(returnTo).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebRestoreArtifactWebArtifactsRestorePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebRestoreArtifactWebArtifactsRestorePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebRestoreArtifactWebArtifactsRestorePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebRestoreArtifactWebArtifactsRestorePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artId** | **string** |  | 
 **csrf** | **string** |  | 
 **returnTo** | **string** |  | [default to &quot;/web/trash&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebRestoreFolderWebFoldersRestorePost

> interface{} WebRestoreFolderWebFoldersRestorePost(ctx).FldId(fldId).Csrf(csrf).ReturnTo(returnTo).Execute()

Web Restore Folder

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
	csrf := "csrf_example" // string | 
	returnTo := "returnTo_example" // string |  (optional) (default to "/web/trash")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebRestoreFolderWebFoldersRestorePost(context.Background()).FldId(fldId).Csrf(csrf).ReturnTo(returnTo).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebRestoreFolderWebFoldersRestorePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebRestoreFolderWebFoldersRestorePost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebRestoreFolderWebFoldersRestorePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebRestoreFolderWebFoldersRestorePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fldId** | **string** |  | 
 **csrf** | **string** |  | 
 **returnTo** | **string** |  | [default to &quot;/web/trash&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebSetMetadataWebSetPost

> interface{} WebSetMetadataWebSetPost(ctx).Target(target).Csrf(csrf).Description(description).ReturnTo(returnTo).Execute()

Web Set Metadata



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
	target := "target_example" // string | 
	csrf := "csrf_example" // string | 
	description := "description_example" // string |  (optional) (default to "")
	returnTo := "returnTo_example" // string |  (optional) (default to "/dashboard")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebSetMetadataWebSetPost(context.Background()).Target(target).Csrf(csrf).Description(description).ReturnTo(returnTo).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebSetMetadataWebSetPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebSetMetadataWebSetPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebSetMetadataWebSetPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebSetMetadataWebSetPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **string** |  | 
 **csrf** | **string** |  | 
 **description** | **string** |  | [default to &quot;&quot;]
 **returnTo** | **string** |  | [default to &quot;/dashboard&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebUploadWebUploadPost

> interface{} WebUploadWebUploadPost(ctx).File(file).Csrf(csrf).DestDir(destDir).ReturnTo(returnTo).Execute()

Web Upload

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
	file := os.NewFile(1234, "some_file") // *os.File | 
	csrf := "csrf_example" // string | 
	destDir := "destDir_example" // string |  (optional) (default to "")
	returnTo := "returnTo_example" // string |  (optional) (default to "/dashboard")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DefaultAPI.WebUploadWebUploadPost(context.Background()).File(file).Csrf(csrf).DestDir(destDir).ReturnTo(returnTo).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebUploadWebUploadPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebUploadWebUploadPost`: interface{}
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebUploadWebUploadPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiWebUploadWebUploadPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | ***os.File** |  | 
 **csrf** | **string** |  | 
 **destDir** | **string** |  | [default to &quot;&quot;]
 **returnTo** | **string** |  | [default to &quot;/dashboard&quot;]

### Return type

**interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WebhooksPageWebhooksGet

> string WebhooksPageWebhooksGet(ctx).Execute()

Webhooks Page

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
	resp, r, err := apiClient.DefaultAPI.WebhooksPageWebhooksGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WebhooksPageWebhooksGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WebhooksPageWebhooksGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WebhooksPageWebhooksGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiWebhooksPageWebhooksGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## WelcomeWelcomeGet

> string WelcomeWelcomeGet(ctx).Execute()

Welcome



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
	resp, r, err := apiClient.DefaultAPI.WelcomeWelcomeGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DefaultAPI.WelcomeWelcomeGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `WelcomeWelcomeGet`: string
	fmt.Fprintf(os.Stdout, "Response from `DefaultAPI.WelcomeWelcomeGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiWelcomeWelcomeGetRequest struct via the builder pattern


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

