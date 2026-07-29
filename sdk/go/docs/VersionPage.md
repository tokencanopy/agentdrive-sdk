# VersionPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]VersionOut**](VersionOut.md) |  |
**NextCursor** | Pointer to **NullableString** |  | [optional]
**PrunedBefore** | Pointer to **NullableInt32** |  | [optional]

## Methods

### NewVersionPage

`func NewVersionPage(items []VersionOut, ) *VersionPage`

NewVersionPage instantiates a new VersionPage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewVersionPageWithDefaults

`func NewVersionPageWithDefaults() *VersionPage`

NewVersionPageWithDefaults instantiates a new VersionPage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *VersionPage) GetItems() []VersionOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *VersionPage) GetItemsOk() (*[]VersionOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *VersionPage) SetItems(v []VersionOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *VersionPage) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *VersionPage) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *VersionPage) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.

### HasNextCursor

`func (o *VersionPage) HasNextCursor() bool`

HasNextCursor returns a boolean if a field has been set.

### SetNextCursorNil

`func (o *VersionPage) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *VersionPage) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil
### GetPrunedBefore

`func (o *VersionPage) GetPrunedBefore() int32`

GetPrunedBefore returns the PrunedBefore field if non-nil, zero value otherwise.

### GetPrunedBeforeOk

`func (o *VersionPage) GetPrunedBeforeOk() (*int32, bool)`

GetPrunedBeforeOk returns a tuple with the PrunedBefore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrunedBefore

`func (o *VersionPage) SetPrunedBefore(v int32)`

SetPrunedBefore sets PrunedBefore field to given value.

### HasPrunedBefore

`func (o *VersionPage) HasPrunedBefore() bool`

HasPrunedBefore returns a boolean if a field has been set.

### SetPrunedBeforeNil

`func (o *VersionPage) SetPrunedBeforeNil(b bool)`

 SetPrunedBeforeNil sets the value for PrunedBefore to be an explicit nil

### UnsetPrunedBefore
`func (o *VersionPage) UnsetPrunedBefore()`

UnsetPrunedBefore ensures that no value is present for PrunedBefore, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
