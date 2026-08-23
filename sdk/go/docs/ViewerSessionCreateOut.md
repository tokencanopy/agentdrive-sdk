# ViewerSessionCreateOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ArtifactId** | **string** |  |
**CreatedAt** | **time.Time** |  |
**Credential** | Pointer to **NullableString** | Plaintext viewer credential. Present only on first execution of a mint; null on idempotent replay — mint a new session with a fresh Idempotency-Key to obtain a credential. | [optional]
**DriveId** | **string** |  |
**ExpiresAt** | **time.Time** |  |
**ExpiresIn** | **int32** | Seconds until the session expires, from mint time. |
**Id** | **string** |  |
**VersionId** | **string** |  |

## Methods

### NewViewerSessionCreateOut

`func NewViewerSessionCreateOut(artifactId string, createdAt time.Time, driveId string, expiresAt time.Time, expiresIn int32, id string, versionId string, ) *ViewerSessionCreateOut`

NewViewerSessionCreateOut instantiates a new ViewerSessionCreateOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewViewerSessionCreateOutWithDefaults

`func NewViewerSessionCreateOutWithDefaults() *ViewerSessionCreateOut`

NewViewerSessionCreateOutWithDefaults instantiates a new ViewerSessionCreateOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetArtifactId

`func (o *ViewerSessionCreateOut) GetArtifactId() string`

GetArtifactId returns the ArtifactId field if non-nil, zero value otherwise.

### GetArtifactIdOk

`func (o *ViewerSessionCreateOut) GetArtifactIdOk() (*string, bool)`

GetArtifactIdOk returns a tuple with the ArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtifactId

`func (o *ViewerSessionCreateOut) SetArtifactId(v string)`

SetArtifactId sets ArtifactId field to given value.


### GetCreatedAt

`func (o *ViewerSessionCreateOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ViewerSessionCreateOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ViewerSessionCreateOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetCredential

`func (o *ViewerSessionCreateOut) GetCredential() string`

GetCredential returns the Credential field if non-nil, zero value otherwise.

### GetCredentialOk

`func (o *ViewerSessionCreateOut) GetCredentialOk() (*string, bool)`

GetCredentialOk returns a tuple with the Credential field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCredential

`func (o *ViewerSessionCreateOut) SetCredential(v string)`

SetCredential sets Credential field to given value.

### HasCredential

`func (o *ViewerSessionCreateOut) HasCredential() bool`

HasCredential returns a boolean if a field has been set.

### SetCredentialNil

`func (o *ViewerSessionCreateOut) SetCredentialNil(b bool)`

 SetCredentialNil sets the value for Credential to be an explicit nil

### UnsetCredential
`func (o *ViewerSessionCreateOut) UnsetCredential()`

UnsetCredential ensures that no value is present for Credential, not even an explicit nil
### GetDriveId

`func (o *ViewerSessionCreateOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *ViewerSessionCreateOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *ViewerSessionCreateOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetExpiresAt

`func (o *ViewerSessionCreateOut) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *ViewerSessionCreateOut) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *ViewerSessionCreateOut) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### GetExpiresIn

`func (o *ViewerSessionCreateOut) GetExpiresIn() int32`

GetExpiresIn returns the ExpiresIn field if non-nil, zero value otherwise.

### GetExpiresInOk

`func (o *ViewerSessionCreateOut) GetExpiresInOk() (*int32, bool)`

GetExpiresInOk returns a tuple with the ExpiresIn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresIn

`func (o *ViewerSessionCreateOut) SetExpiresIn(v int32)`

SetExpiresIn sets ExpiresIn field to given value.


### GetId

`func (o *ViewerSessionCreateOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ViewerSessionCreateOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ViewerSessionCreateOut) SetId(v string)`

SetId sets Id field to given value.


### GetVersionId

`func (o *ViewerSessionCreateOut) GetVersionId() string`

GetVersionId returns the VersionId field if non-nil, zero value otherwise.

### GetVersionIdOk

`func (o *ViewerSessionCreateOut) GetVersionIdOk() (*string, bool)`

GetVersionIdOk returns a tuple with the VersionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionId

`func (o *ViewerSessionCreateOut) SetVersionId(v string)`

SetVersionId sets VersionId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
