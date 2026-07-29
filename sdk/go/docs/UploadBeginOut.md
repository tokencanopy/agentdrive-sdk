# UploadBeginOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExpiresAt** | **time.Time** |  |
**Headers** | **map[string]string** |  |
**MaxBytes** | **int32** |  |
**Method** | Pointer to **string** |  | [optional] [default to "PUT"]
**UploadId** | **string** |  |
**UploadUrl** | **string** |  |

## Methods

### NewUploadBeginOut

`func NewUploadBeginOut(expiresAt time.Time, headers map[string]string, maxBytes int32, uploadId string, uploadUrl string, ) *UploadBeginOut`

NewUploadBeginOut instantiates a new UploadBeginOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUploadBeginOutWithDefaults

`func NewUploadBeginOutWithDefaults() *UploadBeginOut`

NewUploadBeginOutWithDefaults instantiates a new UploadBeginOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetExpiresAt

`func (o *UploadBeginOut) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *UploadBeginOut) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *UploadBeginOut) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### GetHeaders

`func (o *UploadBeginOut) GetHeaders() map[string]string`

GetHeaders returns the Headers field if non-nil, zero value otherwise.

### GetHeadersOk

`func (o *UploadBeginOut) GetHeadersOk() (*map[string]string, bool)`

GetHeadersOk returns a tuple with the Headers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeaders

`func (o *UploadBeginOut) SetHeaders(v map[string]string)`

SetHeaders sets Headers field to given value.


### GetMaxBytes

`func (o *UploadBeginOut) GetMaxBytes() int32`

GetMaxBytes returns the MaxBytes field if non-nil, zero value otherwise.

### GetMaxBytesOk

`func (o *UploadBeginOut) GetMaxBytesOk() (*int32, bool)`

GetMaxBytesOk returns a tuple with the MaxBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxBytes

`func (o *UploadBeginOut) SetMaxBytes(v int32)`

SetMaxBytes sets MaxBytes field to given value.


### GetMethod

`func (o *UploadBeginOut) GetMethod() string`

GetMethod returns the Method field if non-nil, zero value otherwise.

### GetMethodOk

`func (o *UploadBeginOut) GetMethodOk() (*string, bool)`

GetMethodOk returns a tuple with the Method field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMethod

`func (o *UploadBeginOut) SetMethod(v string)`

SetMethod sets Method field to given value.

### HasMethod

`func (o *UploadBeginOut) HasMethod() bool`

HasMethod returns a boolean if a field has been set.

### GetUploadId

`func (o *UploadBeginOut) GetUploadId() string`

GetUploadId returns the UploadId field if non-nil, zero value otherwise.

### GetUploadIdOk

`func (o *UploadBeginOut) GetUploadIdOk() (*string, bool)`

GetUploadIdOk returns a tuple with the UploadId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUploadId

`func (o *UploadBeginOut) SetUploadId(v string)`

SetUploadId sets UploadId field to given value.


### GetUploadUrl

`func (o *UploadBeginOut) GetUploadUrl() string`

GetUploadUrl returns the UploadUrl field if non-nil, zero value otherwise.

### GetUploadUrlOk

`func (o *UploadBeginOut) GetUploadUrlOk() (*string, bool)`

GetUploadUrlOk returns a tuple with the UploadUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUploadUrl

`func (o *UploadBeginOut) SetUploadUrl(v string)`

SetUploadUrl sets UploadUrl field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
