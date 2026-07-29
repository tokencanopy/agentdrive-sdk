# EventOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Action** | **string** |  |
**ActorName** | Pointer to **NullableString** |  | [optional]
**ArtId** | Pointer to **NullableString** |  | [optional]
**CreatedAt** | **time.Time** |  |
**DriveId** | **string** |  |
**Id** | **string** |  |
**Metadata** | Pointer to **map[string]interface{}** |  | [optional]

## Methods

### NewEventOut

`func NewEventOut(action string, createdAt time.Time, driveId string, id string, ) *EventOut`

NewEventOut instantiates a new EventOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEventOutWithDefaults

`func NewEventOutWithDefaults() *EventOut`

NewEventOutWithDefaults instantiates a new EventOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAction

`func (o *EventOut) GetAction() string`

GetAction returns the Action field if non-nil, zero value otherwise.

### GetActionOk

`func (o *EventOut) GetActionOk() (*string, bool)`

GetActionOk returns a tuple with the Action field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAction

`func (o *EventOut) SetAction(v string)`

SetAction sets Action field to given value.


### GetActorName

`func (o *EventOut) GetActorName() string`

GetActorName returns the ActorName field if non-nil, zero value otherwise.

### GetActorNameOk

`func (o *EventOut) GetActorNameOk() (*string, bool)`

GetActorNameOk returns a tuple with the ActorName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActorName

`func (o *EventOut) SetActorName(v string)`

SetActorName sets ActorName field to given value.

### HasActorName

`func (o *EventOut) HasActorName() bool`

HasActorName returns a boolean if a field has been set.

### SetActorNameNil

`func (o *EventOut) SetActorNameNil(b bool)`

 SetActorNameNil sets the value for ActorName to be an explicit nil

### UnsetActorName
`func (o *EventOut) UnsetActorName()`

UnsetActorName ensures that no value is present for ActorName, not even an explicit nil
### GetArtId

`func (o *EventOut) GetArtId() string`

GetArtId returns the ArtId field if non-nil, zero value otherwise.

### GetArtIdOk

`func (o *EventOut) GetArtIdOk() (*string, bool)`

GetArtIdOk returns a tuple with the ArtId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtId

`func (o *EventOut) SetArtId(v string)`

SetArtId sets ArtId field to given value.

### HasArtId

`func (o *EventOut) HasArtId() bool`

HasArtId returns a boolean if a field has been set.

### SetArtIdNil

`func (o *EventOut) SetArtIdNil(b bool)`

 SetArtIdNil sets the value for ArtId to be an explicit nil

### UnsetArtId
`func (o *EventOut) UnsetArtId()`

UnsetArtId ensures that no value is present for ArtId, not even an explicit nil
### GetCreatedAt

`func (o *EventOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *EventOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *EventOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetDriveId

`func (o *EventOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *EventOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *EventOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetId

`func (o *EventOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *EventOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *EventOut) SetId(v string)`

SetId sets Id field to given value.


### GetMetadata

`func (o *EventOut) GetMetadata() map[string]interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *EventOut) GetMetadataOk() (*map[string]interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *EventOut) SetMetadata(v map[string]interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *EventOut) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
