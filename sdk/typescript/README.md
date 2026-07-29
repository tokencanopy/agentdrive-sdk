# @mnexa-ai/agentdrive-sdk@0.0.1

A TypeScript SDK client for the api.agentdrive.run API.

## Usage

First, install the SDK from npm.

```bash
npm install @mnexa-ai/agentdrive-sdk --save
```

Next, try it out.


```ts
import {
  Configuration,
  AgentAuthApi,
} from '@mnexa-ai/agentdrive-sdk';
import type { ExtensionExchangeV0AuthExtensionExchangePostRequest } from '@mnexa-ai/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @mnexa-ai/agentdrive-sdk SDK...");
  const api = new AgentAuthApi();

  const body = {
    // ExtensionExchangeRequest
    extensionExchangeRequest: ...,
  } satisfies ExtensionExchangeV0AuthExtensionExchangePostRequest;

  try {
    const data = await api.extensionExchangeV0AuthExtensionExchangePost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```


## Documentation

### API Endpoints

All URIs are relative to *https://api.agentdrive.run*

| Class | Method | HTTP request | Description
| ----- | ------ | ------------ | -------------
*AgentAuthApi* | [**extensionExchangeV0AuthExtensionExchangePost**](docs/AgentAuthApi.md#extensionexchangev0authextensionexchangepost) | **POST** /v0/auth/extension/exchange | Redeem an extension OAuth ticket for a JWT pair
*AgentAuthApi* | [**initiateClaimAgentIdentityClaimPost**](docs/AgentAuthApi.md#initiateclaimagentidentityclaimpost) | **POST** /agent/identity/claim | Initiate the human-claim ceremony for an agent identity
*AgentAuthApi* | [**jwksWellKnownJwksJsonGet**](docs/AgentAuthApi.md#jwkswellknownjwksjsonget) | **GET** /.well-known/jwks.json | JSON Web Key Set — public keys for verifying AgentDrive JWTs
*AgentAuthApi* | [**oauth2TokenOauth2TokenPost**](docs/AgentAuthApi.md#oauth2tokenoauth2tokenpost) | **POST** /oauth2/token | Exchange a credential for an access_token
*AgentAuthApi* | [**oauthAuthorizationServerWellKnownOauthAuthorizationServerGet**](docs/AgentAuthApi.md#oauthauthorizationserverwellknownoauthauthorizationserverget) | **GET** /.well-known/oauth-authorization-server | Authorization-server metadata (RFC 8414 + auth.md agent_auth block)
*AgentAuthApi* | [**oauthProtectedResourceMcpWellKnownOauthProtectedResourceMcpGet**](docs/AgentAuthApi.md#oauthprotectedresourcemcpwellknownoauthprotectedresourcemcpget) | **GET** /.well-known/oauth-protected-resource/mcp | Protected-resource metadata for the MCP endpoint (RFC 9728 §3.1)
*AgentAuthApi* | [**oauthProtectedResourceWellKnownOauthProtectedResourceGet**](docs/AgentAuthApi.md#oauthprotectedresourcewellknownoauthprotectedresourceget) | **GET** /.well-known/oauth-protected-resource | Protected-resource metadata (auth.md / RFC 9728-like discovery)
*AgentAuthApi* | [**registerAgentIdentityAgentIdentityPost**](docs/AgentAuthApi.md#registeragentidentityagentidentitypost) | **POST** /agent/identity | Register an agent identity (anonymous or ID-JAG)
*DefaultApi* | [**abortUploadV0UploadsUploadIdDelete**](docs/DefaultApi.md#abortuploadv0uploadsuploadiddelete) | **DELETE** /v0/uploads/{upload_id} | Abort a large (direct-to-GCS) upload session
*DefaultApi* | [**beginUploadV0UploadsPost**](docs/DefaultApi.md#beginuploadv0uploadspost) | **POST** /v0/uploads | Begin a large (direct-to-GCS) upload
*DefaultApi* | [**callbackAuthCallbackGet**](docs/DefaultApi.md#callbackauthcallbackget) | **GET** /auth/callback | Callback
*DefaultApi* | [**cancelJobV0JobsJobIdCancelPost**](docs/DefaultApi.md#canceljobv0jobsjobidcancelpost) | **POST** /v0/jobs/{job_id}/cancel | Cancel a queued/running job
*DefaultApi* | [**commitUploadV0UploadsUploadIdCommitPost**](docs/DefaultApi.md#commituploadv0uploadsuploadidcommitpost) | **POST** /v0/uploads/{upload_id}/commit | Commit a large (direct-to-GCS) upload
*DefaultApi* | [**copyArtifactRouteV0ArtifactsArtIdCopyPost**](docs/DefaultApi.md#copyartifactroutev0artifactsartidcopypost) | **POST** /v0/artifacts/{art_id}/copy | Duplicate an artifact to a new path (CAS-shared, new ID)
*DefaultApi* | [**copyFolderByIdV0FoldersFldIdCopyPost**](docs/DefaultApi.md#copyfolderbyidv0foldersfldidcopypost) | **POST** /v0/folders/{fld_id}/copy | Duplicate a folder subtree to a new path (CAS-shared, new IDs)
*DefaultApi* | [**createFolderByPathV0FoldersPathPut**](docs/DefaultApi.md#createfolderbypathv0folderspathput) | **PUT** /v0/folders/{path} | Create a folder (idempotent)
*DefaultApi* | [**createGrantRouteV0GrantsPost**](docs/DefaultApi.md#creategrantroutev0grantspost) | **POST** /v0/grants | Create (or fetch) a per-principal grant on a resource
*DefaultApi* | [**createShareRouteV0SharesPost**](docs/DefaultApi.md#createshareroutev0sharespost) | **POST** /v0/shares | Mint a share link (returns the share_key once)
*DefaultApi* | [**deleteArtifactByIdRouteV0ArtifactsArtIdDelete**](docs/DefaultApi.md#deleteartifactbyidroutev0artifactsartiddelete) | **DELETE** /v0/artifacts/{art_id} | Soft-delete an artifact by its stable ID
*DefaultApi* | [**deleteArtifactV0ArtifactsPathDelete**](docs/DefaultApi.md#deleteartifactv0artifactspathdelete) | **DELETE** /v0/artifacts/{path} | Delete Artifact
*DefaultApi* | [**deleteDriveRouteV0DrivesDriveIdDelete**](docs/DefaultApi.md#deletedriveroutev0drivesdriveiddelete) | **DELETE** /v0/drives/{drive_id} | Soft-delete a drive
*DefaultApi* | [**deleteFolderByIdV0FoldersFldIdDelete**](docs/DefaultApi.md#deletefolderbyidv0foldersfldiddelete) | **DELETE** /v0/folders/{fld_id} | Soft-delete a folder by stable ID (cascade with ?recursive&#x3D;true)
*DefaultApi* | [**deleteFolderByPathV0FoldersPathDelete**](docs/DefaultApi.md#deletefolderbypathv0folderspathdelete) | **DELETE** /v0/folders/{path} | Soft-delete a folder (cascade with ?recursive&#x3D;true)
*DefaultApi* | [**deleteGrantRouteV0GrantsGrnIdDelete**](docs/DefaultApi.md#deletegrantroutev0grantsgrniddelete) | **DELETE** /v0/grants/{grn_id} | Revoke a grant (can_manage, or self-revoke own grant)
*DefaultApi* | [**deleteShareRouteV0SharesShrIdDelete**](docs/DefaultApi.md#deleteshareroutev0sharesshriddelete) | **DELETE** /v0/shares/{shr_id} | Revoke a share link (requires can_manage)
*DefaultApi* | [**downloadArtifactByIdV0ArtifactsArtIdDownloadGet**](docs/DefaultApi.md#downloadartifactbyidv0artifactsartiddownloadget) | **GET** /v0/artifacts/{art_id}/download | Stream the artifact bytes by stable ID (never rendered HTML)
*DefaultApi* | [**downloadArtifactByPathV0ArtifactsPathDownloadGet**](docs/DefaultApi.md#downloadartifactbypathv0artifactspathdownloadget) | **GET** /v0/artifacts/{path}/download | Stream the artifact bytes by path (never rendered HTML)
*DefaultApi* | [**downloadArtifactVersionV0ArtifactsArtIdVersionsVersionNumberDownloadGet**](docs/DefaultApi.md#downloadartifactversionv0artifactsartidversionsversionnumberdownloadget) | **GET** /v0/artifacts/{art_id}/versions/{version_number}/download | Stream bytes for a specific version (machine surface)
*DefaultApi* | [**downloadUrlByIdV0ArtifactsArtIdDownloadUrlGet**](docs/DefaultApi.md#downloadurlbyidv0artifactsartiddownloadurlget) | **GET** /v0/artifacts/{art_id}/download-url | Signed direct-from-GCS download URL by stable ID
*DefaultApi* | [**downloadUrlByPathV0ArtifactsPathDownloadUrlGet**](docs/DefaultApi.md#downloadurlbypathv0artifactspathdownloadurlget) | **GET** /v0/artifacts/{path}/download-url | Signed direct-from-GCS download URL by path
*DefaultApi* | [**downloadUrlVersionV0ArtifactsArtIdVersionsVersionNumberDownloadUrlGet**](docs/DefaultApi.md#downloadurlversionv0artifactsartidversionsversionnumberdownloadurlget) | **GET** /v0/artifacts/{art_id}/versions/{version_number}/download-url | Signed direct-from-GCS download URL for a specific version
*DefaultApi* | [**enqueueJobV0ProjectsFldIdJobsPost**](docs/DefaultApi.md#enqueuejobv0projectsfldidjobspost) | **POST** /v0/projects/{fld_id}/jobs | Enqueue a compile job for a project (folder)
*DefaultApi* | [**extensionStartAuthExtensionStartGet**](docs/DefaultApi.md#extensionstartauthextensionstartget) | **GET** /auth/extension/start | Extension Start
*DefaultApi* | [**findV0FindGet**](docs/DefaultApi.md#findv0findget) | **GET** /v0/find | Hybrid passage retrieval over the full file body
*DefaultApi* | [**getArtifactByIdMetaV0ArtifactsArtIdMetaGet**](docs/DefaultApi.md#getartifactbyidmetav0artifactsartidmetaget) | **GET** /v0/artifacts/{art_id}/meta | Artifact metadata by stable ID (same shape as path /meta)
*DefaultApi* | [**getArtifactByIdV0ArtifactsArtIdGet**](docs/DefaultApi.md#getartifactbyidv0artifactsartidget) | **GET** /v0/artifacts/{art_id} | Canonical lookup of an artifact by its stable ID
*DefaultApi* | [**getArtifactMetaV0ArtifactsPathMetaGet**](docs/DefaultApi.md#getartifactmetav0artifactspathmetaget) | **GET** /v0/artifacts/{path}/meta | Get Artifact Meta
*DefaultApi* | [**getArtifactVersionV0ArtifactsArtIdVersionsVersionNumberGet**](docs/DefaultApi.md#getartifactversionv0artifactsartidversionsversionnumberget) | **GET** /v0/artifacts/{art_id}/versions/{version_number} | Metadata for a specific version of an artifact
*DefaultApi* | [**getDriveRouteV0DrivesDriveIdGet**](docs/DefaultApi.md#getdriveroutev0drivesdriveidget) | **GET** /v0/drives/{drive_id} | Drive overview by id (same shape as /drives/me)
*DefaultApi* | [**getFeedbackStatusV0FeedbackFbkIdGet**](docs/DefaultApi.md#getfeedbackstatusv0feedbackfbkidget) | **GET** /v0/feedback/{fbk_id} | Get Feedback Status
*DefaultApi* | [**getFolderByIdMetaV0FoldersFldIdMetaGet**](docs/DefaultApi.md#getfolderbyidmetav0foldersfldidmetaget) | **GET** /v0/folders/{fld_id}/meta | Folder metadata by stable ID (same shape as the bare id route)
*DefaultApi* | [**getFolderByIdV0FoldersFldIdGet**](docs/DefaultApi.md#getfolderbyidv0foldersfldidget) | **GET** /v0/folders/{fld_id} | Canonical lookup of a folder by its stable ID
*DefaultApi* | [**getFolderByPathMetaV0FoldersPathMetaGet**](docs/DefaultApi.md#getfolderbypathmetav0folderspathmetaget) | **GET** /v0/folders/{path}/meta | Folder metadata by path (same shape as the bare path route)
*DefaultApi* | [**getFolderByPathV0FoldersPathGet**](docs/DefaultApi.md#getfolderbypathv0folderspathget) | **GET** /v0/folders/{path} | Read folder metadata by path
*DefaultApi* | [**getGrantRouteV0GrantsGrnIdGet**](docs/DefaultApi.md#getgrantroutev0grantsgrnidget) | **GET** /v0/grants/{grn_id} | Read a single grant (can_manage, or the grant\&#39;s own principal)
*DefaultApi* | [**getJobLogsV0JobsJobIdLogsGet**](docs/DefaultApi.md#getjoblogsv0jobsjobidlogsget) | **GET** /v0/jobs/{job_id}/logs | Raw compile log (text/plain)
*DefaultApi* | [**getJobV0JobsJobIdGet**](docs/DefaultApi.md#getjobv0jobsjobidget) | **GET** /v0/jobs/{job_id} | Poll a job
*DefaultApi* | [**getProjectV0ProjectsFldIdGet**](docs/DefaultApi.md#getprojectv0projectsfldidget) | **GET** /v0/projects/{fld_id} | Get a project\&#39;s compile config
*DefaultApi* | [**getShareRouteV0SharesShrIdGet**](docs/DefaultApi.md#getshareroutev0sharesshridget) | **GET** /v0/shares/{shr_id} | Read a single share link\&#39;s metadata (requires can_manage)
*DefaultApi* | [**getUploadStatusV0UploadsUploadIdGet**](docs/DefaultApi.md#getuploadstatusv0uploadsuploadidget) | **GET** /v0/uploads/{upload_id} | Get the status of a large (direct-to-GCS) upload session
*DefaultApi* | [**healthHealthGet**](docs/DefaultApi.md#healthhealthget) | **GET** /health | Health
*DefaultApi* | [**listArtifactVersionsV0ArtifactsArtIdVersionsGet**](docs/DefaultApi.md#listartifactversionsv0artifactsartidversionsget) | **GET** /v0/artifacts/{art_id}/versions | List versions of an artifact, newest first
*DefaultApi* | [**listArtifactsV0ArtifactsGet**](docs/DefaultApi.md#listartifactsv0artifactsget) | **GET** /v0/artifacts | List artifacts in the drive
*DefaultApi* | [**listEventsRouteV0EventsGet**](docs/DefaultApi.md#listeventsroutev0eventsget) | **GET** /v0/events | Read the append-only event log for the authenticated drive
*DefaultApi* | [**listGrantsRouteV0GrantsGet**](docs/DefaultApi.md#listgrantsroutev0grantsget) | **GET** /v0/grants | List live grants on a resource (requires can_manage)
*DefaultApi* | [**listProjectJobsV0ProjectsFldIdJobsGet**](docs/DefaultApi.md#listprojectjobsv0projectsfldidjobsget) | **GET** /v0/projects/{fld_id}/jobs | List a project\&#39;s jobs
*DefaultApi* | [**listSharesRouteV0SharesGet**](docs/DefaultApi.md#listsharesroutev0sharesget) | **GET** /v0/shares | List live share links on a resource (requires can_manage)
*DefaultApi* | [**listTrashRouteV0DrivesDriveIdTrashGet**](docs/DefaultApi.md#listtrashroutev0drivesdriveidtrashget) | **GET** /v0/drives/{drive_id}/trash | List the authenticated drive\&#39;s trash
*DefaultApi* | [**loginAuthLoginGet**](docs/DefaultApi.md#loginauthloginget) | **GET** /auth/login | Login
*DefaultApi* | [**logoutAuthLogoutPost**](docs/DefaultApi.md#logoutauthlogoutpost) | **POST** /auth/logout | Logout
*DefaultApi* | [**meUsageV0DrivesMeUsageGet**](docs/DefaultApi.md#meusagev0drivesmeusageget) | **GET** /v0/drives/me/usage | Current-period usage + caps for the authenticated drive
*DefaultApi* | [**meV0DrivesMeGet**](docs/DefaultApi.md#mev0drivesmeget) | **GET** /v0/drives/me | Me
*DefaultApi* | [**moveArtifactRouteV0ArtifactsArtIdMovePost**](docs/DefaultApi.md#moveartifactroutev0artifactsartidmovepost) | **POST** /v0/artifacts/{art_id}/move | Rename / move an artifact to a new path
*DefaultApi* | [**moveFolderByIdV0FoldersFldIdMovePost**](docs/DefaultApi.md#movefolderbyidv0foldersfldidmovepost) | **POST** /v0/folders/{fld_id}/move | Rename / move a folder by stable ID (cascade descendants)
*DefaultApi* | [**moveFolderByPathV0FoldersPathMovePost**](docs/DefaultApi.md#movefolderbypathv0folderspathmovepost) | **POST** /v0/folders/{path}/move | Rename / move a folder (cascade-update descendants)
*DefaultApi* | [**patchArtifactRouteV0ArtifactsArtIdPatch**](docs/DefaultApi.md#patchartifactroutev0artifactsartidpatch) | **PATCH** /v0/artifacts/{art_id} | Edit artifact metadata (labels / metadata / source)
*DefaultApi* | [**patchFolderByIdV0FoldersFldIdPatch**](docs/DefaultApi.md#patchfolderbyidv0foldersfldidpatch) | **PATCH** /v0/folders/{fld_id} | Update folder metadata by stable ID
*DefaultApi* | [**patchFolderByPathV0FoldersPathPatch**](docs/DefaultApi.md#patchfolderbypathv0folderspathpatch) | **PATCH** /v0/folders/{path} | Update folder metadata by path
*DefaultApi* | [**patchGrantRouteV0GrantsGrnIdPatch**](docs/DefaultApi.md#patchgrantroutev0grantsgrnidpatch) | **PATCH** /v0/grants/{grn_id} | Update a grant\&#39;s role and/or expiry (requires can_manage)
*DefaultApi* | [**postDescribeV0QueryDescribePost**](docs/DefaultApi.md#postdescribev0querydescribepost) | **POST** /v0/query/describe | Describe a dataset\&#39;s column schema
*DefaultApi* | [**postFeedbackV0FeedbackPost**](docs/DefaultApi.md#postfeedbackv0feedbackpost) | **POST** /v0/feedback | Post Feedback
*DefaultApi* | [**postLookupValuesV0QueryLookupValuesPost**](docs/DefaultApi.md#postlookupvaluesv0querylookupvaluespost) | **POST** /v0/query/lookup-values | List distinct values of a dataset column
*DefaultApi* | [**postQueryV0QueryPost**](docs/DefaultApi.md#postqueryv0querypost) | **POST** /v0/query | Run a read-only SQL query over authorized datasets
*DefaultApi* | [**putArtifactV0ArtifactsPathPut**](docs/DefaultApi.md#putartifactv0artifactspathput) | **PUT** /v0/artifacts/{path} | Upload (or overwrite) an artifact
*DefaultApi* | [**putProjectV0ProjectsFldIdPut**](docs/DefaultApi.md#putprojectv0projectsfldidput) | **PUT** /v0/projects/{fld_id} | Set a project\&#39;s compile config (entrypoint/engine/auto_compile)
*DefaultApi* | [**redeemShareSShareKeyGet**](docs/DefaultApi.md#redeemsharessharekeyget) | **GET** /s/{share_key} | Redeem Share
*DefaultApi* | [**redeemShareWithPasswordSShareKeyPost**](docs/DefaultApi.md#redeemsharewithpasswordssharekeypost) | **POST** /s/{share_key} | Redeem Share With Password
*DefaultApi* | [**restoreArtifactV0ArtifactsArtIdRestorePost**](docs/DefaultApi.md#restoreartifactv0artifactsartidrestorepost) | **POST** /v0/artifacts/{art_id}/restore | Restore a soft-deleted artifact
*DefaultApi* | [**restoreArtifactVersionV0ArtifactsArtIdVersionsVersionNumberRestorePost**](docs/DefaultApi.md#restoreartifactversionv0artifactsartidversionsversionnumberrestorepost) | **POST** /v0/artifacts/{art_id}/versions/{version_number}/restore | Restore a previous version as a new head version
*DefaultApi* | [**restoreDriveRouteV0DrivesDriveIdRestorePost**](docs/DefaultApi.md#restoredriveroutev0drivesdriveidrestorepost) | **POST** /v0/drives/{drive_id}/restore | Restore a soft-deleted drive
*DefaultApi* | [**restoreFolderByIdV0FoldersFldIdRestorePost**](docs/DefaultApi.md#restorefolderbyidv0foldersfldidrestorepost) | **POST** /v0/folders/{fld_id}/restore | Restore a soft-deleted folder (cascade)
*DefaultApi* | [**rotateShareRouteV0SharesShrIdRotatePost**](docs/DefaultApi.md#rotateshareroutev0sharesshridrotatepost) | **POST** /v0/shares/{shr_id}/rotate | Revoke + reissue a share link\&#39;s key (requires can_share)
*DefaultApi* | [**searchV0SearchGet**](docs/DefaultApi.md#searchv0searchget) | **GET** /v0/search | Full-text search over artifacts in the drive
*DefaultApi* | [**viewArtifactHeadAArtIdHeadGet**](docs/DefaultApi.md#viewartifactheadaartidheadget) | **GET** /a/{art_id}/head | View Artifact Head
*DefaultApi* | [**viewArtifactVersionVArtIdVersionGet**](docs/DefaultApi.md#viewartifactversionvartidversionget) | **GET** /v/{art_id}/{version} | View Artifact Version
*DefaultApi* | [**viewFileDriveIdPathGet**](docs/DefaultApi.md#viewfiledriveidpathget) | **GET** /{drive_id}/{path} | View File
*DefaultApi* | [**viewPermalinkArtifactAArtIdGet**](docs/DefaultApi.md#viewpermalinkartifactaartidget) | **GET** /a/{art_id} | View Permalink Artifact
*DefaultApi* | [**viewPermalinkFolderFFldIdGet**](docs/DefaultApi.md#viewpermalinkfolderffldidget) | **GET** /f/{fld_id} | View Permalink Folder
*DrivesApi* | [**createDriveKeyRouteV0DrivesDriveIdKeysPost**](docs/DrivesApi.md#createdrivekeyroutev0drivesdriveidkeyspost) | **POST** /v0/drives/{drive_id}/keys | Create a drive API key
*DrivesApi* | [**createDriveRouteV0DrivesPost**](docs/DrivesApi.md#createdriveroutev0drivespost) | **POST** /v0/drives | Create a drive in your active space
*DrivesApi* | [**listDriveKeysRouteV0DrivesDriveIdKeysGet**](docs/DrivesApi.md#listdrivekeysroutev0drivesdriveidkeysget) | **GET** /v0/drives/{drive_id}/keys | List a drive\&#39;s API keys
*DrivesApi* | [**listDrivesRouteV0DrivesGet**](docs/DrivesApi.md#listdrivesroutev0drivesget) | **GET** /v0/drives | List the drives you can see
*DrivesApi* | [**renameDriveRouteV0DrivesDriveIdPatch**](docs/DrivesApi.md#renamedriveroutev0drivesdriveidpatch) | **PATCH** /v0/drives/{drive_id} | Rename a drive you own
*DrivesApi* | [**revokeDriveKeyRouteV0DrivesDriveIdKeysKeyIdRevokePost**](docs/DrivesApi.md#revokedrivekeyroutev0drivesdriveidkeyskeyidrevokepost) | **POST** /v0/drives/{drive_id}/keys/{key_id}/revoke | Revoke a drive API key
*DrivesApi* | [**rotateOneKeyRouteV0DrivesDriveIdKeysKeyIdRotatePost**](docs/DrivesApi.md#rotateonekeyroutev0drivesdriveidkeyskeyidrotatepost) | **POST** /v0/drives/{drive_id}/keys/{key_id}/rotate | Rotate one API key
*McpOauthApi* | [**oauth2RegisterOauth2RegisterPost**](docs/McpOauthApi.md#oauth2registeroauth2registerpost) | **POST** /oauth2/register | Dynamic Client Registration (RFC 7591)
*McpOauthApi* | [**oauth2RevokeOauth2RevokePost**](docs/McpOauthApi.md#oauth2revokeoauth2revokepost) | **POST** /oauth2/revoke | Token revocation (RFC 7009)
*McpOauthUiApi* | [**authorizeDecisionOauth2AuthorizePost**](docs/McpOauthUiApi.md#authorizedecisionoauth2authorizepost) | **POST** /oauth2/authorize | Authorize Decision
*McpOauthUiApi* | [**authorizePageOauth2AuthorizeGet**](docs/McpOauthUiApi.md#authorizepageoauth2authorizeget) | **GET** /oauth2/authorize | Authorize Page
*MembersApi* | [**inviteMemberV0MembersInvitePost**](docs/MembersApi.md#invitememberv0membersinvitepost) | **POST** /v0/members/invite | Invite a person to your workspace by email
*MembersApi* | [**listInvitationsV0InvitationsGet**](docs/MembersApi.md#listinvitationsv0invitationsget) | **GET** /v0/invitations | List pending invitations
*MembersApi* | [**listMembersV0MembersGet**](docs/MembersApi.md#listmembersv0membersget) | **GET** /v0/members | List the members of your active workspace
*MembersApi* | [**removeMemberV0MembersTargetUserIdDelete**](docs/MembersApi.md#removememberv0memberstargetuseriddelete) | **DELETE** /v0/members/{target_user_id} | Remove a member (or leave)
*MembersApi* | [**revokeInvitationV0InvitationsInvitationIdDelete**](docs/MembersApi.md#revokeinvitationv0invitationsinvitationiddelete) | **DELETE** /v0/invitations/{invitation_id} | Revoke a pending invitation
*MembersApi* | [**setMemberRoleV0MembersTargetUserIdPatch**](docs/MembersApi.md#setmemberrolev0memberstargetuseridpatch) | **PATCH** /v0/members/{target_user_id} | Change a member\&#39;s role
*TokensApi* | [**listTokensV0TokensGet**](docs/TokensApi.md#listtokensv0tokensget) | **GET** /v0/tokens | List your user-identity tokens
*TokensApi* | [**revokeTokenV0TokensTokenIdRevokePost**](docs/TokensApi.md#revoketokenv0tokenstokenidrevokepost) | **POST** /v0/tokens/{token_id}/revoke | Revoke one of your user-identity tokens
*WorkspacesApi* | [**createWorkspaceRouteV0WorkspacesPost**](docs/WorkspacesApi.md#createworkspaceroutev0workspacespost) | **POST** /v0/workspaces | Create a new shared drive
*WorkspacesApi* | [**listWorkspacesRouteV0WorkspacesGet**](docs/WorkspacesApi.md#listworkspacesroutev0workspacesget) | **GET** /v0/workspaces | List the spaces you belong to
*WorkspacesApi* | [**renameWorkspaceRouteV0WorkspacesOrgIdPatch**](docs/WorkspacesApi.md#renameworkspaceroutev0workspacesorgidpatch) | **PATCH** /v0/workspaces/{org_id} | Rename a shared drive you administer


### Models

- [AgentAuthMetadataOut](docs/AgentAuthMetadataOut.md)
- [AnonymousIdentityResponse](docs/AnonymousIdentityResponse.md)
- [ArtifactDeleteOut](docs/ArtifactDeleteOut.md)
- [ArtifactHeadOut](docs/ArtifactHeadOut.md)
- [ArtifactMoveIn](docs/ArtifactMoveIn.md)
- [ArtifactOut](docs/ArtifactOut.md)
- [ArtifactPatchIn](docs/ArtifactPatchIn.md)
- [ArtifactSource](docs/ArtifactSource.md)
- [AuthorizationServerMetadataOut](docs/AuthorizationServerMetadataOut.md)
- [AuthorizeDecisionOauth2AuthorizePost403Response](docs/AuthorizeDecisionOauth2AuthorizePost403Response.md)
- [ClaimInitRequest](docs/ClaimInitRequest.md)
- [ClaimInitResponse](docs/ClaimInitResponse.md)
- [ClaimMetadata](docs/ClaimMetadata.md)
- [ClientRegistrationOut](docs/ClientRegistrationOut.md)
- [CompileDiagnosticOut](docs/CompileDiagnosticOut.md)
- [CompileJobIn](docs/CompileJobIn.md)
- [CompileJobListOut](docs/CompileJobListOut.md)
- [CompileJobOut](docs/CompileJobOut.md)
- [CompileOptions](docs/CompileOptions.md)
- [CompileProjectOut](docs/CompileProjectOut.md)
- [CopyIn](docs/CopyIn.md)
- [DatasetDescriptionOut](docs/DatasetDescriptionOut.md)
- [DescribeIn](docs/DescribeIn.md)
- [DownloadUrlOut](docs/DownloadUrlOut.md)
- [DriveApiKeyCreateIn](docs/DriveApiKeyCreateIn.md)
- [DriveApiKeyCreateOut](docs/DriveApiKeyCreateOut.md)
- [DriveApiKeyListOut](docs/DriveApiKeyListOut.md)
- [DriveApiKeyOut](docs/DriveApiKeyOut.md)
- [DriveCreateIn](docs/DriveCreateIn.md)
- [DriveCreateOut](docs/DriveCreateOut.md)
- [DriveDeleteOut](docs/DriveDeleteOut.md)
- [DriveList](docs/DriveList.md)
- [DriveOut](docs/DriveOut.md)
- [DriveReadOut](docs/DriveReadOut.md)
- [DriveRenameIn](docs/DriveRenameIn.md)
- [DriveRestoreOut](docs/DriveRestoreOut.md)
- [DriveUsageOut](docs/DriveUsageOut.md)
- [ErrorBody](docs/ErrorBody.md)
- [ErrorDetail](docs/ErrorDetail.md)
- [ErrorResponse](docs/ErrorResponse.md)
- [EventOut](docs/EventOut.md)
- [EventPage](docs/EventPage.md)
- [ExtensionExchangeRequest](docs/ExtensionExchangeRequest.md)
- [ExtensionExchangeResponse](docs/ExtensionExchangeResponse.md)
- [FeedbackCreateOut](docs/FeedbackCreateOut.md)
- [FeedbackStatusOut](docs/FeedbackStatusOut.md)
- [FindHitOut](docs/FindHitOut.md)
- [FindPage](docs/FindPage.md)
- [FolderCopyIn](docs/FolderCopyIn.md)
- [FolderCopyOut](docs/FolderCopyOut.md)
- [FolderCreateIn](docs/FolderCreateIn.md)
- [FolderDeleteOut](docs/FolderDeleteOut.md)
- [FolderMoveIn](docs/FolderMoveIn.md)
- [FolderOut](docs/FolderOut.md)
- [FolderPatchIn](docs/FolderPatchIn.md)
- [FolderRestoreOut](docs/FolderRestoreOut.md)
- [GrantCreateIn](docs/GrantCreateIn.md)
- [GrantList](docs/GrantList.md)
- [GrantOut](docs/GrantOut.md)
- [GrantPatchIn](docs/GrantPatchIn.md)
- [GrantPrincipalIn](docs/GrantPrincipalIn.md)
- [HealthDegradedDetail](docs/HealthDegradedDetail.md)
- [HealthDegradedResponse](docs/HealthDegradedResponse.md)
- [HealthOut](docs/HealthOut.md)
- [HourlyUsageCounterOut](docs/HourlyUsageCounterOut.md)
- [IdentityAssertionMetadataOut](docs/IdentityAssertionMetadataOut.md)
- [InvitationList](docs/InvitationList.md)
- [InvitationOut](docs/InvitationOut.md)
- [InviteCreateOut](docs/InviteCreateOut.md)
- [JwkOut](docs/JwkOut.md)
- [JwksOut](docs/JwksOut.md)
- [LocInner](docs/LocInner.md)
- [LookupValuesIn](docs/LookupValuesIn.md)
- [LookupValuesOut](docs/LookupValuesOut.md)
- [MemberInviteIn](docs/MemberInviteIn.md)
- [MemberList](docs/MemberList.md)
- [MemberOut](docs/MemberOut.md)
- [MemberRemoveOut](docs/MemberRemoveOut.md)
- [MemberRoleIn](docs/MemberRoleIn.md)
- [OAuthProtocolErrorOut](docs/OAuthProtocolErrorOut.md)
- [OperationUsageOut](docs/OperationUsageOut.md)
- [Page](docs/Page.md)
- [ProjectConfigIn](docs/ProjectConfigIn.md)
- [ProtectedResourceMetadataOut](docs/ProtectedResourceMetadataOut.md)
- [QueryColumnOut](docs/QueryColumnOut.md)
- [QueryDryRunOut](docs/QueryDryRunOut.md)
- [QueryIn](docs/QueryIn.md)
- [QueryResultOut](docs/QueryResultOut.md)
- [RegisterAgentIdentityAgentIdentityPost422Response](docs/RegisterAgentIdentityAgentIdentityPost422Response.md)
- [ResponsePostQueryV0QueryPost](docs/ResponsePostQueryV0QueryPost.md)
- [RevokeOut](docs/RevokeOut.md)
- [SearchHitOut](docs/SearchHitOut.md)
- [SearchPage](docs/SearchPage.md)
- [ShareCreateIn](docs/ShareCreateIn.md)
- [ShareErrorOut](docs/ShareErrorOut.md)
- [ShareList](docs/ShareList.md)
- [ShareMintOut](docs/ShareMintOut.md)
- [ShareOut](docs/ShareOut.md)
- [ShareRedeemOut](docs/ShareRedeemOut.md)
- [SourceRef](docs/SourceRef.md)
- [StorageBreakdownOut](docs/StorageBreakdownOut.md)
- [StorageFootprintOut](docs/StorageFootprintOut.md)
- [TokenResponse](docs/TokenResponse.md)
- [TokenUsageOut](docs/TokenUsageOut.md)
- [TrashArtifactOut](docs/TrashArtifactOut.md)
- [TrashDriveOut](docs/TrashDriveOut.md)
- [TrashOut](docs/TrashOut.md)
- [UploadAbortOut](docs/UploadAbortOut.md)
- [UploadBeginIn](docs/UploadBeginIn.md)
- [UploadBeginOut](docs/UploadBeginOut.md)
- [UploadStatusOut](docs/UploadStatusOut.md)
- [UsageCounterOut](docs/UsageCounterOut.md)
- [UsagePeriodOut](docs/UsagePeriodOut.md)
- [UserTokenList](docs/UserTokenList.md)
- [UserTokenOut](docs/UserTokenOut.md)
- [ValidationErrorBody](docs/ValidationErrorBody.md)
- [ValidationErrorDetail](docs/ValidationErrorDetail.md)
- [ValidationErrorResponse](docs/ValidationErrorResponse.md)
- [ValidationIssue](docs/ValidationIssue.md)
- [VersionOut](docs/VersionOut.md)
- [VersionPage](docs/VersionPage.md)
- [VersionRetentionOut](docs/VersionRetentionOut.md)
- [WorkspaceCreateIn](docs/WorkspaceCreateIn.md)
- [WorkspaceCreateOut](docs/WorkspaceCreateOut.md)
- [WorkspaceList](docs/WorkspaceList.md)
- [WorkspaceOut](docs/WorkspaceOut.md)
- [WorkspaceRenameIn](docs/WorkspaceRenameIn.md)

### Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
#### BearerAuth


- **Type**: HTTP Bearer Token authentication (ad_live_ | ad_user_ | JWT)

## About

This TypeScript SDK client supports the [Fetch API](https://fetch.spec.whatwg.org/)
and is automatically generated by the
[OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `&lt;PINNED&gt;`
- Package version: `0.0.1`
- Generator version: `7.24.0`
- Build package: `org.openapitools.codegen.languages.TypeScriptFetchClientCodegen`

The generated npm module supports the following:

- Environments
  * Node.js
  * Webpack
  * Browserify
- Language levels
  * ES5 - you must have a Promises/A+ library installed
  * ES6
- Module systems
  * CommonJS
  * ES6 module system


## Development

### Building

To build the TypeScript source code, you need to have Node.js and npm installed.
After cloning the repository, navigate to the project directory and run:

```bash
npm install
npm run build
```

### Publishing

Once you've built the package, you can publish it to npm:

```bash
npm publish
```

## License

[]()
