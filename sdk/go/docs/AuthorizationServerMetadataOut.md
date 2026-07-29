# AuthorizationServerMetadataOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AgentAuth** | [**AgentAuthMetadataOut**](AgentAuthMetadataOut.md) |  |
**AuthorizationEndpoint** | **string** |  |
**AuthorizationResponseIssParameterSupported** | **bool** |  |
**CodeChallengeMethodsSupported** | **[]string** |  |
**GrantTypesSupported** | **[]string** |  |
**Issuer** | **string** |  |
**JwksUri** | **string** |  |
**RegistrationEndpoint** | **string** |  |
**ResponseModesSupported** | **[]string** |  |
**ResponseTypesSupported** | **[]string** |  |
**RevocationEndpoint** | **string** |  |
**RevocationEndpointAuthMethodsSupported** | **[]string** |  |
**ScopesSupported** | **[]string** |  |
**TokenEndpoint** | **string** |  |
**TokenEndpointAuthMethodsSupported** | **[]string** |  |

## Methods

### NewAuthorizationServerMetadataOut

`func NewAuthorizationServerMetadataOut(agentAuth AgentAuthMetadataOut, authorizationEndpoint string, authorizationResponseIssParameterSupported bool, codeChallengeMethodsSupported []string, grantTypesSupported []string, issuer string, jwksUri string, registrationEndpoint string, responseModesSupported []string, responseTypesSupported []string, revocationEndpoint string, revocationEndpointAuthMethodsSupported []string, scopesSupported []string, tokenEndpoint string, tokenEndpointAuthMethodsSupported []string, ) *AuthorizationServerMetadataOut`

NewAuthorizationServerMetadataOut instantiates a new AuthorizationServerMetadataOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAuthorizationServerMetadataOutWithDefaults

`func NewAuthorizationServerMetadataOutWithDefaults() *AuthorizationServerMetadataOut`

NewAuthorizationServerMetadataOutWithDefaults instantiates a new AuthorizationServerMetadataOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAgentAuth

`func (o *AuthorizationServerMetadataOut) GetAgentAuth() AgentAuthMetadataOut`

GetAgentAuth returns the AgentAuth field if non-nil, zero value otherwise.

### GetAgentAuthOk

`func (o *AuthorizationServerMetadataOut) GetAgentAuthOk() (*AgentAuthMetadataOut, bool)`

GetAgentAuthOk returns a tuple with the AgentAuth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAgentAuth

`func (o *AuthorizationServerMetadataOut) SetAgentAuth(v AgentAuthMetadataOut)`

SetAgentAuth sets AgentAuth field to given value.


### GetAuthorizationEndpoint

`func (o *AuthorizationServerMetadataOut) GetAuthorizationEndpoint() string`

GetAuthorizationEndpoint returns the AuthorizationEndpoint field if non-nil, zero value otherwise.

### GetAuthorizationEndpointOk

`func (o *AuthorizationServerMetadataOut) GetAuthorizationEndpointOk() (*string, bool)`

GetAuthorizationEndpointOk returns a tuple with the AuthorizationEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationEndpoint

`func (o *AuthorizationServerMetadataOut) SetAuthorizationEndpoint(v string)`

SetAuthorizationEndpoint sets AuthorizationEndpoint field to given value.


### GetAuthorizationResponseIssParameterSupported

`func (o *AuthorizationServerMetadataOut) GetAuthorizationResponseIssParameterSupported() bool`

GetAuthorizationResponseIssParameterSupported returns the AuthorizationResponseIssParameterSupported field if non-nil, zero value otherwise.

### GetAuthorizationResponseIssParameterSupportedOk

`func (o *AuthorizationServerMetadataOut) GetAuthorizationResponseIssParameterSupportedOk() (*bool, bool)`

GetAuthorizationResponseIssParameterSupportedOk returns a tuple with the AuthorizationResponseIssParameterSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationResponseIssParameterSupported

`func (o *AuthorizationServerMetadataOut) SetAuthorizationResponseIssParameterSupported(v bool)`

