# DriveDeleteOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ok** | Pointer to **bool** |  | [optional] [default to true]
**Id** | **string** |  | 
**DeletedAt** | **time.Time** |  | 
**PurgeAt** | **time.Time** |  | 
**RestoreUrl** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewDriveDeleteOut

`func NewDriveDeleteOut(id string, deletedAt time.Time, purgeAt time.Time, ) *DriveDeleteOut`

NewDriveDeleteOut instantiates a new DriveDeleteOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDriveDeleteOutWithDefaults

`func NewDriveDeleteOutWithDefaults() *DriveDeleteOut`

NewDriveDeleteOutWithDefaults instantiates a new DriveDeleteOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOk

`func (o *DriveDeleteOut) GetOk() bool`

GetOk returns the Ok field if non-nil, zero value otherwise.

### GetOkOk

`func (o *DriveDeleteOut) GetOkOk() (*bool, bool)`

GetOkOk returns a tuple with the Ok field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOk

`func (o *DriveDeleteOut) SetOk(v bool)`

SetOk sets Ok field to given value.

### HasOk

`func (o *DriveDeleteOut) HasOk() bool`

HasOk returns a boolean if a field has been set.

### GetId

`func (o *DriveDeleteOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DriveDeleteOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DriveDeleteOut) SetId(v string)`

SetId sets Id field to given value.


### GetDeletedAt

`func (o *DriveDeleteOut) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *DriveDeleteOut) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *DriveDeleteOut) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.


### GetPurgeAt

`func (o *DriveDeleteOut) GetPurgeAt() time.Time`

GetPurgeAt returns the PurgeAt field if non-nil, zero value otherwise.

### GetPurgeAtOk

`func (o *DriveDeleteOut) GetPurgeAtOk() (*time.Time, bool)`

GetPurgeAtOk returns a tuple with the PurgeAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurgeAt

`func (o *DriveDeleteOut) SetPurgeAt(v time.Time)`

SetPurgeAt sets PurgeAt field to given value.


### GetRestoreUrl

`func (o *DriveDeleteOut) GetRestoreUrl() string`

GetRestoreUrl returns the RestoreUrl field if non-nil, zero value otherwise.

### GetRestoreUrlOk

`func (o *DriveDeleteOut) GetRestoreUrlOk() (*string, bool)`

GetRestoreUrlOk returns a tuple with the RestoreUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestoreUrl

`func (o *DriveDeleteOut) SetRestoreUrl(v string)`

SetRestoreUrl sets RestoreUrl field to given value.

### HasRestoreUrl

`func (o *DriveDeleteOut) HasRestoreUrl() bool`

HasRestoreUrl returns a boolean if a field has been set.

### SetRestoreUrlNil

`func (o *DriveDeleteOut) SetRestoreUrlNil(b bool)`

 SetRestoreUrlNil sets the value for RestoreUrl to be an explicit nil

### UnsetRestoreUrl
`func (o *DriveDeleteOut) UnsetRestoreUrl()`

UnsetRestoreUrl ensures that no value is present for RestoreUrl, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


