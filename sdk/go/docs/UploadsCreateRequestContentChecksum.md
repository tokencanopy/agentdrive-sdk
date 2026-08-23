# UploadsCreateRequestContentChecksum

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Algorithm** | **string** |  |
**Value** | **string** | Canonical padded standard-base64 CRC32C of exactly four bytes (GCS metadata form). |

## Methods

### NewUploadsCreateRequestContentChecksum

`func NewUploadsCreateRequestContentChecksum(algorithm string, value string, ) *UploadsCreateRequestContentChecksum`

NewUploadsCreateRequestContentChecksum instantiates a new UploadsCreateRequestContentChecksum object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUploadsCreateRequestContentChecksumWithDefaults

`func NewUploadsCreateRequestContentChecksumWithDefaults() *UploadsCreateRequestContentChecksum`

NewUploadsCreateRequestContentChecksumWithDefaults instantiates a new UploadsCreateRequestContentChecksum object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAlgorithm

`func (o *UploadsCreateRequestContentChecksum) GetAlgorithm() string`

GetAlgorithm returns the Algorithm field if non-nil, zero value otherwise.

### GetAlgorithmOk

`func (o *UploadsCreateRequestContentChecksum) GetAlgorithmOk() (*string, bool)`

GetAlgorithmOk returns a tuple with the Algorithm field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlgorithm

`func (o *UploadsCreateRequestContentChecksum) SetAlgorithm(v string)`

SetAlgorithm sets Algorithm field to given value.


### GetValue

`func (o *UploadsCreateRequestContentChecksum) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *UploadsCreateRequestContentChecksum) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *UploadsCreateRequestContentChecksum) SetValue(v string)`

SetValue sets Value field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