SetAuthorizationResponseIssParameterSupported sets AuthorizationResponseIssParameterSupported field to given value.


### GetCodeChallengeMethodsSupported

`func (o *AuthorizationServerMetadataOut) GetCodeChallengeMethodsSupported() []string`

GetCodeChallengeMethodsSupported returns the CodeChallengeMethodsSupported field if non-nil, zero value otherwise.

### GetCodeChallengeMethodsSupportedOk

`func (o *AuthorizationServerMetadataOut) GetCodeChallengeMethodsSupportedOk() (*[]string, bool)`

GetCodeChallengeMethodsSupportedOk returns a tuple with the CodeChallengeMethodsSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCodeChallengeMethodsSupported

`func (o *AuthorizationServerMetadataOut) SetCodeChallengeMethodsSupported(v []string)`

SetCodeChallengeMethodsSupported sets CodeChallengeMethodsSupported field to given value.


### GetGrantTypesSupported

`func (o *AuthorizationServerMetadataOut) GetGrantTypesSupported() []string`

GetGrantTypesSupported returns the GrantTypesSupported field if non-nil, zero value otherwise.

### GetGrantTypesSupportedOk

`func (o *AuthorizationServerMetadataOut) GetGrantTypesSupportedOk() (*[]string, bool)`

GetGrantTypesSupportedOk returns a tuple with the GrantTypesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantTypesSupported

`func (o *AuthorizationServerMetadataOut) SetGrantTypesSupported(v []string)`

SetGrantTypesSupported sets GrantTypesSupported field to given value.


### GetIssuer

`func (o *AuthorizationServerMetadataOut) GetIssuer() string`

GetIssuer returns the Issuer field if non-nil, zero value otherwise.

### GetIssuerOk

`func (o *AuthorizationServerMetadataOut) GetIssuerOk() (*string, bool)`

GetIssuerOk returns a tuple with the Issuer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssuer

`func (o *AuthorizationServerMetadataOut) SetIssuer(v string)`

SetIssuer sets Issuer field to given value.


### GetJwksUri

`func (o *AuthorizationServerMetadataOut) GetJwksUri() string`

GetJwksUri returns the JwksUri field if non-nil, zero value otherwise.

### GetJwksUriOk

`func (o *AuthorizationServerMetadataOut) GetJwksUriOk() (*string, bool)`

GetJwksUriOk returns a tuple with the JwksUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJwksUri

`func (o *AuthorizationServerMetadataOut) SetJwksUri(v string)`

SetJwksUri sets JwksUri field to given value.


### GetRegistrationEndpoint

`func (o *AuthorizationServerMetadataOut) GetRegistrationEndpoint() string`

GetRegistrationEndpoint returns the RegistrationEndpoint field if non-nil, zero value otherwise.

### GetRegistrationEndpointOk

`func (o *AuthorizationServerMetadataOut) GetRegistrationEndpointOk() (*string, bool)`

GetRegistrationEndpointOk returns a tuple with the RegistrationEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegistrationEndpoint

`func (o *AuthorizationServerMetadataOut) SetRegistrationEndpoint(v string)`

SetRegistrationEndpoint sets RegistrationEndpoint field to given value.


### GetResponseModesSupported

`func (o *AuthorizationServerMetadataOut) GetResponseModesSupported() []string`

GetResponseModesSupported returns the ResponseModesSupported field if non-nil, zero value otherwise.

### GetResponseModesSupportedOk

`func (o *AuthorizationServerMetadataOut) GetResponseModesSupportedOk() (*[]string, bool)`

GetResponseModesSupportedOk returns a tuple with the ResponseModesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseModesSupported

`func (o *AuthorizationServerMetadataOut) SetResponseModesSupported(v []string)`

SetResponseModesSupported sets ResponseModesSupported field to given value.


### GetResponseTypesSupported

`func (o *AuthorizationServerMetadataOut) GetResponseTypesSupported() []string`

GetResponseTypesSupported returns the ResponseTypesSupported field if non-nil, zero value otherwise.

