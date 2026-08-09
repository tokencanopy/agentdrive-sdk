# FolderListOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]FolderOut**](FolderOut.md) |  |
**NextCursor** | **NullableString** |  |

## Methods

### NewFolderListOut

`func NewFolderListOut(items []FolderOut, nextCursor NullableString, ) *FolderListOut`

NewFolderListOut instantiates a new FolderListOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFolderListOutWithDefaults

`func NewFolderListOutWithDefaults() *FolderListOut`

NewFolderListOutWithDefaults instantiates a new FolderListOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *FolderListOut) GetItems() []FolderOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *FolderListOut) GetItemsOk() (*[]FolderOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *FolderListOut) SetItems(v []FolderOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *FolderListOut) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *FolderListOut) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *FolderListOut) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.


### SetNextCursorNil

`func (o *FolderListOut) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *FolderListOut) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
