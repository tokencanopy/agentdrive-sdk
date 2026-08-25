# ChangePageOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]ChangeOut**](ChangeOut.md) |  | 
**NextCursor** | **string** |  | 
**HasMore** | **bool** |  | 

## Methods

### NewChangePageOut

`func NewChangePageOut(items []ChangeOut, nextCursor string, hasMore bool, ) *ChangePageOut`

NewChangePageOut instantiates a new ChangePageOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewChangePageOutWithDefaults

`func NewChangePageOutWithDefaults() *ChangePageOut`

NewChangePageOutWithDefaults instantiates a new ChangePageOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ChangePageOut) GetItems() []ChangeOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ChangePageOut) GetItemsOk() (*[]ChangeOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ChangePageOut) SetItems(v []ChangeOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *ChangePageOut) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *ChangePageOut) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *ChangePageOut) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.


### GetHasMore

`func (o *ChangePageOut) GetHasMore() bool`

GetHasMore returns the HasMore field if non-nil, zero value otherwise.

### GetHasMoreOk

`func (o *ChangePageOut) GetHasMoreOk() (*bool, bool)`

GetHasMoreOk returns a tuple with the HasMore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasMore

`func (o *ChangePageOut) SetHasMore(v bool)`

SetHasMore sets HasMore field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


