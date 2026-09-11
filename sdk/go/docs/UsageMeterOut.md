# UsageMeterOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Limit** | **int32** |  |
**Remaining** | **int32** |  |
**Reserved** | **int32** |  |
**ResetAt** | **NullableTime** |  |
**Scope** | **string** |  |
**Used** | **int32** |  |

## Methods

### NewUsageMeterOut

`func NewUsageMeterOut(limit int32, remaining int32, reserved int32, resetAt NullableTime, scope string, used int32, ) *UsageMeterOut`

NewUsageMeterOut instantiates a new UsageMeterOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUsageMeterOutWithDefaults

`func NewUsageMeterOutWithDefaults() *UsageMeterOut`

NewUsageMeterOutWithDefaults instantiates a new UsageMeterOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLimit

`func (o *UsageMeterOut) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *UsageMeterOut) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *UsageMeterOut) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetRemaining

`func (o *UsageMeterOut) GetRemaining() int32`

GetRemaining returns the Remaining field if non-nil, zero value otherwise.

### GetRemainingOk

`func (o *UsageMeterOut) GetRemainingOk() (*int32, bool)`

GetRemainingOk returns a tuple with the Remaining field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemaining

`func (o *UsageMeterOut) SetRemaining(v int32)`

SetRemaining sets Remaining field to given value.


### GetReserved

`func (o *UsageMeterOut) GetReserved() int32`

GetReserved returns the Reserved field if non-nil, zero value otherwise.

### GetReservedOk

`func (o *UsageMeterOut) GetReservedOk() (*int32, bool)`

GetReservedOk returns a tuple with the Reserved field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReserved

`func (o *UsageMeterOut) SetReserved(v int32)`

SetReserved sets Reserved field to given value.


### GetResetAt

`func (o *UsageMeterOut) GetResetAt() time.Time`

GetResetAt returns the ResetAt field if non-nil, zero value otherwise.

### GetResetAtOk

`func (o *UsageMeterOut) GetResetAtOk() (*time.Time, bool)`

GetResetAtOk returns a tuple with the ResetAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResetAt

`func (o *UsageMeterOut) SetResetAt(v time.Time)`

SetResetAt sets ResetAt field to given value.


### SetResetAtNil

`func (o *UsageMeterOut) SetResetAtNil(b bool)`

 SetResetAtNil sets the value for ResetAt to be an explicit nil

### UnsetResetAt
`func (o *UsageMeterOut) UnsetResetAt()`

UnsetResetAt ensures that no value is present for ResetAt, not even an explicit nil
### GetScope

`func (o *UsageMeterOut) GetScope() string`

GetScope returns the Scope field if non-nil, zero value otherwise.

### GetScopeOk

`func (o *UsageMeterOut) GetScopeOk() (*string, bool)`

GetScopeOk returns a tuple with the Scope field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScope

`func (o *UsageMeterOut) SetScope(v string)`

SetScope sets Scope field to given value.


### GetUsed

`func (o *UsageMeterOut) GetUsed() int32`

GetUsed returns the Used field if non-nil, zero value otherwise.

### GetUsedOk

`func (o *UsageMeterOut) GetUsedOk() (*int32, bool)`

GetUsedOk returns a tuple with the Used field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsed

`func (o *UsageMeterOut) SetUsed(v int32)`

SetUsed sets Used field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
