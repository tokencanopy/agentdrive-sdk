# DriveListOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]DriveOut**](DriveOut.md) |  |
**NextCursor** | **NullableString** |  |

## Methods

### NewDriveListOut

`func NewDriveListOut(items []DriveOut, nextCursor NullableString, ) *DriveListOut`

NewDriveListOut instantiates a new DriveListOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDriveListOutWithDefaults

`func NewDriveListOutWithDefaults() *DriveListOut`

NewDriveListOutWithDefaults instantiates a new DriveListOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *DriveListOut) GetItems() []DriveOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *DriveListOut) GetItemsOk() (*[]DriveOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *DriveListOut) SetItems(v []DriveOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *DriveListOut) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *DriveListOut) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *DriveListOut) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.


### SetNextCursorNil

`func (o *DriveListOut) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *DriveListOut) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
