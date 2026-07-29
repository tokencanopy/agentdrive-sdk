# StorageFootprintOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AsOf** | Pointer to **NullableString** |  | [optional]
**LiveBytes** | **int32** |  |
**TotalBytes** | **int32** |  |
**TrashBytes** | **int32** |  |
**VersionBytes** | **int32** |  |

## Methods

### NewStorageFootprintOut

`func NewStorageFootprintOut(liveBytes int32, totalBytes int32, trashBytes int32, versionBytes int32, ) *StorageFootprintOut`

NewStorageFootprintOut instantiates a new StorageFootprintOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStorageFootprintOutWithDefaults

`func NewStorageFootprintOutWithDefaults() *StorageFootprintOut`

NewStorageFootprintOutWithDefaults instantiates a new StorageFootprintOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAsOf

`func (o *StorageFootprintOut) GetAsOf() string`

GetAsOf returns the AsOf field if non-nil, zero value otherwise.

### GetAsOfOk

`func (o *StorageFootprintOut) GetAsOfOk() (*string, bool)`

GetAsOfOk returns a tuple with the AsOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAsOf

`func (o *StorageFootprintOut) SetAsOf(v string)`

SetAsOf sets AsOf field to given value.

### HasAsOf

`func (o *StorageFootprintOut) HasAsOf() bool`

HasAsOf returns a boolean if a field has been set.

### SetAsOfNil

`func (o *StorageFootprintOut) SetAsOfNil(b bool)`

 SetAsOfNil sets the value for AsOf to be an explicit nil

### UnsetAsOf
`func (o *StorageFootprintOut) UnsetAsOf()`

UnsetAsOf ensures that no value is present for AsOf, not even an explicit nil
### GetLiveBytes

`func (o *StorageFootprintOut) GetLiveBytes() int32`

GetLiveBytes returns the LiveBytes field if non-nil, zero value otherwise.

### GetLiveBytesOk

`func (o *StorageFootprintOut) GetLiveBytesOk() (*int32, bool)`

GetLiveBytesOk returns a tuple with the LiveBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLiveBytes

`func (o *StorageFootprintOut) SetLiveBytes(v int32)`

SetLiveBytes sets LiveBytes field to given value.


### GetTotalBytes

`func (o *StorageFootprintOut) GetTotalBytes() int32`

GetTotalBytes returns the TotalBytes field if non-nil, zero value otherwise.

### GetTotalBytesOk

`func (o *StorageFootprintOut) GetTotalBytesOk() (*int32, bool)`

GetTotalBytesOk returns a tuple with the TotalBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalBytes

`func (o *StorageFootprintOut) SetTotalBytes(v int32)`

SetTotalBytes sets TotalBytes field to given value.


### GetTrashBytes

`func (o *StorageFootprintOut) GetTrashBytes() int32`

GetTrashBytes returns the TrashBytes field if non-nil, zero value otherwise.

### GetTrashBytesOk

`func (o *StorageFootprintOut) GetTrashBytesOk() (*int32, bool)`

GetTrashBytesOk returns a tuple with the TrashBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrashBytes

`func (o *StorageFootprintOut) SetTrashBytes(v int32)`

SetTrashBytes sets TrashBytes field to given value.


### GetVersionBytes

`func (o *StorageFootprintOut) GetVersionBytes() int32`

GetVersionBytes returns the VersionBytes field if non-nil, zero value otherwise.

### GetVersionBytesOk

`func (o *StorageFootprintOut) GetVersionBytesOk() (*int32, bool)`

GetVersionBytesOk returns a tuple with the VersionBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionBytes

`func (o *StorageFootprintOut) SetVersionBytes(v int32)`

SetVersionBytes sets VersionBytes field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
