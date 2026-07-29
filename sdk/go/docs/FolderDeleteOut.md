# FolderDeleteOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DeletedAt** | **time.Time** |  |
**Id** | **string** |  |
**NArtifactsDeleted** | **int32** |  |
**NSubfoldersDeleted** | **int32** |  |
**Ok** | Pointer to **bool** |  | [optional] [default to true]
**Path** | **string** |  |
**PurgeAt** | **time.Time** |  |
**RetentionDays** | **int32** |  |

## Methods

### NewFolderDeleteOut

`func NewFolderDeleteOut(deletedAt time.Time, id string, nArtifactsDeleted int32, nSubfoldersDeleted int32, path string, purgeAt time.Time, retentionDays int32, ) *FolderDeleteOut`

NewFolderDeleteOut instantiates a new FolderDeleteOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFolderDeleteOutWithDefaults

`func NewFolderDeleteOutWithDefaults() *FolderDeleteOut`

NewFolderDeleteOutWithDefaults instantiates a new FolderDeleteOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDeletedAt

`func (o *FolderDeleteOut) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *FolderDeleteOut) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *FolderDeleteOut) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.


### GetId

`func (o *FolderDeleteOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FolderDeleteOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FolderDeleteOut) SetId(v string)`

SetId sets Id field to given value.


### GetNArtifactsDeleted

`func (o *FolderDeleteOut) GetNArtifactsDeleted() int32`

GetNArtifactsDeleted returns the NArtifactsDeleted field if non-nil, zero value otherwise.

### GetNArtifactsDeletedOk

`func (o *FolderDeleteOut) GetNArtifactsDeletedOk() (*int32, bool)`

GetNArtifactsDeletedOk returns a tuple with the NArtifactsDeleted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNArtifactsDeleted

`func (o *FolderDeleteOut) SetNArtifactsDeleted(v int32)`

SetNArtifactsDeleted sets NArtifactsDeleted field to given value.


### GetNSubfoldersDeleted

`func (o *FolderDeleteOut) GetNSubfoldersDeleted() int32`

GetNSubfoldersDeleted returns the NSubfoldersDeleted field if non-nil, zero value otherwise.

### GetNSubfoldersDeletedOk

`func (o *FolderDeleteOut) GetNSubfoldersDeletedOk() (*int32, bool)`

GetNSubfoldersDeletedOk returns a tuple with the NSubfoldersDeleted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNSubfoldersDeleted

`func (o *FolderDeleteOut) SetNSubfoldersDeleted(v int32)`

SetNSubfoldersDeleted sets NSubfoldersDeleted field to given value.


### GetOk

`func (o *FolderDeleteOut) GetOk() bool`

GetOk returns the Ok field if non-nil, zero value otherwise.

### GetOkOk

`func (o *FolderDeleteOut) GetOkOk() (*bool, bool)`

GetOkOk returns a tuple with the Ok field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOk

`func (o *FolderDeleteOut) SetOk(v bool)`

SetOk sets Ok field to given value.

### HasOk

`func (o *FolderDeleteOut) HasOk() bool`

HasOk returns a boolean if a field has been set.

### GetPath

`func (o *FolderDeleteOut) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *FolderDeleteOut) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *FolderDeleteOut) SetPath(v string)`

SetPath sets Path field to given value.


### GetPurgeAt

`func (o *FolderDeleteOut) GetPurgeAt() time.Time`

GetPurgeAt returns the PurgeAt field if non-nil, zero value otherwise.

### GetPurgeAtOk

`func (o *FolderDeleteOut) GetPurgeAtOk() (*time.Time, bool)`

GetPurgeAtOk returns a tuple with the PurgeAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurgeAt

`func (o *FolderDeleteOut) SetPurgeAt(v time.Time)`

SetPurgeAt sets PurgeAt field to given value.


### GetRetentionDays

`func (o *FolderDeleteOut) GetRetentionDays() int32`

GetRetentionDays returns the RetentionDays field if non-nil, zero value otherwise.

### GetRetentionDaysOk

`func (o *FolderDeleteOut) GetRetentionDaysOk() (*int32, bool)`

GetRetentionDaysOk returns a tuple with the RetentionDays field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRetentionDays

`func (o *FolderDeleteOut) SetRetentionDays(v int32)`

SetRetentionDays sets RetentionDays field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
