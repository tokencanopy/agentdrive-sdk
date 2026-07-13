# FolderRestoreOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**DriveId** | **string** |  | 
**Path** | **string** |  | 
**Description** | Pointer to **NullableString** |  | [optional] 
**InheritGrants** | Pointer to **bool** |  | [optional] [default to true]
**Metageneration** | Pointer to **int32** |  | [optional] [default to 1]
**Etag** | **string** |  | 
**CreatedAt** | **time.Time** |  | 
**UpdatedAt** | **time.Time** |  | 
**DeletedAt** | Pointer to **NullableTime** |  | [optional] 
**PurgeAt** | Pointer to **NullableTime** |  | [optional] 
**NSubfoldersRestored** | **int32** |  | 
**NArtifactsRestored** | **int32** |  | 

## Methods

### NewFolderRestoreOut

`func NewFolderRestoreOut(id string, driveId string, path string, etag string, createdAt time.Time, updatedAt time.Time, nSubfoldersRestored int32, nArtifactsRestored int32, ) *FolderRestoreOut`

NewFolderRestoreOut instantiates a new FolderRestoreOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFolderRestoreOutWithDefaults

`func NewFolderRestoreOutWithDefaults() *FolderRestoreOut`

NewFolderRestoreOutWithDefaults instantiates a new FolderRestoreOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *FolderRestoreOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FolderRestoreOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FolderRestoreOut) SetId(v string)`

SetId sets Id field to given value.


### GetDriveId

`func (o *FolderRestoreOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *FolderRestoreOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *FolderRestoreOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetPath

`func (o *FolderRestoreOut) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *FolderRestoreOut) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *FolderRestoreOut) SetPath(v string)`

SetPath sets Path field to given value.


### GetDescription

`func (o *FolderRestoreOut) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *FolderRestoreOut) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *FolderRestoreOut) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *FolderRestoreOut) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *FolderRestoreOut) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *FolderRestoreOut) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetInheritGrants

`func (o *FolderRestoreOut) GetInheritGrants() bool`

GetInheritGrants returns the InheritGrants field if non-nil, zero value otherwise.

### GetInheritGrantsOk

`func (o *FolderRestoreOut) GetInheritGrantsOk() (*bool, bool)`

GetInheritGrantsOk returns a tuple with the InheritGrants field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInheritGrants

`func (o *FolderRestoreOut) SetInheritGrants(v bool)`

SetInheritGrants sets InheritGrants field to given value.

### HasInheritGrants

`func (o *FolderRestoreOut) HasInheritGrants() bool`

HasInheritGrants returns a boolean if a field has been set.

### GetMetageneration

`func (o *FolderRestoreOut) GetMetageneration() int32`

GetMetageneration returns the Metageneration field if non-nil, zero value otherwise.

### GetMetagenerationOk

`func (o *FolderRestoreOut) GetMetagenerationOk() (*int32, bool)`

GetMetagenerationOk returns a tuple with the Metageneration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetageneration

`func (o *FolderRestoreOut) SetMetageneration(v int32)`

SetMetageneration sets Metageneration field to given value.

### HasMetageneration

`func (o *FolderRestoreOut) HasMetageneration() bool`

HasMetageneration returns a boolean if a field has been set.

### GetEtag

`func (o *FolderRestoreOut) GetEtag() string`

GetEtag returns the Etag field if non-nil, zero value otherwise.

### GetEtagOk

`func (o *FolderRestoreOut) GetEtagOk() (*string, bool)`

GetEtagOk returns a tuple with the Etag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEtag

`func (o *FolderRestoreOut) SetEtag(v string)`

SetEtag sets Etag field to given value.


### GetCreatedAt

`func (o *FolderRestoreOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *FolderRestoreOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *FolderRestoreOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *FolderRestoreOut) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *FolderRestoreOut) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *FolderRestoreOut) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetDeletedAt

`func (o *FolderRestoreOut) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *FolderRestoreOut) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *FolderRestoreOut) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.

### HasDeletedAt

`func (o *FolderRestoreOut) HasDeletedAt() bool`

HasDeletedAt returns a boolean if a field has been set.

### SetDeletedAtNil

`func (o *FolderRestoreOut) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *FolderRestoreOut) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil
### GetPurgeAt

`func (o *FolderRestoreOut) GetPurgeAt() time.Time`

GetPurgeAt returns the PurgeAt field if non-nil, zero value otherwise.

### GetPurgeAtOk

`func (o *FolderRestoreOut) GetPurgeAtOk() (*time.Time, bool)`

GetPurgeAtOk returns a tuple with the PurgeAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurgeAt

`func (o *FolderRestoreOut) SetPurgeAt(v time.Time)`

SetPurgeAt sets PurgeAt field to given value.

### HasPurgeAt

`func (o *FolderRestoreOut) HasPurgeAt() bool`

HasPurgeAt returns a boolean if a field has been set.

### SetPurgeAtNil

`func (o *FolderRestoreOut) SetPurgeAtNil(b bool)`

 SetPurgeAtNil sets the value for PurgeAt to be an explicit nil

### UnsetPurgeAt
`func (o *FolderRestoreOut) UnsetPurgeAt()`

UnsetPurgeAt ensures that no value is present for PurgeAt, not even an explicit nil
### GetNSubfoldersRestored

`func (o *FolderRestoreOut) GetNSubfoldersRestored() int32`

GetNSubfoldersRestored returns the NSubfoldersRestored field if non-nil, zero value otherwise.

### GetNSubfoldersRestoredOk

`func (o *FolderRestoreOut) GetNSubfoldersRestoredOk() (*int32, bool)`

GetNSubfoldersRestoredOk returns a tuple with the NSubfoldersRestored field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNSubfoldersRestored

`func (o *FolderRestoreOut) SetNSubfoldersRestored(v int32)`

SetNSubfoldersRestored sets NSubfoldersRestored field to given value.


### GetNArtifactsRestored

`func (o *FolderRestoreOut) GetNArtifactsRestored() int32`

GetNArtifactsRestored returns the NArtifactsRestored field if non-nil, zero value otherwise.

### GetNArtifactsRestoredOk

`func (o *FolderRestoreOut) GetNArtifactsRestoredOk() (*int32, bool)`

GetNArtifactsRestoredOk returns a tuple with the NArtifactsRestored field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNArtifactsRestored

`func (o *FolderRestoreOut) SetNArtifactsRestored(v int32)`

SetNArtifactsRestored sets NArtifactsRestored field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


