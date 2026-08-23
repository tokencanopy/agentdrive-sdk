# EntryListOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Entries** | [**[]EntriesInner**](EntriesInner.md) |  |
**NextCursor** | **NullableString** |  |

## Methods

### NewEntryListOut

`func NewEntryListOut(entries []EntriesInner, nextCursor NullableString, ) *EntryListOut`

NewEntryListOut instantiates a new EntryListOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEntryListOutWithDefaults

`func NewEntryListOutWithDefaults() *EntryListOut`

NewEntryListOutWithDefaults instantiates a new EntryListOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEntries

`func (o *EntryListOut) GetEntries() []EntriesInner`

GetEntries returns the Entries field if non-nil, zero value otherwise.

### GetEntriesOk

`func (o *EntryListOut) GetEntriesOk() (*[]EntriesInner, bool)`

GetEntriesOk returns a tuple with the Entries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntries

`func (o *EntryListOut) SetEntries(v []EntriesInner)`

SetEntries sets Entries field to given value.


### GetNextCursor

`func (o *EntryListOut) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *EntryListOut) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *EntryListOut) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.


### SetNextCursorNil

`func (o *EntryListOut) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *EntryListOut) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
