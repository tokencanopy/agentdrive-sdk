# ExtensionExchangeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccessToken** | **string** | 15-minute access_token (scope&#x3D;extension). |
**DriveId** | **string** | The drive these credentials are scoped to. |
**ExpiresIn** | **int32** | Seconds until access_token expiry. |
**IdentityAssertion** | **string** | 90-day identity_assertion. Refresh via POST /oauth2/token. |
**Scope** | Pointer to **string** |  | [optional] [default to "extension"]
**TokenType** | Pointer to **string** |  | [optional] [default to "Bearer"]

## Methods

### NewExtensionExchangeResponse

`func NewExtensionExchangeResponse(accessToken string, driveId string, expiresIn int32, identityAssertion string, ) *ExtensionExchangeResponse`

NewExtensionExchangeResponse instantiates a new ExtensionExchangeResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewExtensionExchangeResponseWithDefaults

`func NewExtensionExchangeResponseWithDefaults() *ExtensionExchangeResponse`

NewExtensionExchangeResponseWithDefaults instantiates a new ExtensionExchangeResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccessToken

`func (o *ExtensionExchangeResponse) GetAccessToken() string`

GetAccessToken returns the AccessToken field if non-nil, zero value otherwise.

### GetAccessTokenOk

`func (o *ExtensionExchangeResponse) GetAccessTokenOk() (*string, bool)`

GetAccessTokenOk returns a tuple with the AccessToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccessToken

`func (o *ExtensionExchangeResponse) SetAccessToken(v string)`

SetAccessToken sets AccessToken field to given value.


### GetDriveId

`func (o *ExtensionExchangeResponse) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *ExtensionExchangeResponse) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *ExtensionExchangeResponse) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetExpiresIn

`func (o *ExtensionExchangeResponse) GetExpiresIn() int32`

GetExpiresIn returns the ExpiresIn field if non-nil, zero value otherwise.

### GetExpiresInOk

`func (o *ExtensionExchangeResponse) GetExpiresInOk() (*int32, bool)`

GetExpiresInOk returns a tuple with the ExpiresIn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresIn

`func (o *ExtensionExchangeResponse) SetExpiresIn(v int32)`

SetExpiresIn sets ExpiresIn field to given value.


### GetIdentityAssertion

`func (o *ExtensionExchangeResponse) GetIdentityAssertion() string`

GetIdentityAssertion returns the IdentityAssertion field if non-nil, zero value otherwise.

### GetIdentityAssertionOk

`func (o *ExtensionExchangeResponse) GetIdentityAssertionOk() (*string, bool)`

GetIdentityAssertionOk returns a tuple with the IdentityAssertion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentityAssertion

`func (o *ExtensionExchangeResponse) SetIdentityAssertion(v string)`

SetIdentityAssertion sets IdentityAssertion field to given value.


### GetScope

`func (o *ExtensionExchangeResponse) GetScope() string`

GetScope returns the Scope field if non-nil, zero value otherwise.

### GetScopeOk

`func (o *ExtensionExchangeResponse) GetScopeOk() (*string, bool)`

GetScopeOk returns a tuple with the Scope field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScope

`func (o *ExtensionExchangeResponse) SetScope(v string)`

SetScope sets Scope field to given value.

### HasScope

`func (o *ExtensionExchangeResponse) HasScope() bool`

HasScope returns a boolean if a field has been set.

### GetTokenType

`func (o *ExtensionExchangeResponse) GetTokenType() string`

GetTokenType returns the TokenType field if non-nil, zero value otherwise.

### GetTokenTypeOk

`func (o *ExtensionExchangeResponse) GetTokenTypeOk() (*string, bool)`

GetTokenTypeOk returns a tuple with the TokenType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenType

`func (o *ExtensionExchangeResponse) SetTokenType(v string)`

SetTokenType sets TokenType field to given value.

### HasTokenType

`func (o *ExtensionExchangeResponse) HasTokenType() bool`

HasTokenType returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
