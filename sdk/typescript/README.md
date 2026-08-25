# @tokencanopy/agentdrive-sdk@0.0.2

A TypeScript SDK client for the drive.tokencanopy.com API.

## Usage

First, install the SDK from npm.

```bash
npm install @tokencanopy/agentdrive-sdk --save
```

Next, try it out.


```ts
import {
  Configuration,
  ArtifactsApi,
} from '@tokencanopy/agentdrive-sdk';
import type { ArtifactsContentRequest } from '@tokencanopy/agentdrive-sdk';

async function example() {
  console.log("🚀 Testing @tokencanopy/agentdrive-sdk SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new ArtifactsApi(config);

  const body = {
    // string
    driveId: driveId_example,
    // string
    artifactId: artifactId_example,
    // string (optional)
    ifNoneMatch: ifNoneMatch_example,
    // string | Deprecated: redundant with the operation\'s `bearerAuth` security requirement, which is how a generated client should learn to authenticate. Scheduled for removal. (optional)
    authorization: authorization_example,
  } satisfies ArtifactsContentRequest;

  try {
    const data = await api.artifactsContent(body);
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

All URIs are relative to *https://drive.tokencanopy.com*

| Class | Method | HTTP request | Description
| ----- | ------ | ------------ | -------------
*ArtifactsApi* | [**artifactsContent**](docs/ArtifactsApi.md#artifactscontent) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id}/content | Read Artifact Content
*ArtifactsApi* | [**artifactsCopy**](docs/ArtifactsApi.md#artifactscopy) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/copy | Copy Artifact
*ArtifactsApi* | [**artifactsCreate**](docs/ArtifactsApi.md#artifactscreate) | **POST** /v0/drives/{drive_id}/artifacts | Create Artifact
*ArtifactsApi* | [**artifactsDelete**](docs/ArtifactsApi.md#artifactsdelete) | **DELETE** /v0/drives/{drive_id}/artifacts/{artifact_id} | Delete Artifact
*ArtifactsApi* | [**artifactsList**](docs/ArtifactsApi.md#artifactslist) | **GET** /v0/drives/{drive_id}/artifacts | List Artifacts
*ArtifactsApi* | [**artifactsRead**](docs/ArtifactsApi.md#artifactsread) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id} | Read Artifact
*ArtifactsApi* | [**artifactsRestore**](docs/ArtifactsApi.md#artifactsrestore) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/restore | Restore Artifact
*ArtifactsApi* | [**artifactsUpdate**](docs/ArtifactsApi.md#artifactsupdate) | **PATCH** /v0/drives/{drive_id}/artifacts/{artifact_id} | Update Artifact
*ChangesApi* | [**changesList**](docs/ChangesApi.md#changeslist) | **GET** /v0/drives/{drive_id}/changes | List Changes
*DefaultApi* | [**health**](docs/DefaultApi.md#health) | **GET** /health | Health
*DiscoveryApi* | [**oauthProtectedResource**](docs/DiscoveryApi.md#oauthprotectedresource) | **GET** /.well-known/oauth-protected-resource | Protected-resource metadata (RFC 9728)
*DownloadsApi* | [**downloadCapabilitiesCreate**](docs/DownloadsApi.md#downloadcapabilitiescreateoperation) | **POST** /v0/drives/{drive_id}/download-capabilities | Create Download Capability
*DrivesApi* | [**drivesCreate**](docs/DrivesApi.md#drivescreate) | **POST** /v0/drives | Create Drive
*DrivesApi* | [**drivesDelete**](docs/DrivesApi.md#drivesdelete) | **DELETE** /v0/drives/{drive_id} | Delete Drive
*DrivesApi* | [**drivesList**](docs/DrivesApi.md#driveslist) | **GET** /v0/drives | List Drives
*DrivesApi* | [**drivesRead**](docs/DrivesApi.md#drivesread) | **GET** /v0/drives/{drive_id} | Read Drive
*DrivesApi* | [**drivesRestore**](docs/DrivesApi.md#drivesrestore) | **POST** /v0/drives/{drive_id}/restore | Restore Drive
*DrivesApi* | [**drivesUpdate**](docs/DrivesApi.md#drivesupdate) | **PATCH** /v0/drives/{drive_id} | Update Drive
*DrivesApi* | [**drivesUsage**](docs/DrivesApi.md#drivesusage) | **GET** /v0/drives/{drive_id}/usage | Drive Usage
*FoldersApi* | [**foldersCopy**](docs/FoldersApi.md#folderscopy) | **POST** /v0/drives/{drive_id}/folders/{folder_id}/copy | Copy Folder
*FoldersApi* | [**foldersCreate**](docs/FoldersApi.md#folderscreate) | **POST** /v0/drives/{drive_id}/folders | Create Folder
*FoldersApi* | [**foldersDelete**](docs/FoldersApi.md#foldersdelete) | **DELETE** /v0/drives/{drive_id}/folders/{folder_id} | Delete Folder
*FoldersApi* | [**foldersList**](docs/FoldersApi.md#folderslist) | **GET** /v0/drives/{drive_id}/folders | List Folders
*FoldersApi* | [**foldersRead**](docs/FoldersApi.md#foldersread) | **GET** /v0/drives/{drive_id}/folders/{folder_id} | Read Folder
*FoldersApi* | [**foldersRestore**](docs/FoldersApi.md#foldersrestore) | **POST** /v0/drives/{drive_id}/folders/{folder_id}/restore | Restore Folder
*FoldersApi* | [**foldersUpdate**](docs/FoldersApi.md#foldersupdate) | **PATCH** /v0/drives/{drive_id}/folders/{folder_id} | Update Folder
*GrantsApi* | [**grantsCreate**](docs/GrantsApi.md#grantscreate) | **POST** /v0/drives/{drive_id}/grants | Create Grant
*GrantsApi* | [**grantsList**](docs/GrantsApi.md#grantslist) | **GET** /v0/drives/{drive_id}/grants | List Grants
*GrantsApi* | [**grantsRead**](docs/GrantsApi.md#grantsread) | **GET** /v0/drives/{drive_id}/grants/{grant_id} | Read Grant
*GrantsApi* | [**grantsRevoke**](docs/GrantsApi.md#grantsrevoke) | **DELETE** /v0/drives/{drive_id}/grants/{grant_id} | Revoke Grant
*GrantsApi* | [**grantsUpdate**](docs/GrantsApi.md#grantsupdate) | **PATCH** /v0/drives/{drive_id}/grants/{grant_id} | Update Grant
*NavigationApi* | [**entriesList**](docs/NavigationApi.md#entrieslist) | **GET** /v0/drives/{drive_id}/entries | List Entries
*NavigationApi* | [**lookup**](docs/NavigationApi.md#lookup) | **GET** /v0/drives/{drive_id}/lookup | Lookup
*SearchApi* | [**driveSearch**](docs/SearchApi.md#drivesearch) | **GET** /v0/drives/{drive_id}/search | Drive Search
*SharesApi* | [**sharesCreate**](docs/SharesApi.md#sharescreate) | **POST** /v0/drives/{drive_id}/shares | Create Share
*SharesApi* | [**sharesList**](docs/SharesApi.md#shareslist) | **GET** /v0/drives/{drive_id}/shares | List Shares
*SharesApi* | [**sharesRead**](docs/SharesApi.md#sharesread) | **GET** /v0/drives/{drive_id}/shares/{share_id} | Read Share
*SharesApi* | [**sharesRevoke**](docs/SharesApi.md#sharesrevoke) | **DELETE** /v0/drives/{drive_id}/shares/{share_id} | Revoke Share
*SharesApi* | [**sharesRotate**](docs/SharesApi.md#sharesrotate) | **POST** /v0/drives/{drive_id}/shares/{share_id}/rotate | Rotate Share
*SharesRedemptionApi* | [**sharesRedeem**](docs/SharesRedemptionApi.md#sharesredeem) | **GET** /s/{share_key} | Redeem Share
*UploadsApi* | [**uploadsComplete**](docs/UploadsApi.md#uploadscomplete) | **POST** /v0/drives/{drive_id}/uploads/{upload_id}/complete | Complete Upload
*UploadsApi* | [**uploadsCreate**](docs/UploadsApi.md#uploadscreateoperation) | **POST** /v0/drives/{drive_id}/uploads | Begin Upload
*UploadsApi* | [**uploadsDelete**](docs/UploadsApi.md#uploadsdelete) | **DELETE** /v0/drives/{drive_id}/uploads/{upload_id} | Cancel Upload
*UploadsApi* | [**uploadsRead**](docs/UploadsApi.md#uploadsread) | **GET** /v0/drives/{drive_id}/uploads/{upload_id} | Read Upload
*VersionsApi* | [**versionsAppend**](docs/VersionsApi.md#versionsappend) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions | Append Version
*VersionsApi* | [**versionsContent**](docs/VersionsApi.md#versionscontent) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/content | Read Version Content
*VersionsApi* | [**versionsList**](docs/VersionsApi.md#versionslist) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions | List Versions
*VersionsApi* | [**versionsRead**](docs/VersionsApi.md#versionsread) | **GET** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id} | Read Version
*VersionsApi* | [**versionsRestore**](docs/VersionsApi.md#versionsrestore) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/versions/{version_id}/restore | Restore Version
*ViewerSessionsApi* | [**viewerSessionsCreate**](docs/ViewerSessionsApi.md#viewersessionscreate) | **POST** /v0/drives/{drive_id}/artifacts/{artifact_id}/viewer-sessions | Create Viewer Session


### Models

- [ArtifactCopyIn](docs/ArtifactCopyIn.md)
- [ArtifactEntryOut](docs/ArtifactEntryOut.md)
- [ArtifactListOut](docs/ArtifactListOut.md)
- [ArtifactOut](docs/ArtifactOut.md)
- [ArtifactUpdateIn](docs/ArtifactUpdateIn.md)
- [ChangeActorOut](docs/ChangeActorOut.md)
- [ChangeOut](docs/ChangeOut.md)
- [ChangePageOut](docs/ChangePageOut.md)
- [ChangeResourceOut](docs/ChangeResourceOut.md)
- [DownloadCapabilitiesCreateRequest](docs/DownloadCapabilitiesCreateRequest.md)
- [DownloadCapabilitiesCreateRequestTarget](docs/DownloadCapabilitiesCreateRequestTarget.md)
- [DownloadCapabilitiesCreateRequestTargetOneOf](docs/DownloadCapabilitiesCreateRequestTargetOneOf.md)
- [DownloadCapabilitiesCreateRequestTargetOneOf1](docs/DownloadCapabilitiesCreateRequestTargetOneOf1.md)
- [DownloadCapabilityOut](docs/DownloadCapabilityOut.md)
- [DownloadOut](docs/DownloadOut.md)
- [DownloadTargetOut](docs/DownloadTargetOut.md)
- [DriveCreateIn](docs/DriveCreateIn.md)
- [DriveListOut](docs/DriveListOut.md)
- [DriveOut](docs/DriveOut.md)
- [DriveUpdateIn](docs/DriveUpdateIn.md)
- [DriveUsageOut](docs/DriveUsageOut.md)
- [EntriesInner](docs/EntriesInner.md)
- [EntryListOut](docs/EntryListOut.md)
- [ErrorResponse](docs/ErrorResponse.md)
- [ErrorResponseError](docs/ErrorResponseError.md)
- [FolderCascadeOut](docs/FolderCascadeOut.md)
- [FolderCopyIn](docs/FolderCopyIn.md)
- [FolderCreateIn](docs/FolderCreateIn.md)
- [FolderEntryOut](docs/FolderEntryOut.md)
- [FolderListOut](docs/FolderListOut.md)
- [FolderOut](docs/FolderOut.md)
- [FolderUpdateIn](docs/FolderUpdateIn.md)
- [GrantCreateIn](docs/GrantCreateIn.md)
- [GrantListOut](docs/GrantListOut.md)
- [GrantOut](docs/GrantOut.md)
- [GrantUpdateIn](docs/GrantUpdateIn.md)
- [HealthDegradedDetail](docs/HealthDegradedDetail.md)
- [HealthDegradedResponse](docs/HealthDegradedResponse.md)
- [HealthOut](docs/HealthOut.md)
- [LookupOut](docs/LookupOut.md)
- [SearchHitOut](docs/SearchHitOut.md)
- [SearchPageOut](docs/SearchPageOut.md)
- [ShareCreateIn](docs/ShareCreateIn.md)
- [ShareCreateOut](docs/ShareCreateOut.md)
- [ShareListOut](docs/ShareListOut.md)
- [ShareOut](docs/ShareOut.md)
- [Target](docs/Target.md)
- [UploadBeginOut](docs/UploadBeginOut.md)
- [UploadChecksumOut](docs/UploadChecksumOut.md)
- [UploadChunksOut](docs/UploadChunksOut.md)
- [UploadCleanupOut](docs/UploadCleanupOut.md)
- [UploadContentOut](docs/UploadContentOut.md)
- [UploadFailureOut](docs/UploadFailureOut.md)
- [UploadInitiationOut](docs/UploadInitiationOut.md)
- [UploadOut](docs/UploadOut.md)
- [UploadResultOut](docs/UploadResultOut.md)
- [UploadSessionOut](docs/UploadSessionOut.md)
- [UploadTargetArtifactOut](docs/UploadTargetArtifactOut.md)
- [UploadTargetVersionOut](docs/UploadTargetVersionOut.md)
- [UploadTransferOut](docs/UploadTransferOut.md)
- [UploadWithTransferOut](docs/UploadWithTransferOut.md)
- [UploadsCreateRequest](docs/UploadsCreateRequest.md)
- [UploadsCreateRequestContent](docs/UploadsCreateRequestContent.md)
- [UploadsCreateRequestContentChecksum](docs/UploadsCreateRequestContentChecksum.md)
- [UploadsCreateRequestTarget](docs/UploadsCreateRequestTarget.md)
- [UploadsCreateRequestTargetOneOf](docs/UploadsCreateRequestTargetOneOf.md)
- [UploadsCreateRequestTargetOneOf1](docs/UploadsCreateRequestTargetOneOf1.md)
- [V0ErrorEnvelope](docs/V0ErrorEnvelope.md)
- [ValidationErrorResponse](docs/ValidationErrorResponse.md)
- [ValidationErrorResponseError](docs/ValidationErrorResponseError.md)
- [ValidationErrorResponseErrorDetails](docs/ValidationErrorResponseErrorDetails.md)
- [ValidationErrorResponseErrorDetailsFieldsInner](docs/ValidationErrorResponseErrorDetailsFieldsInner.md)
- [VersionCreatedOut](docs/VersionCreatedOut.md)
- [VersionListOut](docs/VersionListOut.md)
- [VersionOut](docs/VersionOut.md)
- [ViewerSessionCreateIn](docs/ViewerSessionCreateIn.md)
- [ViewerSessionCreateOut](docs/ViewerSessionCreateOut.md)

### Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
#### bearerAuth


- **Type**: HTTP Bearer Token authentication (JWT)

## About

This TypeScript SDK client supports the [Fetch API](https://fetch.spec.whatwg.org/)
and is automatically generated by the
[OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `0.0.1`
- Package version: `0.0.2`
- Generator version: `7.25.0`
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
