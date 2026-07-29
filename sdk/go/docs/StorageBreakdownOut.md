# StorageBreakdownOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AsOf** | **string** |  |
**LiveBytes** | **int32** |  |
**TrashBytes** | **int32** |  |
**VersionBytes** | **int32** |  |

## Methods

### NewStorageBreakdownOut

`func NewStorageBreakdownOut(asOf string, liveBytes int32, trashBytes int32, versionBytes int32, ) *StorageBreakdownOut`

NewStorageBreakdownOut instantiates a new StorageBreakdownOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStorageBreakdownOutWithDefaults

`func NewStorageBreakdownOutWithDefaults() *StorageBreakdownOut`

NewStorageBreakdownOutWithDefaults instantiates a new StorageBreakdownOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAsOf

`func (o *StorageBreakdownOut) GetAsOf() string`

GetAsOf returns the AsOf field if non-nil, zero value otherwise.

### GetAsOfOk

`func (o *StorageBreakdownOut) GetAsOfOk() (*string, bool)`

GetAsOfOk returns a tuple with the AsOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAsOf

`func (o *StorageBreakdownOut) SetAsOf(v string)`

SetAsOf sets AsOf field to given value.


### GetLiveBytes

`func (o *StorageBreakdownOut) GetLiveBytes() int32`

GetLiveBytes returns the LiveBytes field if non-nil, zero value otherwise.

### GetLiveBytesOk

`func (o *StorageBreakdownOut) GetLiveBytesOk() (*int32, bool)`

GetLiveBytesOk returns a tuple with the LiveBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLiveBytes

`func (o *StorageBreakdownOut) SetLiveBytes(v int32)`

SetLiveBytes sets LiveBytes field to given value.


### GetTrashBytes

`func (o *StorageBreakdownOut) GetTrashBytes() int32`

GetTrashBytes returns the TrashBytes field if non-nil, zero value otherwise.

### GetTrashBytesOk

`func (o *StorageBreakdownOut) GetTrashBytesOk() (*int32, bool)`

GetTrashBytesOk returns a tuple with the TrashBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrashBytes

`func (o *StorageBreakdownOut) SetTrashBytes(v int32)`

SetTrashBytes sets TrashBytes field to given value.


### GetVersionBytes

`func (o *StorageBreakdownOut) GetVersionBytes() int32`

GetVersionBytes returns the VersionBytes field if non-nil, zero value otherwise.

### GetVersionBytesOk

`func (o *StorageBreakdownOut) GetVersionBytesOk() (*int32, bool)`

GetVersionBytesOk returns a tuple with the VersionBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionBytes

`func (o *StorageBreakdownOut) SetVersionBytes(v int32)`

SetVersionBytes sets VersionBytes field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
