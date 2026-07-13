# WorkspaceList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]WorkspaceOut**](WorkspaceOut.md) |  | 
**NextCursor** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewWorkspaceList

`func NewWorkspaceList(items []WorkspaceOut, ) *WorkspaceList`

NewWorkspaceList instantiates a new WorkspaceList object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWorkspaceListWithDefaults

`func NewWorkspaceListWithDefaults() *WorkspaceList`

NewWorkspaceListWithDefaults instantiates a new WorkspaceList object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *WorkspaceList) GetItems() []WorkspaceOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *WorkspaceList) GetItemsOk() (*[]WorkspaceOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *WorkspaceList) SetItems(v []WorkspaceOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *WorkspaceList) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *WorkspaceList) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *WorkspaceList) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.

### HasNextCursor

`func (o *WorkspaceList) HasNextCursor() bool`

HasNextCursor returns a boolean if a field has been set.

### SetNextCursorNil

`func (o *WorkspaceList) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *WorkspaceList) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


