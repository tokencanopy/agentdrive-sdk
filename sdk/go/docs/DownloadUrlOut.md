# DownloadUrlOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ContentType** | **string** |  |
**Direct** | **bool** |  |
**DownloadUrl** | **string** |  |
**ExpiresAt** | Pointer to **NullableTime** |  | [optional]
**Filename** | **string** |  |
**SizeBytes** | **int32** |  |

## Methods

### NewDownloadUrlOut

`func NewDownloadUrlOut(contentType string, direct bool, downloadUrl string, filename string, sizeBytes int32, ) *DownloadUrlOut`

NewDownloadUrlOut instantiates a new DownloadUrlOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDownloadUrlOutWithDefaults

`func NewDownloadUrlOutWithDefaults() *DownloadUrlOut`

NewDownloadUrlOutWithDefaults instantiates a new DownloadUrlOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContentType

`func (o *DownloadUrlOut) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *DownloadUrlOut) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *DownloadUrlOut) SetContentType(v string)`

SetContentType sets ContentType field to given value.


### GetDirect

`func (o *DownloadUrlOut) GetDirect() bool`

GetDirect returns the Direct field if non-nil, zero value otherwise.

### GetDirectOk

`func (o *DownloadUrlOut) GetDirectOk() (*bool, bool)`

GetDirectOk returns a tuple with the Direct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDirect

`func (o *DownloadUrlOut) SetDirect(v bool)`

SetDirect sets Direct field to given value.


### GetDownloadUrl

`func (o *DownloadUrlOut) GetDownloadUrl() string`

GetDownloadUrl returns the DownloadUrl field if non-nil, zero value otherwise.

### GetDownloadUrlOk

`func (o *DownloadUrlOut) GetDownloadUrlOk() (*string, bool)`

GetDownloadUrlOk returns a tuple with the DownloadUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDownloadUrl

`func (o *DownloadUrlOut) SetDownloadUrl(v string)`

SetDownloadUrl sets DownloadUrl field to given value.


### GetExpiresAt

`func (o *DownloadUrlOut) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *DownloadUrlOut) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *DownloadUrlOut) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.

### HasExpiresAt

`func (o *DownloadUrlOut) HasExpiresAt() bool`

HasExpiresAt returns a boolean if a field has been set.

### SetExpiresAtNil

`func (o *DownloadUrlOut) SetExpiresAtNil(b bool)`

 SetExpiresAtNil sets the value for ExpiresAt to be an explicit nil

### UnsetExpiresAt
`func (o *DownloadUrlOut) UnsetExpiresAt()`

UnsetExpiresAt ensures that no value is present for ExpiresAt, not even an explicit nil
### GetFilename

`func (o *DownloadUrlOut) GetFilename() string`

GetFilename returns the Filename field if non-nil, zero value otherwise.

### GetFilenameOk

`func (o *DownloadUrlOut) GetFilenameOk() (*string, bool)`

GetFilenameOk returns a tuple with the Filename field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFilename

`func (o *DownloadUrlOut) SetFilename(v string)`

SetFilename sets Filename field to given value.


### GetSizeBytes

`func (o *DownloadUrlOut) GetSizeBytes() int32`

GetSizeBytes returns the SizeBytes field if non-nil, zero value otherwise.

### GetSizeBytesOk

`func (o *DownloadUrlOut) GetSizeBytesOk() (*int32, bool)`

GetSizeBytesOk returns a tuple with the SizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSizeBytes

`func (o *DownloadUrlOut) SetSizeBytes(v int32)`

SetSizeBytes sets SizeBytes field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
