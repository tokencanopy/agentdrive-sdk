# GrantListOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]GrantOut**](GrantOut.md) |  | 
**NextCursor** | **NullableString** |  | 

## Methods

### NewGrantListOut

`func NewGrantListOut(items []GrantOut, nextCursor NullableString, ) *GrantListOut`

NewGrantListOut instantiates a new GrantListOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGrantListOutWithDefaults

`func NewGrantListOutWithDefaults() *GrantListOut`

NewGrantListOutWithDefaults instantiates a new GrantListOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *GrantListOut) GetItems() []GrantOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *GrantListOut) GetItemsOk() (*[]GrantOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *GrantListOut) SetItems(v []GrantOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *GrantListOut) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *GrantListOut) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *GrantListOut) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.


### SetNextCursorNil

`func (o *GrantListOut) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *GrantListOut) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


