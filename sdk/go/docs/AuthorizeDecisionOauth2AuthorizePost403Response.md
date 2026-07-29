# AuthorizeDecisionOauth2AuthorizePost403Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Error** | **string** |  |
**ErrorDescription** | Pointer to **string** |  | [optional]
**Detail** | [**ErrorDetail**](ErrorDetail.md) |  |

## Methods

### NewAuthorizeDecisionOauth2AuthorizePost403Response

`func NewAuthorizeDecisionOauth2AuthorizePost403Response(error_ string, detail ErrorDetail, ) *AuthorizeDecisionOauth2AuthorizePost403Response`

NewAuthorizeDecisionOauth2AuthorizePost403Response instantiates a new AuthorizeDecisionOauth2AuthorizePost403Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAuthorizeDecisionOauth2AuthorizePost403ResponseWithDefaults

`func NewAuthorizeDecisionOauth2AuthorizePost403ResponseWithDefaults() *AuthorizeDecisionOauth2AuthorizePost403Response`

NewAuthorizeDecisionOauth2AuthorizePost403ResponseWithDefaults instantiates a new AuthorizeDecisionOauth2AuthorizePost403Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetError

`func (o *AuthorizeDecisionOauth2AuthorizePost403Response) GetError() string`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *AuthorizeDecisionOauth2AuthorizePost403Response) GetErrorOk() (*string, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *AuthorizeDecisionOauth2AuthorizePost403Response) SetError(v string)`

SetError sets Error field to given value.


### GetErrorDescription

`func (o *AuthorizeDecisionOauth2AuthorizePost403Response) GetErrorDescription() string`

GetErrorDescription returns the ErrorDescription field if non-nil, zero value otherwise.

### GetErrorDescriptionOk

`func (o *AuthorizeDecisionOauth2AuthorizePost403Response) GetErrorDescriptionOk() (*string, bool)`

GetErrorDescriptionOk returns a tuple with the ErrorDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorDescription

`func (o *AuthorizeDecisionOauth2AuthorizePost403Response) SetErrorDescription(v string)`

SetErrorDescription sets ErrorDescription field to given value.

### HasErrorDescription

`func (o *AuthorizeDecisionOauth2AuthorizePost403Response) HasErrorDescription() bool`

HasErrorDescription returns a boolean if a field has been set.

### GetDetail

`func (o *AuthorizeDecisionOauth2AuthorizePost403Response) GetDetail() ErrorDetail`

GetDetail returns the Detail field if non-nil, zero value otherwise.

### GetDetailOk

`func (o *AuthorizeDecisionOauth2AuthorizePost403Response) GetDetailOk() (*ErrorDetail, bool)`

GetDetailOk returns a tuple with the Detail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetail

`func (o *AuthorizeDecisionOauth2AuthorizePost403Response) SetDetail(v ErrorDetail)`

SetDetail sets Detail field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
