# ClaimMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClaimEndpoint** | **string** |  |
**SupportedEmailHints** | Pointer to **bool** |  | [optional] [default to true]

## Methods

### NewClaimMetadata

`func NewClaimMetadata(claimEndpoint string, ) *ClaimMetadata`

NewClaimMetadata instantiates a new ClaimMetadata object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewClaimMetadataWithDefaults

`func NewClaimMetadataWithDefaults() *ClaimMetadata`

NewClaimMetadataWithDefaults instantiates a new ClaimMetadata object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClaimEndpoint

`func (o *ClaimMetadata) GetClaimEndpoint() string`

GetClaimEndpoint returns the ClaimEndpoint field if non-nil, zero value otherwise.

### GetClaimEndpointOk

`func (o *ClaimMetadata) GetClaimEndpointOk() (*string, bool)`

GetClaimEndpointOk returns a tuple with the ClaimEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClaimEndpoint

`func (o *ClaimMetadata) SetClaimEndpoint(v string)`

SetClaimEndpoint sets ClaimEndpoint field to given value.


### GetSupportedEmailHints

`func (o *ClaimMetadata) GetSupportedEmailHints() bool`

GetSupportedEmailHints returns the SupportedEmailHints field if non-nil, zero value otherwise.

### GetSupportedEmailHintsOk

`func (o *ClaimMetadata) GetSupportedEmailHintsOk() (*bool, bool)`

GetSupportedEmailHintsOk returns a tuple with the SupportedEmailHints field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSupportedEmailHints

`func (o *ClaimMetadata) SetSupportedEmailHints(v bool)`

SetSupportedEmailHints sets SupportedEmailHints field to given value.

### HasSupportedEmailHints

`func (o *ClaimMetadata) HasSupportedEmailHints() bool`

HasSupportedEmailHints returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
