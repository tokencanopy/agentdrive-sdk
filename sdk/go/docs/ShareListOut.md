# ShareListOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]ShareOut**](ShareOut.md) |  |
**NextCursor** | **NullableString** |  |

## Methods

### NewShareListOut

`func NewShareListOut(items []ShareOut, nextCursor NullableString, ) *ShareListOut`

NewShareListOut instantiates a new ShareListOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewShareListOutWithDefaults

`func NewShareListOutWithDefaults() *ShareListOut`

NewShareListOutWithDefaults instantiates a new ShareListOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ShareListOut) GetItems() []ShareOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ShareListOut) GetItemsOk() (*[]ShareOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ShareListOut) SetItems(v []ShareOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *ShareListOut) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *ShareListOut) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *ShareListOut) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.


### SetNextCursorNil

`func (o *ShareListOut) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *ShareListOut) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
