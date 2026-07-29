# DriveApiKeyListOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]DriveApiKeyOut**](DriveApiKeyOut.md) |  |
**Keys** | [**[]DriveApiKeyOut**](DriveApiKeyOut.md) |  |
**NextCursor** | Pointer to **NullableString** |  | [optional]

## Methods

### NewDriveApiKeyListOut

`func NewDriveApiKeyListOut(items []DriveApiKeyOut, keys []DriveApiKeyOut, ) *DriveApiKeyListOut`

NewDriveApiKeyListOut instantiates a new DriveApiKeyListOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDriveApiKeyListOutWithDefaults

`func NewDriveApiKeyListOutWithDefaults() *DriveApiKeyListOut`

NewDriveApiKeyListOutWithDefaults instantiates a new DriveApiKeyListOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *DriveApiKeyListOut) GetItems() []DriveApiKeyOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *DriveApiKeyListOut) GetItemsOk() (*[]DriveApiKeyOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *DriveApiKeyListOut) SetItems(v []DriveApiKeyOut)`

SetItems sets Items field to given value.


### GetKeys

`func (o *DriveApiKeyListOut) GetKeys() []DriveApiKeyOut`

GetKeys returns the Keys field if non-nil, zero value otherwise.

### GetKeysOk

`func (o *DriveApiKeyListOut) GetKeysOk() (*[]DriveApiKeyOut, bool)`

GetKeysOk returns a tuple with the Keys field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKeys

`func (o *DriveApiKeyListOut) SetKeys(v []DriveApiKeyOut)`

SetKeys sets Keys field to given value.


### GetNextCursor

`func (o *DriveApiKeyListOut) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *DriveApiKeyListOut) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *DriveApiKeyListOut) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.

### HasNextCursor

`func (o *DriveApiKeyListOut) HasNextCursor() bool`

HasNextCursor returns a boolean if a field has been set.

### SetNextCursorNil

`func (o *DriveApiKeyListOut) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *DriveApiKeyListOut) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
