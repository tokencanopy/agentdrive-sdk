# TrashOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Artifacts** | [**[]TrashArtifactOut**](TrashArtifactOut.md) | Deprecated alias of items. |
**Drive** | [**TrashDriveOut**](TrashDriveOut.md) |  |
**Items** | [**[]TrashArtifactOut**](TrashArtifactOut.md) |  |
**NextCursor** | Pointer to **NullableString** |  | [optional]

## Methods

### NewTrashOut

`func NewTrashOut(artifacts []TrashArtifactOut, drive TrashDriveOut, items []TrashArtifactOut, ) *TrashOut`

NewTrashOut instantiates a new TrashOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTrashOutWithDefaults

`func NewTrashOutWithDefaults() *TrashOut`

NewTrashOutWithDefaults instantiates a new TrashOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetArtifacts

`func (o *TrashOut) GetArtifacts() []TrashArtifactOut`

GetArtifacts returns the Artifacts field if non-nil, zero value otherwise.

### GetArtifactsOk

`func (o *TrashOut) GetArtifactsOk() (*[]TrashArtifactOut, bool)`

GetArtifactsOk returns a tuple with the Artifacts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtifacts

`func (o *TrashOut) SetArtifacts(v []TrashArtifactOut)`

SetArtifacts sets Artifacts field to given value.


### GetDrive

`func (o *TrashOut) GetDrive() TrashDriveOut`

GetDrive returns the Drive field if non-nil, zero value otherwise.

### GetDriveOk

`func (o *TrashOut) GetDriveOk() (*TrashDriveOut, bool)`

GetDriveOk returns a tuple with the Drive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDrive

`func (o *TrashOut) SetDrive(v TrashDriveOut)`

SetDrive sets Drive field to given value.


### GetItems

`func (o *TrashOut) GetItems() []TrashArtifactOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *TrashOut) GetItemsOk() (*[]TrashArtifactOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *TrashOut) SetItems(v []TrashArtifactOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *TrashOut) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *TrashOut) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *TrashOut) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.

### HasNextCursor

`func (o *TrashOut) HasNextCursor() bool`

HasNextCursor returns a boolean if a field has been set.

### SetNextCursorNil

`func (o *TrashOut) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *TrashOut) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
