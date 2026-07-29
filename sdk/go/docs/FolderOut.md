# FolderOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAt** | **time.Time** |  |
**DeletedAt** | Pointer to **NullableTime** |  | [optional]
**Description** | Pointer to **NullableString** |  | [optional]
**DriveId** | **string** |  |
**Etag** | **string** |  |
**Id** | **string** |  |
**InheritGrants** | Pointer to **bool** |  | [optional] [default to true]
**Metageneration** | Pointer to **int32** |  | [optional] [default to 1]
**Path** | **string** |  |
**PurgeAt** | Pointer to **NullableTime** |  | [optional]
**UpdatedAt** | **time.Time** |  |

## Methods

### NewFolderOut

`func NewFolderOut(createdAt time.Time, driveId string, etag string, id string, path string, updatedAt time.Time, ) *FolderOut`

NewFolderOut instantiates a new FolderOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFolderOutWithDefaults

`func NewFolderOutWithDefaults() *FolderOut`

NewFolderOutWithDefaults instantiates a new FolderOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreatedAt

`func (o *FolderOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *FolderOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *FolderOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetDeletedAt

`func (o *FolderOut) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *FolderOut) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *FolderOut) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.

### HasDeletedAt

`func (o *FolderOut) HasDeletedAt() bool`

HasDeletedAt returns a boolean if a field has been set.

### SetDeletedAtNil

`func (o *FolderOut) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *FolderOut) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil
### GetDescription

`func (o *FolderOut) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *FolderOut) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *FolderOut) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *FolderOut) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *FolderOut) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *FolderOut) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetDriveId

`func (o *FolderOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *FolderOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *FolderOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetEtag

`func (o *FolderOut) GetEtag() string`

GetEtag returns the Etag field if non-nil, zero value otherwise.

### GetEtagOk

`func (o *FolderOut) GetEtagOk() (*string, bool)`

GetEtagOk returns a tuple with the Etag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEtag

`func (o *FolderOut) SetEtag(v string)`

SetEtag sets Etag field to given value.


### GetId

`func (o *FolderOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FolderOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FolderOut) SetId(v string)`

SetId sets Id field to given value.


### GetInheritGrants

`func (o *FolderOut) GetInheritGrants() bool`

GetInheritGrants returns the InheritGrants field if non-nil, zero value otherwise.

### GetInheritGrantsOk

`func (o *FolderOut) GetInheritGrantsOk() (*bool, bool)`

GetInheritGrantsOk returns a tuple with the InheritGrants field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInheritGrants

`func (o *FolderOut) SetInheritGrants(v bool)`

SetInheritGrants sets InheritGrants field to given value.

### HasInheritGrants

`func (o *FolderOut) HasInheritGrants() bool`

HasInheritGrants returns a boolean if a field has been set.

### GetMetageneration

`func (o *FolderOut) GetMetageneration() int32`

GetMetageneration returns the Metageneration field if non-nil, zero value otherwise.

### GetMetagenerationOk

`func (o *FolderOut) GetMetagenerationOk() (*int32, bool)`

GetMetagenerationOk returns a tuple with the Metageneration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetageneration

`func (o *FolderOut) SetMetageneration(v int32)`

SetMetageneration sets Metageneration field to given value.

### HasMetageneration

`func (o *FolderOut) HasMetageneration() bool`

HasMetageneration returns a boolean if a field has been set.

### GetPath

`func (o *FolderOut) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *FolderOut) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *FolderOut) SetPath(v string)`

SetPath sets Path field to given value.


### GetPurgeAt

`func (o *FolderOut) GetPurgeAt() time.Time`

GetPurgeAt returns the PurgeAt field if non-nil, zero value otherwise.

### GetPurgeAtOk

`func (o *FolderOut) GetPurgeAtOk() (*time.Time, bool)`

GetPurgeAtOk returns a tuple with the PurgeAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurgeAt

`func (o *FolderOut) SetPurgeAt(v time.Time)`

SetPurgeAt sets PurgeAt field to given value.

### HasPurgeAt

`func (o *FolderOut) HasPurgeAt() bool`

HasPurgeAt returns a boolean if a field has been set.

### SetPurgeAtNil

`func (o *FolderOut) SetPurgeAtNil(b bool)`

 SetPurgeAtNil sets the value for PurgeAt to be an explicit nil

### UnsetPurgeAt
`func (o *FolderOut) UnsetPurgeAt()`

UnsetPurgeAt ensures that no value is present for PurgeAt, not even an explicit nil
### GetUpdatedAt

`func (o *FolderOut) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *FolderOut) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *FolderOut) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
