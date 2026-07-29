# InvitationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]InvitationOut**](InvitationOut.md) |  |
**NextCursor** | Pointer to **NullableString** |  | [optional]

## Methods

### NewInvitationList

`func NewInvitationList(items []InvitationOut, ) *InvitationList`

NewInvitationList instantiates a new InvitationList object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInvitationListWithDefaults

`func NewInvitationListWithDefaults() *InvitationList`

NewInvitationListWithDefaults instantiates a new InvitationList object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *InvitationList) GetItems() []InvitationOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *InvitationList) GetItemsOk() (*[]InvitationOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *InvitationList) SetItems(v []InvitationOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *InvitationList) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *InvitationList) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *InvitationList) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.

### HasNextCursor

`func (o *InvitationList) HasNextCursor() bool`

HasNextCursor returns a boolean if a field has been set.

### SetNextCursorNil

`func (o *InvitationList) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *InvitationList) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
