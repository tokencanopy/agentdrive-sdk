# UploadStatusOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CommittedAt** | Pointer to **NullableTime** |  | [optional]
**ContentType** | **string** |  |
**CreatedAt** | **time.Time** |  |
**ExpiresAt** | **time.Time** |  |
**MaxBytes** | **int32** |  |
**Path** | **string** |  |
**SizeBytes** | **int32** |  |
**State** | **string** |  |
**UploadId** | **string** |  |

## Methods

### NewUploadStatusOut

`func NewUploadStatusOut(contentType string, createdAt time.Time, expiresAt time.Time, maxBytes int32, path string, sizeBytes int32, state string, uploadId string, ) *UploadStatusOut`

NewUploadStatusOut instantiates a new UploadStatusOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUploadStatusOutWithDefaults

`func NewUploadStatusOutWithDefaults() *UploadStatusOut`

NewUploadStatusOutWithDefaults instantiates a new UploadStatusOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCommittedAt

`func (o *UploadStatusOut) GetCommittedAt() time.Time`

GetCommittedAt returns the CommittedAt field if non-nil, zero value otherwise.

### GetCommittedAtOk

`func (o *UploadStatusOut) GetCommittedAtOk() (*time.Time, bool)`

GetCommittedAtOk returns a tuple with the CommittedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommittedAt

`func (o *UploadStatusOut) SetCommittedAt(v time.Time)`

SetCommittedAt sets CommittedAt field to given value.

### HasCommittedAt

`func (o *UploadStatusOut) HasCommittedAt() bool`

HasCommittedAt returns a boolean if a field has been set.

### SetCommittedAtNil

`func (o *UploadStatusOut) SetCommittedAtNil(b bool)`

 SetCommittedAtNil sets the value for CommittedAt to be an explicit nil

### UnsetCommittedAt
`func (o *UploadStatusOut) UnsetCommittedAt()`

UnsetCommittedAt ensures that no value is present for CommittedAt, not even an explicit nil
### GetContentType

`func (o *UploadStatusOut) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *UploadStatusOut) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *UploadStatusOut) SetContentType(v string)`

SetContentType sets ContentType field to given value.


### GetCreatedAt

`func (o *UploadStatusOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *UploadStatusOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *UploadStatusOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetExpiresAt

`func (o *UploadStatusOut) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *UploadStatusOut) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *UploadStatusOut) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### GetMaxBytes

`func (o *UploadStatusOut) GetMaxBytes() int32`

GetMaxBytes returns the MaxBytes field if non-nil, zero value otherwise.

### GetMaxBytesOk

`func (o *UploadStatusOut) GetMaxBytesOk() (*int32, bool)`

GetMaxBytesOk returns a tuple with the MaxBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxBytes

`func (o *UploadStatusOut) SetMaxBytes(v int32)`

SetMaxBytes sets MaxBytes field to given value.


### GetPath

`func (o *UploadStatusOut) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *UploadStatusOut) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *UploadStatusOut) SetPath(v string)`

SetPath sets Path field to given value.


### GetSizeBytes

`func (o *UploadStatusOut) GetSizeBytes() int32`

GetSizeBytes returns the SizeBytes field if non-nil, zero value otherwise.

### GetSizeBytesOk

`func (o *UploadStatusOut) GetSizeBytesOk() (*int32, bool)`

GetSizeBytesOk returns a tuple with the SizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSizeBytes

`func (o *UploadStatusOut) SetSizeBytes(v int32)`

SetSizeBytes sets SizeBytes field to given value.


### GetState

`func (o *UploadStatusOut) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *UploadStatusOut) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *UploadStatusOut) SetState(v string)`

SetState sets State field to given value.


### GetUploadId

`func (o *UploadStatusOut) GetUploadId() string`

GetUploadId returns the UploadId field if non-nil, zero value otherwise.

### GetUploadIdOk

`func (o *UploadStatusOut) GetUploadIdOk() (*string, bool)`

GetUploadIdOk returns a tuple with the UploadId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUploadId

`func (o *UploadStatusOut) SetUploadId(v string)`

SetUploadId sets UploadId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
