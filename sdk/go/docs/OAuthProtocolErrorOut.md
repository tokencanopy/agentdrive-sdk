# OAuthProtocolErrorOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Error** | **string** |  |
**ErrorDescription** | Pointer to **NullableString** |  | [optional]

## Methods

### NewOAuthProtocolErrorOut

`func NewOAuthProtocolErrorOut(error_ string, ) *OAuthProtocolErrorOut`

NewOAuthProtocolErrorOut instantiates a new OAuthProtocolErrorOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOAuthProtocolErrorOutWithDefaults

`func NewOAuthProtocolErrorOutWithDefaults() *OAuthProtocolErrorOut`

NewOAuthProtocolErrorOutWithDefaults instantiates a new OAuthProtocolErrorOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetError

`func (o *OAuthProtocolErrorOut) GetError() string`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *OAuthProtocolErrorOut) GetErrorOk() (*string, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *OAuthProtocolErrorOut) SetError(v string)`

SetError sets Error field to given value.


### GetErrorDescription

`func (o *OAuthProtocolErrorOut) GetErrorDescription() string`

GetErrorDescription returns the ErrorDescription field if non-nil, zero value otherwise.

### GetErrorDescriptionOk

`func (o *OAuthProtocolErrorOut) GetErrorDescriptionOk() (*string, bool)`

GetErrorDescriptionOk returns a tuple with the ErrorDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorDescription

`func (o *OAuthProtocolErrorOut) SetErrorDescription(v string)`

SetErrorDescription sets ErrorDescription field to given value.

### HasErrorDescription

`func (o *OAuthProtocolErrorOut) HasErrorDescription() bool`

HasErrorDescription returns a boolean if a field has been set.

### SetErrorDescriptionNil

`func (o *OAuthProtocolErrorOut) SetErrorDescriptionNil(b bool)`

 SetErrorDescriptionNil sets the value for ErrorDescription to be an explicit nil

### UnsetErrorDescription
`func (o *OAuthProtocolErrorOut) UnsetErrorDescription()`

UnsetErrorDescription ensures that no value is present for ErrorDescription, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
