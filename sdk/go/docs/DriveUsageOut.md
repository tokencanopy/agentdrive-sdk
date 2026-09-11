# DriveUsageOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EffectiveLimits** | [**EffectiveLimitsOut**](EffectiveLimitsOut.md) |  |
**Meters** | [**UsageMetersOut**](UsageMetersOut.md) |  |
**RetrievalBytes** | **int32** |  |
**StorageBytes** | **int32** |  |

## Methods

### NewDriveUsageOut

`func NewDriveUsageOut(effectiveLimits EffectiveLimitsOut, meters UsageMetersOut, retrievalBytes int32, storageBytes int32, ) *DriveUsageOut`

NewDriveUsageOut instantiates a new DriveUsageOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDriveUsageOutWithDefaults

`func NewDriveUsageOutWithDefaults() *DriveUsageOut`

NewDriveUsageOutWithDefaults instantiates a new DriveUsageOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEffectiveLimits

`func (o *DriveUsageOut) GetEffectiveLimits() EffectiveLimitsOut`

GetEffectiveLimits returns the EffectiveLimits field if non-nil, zero value otherwise.

### GetEffectiveLimitsOk

`func (o *DriveUsageOut) GetEffectiveLimitsOk() (*EffectiveLimitsOut, bool)`

GetEffectiveLimitsOk returns a tuple with the EffectiveLimits field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEffectiveLimits

`func (o *DriveUsageOut) SetEffectiveLimits(v EffectiveLimitsOut)`

SetEffectiveLimits sets EffectiveLimits field to given value.


### GetMeters

`func (o *DriveUsageOut) GetMeters() UsageMetersOut`

GetMeters returns the Meters field if non-nil, zero value otherwise.

### GetMetersOk

`func (o *DriveUsageOut) GetMetersOk() (*UsageMetersOut, bool)`

GetMetersOk returns a tuple with the Meters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMeters

`func (o *DriveUsageOut) SetMeters(v UsageMetersOut)`

SetMeters sets Meters field to given value.


### GetRetrievalBytes

`func (o *DriveUsageOut) GetRetrievalBytes() int32`

GetRetrievalBytes returns the RetrievalBytes field if non-nil, zero value otherwise.

### GetRetrievalBytesOk

`func (o *DriveUsageOut) GetRetrievalBytesOk() (*int32, bool)`

GetRetrievalBytesOk returns a tuple with the RetrievalBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRetrievalBytes

`func (o *DriveUsageOut) SetRetrievalBytes(v int32)`

SetRetrievalBytes sets RetrievalBytes field to given value.


### GetStorageBytes

`func (o *DriveUsageOut) GetStorageBytes() int32`

GetStorageBytes returns the StorageBytes field if non-nil, zero value otherwise.

### GetStorageBytesOk

`func (o *DriveUsageOut) GetStorageBytesOk() (*int32, bool)`

GetStorageBytesOk returns a tuple with the StorageBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStorageBytes

`func (o *DriveUsageOut) SetStorageBytes(v int32)`

SetStorageBytes sets StorageBytes field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
