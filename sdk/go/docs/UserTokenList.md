# UserTokenList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]UserTokenOut**](UserTokenOut.md) |  |
**NextCursor** | Pointer to **NullableString** |  | [optional]

## Methods

### NewUserTokenList

`func NewUserTokenList(items []UserTokenOut, ) *UserTokenList`

NewUserTokenList instantiates a new UserTokenList object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserTokenListWithDefaults

`func NewUserTokenListWithDefaults() *UserTokenList`

NewUserTokenListWithDefaults instantiates a new UserTokenList object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *UserTokenList) GetItems() []UserTokenOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *UserTokenList) GetItemsOk() (*[]UserTokenOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *UserTokenList) SetItems(v []UserTokenOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *UserTokenList) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *UserTokenList) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *UserTokenList) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.

### HasNextCursor

`func (o *UserTokenList) HasNextCursor() bool`

HasNextCursor returns a boolean if a field has been set.

### SetNextCursorNil

`func (o *UserTokenList) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *UserTokenList) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
