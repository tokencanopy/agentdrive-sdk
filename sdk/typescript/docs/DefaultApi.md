# DefaultApi

All URIs are relative to *https://api.agentdrive.run*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**acceptInvitationInvitationsTokenGet**](DefaultApi.md#acceptinvitationinvitationstokenget) | **GET** /invitations/{token} | Accept Invitation |
| [**activityFeedActivityGet**](DefaultApi.md#activityfeedactivityget) | **GET** /activity | Activity Feed |
| [**addGrantWebShareRidGrantPost**](DefaultApi.md#addgrantwebshareridgrantpost) | **POST** /web/share/{rid}/grant | Add Grant |
| [**artifactDetailPreviewPreviewArtifactDetailGet**](DefaultApi.md#artifactdetailpreviewpreviewartifactdetailget) | **GET** /preview/artifact-detail | Artifact Detail Preview |
| [**beginUploadV0UploadsPost**](DefaultApi.md#beginuploadv0uploadspost) | **POST** /v0/uploads | Begin a large (direct-to-GCS) upload |
| [**callbackAuthCallbackGet**](DefaultApi.md#callbackauthcallbackget) | **GET** /auth/callback | Callback |
| [**cancelJobV0JobsJobIdCancelPost**](DefaultApi.md#canceljobv0jobsjobidcancelpost) | **POST** /v0/jobs/{job_id}/cancel | Cancel a queued/running job |
| [**collectionDetailCollectionsSlugGet**](DefaultApi.md#collectiondetailcollectionsslugget) | **GET** /collections/{slug} | Collection Detail |
| [**commitUploadV0UploadsUploadIdCommitPost**](DefaultApi.md#commituploadv0uploadsuploadidcommitpost) | **POST** /v0/uploads/{upload_id}/commit | Commit a large (direct-to-GCS) upload |
| [**connectorsPageConnectorsGet**](DefaultApi.md#connectorspageconnectorsget) | **GET** /connectors | Connectors Page |
| [**copyArtifactRouteV0ArtifactsArtIdCopyPost**](DefaultApi.md#copyartifactroutev0artifactsartidcopypost) | **POST** /v0/artifacts/{art_id}/copy | Duplicate an artifact to a new path (CAS-shared, new ID) |
| [**createDriveKeyWebWebDrivesDriveIdKeysCreatePost**](DefaultApi.md#createdrivekeywebwebdrivesdriveidkeyscreatepost) | **POST** /web/drives/{drive_id}/keys/create | Create Drive Key Web |
| [**createDriveWebWebDrivesPost**](DefaultApi.md#createdrivewebwebdrivespost) | **POST** /web/drives | Create Drive Web |
| [**createFolderByPathV0FoldersPathPost**](DefaultApi.md#createfolderbypathv0folderspathpost) | **POST** /v0/folders/{path} | Create a folder (idempotent) |
| [**createGrantRouteV0GrantsPost**](DefaultApi.md#creategrantroutev0grantspost) | **POST** /v0/grants | Create (or fetch) a per-principal grant on a resource |
| [**createKeyWebKeysCreatePost**](DefaultApi.md#createkeywebkeyscreatepost) | **POST** /web/keys/create | Create Key |
| [**createLinkWebShareRidLinkPost**](DefaultApi.md#createlinkwebshareridlinkpost) | **POST** /web/share/{rid}/link | Create Link |
| [**createShareRouteV0SharesPost**](DefaultApi.md#createshareroutev0sharespost) | **POST** /v0/shares | Mint a share link (returns the share_key once) |
| [**createUserTokenWebTokensCreatePost**](DefaultApi.md#createusertokenwebtokenscreatepost) | **POST** /web/tokens/create | Create User Token |
| [**createWorkspaceWebWebWorkspacesPost**](DefaultApi.md#createworkspacewebwebworkspacespost) | **POST** /web/workspaces | Create Workspace Web |
| [**dangerZoneOldDashboardDangerGet**](DefaultApi.md#dangerzoneolddashboarddangerget) | **GET** /dashboard/danger | Danger Zone Old |
| [**dangerZoneSettingsDangerGet**](DefaultApi.md#dangerzonesettingsdangerget) | **GET** /settings/danger | Danger Zone |
| [**dashboardDashboardGet**](DefaultApi.md#dashboarddashboardget) | **GET** /dashboard | Dashboard |
| [**deleteAccountWebAccountDeletePost**](DefaultApi.md#deleteaccountwebaccountdeletepost) | **POST** /web/account/delete | Delete Account |
| [**deleteArtifactByIdRouteV0ArtifactsArtIdDelete**](DefaultApi.md#deleteartifactbyidroutev0artifactsartiddelete) | **DELETE** /v0/artifacts/{art_id} | Soft-delete an artifact by its stable ID |
| [**deleteArtifactV0ArtifactsPathDelete**](DefaultApi.md#deleteartifactv0artifactspathdelete) | **DELETE** /v0/artifacts/{path} | Delete Artifact |
| [**deleteDriveRouteV0DrivesDriveIdDelete**](DefaultApi.md#deletedriveroutev0drivesdriveiddelete) | **DELETE** /v0/drives/{drive_id} | Soft-delete a drive |
| [**deleteDriveWebWebDrivesDriveIdDeletePost**](DefaultApi.md#deletedrivewebwebdrivesdriveiddeletepost) | **POST** /web/drives/{drive_id}/delete | Delete Drive Web |
| [**deleteFolderByIdV0FoldersFldIdDelete**](DefaultApi.md#deletefolderbyidv0foldersfldiddelete) | **DELETE** /v0/folders/{fld_id} | Soft-delete a folder by stable ID (cascade with ?recursive&#x3D;true) |
| [**deleteFolderByPathV0FoldersPathDelete**](DefaultApi.md#deletefolderbypathv0folderspathdelete) | **DELETE** /v0/folders/{path} | Soft-delete a folder (cascade with ?recursive&#x3D;true) |
| [**deleteGrantRouteV0GrantsGrnIdDelete**](DefaultApi.md#deletegrantroutev0grantsgrniddelete) | **DELETE** /v0/grants/{grn_id} | Revoke a grant (can_manage, or self-revoke own grant) |
| [**deleteShareRouteV0SharesShrIdDelete**](DefaultApi.md#deleteshareroutev0sharesshriddelete) | **DELETE** /v0/shares/{shr_id} | Revoke a share link (requires can_manage) |
| [**deleteWorkspaceWebWebWorkspacesOrgIdDeletePost**](DefaultApi.md#deleteworkspacewebwebworkspacesorgiddeletepost) | **POST** /web/workspaces/{org_id}/delete | Delete Workspace Web |
| [**downloadArtifactByIdV0ArtifactsArtIdDownloadGet**](DefaultApi.md#downloadartifactbyidv0artifactsartiddownloadget) | **GET** /v0/artifacts/{art_id}/download | Stream the artifact bytes by stable ID (never rendered HTML) |
| [**downloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet**](DefaultApi.md#downloadartifactversionv0artifactsartidversionsversionnumberdownloadget) | **GET** /v0/artifacts/{art_id}/versions/{version_number}/download | Stream bytes for a specific version (machine surface) |
| [**downloadUrlByIdV0ArtifactsArtIdDownloadUrlGet**](DefaultApi.md#downloadurlbyidv0artifactsartiddownloadurlget) | **GET** /v0/artifacts/{art_id}/download-url | Signed direct-from-GCS download URL by stable ID |
| [**downloadUrlByPathV0ArtifactsPathDownloadUrlGet**](DefaultApi.md#downloadurlbypathv0artifactspathdownloadurlget) | **GET** /v0/artifacts/{path}/download-url | Signed direct-from-GCS download URL by path |
| [**downloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet**](DefaultApi.md#downloadurlversionv0artifactsartidversionsversionnumberdownloadurlget) | **GET** /v0/artifacts/{art_id}/versions/{version_number}/download-url | Signed direct-from-GCS download URL for a specific version |
| [**editArtifactAArtIdEditGet**](DefaultApi.md#editartifactaartideditget) | **GET** /a/{art_id}/edit | Edit Artifact |
| [**enqueueJobV0ProjectsFldIdJobsPost**](DefaultApi.md#enqueuejobv0projectsfldidjobspost) | **POST** /v0/projects/{fld_id}/jobs | Enqueue a compile job for a project (folder) |
| [**extensionStartAuthExtensionStartGet**](DefaultApi.md#extensionstartauthextensionstartget) | **GET** /auth/extension/start | Extension Start |
| [**feedbackFormFeedbackGet**](DefaultApi.md#feedbackformfeedbackget) | **GET** /feedback | Feedback Form |
| [**feedbackSubmitFeedbackPost**](DefaultApi.md#feedbacksubmitfeedbackpost) | **POST** /feedback | Feedback Submit |
| [**findV0FindGet**](DefaultApi.md#findv0findget) | **GET** /v0/find | Hybrid passage retrieval over the full file body |
| [**getArtifactByIdMetaV0ArtifactsArtIdMetaGet**](DefaultApi.md#getartifactbyidmetav0artifactsartidmetaget) | **GET** /v0/artifacts/{art_id}/meta | Artifact metadata by stable ID (same shape as path /meta) |
| [**getArtifactByIdV0ArtifactsArtIdGet**](DefaultApi.md#getartifactbyidv0artifactsartidget) | **GET** /v0/artifacts/{art_id} | Canonical lookup of an artifact by its stable ID |
| [**getArtifactMetaV0ArtifactsPathMetaGet**](DefaultApi.md#getartifactmetav0artifactspathmetaget) | **GET** /v0/artifacts/{path}/meta | Get Artifact Meta |
| [**getArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet**](DefaultApi.md#getartifactversionv0artifactsartidversionsversionnumberget) | **GET** /v0/artifacts/{art_id}/versions/{version_number} | Metadata for a specific version of an artifact |
| [**getFeedbackStatusV0FeedbackFbkIdGet**](DefaultApi.md#getfeedbackstatusv0feedbackfbkidget) | **GET** /v0/feedback/{fbk_id} | Get Feedback Status |
| [**getFolderByIdMetaV0FoldersFldIdMetaGet**](DefaultApi.md#getfolderbyidmetav0foldersfldidmetaget) | **GET** /v0/folders/{fld_id}/meta | Folder metadata by stable ID (same shape as the bare id route) |
| [**getFolderByIdV0FoldersFldIdGet**](DefaultApi.md#getfolderbyidv0foldersfldidget) | **GET** /v0/folders/{fld_id} | Canonical lookup of a folder by its stable ID |
| [**getFolderByPathMetaV0FoldersPathMetaGet**](DefaultApi.md#getfolderbypathmetav0folderspathmetaget) | **GET** /v0/folders/{path}/meta | Folder metadata by path (same shape as the bare path route) |
| [**getFolderByPathV0FoldersPathGet**](DefaultApi.md#getfolderbypathv0folderspathget) | **GET** /v0/folders/{path} | Read folder metadata by path |
| [**getJobLogsV0JobsJobIdLogsGet**](DefaultApi.md#getjoblogsv0jobsjobidlogsget) | **GET** /v0/jobs/{job_id}/logs | Raw compile log (text/plain) |
| [**getJobV0JobsJobIdGet**](DefaultApi.md#getjobv0jobsjobidget) | **GET** /v0/jobs/{job_id} | Poll a job |
| [**getProjectV0ProjectsFldIdGet**](DefaultApi.md#getprojectv0projectsfldidget) | **GET** /v0/projects/{fld_id} | Get a project\&#39;s compile config |
| [**getShareStateWebShareRidGet**](DefaultApi.md#getsharestatewebshareridget) | **GET** /web/share/{rid} | Get Share State |
| [**healthHealthGet**](DefaultApi.md#healthhealthget) | **GET** /health | Health |
| [**inviteMemberWebWebMembersInvitePost**](DefaultApi.md#invitememberwebwebmembersinvitepost) | **POST** /web/members/invite | Invite Member Web |
| [**listArtifactVersionsV0ArtifactsArtIdVersionsGet**](DefaultApi.md#listartifactversionsv0artifactsartidversionsget) | **GET** /v0/artifacts/{art_id}/versions | List versions of an artifact, newest first |
| [**listArtifactsV0ArtifactsGet**](DefaultApi.md#listartifactsv0artifactsget) | **GET** /v0/artifacts | List artifacts in the drive |
| [**listEventsRouteV0EventsGet**](DefaultApi.md#listeventsroutev0eventsget) | **GET** /v0/events | Read the append-only event log for the authenticated drive |
| [**listGrantsRouteV0GrantsGet**](DefaultApi.md#listgrantsroutev0grantsget) | **GET** /v0/grants | List live grants on a resource (requires can_manage) |
| [**listProjectJobsV0ProjectsFldIdJobsGet**](DefaultApi.md#listprojectjobsv0projectsfldidjobsget) | **GET** /v0/projects/{fld_id}/jobs | List a project\&#39;s jobs |
| [**listSharesRouteV0SharesGet**](DefaultApi.md#listsharesroutev0sharesget) | **GET** /v0/shares | List live share links on a resource (requires can_manage) |
| [**listTrashRouteV0DrivesDriveIdTrashGet**](DefaultApi.md#listtrashroutev0drivesdriveidtrashget) | **GET** /v0/drives/{drive_id}/trash | List the authenticated drive\&#39;s trash |
| [**loginAuthLoginGet**](DefaultApi.md#loginauthloginget) | **GET** /auth/login | Login |
| [**logoutAuthLogoutPost**](DefaultApi.md#logoutauthlogoutpost) | **POST** /auth/logout | Logout |
| [**marketingGet**](DefaultApi.md#marketingget) | **GET** / | Marketing |
| [**marketplaceBrowseMarketplaceGet**](DefaultApi.md#marketplacebrowsemarketplaceget) | **GET** /marketplace | Marketplace Browse |
| [**marketplaceDetailMarketplaceSlugGet**](DefaultApi.md#marketplacedetailmarketplaceslugget) | **GET** /marketplace/{slug} | Marketplace Detail |
| [**meUsageV0DrivesMeUsageGet**](DefaultApi.md#meusagev0drivesmeusageget) | **GET** /v0/drives/me/usage | Current-period usage + caps for the authenticated drive |
| [**meV0DrivesMeGet**](DefaultApi.md#mev0drivesmeget) | **GET** /v0/drives/me | Me |
| [**moveFolderByIdV0FoldersFldIdMovePost**](DefaultApi.md#movefolderbyidv0foldersfldidmovepost) | **POST** /v0/folders/{fld_id}/move | Rename / move a folder by stable ID (cascade descendants) |
| [**moveFolderByPathV0FoldersPathMovePost**](DefaultApi.md#movefolderbypathv0folderspathmovepost) | **POST** /v0/folders/{path}/move | Rename / move a folder (cascade-update descendants) |
| [**oauthDisconnectWebOauthDisconnectPost**](DefaultApi.md#oauthdisconnectweboauthdisconnectpost) | **POST** /web/oauth/disconnect | Oauth Disconnect |
| [**patchFolderByIdV0FoldersFldIdPatch**](DefaultApi.md#patchfolderbyidv0foldersfldidpatch) | **PATCH** /v0/folders/{fld_id} | Update folder metadata by stable ID |
| [**patchFolderByPathV0FoldersPathPatch**](DefaultApi.md#patchfolderbypathv0folderspathpatch) | **PATCH** /v0/folders/{path} | Update folder metadata by path |
| [**patchGrantRouteV0GrantsGrnIdPatch**](DefaultApi.md#patchgrantroutev0grantsgrnidpatch) | **PATCH** /v0/grants/{grn_id} | Update a grant\&#39;s role and/or expiry (requires can_manage) |
| [**postDescribeV0QueryDescribePost**](DefaultApi.md#postdescribev0querydescribepost) | **POST** /v0/query/describe | Describe a dataset\&#39;s column schema |
| [**postFeedbackV0FeedbackPost**](DefaultApi.md#postfeedbackv0feedbackpost) | **POST** /v0/feedback | Post Feedback |
| [**postLookupValuesV0QueryLookupValuesPost**](DefaultApi.md#postlookupvaluesv0querylookupvaluespost) | **POST** /v0/query/lookup-values | List distinct values of a dataset column |
| [**postQueryV0QueryPost**](DefaultApi.md#postqueryv0querypost) | **POST** /v0/query | Run a read-only SQL query over authorized datasets |
| [**privacyPagePrivacyGet**](DefaultApi.md#privacypageprivacyget) | **GET** /privacy | Privacy Page |
| [**projectPreviewPageFFldIdPreviewGet**](DefaultApi.md#projectpreviewpageffldidpreviewget) | **GET** /f/{fld_id}/preview | Project Preview Page |
| [**publisherProfilePublishersHandleGet**](DefaultApi.md#publisherprofilepublishershandleget) | **GET** /publishers/{handle} | Publisher Profile |
| [**putArtifactV0ArtifactsPathPut**](DefaultApi.md#putartifactv0artifactspathput) | **PUT** /v0/artifacts/{path} | Upload (or overwrite) an artifact |
| [**putProjectV0ProjectsFldIdPut**](DefaultApi.md#putprojectv0projectsfldidput) | **PUT** /v0/projects/{fld_id} | Set a project\&#39;s compile config (entrypoint/engine/auto_compile) |
| [**recoveryNewAccountAuthRecoveryNewAccountPost**](DefaultApi.md#recoverynewaccountauthrecoverynewaccountpost) | **POST** /auth/recovery/new-account | Recovery New Account |
| [**recoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGet**](DefaultApi.md#recoverynewaccountexpiredauthrecoverynewaccountexpiredget) | **GET** /auth/recovery/new-account-expired | Recovery New Account Expired |
| [**recoveryPageAuthRecoveryGet**](DefaultApi.md#recoverypageauthrecoveryget) | **GET** /auth/recovery | Recovery Page |
| [**recoveryRestoreAuthRecoveryRestorePost**](DefaultApi.md#recoveryrestoreauthrecoveryrestorepost) | **POST** /auth/recovery/restore | Recovery Restore |
| [**redeemShareSShareKeyGet**](DefaultApi.md#redeemsharessharekeyget) | **GET** /s/{share_key} | Redeem Share |
| [**redeemShareWithPasswordSShareKeyPost**](DefaultApi.md#redeemsharewithpasswordssharekeypost) | **POST** /s/{share_key} | Redeem Share With Password |
| [**removeMemberWebWebMembersTargetUserIdRemovePost**](DefaultApi.md#removememberwebwebmemberstargetuseridremovepost) | **POST** /web/members/{target_user_id}/remove | Remove Member Web |
| [**renameArtifactRouteV0ArtifactsArtIdPatch**](DefaultApi.md#renameartifactroutev0artifactsartidpatch) | **PATCH** /v0/artifacts/{art_id} | Rename / move an artifact to a new path |
| [**renameDriveWebWebDrivesDriveIdRenamePost**](DefaultApi.md#renamedrivewebwebdrivesdriveidrenamepost) | **POST** /web/drives/{drive_id}/rename | Rename Drive Web |
| [**renameWorkspaceWebWebWorkspacesOrgIdRenamePost**](DefaultApi.md#renameworkspacewebwebworkspacesorgidrenamepost) | **POST** /web/workspaces/{org_id}/rename | Rename Workspace Web |
| [**resendInvitationWebWebInvitationsInvitationIdResendPost**](DefaultApi.md#resendinvitationwebwebinvitationsinvitationidresendpost) | **POST** /web/invitations/{invitation_id}/resend | Resend Invitation Web |
| [**restoreArtifactV0ArtifactsArtIdRestorePost**](DefaultApi.md#restoreartifactv0artifactsartidrestorepost) | **POST** /v0/artifacts/{art_id}/restore | Restore a soft-deleted artifact |
| [**restoreDriveRouteV0DrivesDriveIdRestorePost**](DefaultApi.md#restoredriveroutev0drivesdriveidrestorepost) | **POST** /v0/drives/{drive_id}/restore | Restore a soft-deleted drive |
| [**revokeGrantWebShareRidGrantGrnIdRevokePost**](DefaultApi.md#revokegrantwebshareridgrantgrnidrevokepost) | **POST** /web/share/{rid}/grant/{grn_id}/revoke | Revoke Grant |
| [**revokeInvitationWebWebInvitationsInvitationIdRevokePost**](DefaultApi.md#revokeinvitationwebwebinvitationsinvitationidrevokepost) | **POST** /web/invitations/{invitation_id}/revoke | Revoke Invitation Web |
| [**revokeKeyWebKeysRevokePost**](DefaultApi.md#revokekeywebkeysrevokepost) | **POST** /web/keys/revoke | Revoke Key |
| [**revokeLinkWebShareRidLinkShrIdRevokePost**](DefaultApi.md#revokelinkwebshareridlinkshridrevokepost) | **POST** /web/share/{rid}/link/{shr_id}/revoke | Revoke Link |
| [**revokeUserTokenWebTokensRevokePost**](DefaultApi.md#revokeusertokenwebtokensrevokepost) | **POST** /web/tokens/revoke | Revoke User Token |
| [**rotateShareRouteV0SharesShrIdRotatePost**](DefaultApi.md#rotateshareroutev0sharesshridrotatepost) | **POST** /v0/shares/{shr_id}/rotate | Revoke + reissue a share link\&#39;s key (requires can_share) |
| [**searchV0SearchGet**](DefaultApi.md#searchv0searchget) | **GET** /v0/search | Full-text search over artifacts in the drive |
| [**setMemberRoleWebWebMembersTargetUserIdRolePost**](DefaultApi.md#setmemberrolewebwebmemberstargetuseridrolepost) | **POST** /web/members/{target_user_id}/role | Set Member Role Web |
| [**setPublicWebShareRidPublicPost**](DefaultApi.md#setpublicwebshareridpublicpost) | **POST** /web/share/{rid}/public | Set Public |
| [**setSealWebShareRidSealPost**](DefaultApi.md#setsealwebshareridsealpost) | **POST** /web/share/{rid}/seal | Set Seal |
| [**settingsAccountSettingsGet**](DefaultApi.md#settingsaccountsettingsget) | **GET** /settings | Settings Account |
| [**settingsApiKeysSettingsApiKeysGet**](DefaultApi.md#settingsapikeyssettingsapikeysget) | **GET** /settings/api-keys | Settings Api Keys |
| [**settingsQuickstartSettingsQuickstartGet**](DefaultApi.md#settingsquickstartsettingsquickstartget) | **GET** /settings/quickstart | Settings Quickstart |
| [**settingsWorkspaceSettingsWorkspaceGet**](DefaultApi.md#settingsworkspacesettingsworkspaceget) | **GET** /settings/workspace | Settings Workspace |
| [**sharedFilesSharedGet**](DefaultApi.md#sharedfilessharedget) | **GET** /shared | Shared Files |
| [**streamUploadV0UploadTokenPut**](DefaultApi.md#streamuploadv0uploadtokenput) | **PUT** /v0/upload/{token} | Proxied streaming upload (via an upload_url token) |
| [**switchDriveWebSwitchPost**](DefaultApi.md#switchdrivewebswitchpost) | **POST** /web/switch | Switch Drive |
| [**termsPageTermsGet**](DefaultApi.md#termspagetermsget) | **GET** /terms | Terms Page |
| [**toggleIndexingWebAccountIndexingPost**](DefaultApi.md#toggleindexingwebaccountindexingpost) | **POST** /web/account/indexing | Toggle Indexing |
| [**trashWebTrashGet**](DefaultApi.md#trashwebtrashget) | **GET** /web/trash | Trash |
| [**viewArtifactHeadAArtIdHeadGet**](DefaultApi.md#viewartifactheadaartidheadget) | **GET** /a/{art_id}/head | View Artifact Head |
| [**viewFileDriveIdPathGet**](DefaultApi.md#viewfiledriveidpathget) | **GET** /{drive_id}/{path} | View File |
| [**viewPermalinkArtifactAArtIdGet**](DefaultApi.md#viewpermalinkartifactaartidget) | **GET** /a/{art_id} | View Permalink Artifact |
| [**viewPermalinkFolderFFldIdGet**](DefaultApi.md#viewpermalinkfolderffldidget) | **GET** /f/{fld_id} | View Permalink Folder |
| [**webArtifactIndexedWebArtifactsIndexedGet**](DefaultApi.md#webartifactindexedwebartifactsindexedget) | **GET** /web/artifacts/indexed | Web Artifact Indexed |
| [**webCopyArtifactWebArtifactsCopyPost**](DefaultApi.md#webcopyartifactwebartifactscopypost) | **POST** /web/artifacts/copy | Web Copy Artifact |
| [**webDeleteArtifactOpWebArtifactsDeletePost**](DefaultApi.md#webdeleteartifactopwebartifactsdeletepost) | **POST** /web/artifacts/delete | Web Delete Artifact Op |
| [**webDeleteArtifactWebArtifactsPathDelete**](DefaultApi.md#webdeleteartifactwebartifactspathdelete) | **DELETE** /web/artifacts/{path} | Web Delete Artifact |
| [**webDeleteFolderWebFoldersDeletePost**](DefaultApi.md#webdeletefolderwebfoldersdeletepost) | **POST** /web/folders/delete | Web Delete Folder |
| [**webMoveFolderWebFoldersMovePost**](DefaultApi.md#webmovefolderwebfoldersmovepost) | **POST** /web/folders/move | Web Move Folder |
| [**webNewFolderWebFoldersNewPost**](DefaultApi.md#webnewfolderwebfoldersnewpost) | **POST** /web/folders/new | Web New Folder |
| [**webProjectCompileWebProjectsFldIdCompilePost**](DefaultApi.md#webprojectcompilewebprojectsfldidcompilepost) | **POST** /web/projects/{fld_id}/compile | Web Project Compile |
| [**webProjectFilesWebProjectsFldIdFilesGet**](DefaultApi.md#webprojectfileswebprojectsfldidfilesget) | **GET** /web/projects/{fld_id}/files | Web Project Files |
| [**webProjectPreviewWebProjectsFldIdPreviewGet**](DefaultApi.md#webprojectpreviewwebprojectsfldidpreviewget) | **GET** /web/projects/{fld_id}/preview | Web Project Preview |
| [**webPutArtifactWebArtifactsPathPut**](DefaultApi.md#webputartifactwebartifactspathput) | **PUT** /web/artifacts/{path} | Web Put Artifact |
| [**webRenameArtifactWebArtifactsRenamePost**](DefaultApi.md#webrenameartifactwebartifactsrenamepost) | **POST** /web/artifacts/rename | Web Rename Artifact |
| [**webRestoreArtifactWebArtifactsRestorePost**](DefaultApi.md#webrestoreartifactwebartifactsrestorepost) | **POST** /web/artifacts/restore | Web Restore Artifact |
| [**webRestoreFolderWebFoldersRestorePost**](DefaultApi.md#webrestorefolderwebfoldersrestorepost) | **POST** /web/folders/restore | Web Restore Folder |
| [**webSetMetadataWebSetPost**](DefaultApi.md#websetmetadatawebsetpost) | **POST** /web/set | Web Set Metadata |
| [**webUploadWebUploadPost**](DefaultApi.md#webuploadwebuploadpost) | **POST** /web/upload | Web Upload |
| [**webhooksPageWebhooksGet**](DefaultApi.md#webhookspagewebhooksget) | **GET** /webhooks | Webhooks Page |
| [**welcomeWelcomeGet**](DefaultApi.md#welcomewelcomeget) | **GET** /welcome | Welcome |



## acceptInvitationInvitationsTokenGet

> string acceptInvitationInvitationsTokenGet(token)

Accept Invitation

Accept a workspace invitation (workspaces-design §4.4). Top-level route — deliberately OFF the reserved single-letter prefixes (&#x60;/a /f /s /v /_&#x60;).  If the visitor isn\&#39;t signed in, bounce through &#x60;/auth/login&#x60; with a same-origin &#x60;return_to&#x60; back here (the login flow validates return_to, so the path is safe). Once signed in, validate + accept:   * email mismatch / expired / revoked / unknown → friendly error page,   * success → join the workspace, set it active, land on the dashboard.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { AcceptInvitationInvitationsTokenGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    token: token_example,
  } satisfies AcceptInvitationInvitationsTokenGetRequest;

  try {
    const data = await api.acceptInvitationInvitationsTokenGet(body);
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
| **token** | `string` |  | [Defaults to `undefined`] |

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
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## activityFeedActivityGet

> string activityFeedActivityGet()

Activity Feed

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ActivityFeedActivityGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.activityFeedActivityGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## addGrantWebShareRidGrantPost

> any addGrantWebShareRidGrantPost(rid, grantIn, xCsrfToken)

Add Grant

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { AddGrantWebShareRidGrantPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    rid: rid_example,
    // GrantIn
    grantIn: ...,
    // string (optional)
    xCsrfToken: xCsrfToken_example,
  } satisfies AddGrantWebShareRidGrantPostRequest;

  try {
    const data = await api.addGrantWebShareRidGrantPost(body);
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
| **rid** | `string` |  | [Defaults to `undefined`] |
| **grantIn** | [GrantIn](GrantIn.md) |  | |
| **xCsrfToken** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## artifactDetailPreviewPreviewArtifactDetailGet

> string artifactDetailPreviewPreviewArtifactDetailGet()

Artifact Detail Preview

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ArtifactDetailPreviewPreviewArtifactDetailGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.artifactDetailPreviewPreviewArtifactDetailGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## beginUploadV0UploadsPost

> UploadBeginOut beginUploadV0UploadsPost(uploadBeginIn, authorization)

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
  const api = new DefaultApi();

  const body = {
    // UploadBeginIn
    uploadBeginIn: ...,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**UploadBeginOut**](UploadBeginOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **400** | Invalid path / labels / metadata / source |  -  |
| **402** | Drive storage quota would be exceeded |  -  |
| **403** | Path reserved for the system (WIKI_RESERVED) |  -  |
| **413** | size_bytes exceeds the drive\&#39;s per-artifact cap |  -  |
| **429** | Drive\&#39;s per-hour write budget exhausted |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## callbackAuthCallbackGet

> any callbackAuthCallbackGet(code, state, error)

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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## cancelJobV0JobsJobIdCancelPost

> any cancelJobV0JobsJobIdCancelPost(jobId, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    jobId: jobId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## collectionDetailCollectionsSlugGet

> string collectionDetailCollectionsSlugGet(slug)

Collection Detail

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CollectionDetailCollectionsSlugGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    slug: slug_example,
  } satisfies CollectionDetailCollectionsSlugGetRequest;

  try {
    const data = await api.collectionDetailCollectionsSlugGet(body);
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
| **slug** | `string` |  | [Defaults to `undefined`] |

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
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## commitUploadV0UploadsUploadIdCommitPost

> ArtifactOut commitUploadV0UploadsUploadIdCommitPost(uploadId, authorization)

Commit a large (direct-to-GCS) upload

Finalize the upload begun at &#x60;/v0/uploads&#x60;: AgentDrive verifies the object that landed in GCS (size + checksum) and creates the artifact. Idempotent — a retry after a successful commit returns the same artifact. The write budget is charged here (begin is free metadata).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CommitUploadV0UploadsUploadIdCommitPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    uploadId: uploadId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **404** | No such upload for this drive |  -  |
| **409** | Uploaded object size !&#x3D; declared size_bytes |  -  |
| **410** | Upload session expired |  -  |
| **412** | If-Match precondition failed |  -  |
| **429** | Drive\&#39;s per-hour write budget exhausted |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## connectorsPageConnectorsGet

> string connectorsPageConnectorsGet()

Connectors Page

Connectors landing — Google Drive, Notion, etc. Each connector pipes its files into a virtual folder at the drive root (&#x60;gdrive/&#x60;, &#x60;notion/&#x60;) so the indexer can build wiki pages across all of an org\&#39;s knowledge. No backend in v0; cards read from &#x60;mock/data.py&#x60;.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ConnectorsPageConnectorsGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.connectorsPageConnectorsGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## copyArtifactRouteV0ArtifactsArtIdCopyPost

> ArtifactOut copyArtifactRouteV0ArtifactsArtIdCopyPost(artId, copyIn, xAgentdriveActor, authorization)

Duplicate an artifact to a new path (CAS-shared, new ID)

Create a new artifact at &#x60;path&#x60; whose bytes are identical to the source artifact\&#39;s. The copy reuses the source\&#39;s CAS object (zero new storage) but gets a fresh &#x60;art_…&#x60; ID, a fresh version 1, and — by default — &#x60;source.refs &#x3D; [{type: \&#39;artifact\&#39;, id: \&#39;&lt;source&gt;\&#39;}]&#x60; so provenance is preserved.  Quota: the copy\&#39;s &#x60;size_bytes&#x60; is added to the drive\&#39;s &#x60;storage_bytes&#x60; even though physical bytes are shared.  Returns 409 PATH_CONFLICT if the target path is already taken; 413 STORAGE_QUOTA_EXCEEDED if the copy would push the drive over its limit.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CopyArtifactRouteV0ArtifactsArtIdCopyPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // CopyIn
    copyIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createDriveKeyWebWebDrivesDriveIdKeysCreatePost

> any createDriveKeyWebWebDrivesDriveIdKeysCreatePost(driveId, csrf, label)

Create Drive Key Web

Mint a new &#x60;ad_live_&#x60; key for a specific owned drive + reveal once (workspaces-design §5.6). Manager-only (no-leak no-op otherwise).  The per-drive twin of &#x60;/web/keys/create&#x60; (which acts on the active drive). Pins the target drive active so the reveal on the api-keys tab shows the key for the drive the user just minted on.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateDriveKeyWebWebDrivesDriveIdKeysCreatePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    driveId: driveId_example,
    // string
    csrf: csrf_example,
    // string (optional)
    label: label_example,
  } satisfies CreateDriveKeyWebWebDrivesDriveIdKeysCreatePostRequest;

  try {
    const data = await api.createDriveKeyWebWebDrivesDriveIdKeysCreatePost(body);
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
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **label** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createDriveWebWebDrivesPost

> any createDriveWebWebDrivesPost(name, csrf)

Create Drive Web

Create a drive in the active workspace + reveal its key once (workspaces-design §4.5, §5.6).  The web (session+CSRF) twin of &#x60;POST /v0/drives&#x60;. Any MEMBER of the active workspace may create a drive; the creator becomes its owner. The new drive\&#39;s &#x60;ad_live_&#x60; key is shown ONCE via the same &#x60;reveal_key&#x60;-in-session mechanism the api-keys tab consumes; we also pin the new drive as active and land on the api-keys tab so the user sees the reveal.  Authorization is by &#x60;current_user&#x60; + membership, NOT &#x60;current_drive&#x60; (workspaces-design §4.3 empty state): a freshly-invited member owns 0 drives, so &#x60;current_drive&#x60; is None for them — yet this is exactly the \&quot;create your first drive\&quot; moment that MUST work. Gating on a pre-existing drive would dead-end the web onboarding path. Membership + the per-member cap are the real guards; both hold whether or not the user already owns a drive.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateDriveWebWebDrivesPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    name: name_example,
    // string
    csrf: csrf_example,
  } satisfies CreateDriveWebWebDrivesPostRequest;

  try {
    const data = await api.createDriveWebWebDrivesPost(body);
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
| **name** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createFolderByPathV0FoldersPathPost

> FolderOut createFolderByPathV0FoldersPathPost(path, xAgentdriveActor, authorization, folderCreateIn)

Create a folder (idempotent)

Create a folder at the URL path. Idempotent — a second call for the same live path returns the existing row unchanged (metadata updates require PATCH).  Returns 409 &#x60;FOLDER_PATH_CONFLICT&#x60; if a live artifact occupies the file form of the path (e.g. mkdir &#x60;/foo/&#x60; when an artifact lives at &#x60;/foo&#x60;).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateFolderByPathV0FoldersPathPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
    // FolderCreateIn (optional)
    folderCreateIn: ...,
  } satisfies CreateFolderByPathV0FoldersPathPostRequest;

  try {
    const data = await api.createFolderByPathV0FoldersPathPost(body);
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |
| **folderCreateIn** | [FolderCreateIn](FolderCreateIn.md) |  | [Optional] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createGrantRouteV0GrantsPost

> GrantOut createGrantRouteV0GrantsPost(grantCreateIn, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // GrantCreateIn
    grantCreateIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createKeyWebKeysCreatePost

> any createKeyWebKeysCreatePost(csrf, label)

Create Key

Mint a new &#x60;ad_live_&#x60; key for the active drive (reveal-once).  A drive may hold several keys — this appends one rather than replacing. Management gate (workspaces-v2 §4.4): personal → owner, team → admin. Without it a team MEMBER (who now reaches the shared drive) could mint a shared key. No-leak redirect on non-manage.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateKeyWebKeysCreatePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    csrf: csrf_example,
    // string (optional)
    label: label_example,
  } satisfies CreateKeyWebKeysCreatePostRequest;

  try {
    const data = await api.createKeyWebKeysCreatePost(body);
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
| **label** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createLinkWebShareRidLinkPost

> any createLinkWebShareRidLinkPost(rid, linkIn, xCsrfToken)

Create Link

Mint a viewer share link. Returns the fresh state PLUS &#x60;minted&#x60; with the raw &#x60;share_key&#x60; + url — the ONLY response that carries the key. Artifacts only (v1: folder share links are not supported).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateLinkWebShareRidLinkPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    rid: rid_example,
    // LinkIn
    linkIn: ...,
    // string (optional)
    xCsrfToken: xCsrfToken_example,
  } satisfies CreateLinkWebShareRidLinkPostRequest;

  try {
    const data = await api.createLinkWebShareRidLinkPost(body);
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
| **rid** | `string` |  | [Defaults to `undefined`] |
| **linkIn** | [LinkIn](LinkIn.md) |  | |
| **xCsrfToken** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createShareRouteV0SharesPost

> ShareMintOut createShareRouteV0SharesPost(shareCreateIn, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // ShareCreateIn
    shareCreateIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ShareMintOut**](ShareMintOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createUserTokenWebTokensCreatePost

> any createUserTokenWebTokensCreatePost(csrf, label, scope)

Create User Token

Mint an &#x60;ad_user_&#x60; user-identity token (workspaces-design §5.2, §5.6).  **Web-only minting**: the bootstrap chicken-and-egg is solved here, and a leaked token must not be able to mint persistent siblings — so this path exists only behind the browser session + CSRF, never over the &#x60;/v0/&#x60; API.  The raw token is shown ONCE via &#x60;reveal_token&#x60; in the session, then consumed on the next GET of the api-keys tab.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateUserTokenWebTokensCreatePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    csrf: csrf_example,
    // string (optional)
    label: label_example,
    // string (optional)
    scope: scope_example,
  } satisfies CreateUserTokenWebTokensCreatePostRequest;

  try {
    const data = await api.createUserTokenWebTokensCreatePost(body);
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
| **label** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **scope** | `string` |  | [Optional] [Defaults to `&#39;full&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createWorkspaceWebWebWorkspacesPost

> any createWorkspaceWebWebWorkspacesPost(name, csrf)

Create Workspace Web

Create a new workspace, set it active, reveal its starter key once (workspaces-design §4.7).  The web (session+CSRF) twin of &#x60;POST /v0/workspaces&#x60;. A user may administer up to their plan\&#39;s number of TEAM workspaces (&#x60;core.entitlements.can_create_workspace&#x60;, tier-governed — workspaces-v2 §4.6); a blocked create bounces to the dashboard with a limit-reached affordance (&#x60;?err&#x3D;workspace_limit&#x60;). On success the new workspace + its starter drive become active and we land on the api-keys tab so the user sees the one-time key reveal.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { CreateWorkspaceWebWebWorkspacesPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    name: name_example,
    // string
    csrf: csrf_example,
  } satisfies CreateWorkspaceWebWebWorkspacesPostRequest;

  try {
    const data = await api.createWorkspaceWebWebWorkspacesPost(body);
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
| **name** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## dangerZoneOldDashboardDangerGet

> any dangerZoneOldDashboardDangerGet()

Danger Zone Old

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DangerZoneOldDashboardDangerGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.dangerZoneOldDashboardDangerGet();
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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## dangerZoneSettingsDangerGet

> string dangerZoneSettingsDangerGet()

Danger Zone

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DangerZoneSettingsDangerGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.dangerZoneSettingsDangerGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## dashboardDashboardGet

> string dashboardDashboardGet(q, path, wiki, type, label, after, before, view, sort, dir)

Dashboard

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DashboardDashboardGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string (optional)
    q: q_example,
    // string (optional)
    path: path_example,
    // number (optional)
    wiki: 56,
    // string (optional)
    type: type_example,
    // Array<string> (optional)
    label: ...,
    // string (optional)
    after: after_example,
    // string (optional)
    before: before_example,
    // string (optional)
    view: view_example,
    // string (optional)
    sort: sort_example,
    // string (optional)
    dir: dir_example,
  } satisfies DashboardDashboardGetRequest;

  try {
    const data = await api.dashboardDashboardGet(body);
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
| **q** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **path** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **wiki** | `number` |  | [Optional] [Defaults to `0`] |
| **type** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **label** | `Array<string>` |  | [Optional] |
| **after** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **before** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **view** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **sort** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **dir** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |

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
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteAccountWebAccountDeletePost

> any deleteAccountWebAccountDeletePost(confirm, csrf)

Delete Account

Soft-delete the user + their solo workspace + drive.  v1 semantics (solo orgs): deleting the account also deletes the workspace and its data under one aligned retention window, after which everything is hard-purged. \&quot;Delete my account\&quot; means \&quot;delete everything mine,\&quot; matching Notion / Linear / Slack consumer-tier semantics. Membership-transfer for shared orgs lands in v1.5+.  The response routes through the auth provider\&#39;s logout so the upstream session is cleared before the user returns, preventing a silent re-authentication that would re-provision the just-deleted account. Falls back to a local-only redirect when there is no upstream session to clear.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DeleteAccountWebAccountDeletePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    confirm: confirm_example,
    // string
    csrf: csrf_example,
  } satisfies DeleteAccountWebAccountDeletePostRequest;

  try {
    const data = await api.deleteAccountWebAccountDeletePost(body);
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
| **confirm** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteArtifactByIdRouteV0ArtifactsArtIdDelete

> any deleteArtifactByIdRouteV0ArtifactsArtIdDelete(artId, ifMatch, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // string (optional)
    ifMatch: ifMatch_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteArtifactV0ArtifactsPathDelete

> any deleteArtifactV0ArtifactsPathDelete(path, ifMatch, xAgentdriveActor, authorization)

Delete Artifact

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DeleteArtifactV0ArtifactsPathDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
    // string (optional)
    ifMatch: ifMatch_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteDriveRouteV0DrivesDriveIdDelete

> any deleteDriveRouteV0DrivesDriveIdDelete(driveId, xAgentdriveActor, authorization)

Soft-delete a drive

Mark the drive for cleanup. All tenant data (artifacts, versions, wiki, embeddings, events) is hidden via the &#x60;live_*&#x60; views and CASCADE-removed by the GC cleanup cron at &#x60;purge_at&#x60;. Restore via &#x60;POST /v0/drives/{id}/restore&#x60; while the row is still in trash. The path-param &#x60;drive_id&#x60; MUST match the authenticated drive.  Accepts either an &#x60;ad_live_&#x60; per-drive key (deletes that key\&#39;s drive) or an &#x60;ad_user_&#x60; user token selecting an owned drive (workspaces-design §5.3); a &#x60;read&#x60;-scope user token is rejected with 403 &#x60;INSUFFICIENT_SCOPE&#x60;. **Guard (§8):** a workspace must retain at least one live drive — deleting the workspace\&#39;s last live drive returns 409 &#x60;LAST_DRIVE&#x60;.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DeleteDriveRouteV0DrivesDriveIdDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    driveId: driveId_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteDriveWebWebDrivesDriveIdDeletePost

> any deleteDriveWebWebDrivesDriveIdDeletePost(driveId, csrf)

Delete Drive Web

Soft-delete a drive the caller owns, with the last-drive guard (workspaces-design §8). Owner-only (no-leak no-op otherwise).  Guard: blocks deleting the workspace\&#39;s LAST live drive — a member must always land somewhere. On a successful delete of the *active* drive, we drop the pin so &#x60;current_drive&#x60; falls back to the user\&#39;s next oldest owned drive.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DeleteDriveWebWebDrivesDriveIdDeletePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    driveId: driveId_example,
    // string
    csrf: csrf_example,
  } satisfies DeleteDriveWebWebDrivesDriveIdDeletePostRequest;

  try {
    const data = await api.deleteDriveWebWebDrivesDriveIdDeletePost(body);
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
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteFolderByIdV0FoldersFldIdDelete

> FolderDeleteOut deleteFolderByIdV0FoldersFldIdDelete(fldId, recursive, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // boolean (optional)
    recursive: true,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderDeleteOut**](FolderDeleteOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteFolderByPathV0FoldersPathDelete

> FolderDeleteOut deleteFolderByPathV0FoldersPathDelete(path, recursive, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
    // boolean (optional)
    recursive: true,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderDeleteOut**](FolderDeleteOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteGrantRouteV0GrantsGrnIdDelete

> any deleteGrantRouteV0GrantsGrnIdDelete(grnId, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    grnId: grnId_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteShareRouteV0SharesShrIdDelete

> any deleteShareRouteV0SharesShrIdDelete(shrId, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    shrId: shrId_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteWorkspaceWebWebWorkspacesOrgIdDeletePost

> any deleteWorkspaceWebWebWorkspacesOrgIdDeletePost(orgId, csrf, confirm)

Delete Workspace Web

Explicit delete-workspace path (workspaces-design §4.4): a sole admin who can\&#39;t leave (members remain) may instead destroy the workspace — cascade soft-delete the org + all its live drives.  Admin-gated against the PATH org (not just the session) so a stale cookie can\&#39;t redirect the cascade. A non-admin is a no-leak no-op.  **Typed confirmation required** (parallel to &#x60;delete_account&#x60;\&#39;s &#x60;confirm &#x3D;&#x3D; \&quot;DELETE\&quot;&#x60;): this cascade soft-deletes the WHOLE workspace plus every member\&#39;s drives in it, so a single mis-clicked CSRF POST must not be able to trigger it. The caller must type either the literal &#x60;DELETE&#x60; or the exact workspace name; anything else bounces with no cascade. (Restricting to sole-admin is a separate product question, flagged to the user — not changed here.)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { DeleteWorkspaceWebWebWorkspacesOrgIdDeletePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    orgId: orgId_example,
    // string
    csrf: csrf_example,
    // string (optional)
    confirm: confirm_example,
  } satisfies DeleteWorkspaceWebWebWorkspacesOrgIdDeletePostRequest;

  try {
    const data = await api.deleteWorkspaceWebWebWorkspacesOrgIdDeletePost(body);
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
| **orgId** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **confirm** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadArtifactByIdV0ArtifactsArtIdDownloadGet

> any downloadArtifactByIdV0ArtifactsArtIdDownloadGet(artId, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet

> any downloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet(artId, versionNumber, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // number
    versionNumber: 56,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadUrlByIdV0ArtifactsArtIdDownloadUrlGet

> DownloadUrlOut downloadUrlByIdV0ArtifactsArtIdDownloadUrlGet(artId, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadUrlByPathV0ArtifactsPathDownloadUrlGet

> DownloadUrlOut downloadUrlByPathV0ArtifactsPathDownloadUrlGet(path, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## downloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet

> DownloadUrlOut downloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet(artId, versionNumber, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // number
    versionNumber: 56,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**DownloadUrlOut**](DownloadUrlOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## editArtifactAArtIdEditGet

> string editArtifactAArtIdEditGet(artId)

Edit Artifact

SnipIt annotation editor for an image artifact.  URL pattern mirrors the artifact permalink (&#x60;/a/{art_id}&#x60; → viewer; &#x60;/a/{art_id}/edit&#x60; → editor). FastAPI matches the more-specific &#x60;/edit&#x60; path before &#x60;/a/{art_id}&#x60; so there\&#39;s no collision.  Owner-only: requires a signed-in session cookie AND the artifact must belong to the user\&#39;s currently-active drive. Non-owners and anonymous viewers redirect to /auth/login with this URL as &#x60;return_to&#x60; so they land back here after sign-in.  Renders an editor shell — the editor JS owns all behavior (load the PNG, draw annotations on a canvas overlay, auto-save via &#x60;PUT /web/artifacts/{path}&#x60; with cookie auth). v0 supports image artifacts only; non-image art_ids redirect to the canonical viewer URL.  Pairs with the SnipIt Chrome extension: after auto-upload finishes the extension\&#39;s SW navigates the tab to this URL, so the user\&#39;s URL bar shows the real &#x60;agentdrive.run/a/&lt;art_id&gt;/edit&#x60; instead of a chrome-extension://... page. Editing on the web app side also means the same flow is reachable from the dashboard (\&quot;Edit this clip\&quot;) without the extension installed.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { EditArtifactAArtIdEditGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
  } satisfies EditArtifactAArtIdEditGetRequest;

  try {
    const data = await api.editArtifactAArtIdEditGet(body);
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## enqueueJobV0ProjectsFldIdJobsPost

> any enqueueJobV0ProjectsFldIdJobsPost(fldId, compileJobIn, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // CompileJobIn
    compileJobIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## extensionStartAuthExtensionStartGet

> any extensionStartAuthExtensionStartGet(extId)

Extension Start

Begin a WorkOS sign-in flow on behalf of a Chrome extension.  Stamps &#x60;for&#x3D;ext&#x60; + &#x60;ext_id&#x60; into the signed OAuth state so the callback handler knows to render the extension handoff page instead of setting a session cookie.  Three short-circuits, all surface as actionable errors:   * EXTENSION_AUTH_DISABLED (503): kill switch flipped off.   * UNKNOWN_EXTENSION (400): &#x60;ext_id&#x60; not on the allow-list.   * Missing &#x60;ext_id&#x60; query string (400 INVALID_REQUEST).

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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## feedbackFormFeedbackGet

> string feedbackFormFeedbackGet()

Feedback Form

Render the feedback form. Auth-required.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { FeedbackFormFeedbackGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.feedbackFormFeedbackGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## feedbackSubmitFeedbackPost

> any feedbackSubmitFeedbackPost(csrf, category, title, message, contact, attachments)

Feedback Submit

Validate, charge the feedback budget, insert the ticket, redirect with a flash.  Validation runs BEFORE the quota charge so users get clear field errors without burning budget. The ticket insert is LLM-free and GitHub-free (§5.2) — the triage lane picks it up on its next tick.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { FeedbackSubmitFeedbackPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    csrf: csrf_example,
    // string (optional)
    category: category_example,
    // string (optional)
    title: title_example,
    // string (optional)
    message: message_example,
    // string (optional)
    contact: contact_example,
    // Array<Blob> (optional)
    attachments: /path/to/file.txt,
  } satisfies FeedbackSubmitFeedbackPostRequest;

  try {
    const data = await api.feedbackSubmitFeedbackPost(body);
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
| **category** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **title** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **message** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **contact** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **attachments** | `Array<Blob>` |  | [Optional] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## findV0FindGet

> FindPage findV0FindGet(q, mode, label, fileType, prefix, modality, updatedAfter, updatedBefore, limit, authorization)

Hybrid passage retrieval over the full file body

Passage-level chunk RAG over &#x60;embed_chunks&#x60;. Lexical (&#x60;chunk_tsv&#x60;, GIN) + semantic (HNSW over &#x60;embedding&#x60;) are run in parallel and fused via Reciprocal Rank Fusion (k&#x3D;60). Unlike &#x60;/v0/search&#x60;, which only sees the first ~16 KB preview of each artifact, &#x60;/v0/find&#x60; reaches the full file body.  **Modes:** - &#x60;hybrid&#x60; (default) — lexical + semantic, RRF-fused. - &#x60;lexical&#x60; — &#x60;chunk_tsv&#x60; only. Best for exact tokens, identifiers, code snippets. - &#x60;semantic&#x60; — embedding only. Best for conceptual queries where the surface terms differ from the query phrasing.  **Granularity:** results are passages, not files. A long document with multiple matching regions returns multiple hits with distinct &#x60;ord&#x60; values; consecutive &#x60;ord&#x60;s overlap by ~400 tokens. Dedupe by &#x60;art_id&#x60; if you want one row per file.  **Span citations:** &#x60;char_start&#x60;/&#x60;char_end&#x60; for text &amp; code, &#x60;page_start&#x60;/&#x60;page_end&#x60; for PDFs, &#x60;time_start_ms&#x60;/&#x60;time_end_ms&#x60; for audio &amp; video. Only the modality-relevant pair is populated.  **Filters:** &#x60;label&#x60;, &#x60;file_type&#x60;, &#x60;prefix&#x60;, &#x60;modality&#x60; (repeatable), &#x60;updated_after&#x60; / &#x60;updated_before&#x60; (RFC 3339 timestamps, inclusive bounds on &#x60;updated_at&#x60;, applied to both legs).  **Wiki coverage:** &#x60;/v0/find&#x60; excludes &#x60;_wiki/&#x60; paths by default and — importantly — does NOT cover them even when the caller passes &#x60;prefix&#x3D;_wiki/...&#x60;. Wiki pages are not embedded by the pipeline (they\&#39;re system-generated output, not user input), so &#x60;embed_chunks&#x60; has no rows for them and the join returns empty. Use &#x60;wiki_search&#x60; (or &#x60;list&#x60;/&#x60;grep&#x60; with a &#x60;_wiki/&#x60; prefix) for the wiki layer.  **Embedding availability:** when &#x60;GEMINI_API_KEY&#x60; is not configured, &#x60;mode&#x3D;semantic&#x60; returns 500; &#x60;mode&#x3D;hybrid&#x60; logs a warning and falls back to lexical-only; &#x60;mode&#x3D;lexical&#x60; is unaffected.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { FindV0FindGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

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
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FindPage**](FindPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getArtifactByIdMetaV0ArtifactsArtIdMetaGet

> ArtifactOut getArtifactByIdMetaV0ArtifactsArtIdMetaGet(artId, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getArtifactByIdV0ArtifactsArtIdGet

> ArtifactOut getArtifactByIdV0ArtifactsArtIdGet(artId, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getArtifactMetaV0ArtifactsPathMetaGet

> ArtifactOut getArtifactMetaV0ArtifactsPathMetaGet(path, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet

> VersionOut getArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet(artId, versionNumber, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // number
    versionNumber: 56,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**VersionOut**](VersionOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFeedbackStatusV0FeedbackFbkIdGet

> any getFeedbackStatusV0FeedbackFbkIdGet(fbkId, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    fbkId: fbkId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFolderByIdMetaV0FoldersFldIdMetaGet

> FolderOut getFolderByIdMetaV0FoldersFldIdMetaGet(fldId, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFolderByIdV0FoldersFldIdGet

> FolderOut getFolderByIdV0FoldersFldIdGet(fldId, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFolderByPathMetaV0FoldersPathMetaGet

> FolderOut getFolderByPathMetaV0FoldersPathMetaGet(path, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getFolderByPathV0FoldersPathGet

> FolderOut getFolderByPathV0FoldersPathGet(path, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getJobLogsV0JobsJobIdLogsGet

> any getJobLogsV0JobsJobIdLogsGet(jobId, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    jobId: jobId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getJobV0JobsJobIdGet

> any getJobV0JobsJobIdGet(jobId, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    jobId: jobId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getProjectV0ProjectsFldIdGet

> any getProjectV0ProjectsFldIdGet(fldId, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getShareStateWebShareRidGet

> any getShareStateWebShareRidGet(rid)

Get Share State

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { GetShareStateWebShareRidGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    rid: rid_example,
  } satisfies GetShareStateWebShareRidGetRequest;

  try {
    const data = await api.getShareStateWebShareRidGet(body);
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
| **rid** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## healthHealthGet

> any healthHealthGet()

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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## inviteMemberWebWebMembersInvitePost

> any inviteMemberWebWebMembersInvitePost(email, csrf, role, workspaceName)

Invite Member Web

Admin invites a person by email (workspaces-design §4.4). Sends the invite email via the e2a lane. Admin-only; a non-admin is bounced.  Rename-on-first-invite (workspaces-design §4.6): a single-member workspace still carries its onboarding default name. The invite form offers an optional &#x60;workspace_name&#x60; — a LIGHT prompt, not a gate. If non-empty, we rename the workspace in the SAME submit (before sending) so teammates land in a named workspace, not \&quot;Someone\&#39;s Drive\&quot;.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { InviteMemberWebWebMembersInvitePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    email: email_example,
    // string
    csrf: csrf_example,
    // string (optional)
    role: role_example,
    // string (optional)
    workspaceName: workspaceName_example,
  } satisfies InviteMemberWebWebMembersInvitePostRequest;

  try {
    const data = await api.inviteMemberWebWebMembersInvitePost(body);
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
| **email** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **role** | `string` |  | [Optional] [Defaults to `&#39;member&#39;`] |
| **workspaceName** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listArtifactVersionsV0ArtifactsArtIdVersionsGet

> VersionPage listArtifactVersionsV0ArtifactsArtIdVersionsGet(artId, cursor, limit, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // string (optional)
    cursor: cursor_example,
    // number (optional)
    limit: 56,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**VersionPage**](VersionPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listArtifactsV0ArtifactsGet

> Page listArtifactsV0ArtifactsGet(prefix, label, fileType, cursor, limit, authorization)

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
  const api = new DefaultApi();

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
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listEventsRouteV0EventsGet

> EventPage listEventsRouteV0EventsGet(artId, action, since, before, cursor, limit, authorization)

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
  const api = new DefaultApi();

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
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**EventPage**](EventPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listGrantsRouteV0GrantsGet

> GrantList listGrantsRouteV0GrantsGet(resource, authorization)

List live grants on a resource (requires can_manage)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListGrantsRouteV0GrantsGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string | art_*_/fld_* id or a path
    resource: resource_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**GrantList**](GrantList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listProjectJobsV0ProjectsFldIdJobsGet

> any listProjectJobsV0ProjectsFldIdJobsGet(fldId, status, limit, authorization)

List a project\&#39;s jobs

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListProjectJobsV0ProjectsFldIdJobsGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // string (optional)
    status: status_example,
    // number (optional)
    limit: 56,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSharesRouteV0SharesGet

> ShareList listSharesRouteV0SharesGet(resource, authorization)

List live share links on a resource (requires can_manage)

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListSharesRouteV0SharesGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string | art_*_/fld_* id or a path
    resource: resource_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ShareList**](ShareList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listTrashRouteV0DrivesDriveIdTrashGet

> any listTrashRouteV0DrivesDriveIdTrashGet(driveId, authorization)

List the authenticated drive\&#39;s trash

Returns soft-deleted artifacts on the drive plus the drive\&#39;s own soft-delete state (if applicable). The path-param &#x60;drive_id&#x60; MUST match the authenticated drive.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ListTrashRouteV0DrivesDriveIdTrashGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    driveId: driveId_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## loginAuthLoginGet

> any loginAuthLoginGet(returnTo)

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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## logoutAuthLogoutPost

> any logoutAuthLogoutPost(csrf)

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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## marketingGet

> string marketingGet()

Marketing

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { MarketingGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.marketingGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## marketplaceBrowseMarketplaceGet

> string marketplaceBrowseMarketplaceGet()

Marketplace Browse

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { MarketplaceBrowseMarketplaceGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.marketplaceBrowseMarketplaceGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## marketplaceDetailMarketplaceSlugGet

> string marketplaceDetailMarketplaceSlugGet(slug)

Marketplace Detail

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { MarketplaceDetailMarketplaceSlugGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    slug: slug_example,
  } satisfies MarketplaceDetailMarketplaceSlugGetRequest;

  try {
    const data = await api.marketplaceDetailMarketplaceSlugGet(body);
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
| **slug** | `string` |  | [Defaults to `undefined`] |

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
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## meUsageV0DrivesMeUsageGet

> any meUsageV0DrivesMeUsageGet(authorization)

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
  const api = new DefaultApi();

  const body = {
    // string (optional)
    authorization: authorization_example,
  } satisfies MeUsageV0DrivesMeUsageGetRequest;

  try {
    const data = await api.meUsageV0DrivesMeUsageGet(body);
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## meV0DrivesMeGet

> any meV0DrivesMeGet(authorization)

Me

Drive overview for the authenticated bearer token.  Wire-protocol preservation (WorkOS integration §6): the &#x60;email&#x60; field is preserved in the response shape; its meaning is now \&quot;the drive\&#39;s owner\&#39;s email\&quot; (via &#x60;drives.owner_user_id&#x60; → &#x60;users.email&#x60;, joined in &#x60;auth.resolve_drive&#x60;). For solo signups this equals v0 behavior — the email the user signed up with. Returns null if the owner has been hard-purged. &#x60;organization_id&#x60; is a new additive field.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { MeV0DrivesMeGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string (optional)
    authorization: authorization_example,
  } satisfies MeV0DrivesMeGetRequest;

  try {
    const data = await api.meV0DrivesMeGet(body);
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## moveFolderByIdV0FoldersFldIdMovePost

> FolderOut moveFolderByIdV0FoldersFldIdMovePost(fldId, folderMoveIn, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // FolderMoveIn
    folderMoveIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## moveFolderByPathV0FoldersPathMovePost

> FolderOut moveFolderByPathV0FoldersPathMovePost(path, folderMoveIn, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
    // FolderMoveIn
    folderMoveIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## oauthDisconnectWebOauthDisconnectPost

> any oauthDisconnectWebOauthDisconnectPost(chainId, csrf)

Oauth Disconnect

Disconnect one MCP client: revoke its whole rotation chain (mcp-oauth-design §4.8). Ownership is checked against the chain\&#39;s user_id — the form value is attacker-controllable.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { OauthDisconnectWebOauthDisconnectPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    chainId: chainId_example,
    // string
    csrf: csrf_example,
  } satisfies OauthDisconnectWebOauthDisconnectPostRequest;

  try {
    const data = await api.oauthDisconnectWebOauthDisconnectPost(body);
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
| **chainId** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## patchFolderByIdV0FoldersFldIdPatch

> FolderOut patchFolderByIdV0FoldersFldIdPatch(fldId, folderPatchIn, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // FolderPatchIn
    folderPatchIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## patchFolderByPathV0FoldersPathPatch

> FolderOut patchFolderByPathV0FoldersPathPatch(path, folderPatchIn, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
    // FolderPatchIn
    folderPatchIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**FolderOut**](FolderOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## patchGrantRouteV0GrantsGrnIdPatch

> GrantOut patchGrantRouteV0GrantsGrnIdPatch(grnId, grantPatchIn, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    grnId: grnId_example,
    // GrantPatchIn
    grantPatchIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**GrantOut**](GrantOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## postDescribeV0QueryDescribePost

> any postDescribeV0QueryDescribePost(describeIn, authorization)

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
  const api = new DefaultApi();

  const body = {
    // DescribeIn
    describeIn: ...,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## postFeedbackV0FeedbackPost

> any postFeedbackV0FeedbackPost(authorization)

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
  const api = new DefaultApi();

  const body = {
    // string (optional)
    authorization: authorization_example,
  } satisfies PostFeedbackV0FeedbackPostRequest;

  try {
    const data = await api.postFeedbackV0FeedbackPost(body);
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## postLookupValuesV0QueryLookupValuesPost

> any postLookupValuesV0QueryLookupValuesPost(lookupValuesIn, authorization)

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
  const api = new DefaultApi();

  const body = {
    // LookupValuesIn
    lookupValuesIn: ...,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## postQueryV0QueryPost

> any postQueryV0QueryPost(queryIn, authorization)

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
  const api = new DefaultApi();

  const body = {
    // QueryIn
    queryIn: ...,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## privacyPagePrivacyGet

> string privacyPagePrivacyGet()

Privacy Page

Public privacy &amp; data-handling disclosure. Linked from the marketing footer and the per-drive privacy settings card. Public — same disclosure for every visitor; no per-drive personalization.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PrivacyPagePrivacyGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.privacyPagePrivacyGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## projectPreviewPageFFldIdPreviewGet

> string projectPreviewPageFFldIdPreviewGet(fldId)

Project Preview Page

Live PDF preview for a project folder (latex-live-preview-design.md).  URL mirrors the folder permalink (&#x60;/f/{fld_id}&#x60; → dashboard; &#x60;/f/{fld_id}/preview&#x60; → live preview) and the editor (&#x60;/a/{art_id}/edit&#x60;). Owner-only focused viewer: the page polls &#x60;/web/projects/{fld_id}/preview&#x60; and re-renders the compiled PDF in place (PDF.js) as the agent recompiles. Anonymous / non-owner → bounce through login with this URL as return_to. The page renders an empty shell; preview.js owns all behavior.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ProjectPreviewPageFFldIdPreviewGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
  } satisfies ProjectPreviewPageFFldIdPreviewGetRequest;

  try {
    const data = await api.projectPreviewPageFFldIdPreviewGet(body);
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## publisherProfilePublishersHandleGet

> string publisherProfilePublishersHandleGet(handle)

Publisher Profile

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PublisherProfilePublishersHandleGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    handle: handle_example,
  } satisfies PublisherProfilePublishersHandleGetRequest;

  try {
    const data = await api.publisherProfilePublishersHandleGet(body);
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
| **handle** | `string` |  | [Defaults to `undefined`] |

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
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## putArtifactV0ArtifactsPathPut

> ArtifactOut putArtifactV0ArtifactsPathPut(path, contentType, xAgentdriveLabels, xAgentdriveMetadata, xAgentdriveSource, xAgentdriveActor, xAgentdriveChangeSummary, ifMatch, authorization)

Upload (or overwrite) an artifact

Upload an artifact at the given path. The path is treated as the artifact\&#39;s location in the drive — re-uploading the same path overwrites in place (idempotent).  **Limits:** request body must not exceed **50 MB**. Path must be non-empty, ≤256 chars, only &#x60;[A-Za-z0-9_./-]&#x60;, no &#x60;..&#x60; segments, no leading/trailing slash. Per-token write rate limit: 100/hour.  **Optional headers.** Each preserves the existing artifact\&#39;s value when omitted on an overwrite, and takes the create-default on a new path; send the header to replace it: - &#x60;X-AgentDrive-Labels&#x60;: comma-separated labels (e.g. &#x60;draft,report&#x60;); an empty value clears them. Each: lowercase &#x60;[a-z0-9_-]+&#x60;, ≤64 chars; ≤16 labels per artifact. - &#x60;X-AgentDrive-Metadata&#x60;: JSON object of agent-attached fields. - &#x60;X-AgentDrive-Source&#x60;: JSON &#x60;{\&quot;refs\&quot;: [...]}&#x60; source provenance (present, including &#x60;{\&quot;refs\&quot;: []}&#x60;, replaces). - &#x60;X-AgentDrive-Actor&#x60;: caller-supplied actor name (≤64 chars) for event-log attribution. Untrusted; never used for authz.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { PutArtifactV0ArtifactsPathPutRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

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
    ifMatch: ifMatch_example,
    // string (optional)
    authorization: authorization_example,
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
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## putProjectV0ProjectsFldIdPut

> any putProjectV0ProjectsFldIdPut(fldId, projectConfigIn, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // ProjectConfigIn
    projectConfigIn: ...,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## recoveryNewAccountAuthRecoveryNewAccountPost

> any recoveryNewAccountAuthRecoveryNewAccountPost(csrf, claim)

Recovery New Account

Start fresh under the same identity.  Provisions a new user / org / drive; the soft-deleted record stays in trash until garbage-collected. Lands on /welcome so the user sees the freshly-minted API key once.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RecoveryNewAccountAuthRecoveryNewAccountPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    csrf: csrf_example,
    // string (optional)
    claim: claim_example,
  } satisfies RecoveryNewAccountAuthRecoveryNewAccountPostRequest;

  try {
    const data = await api.recoveryNewAccountAuthRecoveryNewAccountPost(body);
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
| **claim** | `string` |  | [Optional] [Defaults to `&#39;bind&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## recoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGet

> any recoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGet()

Recovery New Account Expired

Friendly landing for the rare race where the soft-deleted row has been hard-purged between callback and recovery-page render. Clears the recovery cookie (only when one is present) and tells the user to retry — fresh sign-in will JIT-provision cleanly since no soft-deleted record blocks it any more.  Gated on &#x60;pending_recovery&#x60; so a normal signed-in user who navigates here directly doesn\&#39;t get their session wiped. Without a pending payload there\&#39;s nothing to expire; bounce home.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RecoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.recoveryNewAccountExpiredAuthRecoveryNewAccountExpiredGet();
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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## recoveryPageAuthRecoveryGet

> any recoveryPageAuthRecoveryGet()

Recovery Page

Show the recover-or-start-fresh decision. Requires a valid &#x60;pending_recovery&#x60; payload — direct hits without one bounce to /auth/login (the recovery state is only meaningful inside the callback → recovery → resolve chain).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RecoveryPageAuthRecoveryGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.recoveryPageAuthRecoveryGet();
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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## recoveryRestoreAuthRecoveryRestorePost

> any recoveryRestoreAuthRecoveryRestorePost(csrf)

Recovery Restore

Recover the soft-deleted account. Undelete cascade runs in &#x60;onboarding.recover_account&#x60;; on success we set the normal session and bounce to /dashboard. If the retention window has lapsed between page-render and POST (the GC raced us), surface the same \&quot;expired\&quot; redirect so the user lands somewhere actionable.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RecoveryRestoreAuthRecoveryRestorePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    csrf: csrf_example,
  } satisfies RecoveryRestoreAuthRecoveryRestorePostRequest;

  try {
    const data = await api.recoveryRestoreAuthRecoveryRestorePost(body);
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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## redeemShareSShareKeyGet

> any redeemShareSShareKeyGet(shareKey)

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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## redeemShareWithPasswordSShareKeyPost

> any redeemShareWithPasswordSShareKeyPost(shareKey, password)

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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## removeMemberWebWebMembersTargetUserIdRemovePost

> any removeMemberWebWebMembersTargetUserIdRemovePost(targetUserId, csrf, organizationId)

Remove Member Web

Remove a member (admin) or self-leave (any member). Soft-deletes the member\&#39;s owned drives in that workspace (workspaces-design §4.4). The sole-admin-with-members case is blocked (promote-or-delete).  Org scoping: defaults to the session\&#39;s active workspace. The \&quot;Your workspaces\&quot; list passes an explicit &#x60;organization_id&#x60; so a user can Leave a NON-active workspace too — authorized against THAT org\&#39;s standing (self-leave for any member there; admin to remove others). A forged/non-member org id is a no-leak forbidden.  Auth: gates on &#x60;current_user&#x60; + per-org standing, NOT &#x60;current_drive&#x60; (a driveless member of the target workspace must still be able to leave it). Attribution uses the user\&#39;s email.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RemoveMemberWebWebMembersTargetUserIdRemovePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    targetUserId: targetUserId_example,
    // string
    csrf: csrf_example,
    // string (optional)
    organizationId: organizationId_example,
  } satisfies RemoveMemberWebWebMembersTargetUserIdRemovePostRequest;

  try {
    const data = await api.removeMemberWebWebMembersTargetUserIdRemovePost(body);
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
| **targetUserId** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **organizationId** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## renameArtifactRouteV0ArtifactsArtIdPatch

> ArtifactOut renameArtifactRouteV0ArtifactsArtIdPatch(artId, renameIn, xAgentdriveActor, ifMatch, authorization)

Rename / move an artifact to a new path

Move the artifact to a new path on the same drive. ID, version history, source refs, labels, metadata, and the underlying CAS blob are preserved — only &#x60;path&#x60; and &#x60;updated_at&#x60; change.  Returns 409 PATH_CONFLICT if the target path is already taken. Use &#x60;X-AgentDrive-Actor&#x60; to attach attribution to the emitted &#x60;artifact.renamed&#x60; event.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RenameArtifactRouteV0ArtifactsArtIdPatchRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // RenameIn
    renameIn: ...,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    ifMatch: ifMatch_example,
    // string (optional)
    authorization: authorization_example,
  } satisfies RenameArtifactRouteV0ArtifactsArtIdPatchRequest;

  try {
    const data = await api.renameArtifactRouteV0ArtifactsArtIdPatch(body);
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
| **renameIn** | [RenameIn](RenameIn.md) |  | |
| **xAgentdriveActor** | `string` |  | [Optional] [Defaults to `undefined`] |
| **ifMatch** | `string` |  | [Optional] [Defaults to `undefined`] |
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## renameDriveWebWebDrivesDriveIdRenamePost

> any renameDriveWebWebDrivesDriveIdRenamePost(driveId, name, csrf)

Rename Drive Web

Rename a drive the caller owns (workspaces-design §4.5).  Owner-only: &#x60;drives.get_owned_drive&#x60; returns None for a peer-owned / forged / soft-deleted id, which we treat as a silent no-op (no-leak) and bounce back to the dashboard.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RenameDriveWebWebDrivesDriveIdRenamePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    driveId: driveId_example,
    // string
    name: name_example,
    // string
    csrf: csrf_example,
  } satisfies RenameDriveWebWebDrivesDriveIdRenamePostRequest;

  try {
    const data = await api.renameDriveWebWebDrivesDriveIdRenamePost(body);
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
| **name** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## renameWorkspaceWebWebWorkspacesOrgIdRenamePost

> any renameWorkspaceWebWebWorkspacesOrgIdRenamePost(orgId, name, csrf)

Rename Workspace Web

Rename a workspace the caller administers (workspaces-design §4.6).  Admin-gated against the PATH org (not just the session) so a stale cookie can\&#39;t redirect the rename. A non-admin / non-member is a no-leak no-op.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RenameWorkspaceWebWebWorkspacesOrgIdRenamePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    orgId: orgId_example,
    // string
    name: name_example,
    // string
    csrf: csrf_example,
  } satisfies RenameWorkspaceWebWebWorkspacesOrgIdRenamePostRequest;

  try {
    const data = await api.renameWorkspaceWebWebWorkspacesOrgIdRenamePost(body);
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
| **orgId** | `string` |  | [Defaults to `undefined`] |
| **name** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## resendInvitationWebWebInvitationsInvitationIdResendPost

> any resendInvitationWebWebInvitationsInvitationIdResendPost(invitationId, csrf)

Resend Invitation Web

Admin re-mints + re-emails a pending invite (workspaces-design §8).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ResendInvitationWebWebInvitationsInvitationIdResendPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    invitationId: invitationId_example,
    // string
    csrf: csrf_example,
  } satisfies ResendInvitationWebWebInvitationsInvitationIdResendPostRequest;

  try {
    const data = await api.resendInvitationWebWebInvitationsInvitationIdResendPost(body);
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
| **invitationId** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## restoreArtifactV0ArtifactsArtIdRestorePost

> ArtifactOut restoreArtifactV0ArtifactsArtIdRestorePost(artId, rename, overwrite, xAgentdriveActor, authorization)

Restore a soft-deleted artifact

Clear &#x60;deleted_at&#x60; + &#x60;purge_at&#x60; on a soft-deleted artifact. Available only while the artifact is in trash (i.e. before the GC cleanup cron purges it). Returns 404 if the artifact is live or already hard-deleted; 409 PATH_OCCUPIED if its path is now occupied by another live artifact. The 409 payload includes a &#x60;restore_options&#x60; block with &#x60;rename_to&#x60; and &#x60;force_overwrite&#x60; URLs the caller can follow to resolve the conflict — see deletion-design.md §5.4.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RestoreArtifactV0ArtifactsArtIdRestorePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

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
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## restoreDriveRouteV0DrivesDriveIdRestorePost

> any restoreDriveRouteV0DrivesDriveIdRestorePost(driveId, xAgentdriveActor, authorization)

Restore a soft-deleted drive

Clear &#x60;deleted_at&#x60; + &#x60;purge_at&#x60; on a soft-deleted drive. Soft-deleted child artifacts get their retention window rebased to the drive-restore moment (see deletion-design.md §5.2). Available only while the drive is in trash. Returns 404 if the drive is live or already hard-deleted.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RestoreDriveRouteV0DrivesDriveIdRestorePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    driveId: driveId_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## revokeGrantWebShareRidGrantGrnIdRevokePost

> any revokeGrantWebShareRidGrantGrnIdRevokePost(rid, grnId, xCsrfToken)

Revoke Grant

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RevokeGrantWebShareRidGrantGrnIdRevokePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    rid: rid_example,
    // string
    grnId: grnId_example,
    // string (optional)
    xCsrfToken: xCsrfToken_example,
  } satisfies RevokeGrantWebShareRidGrantGrnIdRevokePostRequest;

  try {
    const data = await api.revokeGrantWebShareRidGrantGrnIdRevokePost(body);
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
| **rid** | `string` |  | [Defaults to `undefined`] |
| **grnId** | `string` |  | [Defaults to `undefined`] |
| **xCsrfToken** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## revokeInvitationWebWebInvitationsInvitationIdRevokePost

> any revokeInvitationWebWebInvitationsInvitationIdRevokePost(invitationId, csrf)

Revoke Invitation Web

Admin revokes a pending invite (org-scoped, no-leak).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RevokeInvitationWebWebInvitationsInvitationIdRevokePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    invitationId: invitationId_example,
    // string
    csrf: csrf_example,
  } satisfies RevokeInvitationWebWebInvitationsInvitationIdRevokePostRequest;

  try {
    const data = await api.revokeInvitationWebWebInvitationsInvitationIdRevokePost(body);
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
| **invitationId** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## revokeKeyWebKeysRevokePost

> any revokeKeyWebKeysRevokePost(keyId, csrf)

Revoke Key

Revoke one of the active drive\&#39;s &#x60;ad_live_&#x60; keys.  Management gate (workspaces-v2 §4.4): revoking a shared drive\&#39;s key is admin-for-team / owner-for-personal — a mere member must not revoke a key out from under the team. &#x60;drive_keys.revoke&#x60; is additionally scoped by drive_id, so the form\&#39;s &#x60;key_id&#x60; can\&#39;t reach another drive\&#39;s key.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RevokeKeyWebKeysRevokePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    keyId: keyId_example,
    // string
    csrf: csrf_example,
  } satisfies RevokeKeyWebKeysRevokePostRequest;

  try {
    const data = await api.revokeKeyWebKeysRevokePost(body);
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
| **keyId** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## revokeLinkWebShareRidLinkShrIdRevokePost

> any revokeLinkWebShareRidLinkShrIdRevokePost(rid, shrId, xCsrfToken)

Revoke Link

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RevokeLinkWebShareRidLinkShrIdRevokePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    rid: rid_example,
    // string
    shrId: shrId_example,
    // string (optional)
    xCsrfToken: xCsrfToken_example,
  } satisfies RevokeLinkWebShareRidLinkShrIdRevokePostRequest;

  try {
    const data = await api.revokeLinkWebShareRidLinkShrIdRevokePost(body);
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
| **rid** | `string` |  | [Defaults to `undefined`] |
| **shrId** | `string` |  | [Defaults to `undefined`] |
| **xCsrfToken** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## revokeUserTokenWebTokensRevokePost

> any revokeUserTokenWebTokensRevokePost(tokenId, csrf)

Revoke User Token

Revoke one of the caller\&#39;s &#x60;ad_user_&#x60; tokens.  Ownership is enforced inside &#x60;user_tokens.revoke(token_id, user_id)&#x60; — the form\&#39;s &#x60;token_id&#x60; is attacker-controllable, so we never revoke by id alone. A non-matching id is a silent no-op (same redirect).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { RevokeUserTokenWebTokensRevokePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    tokenId: tokenId_example,
    // string
    csrf: csrf_example,
  } satisfies RevokeUserTokenWebTokensRevokePostRequest;

  try {
    const data = await api.revokeUserTokenWebTokensRevokePost(body);
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
| **tokenId** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## rotateShareRouteV0SharesShrIdRotatePost

> ShareMintOut rotateShareRouteV0SharesShrIdRotatePost(shrId, xAgentdriveActor, authorization)

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
  const api = new DefaultApi();

  const body = {
    // string
    shrId: shrId_example,
    // string (optional)
    xAgentdriveActor: xAgentdriveActor_example,
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ShareMintOut**](ShareMintOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## searchV0SearchGet

> SearchPage searchV0SearchGet(q, label, fileType, prefix, updatedAfter, updatedBefore, limit, authorization)

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
  const api = new DefaultApi();

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
    // string (optional)
    authorization: authorization_example,
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
| **authorization** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**SearchPage**](SearchPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## setMemberRoleWebWebMembersTargetUserIdRolePost

> any setMemberRoleWebWebMembersTargetUserIdRolePost(targetUserId, role, csrf)

Set Member Role Web

Admin promotes/demotes a member. Last-admin demote is blocked (workspaces-design §4.4).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { SetMemberRoleWebWebMembersTargetUserIdRolePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    targetUserId: targetUserId_example,
    // string
    role: role_example,
    // string
    csrf: csrf_example,
  } satisfies SetMemberRoleWebWebMembersTargetUserIdRolePostRequest;

  try {
    const data = await api.setMemberRoleWebWebMembersTargetUserIdRolePost(body);
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
| **targetUserId** | `string` |  | [Defaults to `undefined`] |
| **role** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## setPublicWebShareRidPublicPost

> any setPublicWebShareRidPublicPost(rid, publicIn, xCsrfToken)

Set Public

Toggle world-readable: create (idempotent) or revoke the &#x60;anyone:viewer&#x60; grant. On a folder this cascades to the subtree (the response carries the blast-radius the UI confirmed).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { SetPublicWebShareRidPublicPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    rid: rid_example,
    // PublicIn
    publicIn: ...,
    // string (optional)
    xCsrfToken: xCsrfToken_example,
  } satisfies SetPublicWebShareRidPublicPostRequest;

  try {
    const data = await api.setPublicWebShareRidPublicPost(body);
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
| **rid** | `string` |  | [Defaults to `undefined`] |
| **publicIn** | [PublicIn](PublicIn.md) |  | |
| **xCsrfToken** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## setSealWebShareRidSealPost

> any setSealWebShareRidSealPost(rid, sealIn, xCsrfToken)

Set Seal

Set the limited-access seal (&#x60;inherit_grants&#x60;). &#x60;false&#x60; makes the resource ignore grants inherited from ancestor folders (§4.6/§4.11). Gated on &#x60;can_manage&#x60; (changing who can reach the resource).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { SetSealWebShareRidSealPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    rid: rid_example,
    // SealIn
    sealIn: ...,
    // string (optional)
    xCsrfToken: xCsrfToken_example,
  } satisfies SetSealWebShareRidSealPostRequest;

  try {
    const data = await api.setSealWebShareRidSealPost(body);
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
| **rid** | `string` |  | [Defaults to `undefined`] |
| **sealIn** | [SealIn](SealIn.md) |  | |
| **xCsrfToken** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## settingsAccountSettingsGet

> string settingsAccountSettingsGet()

Settings Account

Default settings landing — Account info + Usage + Danger zone.  Usage folded in here (was a standalone &#x60;/settings/usage&#x60; tab): the same meter data is fetched via &#x60;_usage_context&#x60; and rendered as a section on this page.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { SettingsAccountSettingsGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.settingsAccountSettingsGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## settingsApiKeysSettingsApiKeysGet

> string settingsApiKeysSettingsApiKeysGet()

Settings Api Keys

API key tab. Also where &#x60;reveal_key&#x60; is rendered once after a key is minted; the reveal is consumed (removed from session) on first read.  Surfaces two credential classes (workspaces-design §5.6):   * the drive\&#39;s &#x60;ad_live_&#x60; per-drive keys (&#x60;drive_keys.list_for_drive&#x60;) —     a drive may hold several, each created/revoked individually.   * the user\&#39;s &#x60;ad_user_&#x60; identity tokens (&#x60;user_tokens&#x60;, mint/list/     revoke). Minting reveals the raw token once via the same     &#x60;reveal_key&#x60;-in-session mechanism as the drive keys.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { SettingsApiKeysSettingsApiKeysGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.settingsApiKeysSettingsApiKeysGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## settingsQuickstartSettingsQuickstartGet

> string settingsQuickstartSettingsQuickstartGet()

Settings Quickstart

Quickstart tab — the single connect-and-use surface, consolidating the former Skill + MCP-setup tabs. Hero is the copy-paste bootstrap prompt (for terminal-less agents); the &#x60;claude mcp add&#x60; one-liner is second (for Claude Code). Connected clients fold into a collapsible section below.  The full tool reference lives at &#x60;/agentdrive.md&#x60; (rendered from &#x60;skills/SKILL.md&#x60;); the bootstrap prompt points the agent there rather than inlining it here, keeping the tab drift-free.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { SettingsQuickstartSettingsQuickstartGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.settingsQuickstartSettingsQuickstartGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## settingsWorkspaceSettingsWorkspaceGet

> string settingsWorkspaceSettingsWorkspaceGet()

Settings Workspace

Standalone workspace settings page (decision O4): members list + pending invites + invite form + role change + remove.  Admin-gated for the management actions; a member sees the roster but no management controls (the template hides them unless &#x60;is_admin&#x60;). The active workspace is the session\&#39;s &#x60;active_organization_id&#x60;.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { SettingsWorkspaceSettingsWorkspaceGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.settingsWorkspaceSettingsWorkspaceGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## sharedFilesSharedGet

> string sharedFilesSharedGet()

Shared Files

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { SharedFilesSharedGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.sharedFilesSharedGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## streamUploadV0UploadTokenPut

> ArtifactOut streamUploadV0UploadTokenPut(token)

Proxied streaming upload (via an upload_url token)

Streams an artifact body into AgentDrive using a single-use token that was previously minted by the &#x60;upload_url&#x60; MCP tool. The token encodes the artifact path, content type, size cap, labels, metadata, source, actor, change summary, and &#x60;if_match&#x60; — all frozen at mint time. The request carries only the raw bytes + a &#x60;Content-Type&#x60; header that must match the signed value.  **Auth.** No Authorization header — the token in the path is the credential.  **Single-use.** Replay returns 409 TOKEN_REPLAYED. Expiry returns 401 TOKEN_EXPIRED. Bodies exceeding the signed cap return 413 BYTES_LIMIT.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { StreamUploadV0UploadTokenPutRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    token: token_example,
  } satisfies StreamUploadV0UploadTokenPutRequest;

  try {
    const data = await api.streamUploadV0UploadTokenPut(body);
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
| **token** | `string` |  | [Defaults to `undefined`] |

### Return type

[**ArtifactOut**](ArtifactOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **400** | Content-Type mismatch or other validation failure |  -  |
| **401** | Token invalid / expired / drive deleted |  -  |
| **403** | Path reserved for the system (WIKI_RESERVED) |  -  |
| **409** | Token already consumed (replay) |  -  |
| **412** | If-Match precondition failed |  -  |
| **413** | Body exceeded signed max_bytes or drive quota |  -  |
| **429** | Drive\&#39;s per-hour write budget exhausted |  -  |
| **503** | Storage backend unavailable (STORAGE_FAILURE) |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## switchDriveWebSwitchPost

> any switchDriveWebSwitchPost(csrf, driveId, organizationId)

Switch Drive

Switch the active workspace (and drive) — workspace-first (workspaces-design §4.3).  Two modes, mirroring the Linear/Slack/GitHub \&quot;switch by workspace\&quot; model:    * **Workspace switch** (&#x60;organization_id&#x60;): membership-check the     target org for the user; on success set it active and pin the     user\&#39;s OLDEST owned live drive there (deterministic), or None if     they own none — in which case the dashboard\&#39;s     &#x60;resolve_driveless_member&#x60; renders the \&quot;create your first drive\&quot;     empty state for that workspace.   * **Drive switch** (&#x60;drive_id&#x60;): validate the user OWNS the posted     drive (and is a live member of its workspace) via     &#x60;drives_svc.user_owns_drive&#x60;, then set both org + drive active.     Lets a multi-drive workspace pick a specific drive. If BOTH are     posted, the explicit &#x60;drive_id&#x60; wins (subject to its own check).  Both forms are no-leak: a forged / peer-owned / non-member target fails its check and is treated identically to \&quot;no such target\&quot; (303 back to /dashboard without mutating the session — no leak, no error oracle).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { SwitchDriveWebSwitchPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    csrf: csrf_example,
    // string (optional)
    driveId: driveId_example,
    // string (optional)
    organizationId: organizationId_example,
  } satisfies SwitchDriveWebSwitchPostRequest;

  try {
    const data = await api.switchDriveWebSwitchPost(body);
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
| **driveId** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **organizationId** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## termsPageTermsGet

> string termsPageTermsGet()

Terms Page

Public beta terms of service. Linked from the marketing footer.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { TermsPageTermsGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.termsPageTermsGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## toggleIndexingWebAccountIndexingPost

> any toggleIndexingWebAccountIndexingPost(csrf, enabled)

Toggle Indexing

Flip the per-drive &#x60;indexing_enabled&#x60; flag (privacy opt-out for sending file content to Gemini). Checkbox semantics: a checked HTML &#x60;&lt;input type&#x3D;checkbox name&#x3D;enabled value&#x3D;on&gt;&#x60; POSTs &#x60;enabled&#x3D;on&#x60;; unchecked posts NO &#x60;enabled&#x60; field at all, which Form(default&#x3D;\&#39;\&#39;) surfaces as the empty string.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ToggleIndexingWebAccountIndexingPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    csrf: csrf_example,
    // string (optional)
    enabled: enabled_example,
  } satisfies ToggleIndexingWebAccountIndexingPostRequest;

  try {
    const data = await api.toggleIndexingWebAccountIndexingPost(body);
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
| **enabled** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## trashWebTrashGet

> string trashWebTrashGet()

Trash

Drive-wide Trash: soft-deleted artifacts + folder roots, each with a Restore action. Restore wiring lives in web/file_ops.py.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { TrashWebTrashGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.trashWebTrashGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## viewArtifactHeadAArtIdHeadGet

> any viewArtifactHeadAArtIdHeadGet(artId)

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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## viewFileDriveIdPathGet

> any viewFileDriveIdPathGet(driveId, path, raw, download)

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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## viewPermalinkArtifactAArtIdGet

> any viewPermalinkArtifactAArtIdGet(artId)

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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## viewPermalinkFolderFFldIdGet

> any viewPermalinkFolderFFldIdGet(fldId)

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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webArtifactIndexedWebArtifactsIndexedGet

> any webArtifactIndexedWebArtifactsIndexedGet(path)

Web Artifact Indexed

Session-auth companion to &#x60;/v0/artifacts/{path}/meta&#x60; used by the wiki-banner poller in the browser. The poller runs in any logged-in owner\&#39;s tab; the v0 endpoint requires Bearer auth and was therefore dead for browser owners (the banner spinner never resolved).  Returns &#x60;{indexed_at, has_index}&#x60; so the poller can detect when the extraction finishes and reload the page. 401 if not signed in (anon viewer); 404 if the path doesn\&#39;t exist in the caller\&#39;s drive.  Rate limit is generous (120/min) because the banner polls every 5s and a user might leave multiple tabs open. Per-IP keying so one abusive client doesn\&#39;t starve out concurrent legit polls from other users.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebArtifactIndexedWebArtifactsIndexedGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
  } satisfies WebArtifactIndexedWebArtifactsIndexedGetRequest;

  try {
    const data = await api.webArtifactIndexedWebArtifactsIndexedGet(body);
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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webCopyArtifactWebArtifactsCopyPost

> any webCopyArtifactWebArtifactsCopyPost(artId, newPath, csrf, returnTo)

Web Copy Artifact

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebCopyArtifactWebArtifactsCopyPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // string
    newPath: newPath_example,
    // string
    csrf: csrf_example,
    // string (optional)
    returnTo: returnTo_example,
  } satisfies WebCopyArtifactWebArtifactsCopyPostRequest;

  try {
    const data = await api.webCopyArtifactWebArtifactsCopyPost(body);
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
| **newPath** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **returnTo** | `string` |  | [Optional] [Defaults to `&#39;/dashboard&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webDeleteArtifactOpWebArtifactsDeletePost

> any webDeleteArtifactOpWebArtifactsDeletePost(path, csrf, returnTo)

Web Delete Artifact Op

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebDeleteArtifactOpWebArtifactsDeletePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
    // string
    csrf: csrf_example,
    // string (optional)
    returnTo: returnTo_example,
  } satisfies WebDeleteArtifactOpWebArtifactsDeletePostRequest;

  try {
    const data = await api.webDeleteArtifactOpWebArtifactsDeletePost(body);
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
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **returnTo** | `string` |  | [Optional] [Defaults to `&#39;/dashboard&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webDeleteArtifactWebArtifactsPathDelete

> any webDeleteArtifactWebArtifactsPathDelete(path, xCsrfToken)

Web Delete Artifact

Cookie-authed delete used by the editor\&#39;s Discard button (&#x60;/a/{art_id}/edit&#x60;): if the user isn\&#39;t happy with a capture, they delete it right there instead of round-tripping through the dashboard. The bearer-authed &#x60;DELETE /v0/artifacts/{path}&#x60; won\&#39;t accept a cookie-only session, hence this &#x60;/web/...&#x60; alias — the same split as the autosave PUT above.  Mirrors the v0 DELETE\&#39;s guards: CSRF header (cross-site fetch can\&#39;t forge the token), write-quota consumption, and reserved &#x60;_wiki/&#x60; namespace rejection. Soft-delete semantics are identical too — the artifact lands in trash and is restorable until the GC cron purges it at &#x60;purge_at&#x60;, so a misclick through the confirm dialog is recoverable. &#x60;If-Match&#x60; is deliberately not supported: the editor is the only intended caller and always deletes whatever is current.  Note: &#x60;restore_url&#x60; in the response points at the bearer-authed v0 endpoint, which this cookie-only caller can\&#39;t hit — it\&#39;s kept for shape parity with the v0 DELETE and is informational here (a future web trash UI would need a &#x60;/web/...&#x60; restore alias).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebDeleteArtifactWebArtifactsPathDeleteRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
    // string (optional)
    xCsrfToken: xCsrfToken_example,
  } satisfies WebDeleteArtifactWebArtifactsPathDeleteRequest;

  try {
    const data = await api.webDeleteArtifactWebArtifactsPathDelete(body);
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
| **xCsrfToken** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webDeleteFolderWebFoldersDeletePost

> any webDeleteFolderWebFoldersDeletePost(fldId, csrf, recursive, returnTo)

Web Delete Folder

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebDeleteFolderWebFoldersDeletePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // string
    csrf: csrf_example,
    // string (optional)
    recursive: recursive_example,
    // string (optional)
    returnTo: returnTo_example,
  } satisfies WebDeleteFolderWebFoldersDeletePostRequest;

  try {
    const data = await api.webDeleteFolderWebFoldersDeletePost(body);
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
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **recursive** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **returnTo** | `string` |  | [Optional] [Defaults to `&#39;/dashboard&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webMoveFolderWebFoldersMovePost

> any webMoveFolderWebFoldersMovePost(fldId, newPath, csrf, returnTo)

Web Move Folder

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebMoveFolderWebFoldersMovePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // string
    newPath: newPath_example,
    // string
    csrf: csrf_example,
    // string (optional)
    returnTo: returnTo_example,
  } satisfies WebMoveFolderWebFoldersMovePostRequest;

  try {
    const data = await api.webMoveFolderWebFoldersMovePost(body);
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
| **newPath** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **returnTo** | `string` |  | [Optional] [Defaults to `&#39;/dashboard&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webNewFolderWebFoldersNewPost

> any webNewFolderWebFoldersNewPost(name, csrf, parent, returnTo)

Web New Folder

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebNewFolderWebFoldersNewPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    name: name_example,
    // string
    csrf: csrf_example,
    // string (optional)
    parent: parent_example,
    // string (optional)
    returnTo: returnTo_example,
  } satisfies WebNewFolderWebFoldersNewPostRequest;

  try {
    const data = await api.webNewFolderWebFoldersNewPost(body);
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
| **name** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **parent** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **returnTo** | `string` |  | [Optional] [Defaults to `&#39;/dashboard&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webProjectCompileWebProjectsFldIdCompilePost

> any webProjectCompileWebProjectsFldIdCompilePost(fldId, csrf, engine, entrypoint)

Web Project Compile

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebProjectCompileWebProjectsFldIdCompilePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // string
    csrf: csrf_example,
    // string (optional)
    engine: engine_example,
    // string (optional)
    entrypoint: entrypoint_example,
  } satisfies WebProjectCompileWebProjectsFldIdCompilePostRequest;

  try {
    const data = await api.webProjectCompileWebProjectsFldIdCompilePost(body);
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
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **engine** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **entrypoint** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webProjectFilesWebProjectsFldIdFilesGet

> any webProjectFilesWebProjectsFldIdFilesGet(fldId)

Web Project Files

Cookie-authed file tree + read-only source manifest for the LaTeX workspace (handoff §3). Same auth contract as the preview poll (401 / 404-not-403). Source bytes themselves stream from &#x60;/a/{art_id}?raw&#x3D;1&#x60; (owner session authorizes private files) — this endpoint only lists.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebProjectFilesWebProjectsFldIdFilesGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
  } satisfies WebProjectFilesWebProjectsFldIdFilesGetRequest;

  try {
    const data = await api.webProjectFilesWebProjectsFldIdFilesGet(body);
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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webProjectPreviewWebProjectsFldIdPreviewGet

> any webProjectPreviewWebProjectsFldIdPreviewGet(fldId)

Web Project Preview

Session-auth poll for the live PDF preview page (latex-live-preview- design.md §4.2). The browser uses the session cookie (the &#x60;/v0&#x60; jobs API is Bearer-only), so this is the cookie-authed companion. Returns the current compile status + the last successful PDF + diagnostics so the page updates in place. 401 if not signed in; 404 (not 403) if the folder isn\&#39;t in the caller\&#39;s drive, to avoid existence leakage.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebProjectPreviewWebProjectsFldIdPreviewGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
  } satisfies WebProjectPreviewWebProjectsFldIdPreviewGetRequest;

  try {
    const data = await api.webProjectPreviewWebProjectsFldIdPreviewGet(body);
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

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webPutArtifactWebArtifactsPathPut

> any webPutArtifactWebArtifactsPathPut(path, xCsrfToken)

Web Put Artifact

Cookie-authed write of an image artifact. Used by the SnipIt web editor (&#x60;/a/{art_id}/edit&#x60;) for autosave; the bearer-authed &#x60;PUT /v0/artifacts/{path}&#x60; won\&#39;t accept a cookie-only session.  Owner-only; the path is checked against the signed-in user\&#39;s drive. Accepts &#x60;image/_*&#x60; (SnipIt editor autosave) and &#x60;application/pdf&#x60; (the PDF viewer\&#39;s annotation save) only — refuses everything else so the editor can\&#39;t smuggle markdown/HTML or anything else through this surface. Mirrors every guard the v0 PUT enforces — write quota, reserved &#x60;_wiki/&#x60; namespace rejection, per-tier max-bytes cap (both &#x60;Content-Length&#x60; short-circuit and post-body length check) — so a logged-in user can\&#39;t bypass quota or write into the wiki by routing autosaves through this endpoint instead of the v0 API. CSRF is checked via the &#x60;X-CSRF-Token&#x60; header (see &#x60;csrf.require_csrf_header&#x60;); the editor reads the token from the &#x60;&lt;meta name&#x3D;\&quot;csrf-token\&quot;&gt;&#x60; tag rendered into the edit page. Rate-limited per-IP/user at the same cadence the editor\&#39;s 1.5s autosave can sustain without flagging abuse.  Cross-workspace (design §4.3): the editor page is reached by a stable-id URL that may name a drive outside the session\&#39;s active workspace, so the write must target the RESOURCE\&#39;s drive, not the active one. The editor sends the resolved drive in an &#x60;X-Drive-Id&#x60; header; we authorize ownership of THAT drive via &#x60;resolve_owned_drive&#x60; (it returns None for a forged / unowned id → 401, never a write). Absent header ⇒ fall back to &#x60;current_drive&#x60; (pre-fast-follow behavior; a cached old client still works, only without the cross-workspace fix).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebPutArtifactWebArtifactsPathPutRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    path: path_example,
    // string (optional)
    xCsrfToken: xCsrfToken_example,
  } satisfies WebPutArtifactWebArtifactsPathPutRequest;

  try {
    const data = await api.webPutArtifactWebArtifactsPathPut(body);
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
| **xCsrfToken** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webRenameArtifactWebArtifactsRenamePost

> any webRenameArtifactWebArtifactsRenamePost(artId, newPath, csrf, returnTo)

Web Rename Artifact

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebRenameArtifactWebArtifactsRenamePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // string
    newPath: newPath_example,
    // string
    csrf: csrf_example,
    // string (optional)
    returnTo: returnTo_example,
  } satisfies WebRenameArtifactWebArtifactsRenamePostRequest;

  try {
    const data = await api.webRenameArtifactWebArtifactsRenamePost(body);
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
| **newPath** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **returnTo** | `string` |  | [Optional] [Defaults to `&#39;/dashboard&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webRestoreArtifactWebArtifactsRestorePost

> any webRestoreArtifactWebArtifactsRestorePost(artId, csrf, returnTo)

Web Restore Artifact

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebRestoreArtifactWebArtifactsRestorePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    artId: artId_example,
    // string
    csrf: csrf_example,
    // string (optional)
    returnTo: returnTo_example,
  } satisfies WebRestoreArtifactWebArtifactsRestorePostRequest;

  try {
    const data = await api.webRestoreArtifactWebArtifactsRestorePost(body);
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
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **returnTo** | `string` |  | [Optional] [Defaults to `&#39;/web/trash&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webRestoreFolderWebFoldersRestorePost

> any webRestoreFolderWebFoldersRestorePost(fldId, csrf, returnTo)

Web Restore Folder

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebRestoreFolderWebFoldersRestorePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    fldId: fldId_example,
    // string
    csrf: csrf_example,
    // string (optional)
    returnTo: returnTo_example,
  } satisfies WebRestoreFolderWebFoldersRestorePostRequest;

  try {
    const data = await api.webRestoreFolderWebFoldersRestorePost(body);
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
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **returnTo** | `string` |  | [Optional] [Defaults to `&#39;/web/trash&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webSetMetadataWebSetPost

> any webSetMetadataWebSetPost(target, csrf, description, returnTo)

Web Set Metadata

Folder description edit (target &#x3D; &#x60;fld_&lt;id&gt;&#x60;).  \&quot;Public/private\&quot; is no longer a folder/artifact flag — access is expressed through grants (permission-sharing-design §4.4), so this endpoint only edits folder descriptions. Artifact targets are rejected; publishing an artifact is the dedicated grant/&#x60;publish&#x60; flow, not a metadata toggle.

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebSetMetadataWebSetPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // string
    target: target_example,
    // string
    csrf: csrf_example,
    // string (optional)
    description: description_example,
    // string (optional)
    returnTo: returnTo_example,
  } satisfies WebSetMetadataWebSetPostRequest;

  try {
    const data = await api.webSetMetadataWebSetPost(body);
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
| **target** | `string` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **description** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **returnTo** | `string` |  | [Optional] [Defaults to `&#39;/dashboard&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webUploadWebUploadPost

> any webUploadWebUploadPost(file, csrf, destDir, returnTo)

Web Upload

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebUploadWebUploadPostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  const body = {
    // Blob
    file: BINARY_DATA_HERE,
    // string
    csrf: csrf_example,
    // string (optional)
    destDir: destDir_example,
    // string (optional)
    returnTo: returnTo_example,
  } satisfies WebUploadWebUploadPostRequest;

  try {
    const data = await api.webUploadWebUploadPost(body);
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
| **file** | `Blob` |  | [Defaults to `undefined`] |
| **csrf** | `string` |  | [Defaults to `undefined`] |
| **destDir** | `string` |  | [Optional] [Defaults to `&#39;&#39;`] |
| **returnTo** | `string` |  | [Optional] [Defaults to `&#39;/dashboard&#39;`] |

### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## webhooksPageWebhooksGet

> string webhooksPageWebhooksGet()

Webhooks Page

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WebhooksPageWebhooksGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.webhooksPageWebhooksGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## welcomeWelcomeGet

> string welcomeWelcomeGet()

Welcome

Show the three-step welcome screen and consume &#x60;reveal_key&#x60;.  Auth-required. If no key is in the session, redirect onward to &#x60;/dashboard&#x60; (the user has already saved theirs, or is a returning visitor who arrived here by typing the URL).

### Example

```ts
import {
  Configuration,
  DefaultApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { WelcomeWelcomeGetRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new DefaultApi();

  try {
    const data = await api.welcomeWelcomeGet();
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

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

