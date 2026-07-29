# UploadAbortOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ReleasedBytes** | **int32** |  |
**State** | Pointer to **string** |  | [optional] [default to "aborted"]
**UploadId** | **string** |  |

## Methods

### NewUploadAbortOut

`func NewUploadAbortOut(releasedBytes int32, uploadId string, ) *UploadAbortOut`

NewUploadAbortOut instantiates a new UploadAbortOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUploadAbortOutWithDefaults

`func NewUploadAbortOutWithDefaults() *UploadAbortOut`

NewUploadAbortOutWithDefaults instantiates a new UploadAbortOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetReleasedBytes

`func (o *UploadAbortOut) GetReleasedBytes() int32`

GetReleasedBytes returns the ReleasedBytes field if non-nil, zero value otherwise.

### GetReleasedBytesOk

`func (o *UploadAbortOut) GetReleasedBytesOk() (*int32, bool)`

GetReleasedBytesOk returns a tuple with the ReleasedBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReleasedBytes

`func (o *UploadAbortOut) SetReleasedBytes(v int32)`

SetReleasedBytes sets ReleasedBytes field to given value.


### GetState

`func (o *UploadAbortOut) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *UploadAbortOut) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *UploadAbortOut) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *UploadAbortOut) HasState() bool`

HasState returns a boolean if a field has been set.

### GetUploadId

`func (o *UploadAbortOut) GetUploadId() string`

GetUploadId returns the UploadId field if non-nil, zero value otherwise.

### GetUploadIdOk

`func (o *UploadAbortOut) GetUploadIdOk() (*string, bool)`

GetUploadIdOk returns a tuple with the UploadId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUploadId

`func (o *UploadAbortOut) SetUploadId(v string)`

SetUploadId sets UploadId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
