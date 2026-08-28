# SessionCreateIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LeaseSeconds** | Pointer to **NullableInt32** |  | [optional]

## Methods

### NewSessionCreateIn

`func NewSessionCreateIn() *SessionCreateIn`

NewSessionCreateIn instantiates a new SessionCreateIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSessionCreateInWithDefaults

`func NewSessionCreateInWithDefaults() *SessionCreateIn`

NewSessionCreateInWithDefaults instantiates a new SessionCreateIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLeaseSeconds

`func (o *SessionCreateIn) GetLeaseSeconds() int32`

GetLeaseSeconds returns the LeaseSeconds field if non-nil, zero value otherwise.

### GetLeaseSecondsOk

`func (o *SessionCreateIn) GetLeaseSecondsOk() (*int32, bool)`

GetLeaseSecondsOk returns a tuple with the LeaseSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeaseSeconds

`func (o *SessionCreateIn) SetLeaseSeconds(v int32)`

SetLeaseSeconds sets LeaseSeconds field to given value.

### HasLeaseSeconds

`func (o *SessionCreateIn) HasLeaseSeconds() bool`

HasLeaseSeconds returns a boolean if a field has been set.

### SetLeaseSecondsNil

`func (o *SessionCreateIn) SetLeaseSecondsNil(b bool)`

 SetLeaseSecondsNil sets the value for LeaseSeconds to be an explicit nil

### UnsetLeaseSeconds
`func (o *SessionCreateIn) UnsetLeaseSeconds()`

UnsetLeaseSeconds ensures that no value is present for LeaseSeconds, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
