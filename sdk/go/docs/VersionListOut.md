# VersionListOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]VersionOut**](VersionOut.md) |  |
**NextCursor** | **NullableString** |  |

## Methods

### NewVersionListOut

`func NewVersionListOut(items []VersionOut, nextCursor NullableString, ) *VersionListOut`

NewVersionListOut instantiates a new VersionListOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewVersionListOutWithDefaults

`func NewVersionListOutWithDefaults() *VersionListOut`

NewVersionListOutWithDefaults instantiates a new VersionListOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *VersionListOut) GetItems() []VersionOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *VersionListOut) GetItemsOk() (*[]VersionOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *VersionListOut) SetItems(v []VersionOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *VersionListOut) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *VersionListOut) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *VersionListOut) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.


### SetNextCursorNil

`func (o *VersionListOut) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *VersionListOut) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
