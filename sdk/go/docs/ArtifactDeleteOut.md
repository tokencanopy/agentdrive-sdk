# ArtifactDeleteOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ok** | Pointer to **bool** |  | [optional] [default to true]
**Id** | **string** |  | 
**Path** | **string** |  | 
**DeletedAt** | **time.Time** |  | 
**PurgeAt** | **time.Time** |  | 
**RestoreUrl** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewArtifactDeleteOut

`func NewArtifactDeleteOut(id string, path string, deletedAt time.Time, purgeAt time.Time, ) *ArtifactDeleteOut`

NewArtifactDeleteOut instantiates a new ArtifactDeleteOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactDeleteOutWithDefaults

`func NewArtifactDeleteOutWithDefaults() *ArtifactDeleteOut`

NewArtifactDeleteOutWithDefaults instantiates a new ArtifactDeleteOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOk

`func (o *ArtifactDeleteOut) GetOk() bool`

GetOk returns the Ok field if non-nil, zero value otherwise.

### GetOkOk

`func (o *ArtifactDeleteOut) GetOkOk() (*bool, bool)`

GetOkOk returns a tuple with the Ok field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOk

`func (o *ArtifactDeleteOut) SetOk(v bool)`

SetOk sets Ok field to given value.

### HasOk

`func (o *ArtifactDeleteOut) HasOk() bool`

HasOk returns a boolean if a field has been set.

### GetId

`func (o *ArtifactDeleteOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ArtifactDeleteOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ArtifactDeleteOut) SetId(v string)`

SetId sets Id field to given value.


### GetPath

`func (o *ArtifactDeleteOut) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *ArtifactDeleteOut) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *ArtifactDeleteOut) SetPath(v string)`

SetPath sets Path field to given value.


### GetDeletedAt

`func (o *ArtifactDeleteOut) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *ArtifactDeleteOut) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *ArtifactDeleteOut) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.


### GetPurgeAt

`func (o *ArtifactDeleteOut) GetPurgeAt() time.Time`

GetPurgeAt returns the PurgeAt field if non-nil, zero value otherwise.

### GetPurgeAtOk

`func (o *ArtifactDeleteOut) GetPurgeAtOk() (*time.Time, bool)`

GetPurgeAtOk returns a tuple with the PurgeAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurgeAt

`func (o *ArtifactDeleteOut) SetPurgeAt(v time.Time)`

SetPurgeAt sets PurgeAt field to given value.


### GetRestoreUrl

`func (o *ArtifactDeleteOut) GetRestoreUrl() string`

GetRestoreUrl returns the RestoreUrl field if non-nil, zero value otherwise.

### GetRestoreUrlOk

`func (o *ArtifactDeleteOut) GetRestoreUrlOk() (*string, bool)`

GetRestoreUrlOk returns a tuple with the RestoreUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestoreUrl

`func (o *ArtifactDeleteOut) SetRestoreUrl(v string)`

SetRestoreUrl sets RestoreUrl field to given value.

### HasRestoreUrl

`func (o *ArtifactDeleteOut) HasRestoreUrl() bool`

HasRestoreUrl returns a boolean if a field has been set.

### SetRestoreUrlNil

`func (o *ArtifactDeleteOut) SetRestoreUrlNil(b bool)`

 SetRestoreUrlNil sets the value for RestoreUrl to be an explicit nil

### UnsetRestoreUrl
`func (o *ArtifactDeleteOut) UnsetRestoreUrl()`

UnsetRestoreUrl ensures that no value is present for RestoreUrl, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


