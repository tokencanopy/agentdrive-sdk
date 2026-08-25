# UploadsCreateRequestContent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SizeBytes** | **int32** | Declared object size in bytes, within the enabled B8-configured window. | 
**MediaType** | **string** | Bare IANA type/subtype, no parameters. | 
**Checksum** | [**UploadsCreateRequestContentChecksum**](UploadsCreateRequestContentChecksum.md) |  | 

## Methods

### NewUploadsCreateRequestContent

`func NewUploadsCreateRequestContent(sizeBytes int32, mediaType string, checksum UploadsCreateRequestContentChecksum, ) *UploadsCreateRequestContent`

NewUploadsCreateRequestContent instantiates a new UploadsCreateRequestContent object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUploadsCreateRequestContentWithDefaults

`func NewUploadsCreateRequestContentWithDefaults() *UploadsCreateRequestContent`

NewUploadsCreateRequestContentWithDefaults instantiates a new UploadsCreateRequestContent object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSizeBytes

`func (o *UploadsCreateRequestContent) GetSizeBytes() int32`

GetSizeBytes returns the SizeBytes field if non-nil, zero value otherwise.

### GetSizeBytesOk

`func (o *UploadsCreateRequestContent) GetSizeBytesOk() (*int32, bool)`

GetSizeBytesOk returns a tuple with the SizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSizeBytes

`func (o *UploadsCreateRequestContent) SetSizeBytes(v int32)`

SetSizeBytes sets SizeBytes field to given value.


### GetMediaType

`func (o *UploadsCreateRequestContent) GetMediaType() string`

GetMediaType returns the MediaType field if non-nil, zero value otherwise.

### GetMediaTypeOk

`func (o *UploadsCreateRequestContent) GetMediaTypeOk() (*string, bool)`

GetMediaTypeOk returns a tuple with the MediaType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMediaType

`func (o *UploadsCreateRequestContent) SetMediaType(v string)`

SetMediaType sets MediaType field to given value.


### GetChecksum

`func (o *UploadsCreateRequestContent) GetChecksum() UploadsCreateRequestContentChecksum`

GetChecksum returns the Checksum field if non-nil, zero value otherwise.

### GetChecksumOk

`func (o *UploadsCreateRequestContent) GetChecksumOk() (*UploadsCreateRequestContentChecksum, bool)`

GetChecksumOk returns a tuple with the Checksum field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChecksum

`func (o *UploadsCreateRequestContent) SetChecksum(v UploadsCreateRequestContentChecksum)`

SetChecksum sets Checksum field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