### GetResponseTypesSupportedOk

`func (o *AuthorizationServerMetadataOut) GetResponseTypesSupportedOk() (*[]string, bool)`

GetResponseTypesSupportedOk returns a tuple with the ResponseTypesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseTypesSupported

`func (o *AuthorizationServerMetadataOut) SetResponseTypesSupported(v []string)`

SetResponseTypesSupported sets ResponseTypesSupported field to given value.


### GetRevocationEndpoint

`func (o *AuthorizationServerMetadataOut) GetRevocationEndpoint() string`

GetRevocationEndpoint returns the RevocationEndpoint field if non-nil, zero value otherwise.

### GetRevocationEndpointOk

`func (o *AuthorizationServerMetadataOut) GetRevocationEndpointOk() (*string, bool)`

GetRevocationEndpointOk returns a tuple with the RevocationEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevocationEndpoint

`func (o *AuthorizationServerMetadataOut) SetRevocationEndpoint(v string)`

SetRevocationEndpoint sets RevocationEndpoint field to given value.


### GetRevocationEndpointAuthMethodsSupported

`func (o *AuthorizationServerMetadataOut) GetRevocationEndpointAuthMethodsSupported() []string`

GetRevocationEndpointAuthMethodsSupported returns the RevocationEndpointAuthMethodsSupported field if non-nil, zero value otherwise.

### GetRevocationEndpointAuthMethodsSupportedOk

`func (o *AuthorizationServerMetadataOut) GetRevocationEndpointAuthMethodsSupportedOk() (*[]string, bool)`

GetRevocationEndpointAuthMethodsSupportedOk returns a tuple with the RevocationEndpointAuthMethodsSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevocationEndpointAuthMethodsSupported

`func (o *AuthorizationServerMetadataOut) SetRevocationEndpointAuthMethodsSupported(v []string)`

SetRevocationEndpointAuthMethodsSupported sets RevocationEndpointAuthMethodsSupported field to given value.


### GetScopesSupported

`func (o *AuthorizationServerMetadataOut) GetScopesSupported() []string`

GetScopesSupported returns the ScopesSupported field if non-nil, zero value otherwise.

### GetScopesSupportedOk

`func (o *AuthorizationServerMetadataOut) GetScopesSupportedOk() (*[]string, bool)`

GetScopesSupportedOk returns a tuple with the ScopesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopesSupported

`func (o *AuthorizationServerMetadataOut) SetScopesSupported(v []string)`

SetScopesSupported sets ScopesSupported field to given value.


### GetTokenEndpoint

`func (o *AuthorizationServerMetadataOut) GetTokenEndpoint() string`

GetTokenEndpoint returns the TokenEndpoint field if non-nil, zero value otherwise.

### GetTokenEndpointOk

`func (o *AuthorizationServerMetadataOut) GetTokenEndpointOk() (*string, bool)`

GetTokenEndpointOk returns a tuple with the TokenEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenEndpoint

`func (o *AuthorizationServerMetadataOut) SetTokenEndpoint(v string)`

SetTokenEndpoint sets TokenEndpoint field to given value.


### GetTokenEndpointAuthMethodsSupported

`func (o *AuthorizationServerMetadataOut) GetTokenEndpointAuthMethodsSupported() []string`

GetTokenEndpointAuthMethodsSupported returns the TokenEndpointAuthMethodsSupported field if non-nil, zero value otherwise.

### GetTokenEndpointAuthMethodsSupportedOk

`func (o *AuthorizationServerMetadataOut) GetTokenEndpointAuthMethodsSupportedOk() (*[]string, bool)`

GetTokenEndpointAuthMethodsSupportedOk returns a tuple with the TokenEndpointAuthMethodsSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenEndpointAuthMethodsSupported

`func (o *AuthorizationServerMetadataOut) SetTokenEndpointAuthMethodsSupported(v []string)`

SetTokenEndpointAuthMethodsSupported sets TokenEndpointAuthMethodsSupported field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
