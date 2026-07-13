# ShareList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]ShareOut**](ShareOut.md) |  | 
**NextCursor** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewShareList

`func NewShareList(items []ShareOut, ) *ShareList`

NewShareList instantiates a new ShareList object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewShareListWithDefaults

`func NewShareListWithDefaults() *ShareList`

NewShareListWithDefaults instantiates a new ShareList object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ShareList) GetItems() []ShareOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ShareList) GetItemsOk() (*[]ShareOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ShareList) SetItems(v []ShareOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *ShareList) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *ShareList) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *ShareList) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.

### HasNextCursor

`func (o *ShareList) HasNextCursor() bool`

HasNextCursor returns a boolean if a field has been set.

### SetNextCursorNil

`func (o *ShareList) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *ShareList) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


