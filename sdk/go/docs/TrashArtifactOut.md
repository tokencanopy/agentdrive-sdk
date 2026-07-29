# TrashArtifactOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DeletedAt** | Pointer to **NullableTime** |  | [optional]
**Id** | **string** |  |
**Path** | **string** |  |
**PurgeAt** | Pointer to **NullableTime** |  | [optional]
**RestoreUrl** | **string** |  |
**SizeBytes** | **int32** |  |

## Methods

### NewTrashArtifactOut

`func NewTrashArtifactOut(id string, path string, restoreUrl string, sizeBytes int32, ) *TrashArtifactOut`

NewTrashArtifactOut instantiates a new TrashArtifactOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTrashArtifactOutWithDefaults

`func NewTrashArtifactOutWithDefaults() *TrashArtifactOut`

NewTrashArtifactOutWithDefaults instantiates a new TrashArtifactOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDeletedAt

`func (o *TrashArtifactOut) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *TrashArtifactOut) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *TrashArtifactOut) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.

### HasDeletedAt

`func (o *TrashArtifactOut) HasDeletedAt() bool`

HasDeletedAt returns a boolean if a field has been set.

### SetDeletedAtNil

`func (o *TrashArtifactOut) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *TrashArtifactOut) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil
### GetId

`func (o *TrashArtifactOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TrashArtifactOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TrashArtifactOut) SetId(v string)`

SetId sets Id field to given value.


### GetPath

`func (o *TrashArtifactOut) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *TrashArtifactOut) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *TrashArtifactOut) SetPath(v string)`

SetPath sets Path field to given value.


### GetPurgeAt

`func (o *TrashArtifactOut) GetPurgeAt() time.Time`

GetPurgeAt returns the PurgeAt field if non-nil, zero value otherwise.

### GetPurgeAtOk

`func (o *TrashArtifactOut) GetPurgeAtOk() (*time.Time, bool)`

GetPurgeAtOk returns a tuple with the PurgeAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurgeAt

`func (o *TrashArtifactOut) SetPurgeAt(v time.Time)`

SetPurgeAt sets PurgeAt field to given value.

### HasPurgeAt

`func (o *TrashArtifactOut) HasPurgeAt() bool`

HasPurgeAt returns a boolean if a field has been set.

### SetPurgeAtNil

`func (o *TrashArtifactOut) SetPurgeAtNil(b bool)`

 SetPurgeAtNil sets the value for PurgeAt to be an explicit nil

### UnsetPurgeAt
`func (o *TrashArtifactOut) UnsetPurgeAt()`

UnsetPurgeAt ensures that no value is present for PurgeAt, not even an explicit nil
### GetRestoreUrl

`func (o *TrashArtifactOut) GetRestoreUrl() string`

GetRestoreUrl returns the RestoreUrl field if non-nil, zero value otherwise.

### GetRestoreUrlOk

`func (o *TrashArtifactOut) GetRestoreUrlOk() (*string, bool)`

GetRestoreUrlOk returns a tuple with the RestoreUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestoreUrl

`func (o *TrashArtifactOut) SetRestoreUrl(v string)`

SetRestoreUrl sets RestoreUrl field to given value.


### GetSizeBytes

`func (o *TrashArtifactOut) GetSizeBytes() int32`

GetSizeBytes returns the SizeBytes field if non-nil, zero value otherwise.

### GetSizeBytesOk

`func (o *TrashArtifactOut) GetSizeBytesOk() (*int32, bool)`

GetSizeBytesOk returns a tuple with the SizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSizeBytes

`func (o *TrashArtifactOut) SetSizeBytes(v int32)`

SetSizeBytes sets SizeBytes field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
