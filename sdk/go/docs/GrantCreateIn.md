# GrantCreateIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExpiresIn** | Pointer to **NullableInt32** |  | [optional]
**Principal** | [**GrantPrincipalIn**](GrantPrincipalIn.md) |  |
**Resource** | **string** |  |
**Role** | **string** |  |

## Methods

### NewGrantCreateIn

`func NewGrantCreateIn(principal GrantPrincipalIn, resource string, role string, ) *GrantCreateIn`

NewGrantCreateIn instantiates a new GrantCreateIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGrantCreateInWithDefaults

`func NewGrantCreateInWithDefaults() *GrantCreateIn`

NewGrantCreateInWithDefaults instantiates a new GrantCreateIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetExpiresIn

`func (o *GrantCreateIn) GetExpiresIn() int32`

GetExpiresIn returns the ExpiresIn field if non-nil, zero value otherwise.

### GetExpiresInOk

`func (o *GrantCreateIn) GetExpiresInOk() (*int32, bool)`

GetExpiresInOk returns a tuple with the ExpiresIn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresIn

`func (o *GrantCreateIn) SetExpiresIn(v int32)`

SetExpiresIn sets ExpiresIn field to given value.

### HasExpiresIn

`func (o *GrantCreateIn) HasExpiresIn() bool`

HasExpiresIn returns a boolean if a field has been set.

### SetExpiresInNil

`func (o *GrantCreateIn) SetExpiresInNil(b bool)`

 SetExpiresInNil sets the value for ExpiresIn to be an explicit nil

### UnsetExpiresIn
`func (o *GrantCreateIn) UnsetExpiresIn()`

UnsetExpiresIn ensures that no value is present for ExpiresIn, not even an explicit nil
### GetPrincipal

`func (o *GrantCreateIn) GetPrincipal() GrantPrincipalIn`

GetPrincipal returns the Principal field if non-nil, zero value otherwise.

### GetPrincipalOk

`func (o *GrantCreateIn) GetPrincipalOk() (*GrantPrincipalIn, bool)`

GetPrincipalOk returns a tuple with the Principal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrincipal

`func (o *GrantCreateIn) SetPrincipal(v GrantPrincipalIn)`

SetPrincipal sets Principal field to given value.


### GetResource

`func (o *GrantCreateIn) GetResource() string`

GetResource returns the Resource field if non-nil, zero value otherwise.

### GetResourceOk

`func (o *GrantCreateIn) GetResourceOk() (*string, bool)`

GetResourceOk returns a tuple with the Resource field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResource

`func (o *GrantCreateIn) SetResource(v string)`

SetResource sets Resource field to given value.


### GetRole

`func (o *GrantCreateIn) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *GrantCreateIn) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *GrantCreateIn) SetRole(v string)`

SetRole sets Role field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
