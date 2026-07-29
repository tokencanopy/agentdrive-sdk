# ClientRegistrationOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClientId** | **string** |  |
**ClientIdIssuedAt** | **int32** |  |
**ClientName** | **string** |  |
**GrantTypes** | **[]string** |  |
**RedirectUris** | **[]string** |  |
**ResponseTypes** | **[]string** |  |
**Scope** | **string** |  |
**TokenEndpointAuthMethod** | **string** |  |

## Methods

### NewClientRegistrationOut

`func NewClientRegistrationOut(clientId string, clientIdIssuedAt int32, clientName string, grantTypes []string, redirectUris []string, responseTypes []string, scope string, tokenEndpointAuthMethod string, ) *ClientRegistrationOut`

NewClientRegistrationOut instantiates a new ClientRegistrationOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewClientRegistrationOutWithDefaults

`func NewClientRegistrationOutWithDefaults() *ClientRegistrationOut`

NewClientRegistrationOutWithDefaults instantiates a new ClientRegistrationOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClientId

`func (o *ClientRegistrationOut) GetClientId() string`

GetClientId returns the ClientId field if non-nil, zero value otherwise.

### GetClientIdOk

`func (o *ClientRegistrationOut) GetClientIdOk() (*string, bool)`

GetClientIdOk returns a tuple with the ClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientId

`func (o *ClientRegistrationOut) SetClientId(v string)`

SetClientId sets ClientId field to given value.


### GetClientIdIssuedAt

`func (o *ClientRegistrationOut) GetClientIdIssuedAt() int32`

GetClientIdIssuedAt returns the ClientIdIssuedAt field if non-nil, zero value otherwise.

### GetClientIdIssuedAtOk

`func (o *ClientRegistrationOut) GetClientIdIssuedAtOk() (*int32, bool)`

GetClientIdIssuedAtOk returns a tuple with the ClientIdIssuedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientIdIssuedAt

`func (o *ClientRegistrationOut) SetClientIdIssuedAt(v int32)`

SetClientIdIssuedAt sets ClientIdIssuedAt field to given value.


### GetClientName

`func (o *ClientRegistrationOut) GetClientName() string`

GetClientName returns the ClientName field if non-nil, zero value otherwise.

### GetClientNameOk

`func (o *ClientRegistrationOut) GetClientNameOk() (*string, bool)`

GetClientNameOk returns a tuple with the ClientName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientName

`func (o *ClientRegistrationOut) SetClientName(v string)`

SetClientName sets ClientName field to given value.


### GetGrantTypes

`func (o *ClientRegistrationOut) GetGrantTypes() []string`

GetGrantTypes returns the GrantTypes field if non-nil, zero value otherwise.

### GetGrantTypesOk

`func (o *ClientRegistrationOut) GetGrantTypesOk() (*[]string, bool)`

GetGrantTypesOk returns a tuple with the GrantTypes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantTypes

`func (o *ClientRegistrationOut) SetGrantTypes(v []string)`

SetGrantTypes sets GrantTypes field to given value.


### GetRedirectUris

`func (o *ClientRegistrationOut) GetRedirectUris() []string`

GetRedirectUris returns the RedirectUris field if non-nil, zero value otherwise.

### GetRedirectUrisOk

`func (o *ClientRegistrationOut) GetRedirectUrisOk() (*[]string, bool)`

GetRedirectUrisOk returns a tuple with the RedirectUris field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedirectUris

`func (o *ClientRegistrationOut) SetRedirectUris(v []string)`

SetRedirectUris sets RedirectUris field to given value.


### GetResponseTypes

`func (o *ClientRegistrationOut) GetResponseTypes() []string`

GetResponseTypes returns the ResponseTypes field if non-nil, zero value otherwise.

### GetResponseTypesOk

`func (o *ClientRegistrationOut) GetResponseTypesOk() (*[]string, bool)`

GetResponseTypesOk returns a tuple with the ResponseTypes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseTypes

`func (o *ClientRegistrationOut) SetResponseTypes(v []string)`

SetResponseTypes sets ResponseTypes field to given value.


### GetScope

`func (o *ClientRegistrationOut) GetScope() string`

GetScope returns the Scope field if non-nil, zero value otherwise.

### GetScopeOk

`func (o *ClientRegistrationOut) GetScopeOk() (*string, bool)`

GetScopeOk returns a tuple with the Scope field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScope

`func (o *ClientRegistrationOut) SetScope(v string)`

SetScope sets Scope field to given value.


### GetTokenEndpointAuthMethod

`func (o *ClientRegistrationOut) GetTokenEndpointAuthMethod() string`

GetTokenEndpointAuthMethod returns the TokenEndpointAuthMethod field if non-nil, zero value otherwise.

### GetTokenEndpointAuthMethodOk

`func (o *ClientRegistrationOut) GetTokenEndpointAuthMethodOk() (*string, bool)`

GetTokenEndpointAuthMethodOk returns a tuple with the TokenEndpointAuthMethod field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenEndpointAuthMethod

`func (o *ClientRegistrationOut) SetTokenEndpointAuthMethod(v string)`

SetTokenEndpointAuthMethod sets TokenEndpointAuthMethod field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
