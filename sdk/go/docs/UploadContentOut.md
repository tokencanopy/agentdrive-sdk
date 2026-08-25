# UploadContentOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SizeBytes** | **int32** |  | 
**MediaType** | **string** |  | 
**Checksum** | [**UploadChecksumOut**](UploadChecksumOut.md) |  | 

## Methods

### NewUploadContentOut

`func NewUploadContentOut(sizeBytes int32, mediaType string, checksum UploadChecksumOut, ) *UploadContentOut`

NewUploadContentOut instantiates a new UploadContentOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUploadContentOutWithDefaults

`func NewUploadContentOutWithDefaults() *UploadContentOut`

NewUploadContentOutWithDefaults instantiates a new UploadContentOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSizeBytes

`func (o *UploadContentOut) GetSizeBytes() int32`

GetSizeBytes returns the SizeBytes field if non-nil, zero value otherwise.

### GetSizeBytesOk

`func (o *UploadContentOut) GetSizeBytesOk() (*int32, bool)`

GetSizeBytesOk returns a tuple with the SizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSizeBytes

`func (o *UploadContentOut) SetSizeBytes(v int32)`

SetSizeBytes sets SizeBytes field to given value.


### GetMediaType

`func (o *UploadContentOut) GetMediaType() string`

GetMediaType returns the MediaType field if non-nil, zero value otherwise.

### GetMediaTypeOk

`func (o *UploadContentOut) GetMediaTypeOk() (*string, bool)`

GetMediaTypeOk returns a tuple with the MediaType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMediaType

`func (o *UploadContentOut) SetMediaType(v string)`

SetMediaType sets MediaType field to given value.


### GetChecksum

`func (o *UploadContentOut) GetChecksum() UploadChecksumOut`

GetChecksum returns the Checksum field if non-nil, zero value otherwise.

### GetChecksumOk

`func (o *UploadContentOut) GetChecksumOk() (*UploadChecksumOut, bool)`

GetChecksumOk returns a tuple with the Checksum field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChecksum

`func (o *UploadContentOut) SetChecksum(v UploadChecksumOut)`

SetChecksum sets Checksum field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


