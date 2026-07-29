# DriveRestoreOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  |
**RebasedArtifactCount** | **int32** |  |
**RestoredAt** | **time.Time** |  |

## Methods

### NewDriveRestoreOut

`func NewDriveRestoreOut(id string, rebasedArtifactCount int32, restoredAt time.Time, ) *DriveRestoreOut`

NewDriveRestoreOut instantiates a new DriveRestoreOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDriveRestoreOutWithDefaults

`func NewDriveRestoreOutWithDefaults() *DriveRestoreOut`

NewDriveRestoreOutWithDefaults instantiates a new DriveRestoreOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *DriveRestoreOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DriveRestoreOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DriveRestoreOut) SetId(v string)`

SetId sets Id field to given value.


### GetRebasedArtifactCount

`func (o *DriveRestoreOut) GetRebasedArtifactCount() int32`

GetRebasedArtifactCount returns the RebasedArtifactCount field if non-nil, zero value otherwise.

### GetRebasedArtifactCountOk

`func (o *DriveRestoreOut) GetRebasedArtifactCountOk() (*int32, bool)`

GetRebasedArtifactCountOk returns a tuple with the RebasedArtifactCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRebasedArtifactCount

`func (o *DriveRestoreOut) SetRebasedArtifactCount(v int32)`

SetRebasedArtifactCount sets RebasedArtifactCount field to given value.


### GetRestoredAt

`func (o *DriveRestoreOut) GetRestoredAt() time.Time`

GetRestoredAt returns the RestoredAt field if non-nil, zero value otherwise.

### GetRestoredAtOk

`func (o *DriveRestoreOut) GetRestoredAtOk() (*time.Time, bool)`

GetRestoredAtOk returns a tuple with the RestoredAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestoredAt

`func (o *DriveRestoreOut) SetRestoredAt(v time.Time)`

SetRestoredAt sets RestoredAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
