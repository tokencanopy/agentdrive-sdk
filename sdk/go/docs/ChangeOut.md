# ChangeOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**ChangeSetId** | **string** |  | 
**Type** | **string** |  | 
**DriveId** | **string** |  | 
**Actor** | [**ChangeActorOut**](ChangeActorOut.md) |  | 
**Resource** | [**ChangeResourceOut**](ChangeResourceOut.md) |  | 
**PreviousRevision** | **NullableString** |  | 
**Revision** | **NullableString** |  | 
**OccurredAt** | **time.Time** |  | 
**Data** | **map[string]interface{}** |  | 

## Methods

### NewChangeOut

`func NewChangeOut(id string, changeSetId string, type_ string, driveId string, actor ChangeActorOut, resource ChangeResourceOut, previousRevision NullableString, revision NullableString, occurredAt time.Time, data map[string]interface{}, ) *ChangeOut`

NewChangeOut instantiates a new ChangeOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewChangeOutWithDefaults

`func NewChangeOutWithDefaults() *ChangeOut`

NewChangeOutWithDefaults instantiates a new ChangeOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ChangeOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ChangeOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ChangeOut) SetId(v string)`

SetId sets Id field to given value.


### GetChangeSetId

`func (o *ChangeOut) GetChangeSetId() string`

GetChangeSetId returns the ChangeSetId field if non-nil, zero value otherwise.

### GetChangeSetIdOk

`func (o *ChangeOut) GetChangeSetIdOk() (*string, bool)`

GetChangeSetIdOk returns a tuple with the ChangeSetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangeSetId

`func (o *ChangeOut) SetChangeSetId(v string)`

SetChangeSetId sets ChangeSetId field to given value.


### GetType

`func (o *ChangeOut) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ChangeOut) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ChangeOut) SetType(v string)`

SetType sets Type field to given value.


### GetDriveId

`func (o *ChangeOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *ChangeOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *ChangeOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetActor

`func (o *ChangeOut) GetActor() ChangeActorOut`

GetActor returns the Actor field if non-nil, zero value otherwise.

### GetActorOk

`func (o *ChangeOut) GetActorOk() (*ChangeActorOut, bool)`

GetActorOk returns a tuple with the Actor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActor

`func (o *ChangeOut) SetActor(v ChangeActorOut)`

SetActor sets Actor field to given value.


### GetResource

`func (o *ChangeOut) GetResource() ChangeResourceOut`

GetResource returns the Resource field if non-nil, zero value otherwise.

### GetResourceOk

`func (o *ChangeOut) GetResourceOk() (*ChangeResourceOut, bool)`

GetResourceOk returns a tuple with the Resource field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResource

`func (o *ChangeOut) SetResource(v ChangeResourceOut)`

SetResource sets Resource field to given value.


### GetPreviousRevision

`func (o *ChangeOut) GetPreviousRevision() string`

GetPreviousRevision returns the PreviousRevision field if non-nil, zero value otherwise.

### GetPreviousRevisionOk

`func (o *ChangeOut) GetPreviousRevisionOk() (*string, bool)`

GetPreviousRevisionOk returns a tuple with the PreviousRevision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPreviousRevision

`func (o *ChangeOut) SetPreviousRevision(v string)`

SetPreviousRevision sets PreviousRevision field to given value.


### SetPreviousRevisionNil

`func (o *ChangeOut) SetPreviousRevisionNil(b bool)`

 SetPreviousRevisionNil sets the value for PreviousRevision to be an explicit nil

### UnsetPreviousRevision
`func (o *ChangeOut) UnsetPreviousRevision()`

UnsetPreviousRevision ensures that no value is present for PreviousRevision, not even an explicit nil
### GetRevision

`func (o *ChangeOut) GetRevision() string`

GetRevision returns the Revision field if non-nil, zero value otherwise.

### GetRevisionOk

`func (o *ChangeOut) GetRevisionOk() (*string, bool)`

GetRevisionOk returns a tuple with the Revision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevision

`func (o *ChangeOut) SetRevision(v string)`

SetRevision sets Revision field to given value.


### SetRevisionNil

`func (o *ChangeOut) SetRevisionNil(b bool)`

 SetRevisionNil sets the value for Revision to be an explicit nil

### UnsetRevision
`func (o *ChangeOut) UnsetRevision()`

UnsetRevision ensures that no value is present for Revision, not even an explicit nil
### GetOccurredAt

`func (o *ChangeOut) GetOccurredAt() time.Time`

GetOccurredAt returns the OccurredAt field if non-nil, zero value otherwise.

### GetOccurredAtOk

`func (o *ChangeOut) GetOccurredAtOk() (*time.Time, bool)`

GetOccurredAtOk returns a tuple with the OccurredAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOccurredAt

`func (o *ChangeOut) SetOccurredAt(v time.Time)`

SetOccurredAt sets OccurredAt field to given value.


### GetData

`func (o *ChangeOut) GetData() map[string]interface{}`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *ChangeOut) GetDataOk() (*map[string]interface{}, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *ChangeOut) SetData(v map[string]interface{})`

SetData sets Data field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


