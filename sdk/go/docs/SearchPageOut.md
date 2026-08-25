# SearchPageOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]SearchHitOut**](SearchHitOut.md) |  | 
**NextCursor** | **NullableString** |  | 

## Methods

### NewSearchPageOut

`func NewSearchPageOut(items []SearchHitOut, nextCursor NullableString, ) *SearchPageOut`

NewSearchPageOut instantiates a new SearchPageOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSearchPageOutWithDefaults

`func NewSearchPageOutWithDefaults() *SearchPageOut`

NewSearchPageOutWithDefaults instantiates a new SearchPageOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *SearchPageOut) GetItems() []SearchHitOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *SearchPageOut) GetItemsOk() (*[]SearchHitOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *SearchPageOut) SetItems(v []SearchHitOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *SearchPageOut) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *SearchPageOut) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *SearchPageOut) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.


### SetNextCursorNil

`func (o *SearchPageOut) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *SearchPageOut) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


