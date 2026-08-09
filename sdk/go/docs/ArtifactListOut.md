# ArtifactListOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]ArtifactOut**](ArtifactOut.md) |  |
**NextCursor** | **NullableString** |  |

## Methods

### NewArtifactListOut

`func NewArtifactListOut(items []ArtifactOut, nextCursor NullableString, ) *ArtifactListOut`

NewArtifactListOut instantiates a new ArtifactListOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactListOutWithDefaults

`func NewArtifactListOutWithDefaults() *ArtifactListOut`

NewArtifactListOutWithDefaults instantiates a new ArtifactListOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ArtifactListOut) GetItems() []ArtifactOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ArtifactListOut) GetItemsOk() (*[]ArtifactOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ArtifactListOut) SetItems(v []ArtifactOut)`

SetItems sets Items field to given value.


### GetNextCursor

`func (o *ArtifactListOut) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *ArtifactListOut) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *ArtifactListOut) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.


### SetNextCursorNil

`func (o *ArtifactListOut) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *ArtifactListOut) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
