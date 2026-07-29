# TokenResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccessToken** | **string** |  |
**ExpiresIn** | **int32** | Seconds until access_token expiry. |
**IdentityAssertion** | Pointer to **NullableString** |  | [optional]
**Scope** | **string** |  |
**TokenType** | Pointer to **string** |  | [optional] [default to "Bearer"]

## Methods

### NewTokenResponse

`func NewTokenResponse(accessToken string, expiresIn int32, scope string, ) *TokenResponse`

NewTokenResponse instantiates a new TokenResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTokenResponseWithDefaults

`func NewTokenResponseWithDefaults() *TokenResponse`

NewTokenResponseWithDefaults instantiates a new TokenResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccessToken

`func (o *TokenResponse) GetAccessToken() string`

GetAccessToken returns the AccessToken field if non-nil, zero value otherwise.

### GetAccessTokenOk

`func (o *TokenResponse) GetAccessTokenOk() (*string, bool)`

GetAccessTokenOk returns a tuple with the AccessToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccessToken

`func (o *TokenResponse) SetAccessToken(v string)`

SetAccessToken sets AccessToken field to given value.


### GetExpiresIn

`func (o *TokenResponse) GetExpiresIn() int32`

GetExpiresIn returns the ExpiresIn field if non-nil, zero value otherwise.

### GetExpiresInOk

`func (o *TokenResponse) GetExpiresInOk() (*int32, bool)`

GetExpiresInOk returns a tuple with the ExpiresIn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresIn

`func (o *TokenResponse) SetExpiresIn(v int32)`

SetExpiresIn sets ExpiresIn field to given value.


### GetIdentityAssertion

`func (o *TokenResponse) GetIdentityAssertion() string`

GetIdentityAssertion returns the IdentityAssertion field if non-nil, zero value otherwise.

### GetIdentityAssertionOk

`func (o *TokenResponse) GetIdentityAssertionOk() (*string, bool)`

GetIdentityAssertionOk returns a tuple with the IdentityAssertion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentityAssertion

`func (o *TokenResponse) SetIdentityAssertion(v string)`

SetIdentityAssertion sets IdentityAssertion field to given value.

### HasIdentityAssertion

`func (o *TokenResponse) HasIdentityAssertion() bool`

HasIdentityAssertion returns a boolean if a field has been set.

### SetIdentityAssertionNil

`func (o *TokenResponse) SetIdentityAssertionNil(b bool)`

 SetIdentityAssertionNil sets the value for IdentityAssertion to be an explicit nil

### UnsetIdentityAssertion
`func (o *TokenResponse) UnsetIdentityAssertion()`

UnsetIdentityAssertion ensures that no value is present for IdentityAssertion, not even an explicit nil
### GetScope

`func (o *TokenResponse) GetScope() string`

GetScope returns the Scope field if non-nil, zero value otherwise.

### GetScopeOk

`func (o *TokenResponse) GetScopeOk() (*string, bool)`

GetScopeOk returns a tuple with the Scope field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScope

`func (o *TokenResponse) SetScope(v string)`

SetScope sets Scope field to given value.


### GetTokenType

`func (o *TokenResponse) GetTokenType() string`

GetTokenType returns the TokenType field if non-nil, zero value otherwise.

### GetTokenTypeOk

`func (o *TokenResponse) GetTokenTypeOk() (*string, bool)`

GetTokenTypeOk returns a tuple with the TokenType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenType

`func (o *TokenResponse) SetTokenType(v string)`

SetTokenType sets TokenType field to given value.

### HasTokenType

`func (o *TokenResponse) HasTokenType() bool`

HasTokenType returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
