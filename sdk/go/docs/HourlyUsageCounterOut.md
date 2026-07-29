# HourlyUsageCounterOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Limit** | **int32** |  |
**ResetAt** | **time.Time** |  |
**Used** | **int32** |  |

## Methods

### NewHourlyUsageCounterOut

`func NewHourlyUsageCounterOut(limit int32, resetAt time.Time, used int32, ) *HourlyUsageCounterOut`

NewHourlyUsageCounterOut instantiates a new HourlyUsageCounterOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHourlyUsageCounterOutWithDefaults

`func NewHourlyUsageCounterOutWithDefaults() *HourlyUsageCounterOut`

NewHourlyUsageCounterOutWithDefaults instantiates a new HourlyUsageCounterOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLimit

`func (o *HourlyUsageCounterOut) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *HourlyUsageCounterOut) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *HourlyUsageCounterOut) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetResetAt

`func (o *HourlyUsageCounterOut) GetResetAt() time.Time`

GetResetAt returns the ResetAt field if non-nil, zero value otherwise.

### GetResetAtOk

`func (o *HourlyUsageCounterOut) GetResetAtOk() (*time.Time, bool)`

GetResetAtOk returns a tuple with the ResetAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResetAt

`func (o *HourlyUsageCounterOut) SetResetAt(v time.Time)`

SetResetAt sets ResetAt field to given value.


### GetUsed

`func (o *HourlyUsageCounterOut) GetUsed() int32`

GetUsed returns the Used field if non-nil, zero value otherwise.

### GetUsedOk

`func (o *HourlyUsageCounterOut) GetUsedOk() (*int32, bool)`

GetUsedOk returns a tuple with the Used field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsed

`func (o *HourlyUsageCounterOut) SetUsed(v int32)`

SetUsed sets Used field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
