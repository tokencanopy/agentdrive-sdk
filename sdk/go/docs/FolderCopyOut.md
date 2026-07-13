# FolderCopyOut

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
**FromFldId** | **string** |  | 
**NArtifactsCopied** | **int32** |  | 

## Methods

### NewFolderCopyOut

`func NewFolderCopyOut(id string, driveId string, path string, etag string, createdAt time.Time, updatedAt time.Time, fromFldId string, nArtifactsCopied int32, ) *FolderCopyOut`

NewFolderCopyOut instantiates a new FolderCopyOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFolderCopyOutWithDefaults

`func NewFolderCopyOutWithDefaults() *FolderCopyOut`

NewFolderCopyOutWithDefaults instantiates a new FolderCopyOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *FolderCopyOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FolderCopyOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FolderCopyOut) SetId(v string)`

SetId sets Id field to given value.


### GetDriveId

`func (o *FolderCopyOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *FolderCopyOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *FolderCopyOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetPath

`func (o *FolderCopyOut) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *FolderCopyOut) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *FolderCopyOut) SetPath(v string)`

SetPath sets Path field to given value.


### GetDescription

`func (o *FolderCopyOut) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *FolderCopyOut) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *FolderCopyOut) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *FolderCopyOut) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *FolderCopyOut) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *FolderCopyOut) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetInheritGrants

`func (o *FolderCopyOut) GetInheritGrants() bool`

GetInheritGrants returns the InheritGrants field if non-nil, zero value otherwise.

### GetInheritGrantsOk

`func (o *FolderCopyOut) GetInheritGrantsOk() (*bool, bool)`

GetInheritGrantsOk returns a tuple with the InheritGrants field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInheritGrants

`func (o *FolderCopyOut) SetInheritGrants(v bool)`

SetInheritGrants sets InheritGrants field to given value.

### HasInheritGrants

`func (o *FolderCopyOut) HasInheritGrants() bool`

HasInheritGrants returns a boolean if a field has been set.

### GetMetageneration

`func (o *FolderCopyOut) GetMetageneration() int32`

GetMetageneration returns the Metageneration field if non-nil, zero value otherwise.

### GetMetagenerationOk

`func (o *FolderCopyOut) GetMetagenerationOk() (*int32, bool)`

GetMetagenerationOk returns a tuple with the Metageneration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetageneration

`func (o *FolderCopyOut) SetMetageneration(v int32)`

SetMetageneration sets Metageneration field to given value.

### HasMetageneration

`func (o *FolderCopyOut) HasMetageneration() bool`

HasMetageneration returns a boolean if a field has been set.

### GetEtag

`func (o *FolderCopyOut) GetEtag() string`

GetEtag returns the Etag field if non-nil, zero value otherwise.

### GetEtagOk

`func (o *FolderCopyOut) GetEtagOk() (*string, bool)`

GetEtagOk returns a tuple with the Etag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEtag

`func (o *FolderCopyOut) SetEtag(v string)`

SetEtag sets Etag field to given value.


### GetCreatedAt

`func (o *FolderCopyOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *FolderCopyOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *FolderCopyOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *FolderCopyOut) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *FolderCopyOut) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *FolderCopyOut) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetDeletedAt

`func (o *FolderCopyOut) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *FolderCopyOut) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *FolderCopyOut) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.

### HasDeletedAt

`func (o *FolderCopyOut) HasDeletedAt() bool`

HasDeletedAt returns a boolean if a field has been set.

### SetDeletedAtNil

`func (o *FolderCopyOut) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *FolderCopyOut) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil
### GetPurgeAt

`func (o *FolderCopyOut) GetPurgeAt() time.Time`

GetPurgeAt returns the PurgeAt field if non-nil, zero value otherwise.

### GetPurgeAtOk

`func (o *FolderCopyOut) GetPurgeAtOk() (*time.Time, bool)`

GetPurgeAtOk returns a tuple with the PurgeAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurgeAt

`func (o *FolderCopyOut) SetPurgeAt(v time.Time)`

SetPurgeAt sets PurgeAt field to given value.

### HasPurgeAt

`func (o *FolderCopyOut) HasPurgeAt() bool`

HasPurgeAt returns a boolean if a field has been set.

### SetPurgeAtNil

`func (o *FolderCopyOut) SetPurgeAtNil(b bool)`

 SetPurgeAtNil sets the value for PurgeAt to be an explicit nil

### UnsetPurgeAt
`func (o *FolderCopyOut) UnsetPurgeAt()`

UnsetPurgeAt ensures that no value is present for PurgeAt, not even an explicit nil
### GetFromFldId

`func (o *FolderCopyOut) GetFromFldId() string`

GetFromFldId returns the FromFldId field if non-nil, zero value otherwise.

### GetFromFldIdOk

`func (o *FolderCopyOut) GetFromFldIdOk() (*string, bool)`

GetFromFldIdOk returns a tuple with the FromFldId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFromFldId

`func (o *FolderCopyOut) SetFromFldId(v string)`

SetFromFldId sets FromFldId field to given value.


### GetNArtifactsCopied

`func (o *FolderCopyOut) GetNArtifactsCopied() int32`

GetNArtifactsCopied returns the NArtifactsCopied field if non-nil, zero value otherwise.

### GetNArtifactsCopiedOk

`func (o *FolderCopyOut) GetNArtifactsCopiedOk() (*int32, bool)`

GetNArtifactsCopiedOk returns a tuple with the NArtifactsCopied field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNArtifactsCopied

`func (o *FolderCopyOut) SetNArtifactsCopied(v int32)`

SetNArtifactsCopied sets NArtifactsCopied field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


