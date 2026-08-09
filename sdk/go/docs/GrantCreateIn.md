# GrantCreateIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExpiresAt** | Pointer to **NullableTime** |  | [optional]
**PrincipalId** | Pointer to **NullableString** |  | [optional]
**PrincipalType** | **string** |  |
**ResourceId** | **string** |  |
**ResourceType** | **string** |  |
**Role** | **string** |  |

## Methods

### NewGrantCreateIn

`func NewGrantCreateIn(principalType string, resourceId string, resourceType string, role string, ) *GrantCreateIn`

NewGrantCreateIn instantiates a new GrantCreateIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGrantCreateInWithDefaults

`func NewGrantCreateInWithDefaults() *GrantCreateIn`

NewGrantCreateInWithDefaults instantiates a new GrantCreateIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetExpiresAt

`func (o *GrantCreateIn) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *GrantCreateIn) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *GrantCreateIn) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.

### HasExpiresAt

`func (o *GrantCreateIn) HasExpiresAt() bool`

HasExpiresAt returns a boolean if a field has been set.

### SetExpiresAtNil

`func (o *GrantCreateIn) SetExpiresAtNil(b bool)`

 SetExpiresAtNil sets the value for ExpiresAt to be an explicit nil

### UnsetExpiresAt
`func (o *GrantCreateIn) UnsetExpiresAt()`

UnsetExpiresAt ensures that no value is present for ExpiresAt, not even an explicit nil
### GetPrincipalId

`func (o *GrantCreateIn) GetPrincipalId() string`

GetPrincipalId returns the PrincipalId field if non-nil, zero value otherwise.

### GetPrincipalIdOk

`func (o *GrantCreateIn) GetPrincipalIdOk() (*string, bool)`

GetPrincipalIdOk returns a tuple with the PrincipalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrincipalId

`func (o *GrantCreateIn) SetPrincipalId(v string)`

SetPrincipalId sets PrincipalId field to given value.

### HasPrincipalId

`func (o *GrantCreateIn) HasPrincipalId() bool`

HasPrincipalId returns a boolean if a field has been set.

### SetPrincipalIdNil

`func (o *GrantCreateIn) SetPrincipalIdNil(b bool)`

 SetPrincipalIdNil sets the value for PrincipalId to be an explicit nil

### UnsetPrincipalId
`func (o *GrantCreateIn) UnsetPrincipalId()`

UnsetPrincipalId ensures that no value is present for PrincipalId, not even an explicit nil
### GetPrincipalType

`func (o *GrantCreateIn) GetPrincipalType() string`

GetPrincipalType returns the PrincipalType field if non-nil, zero value otherwise.

### GetPrincipalTypeOk

`func (o *GrantCreateIn) GetPrincipalTypeOk() (*string, bool)`

GetPrincipalTypeOk returns a tuple with the PrincipalType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrincipalType

`func (o *GrantCreateIn) SetPrincipalType(v string)`

SetPrincipalType sets PrincipalType field to given value.


### GetResourceId

`func (o *GrantCreateIn) GetResourceId() string`

GetResourceId returns the ResourceId field if non-nil, zero value otherwise.

### GetResourceIdOk

`func (o *GrantCreateIn) GetResourceIdOk() (*string, bool)`

GetResourceIdOk returns a tuple with the ResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceId

`func (o *GrantCreateIn) SetResourceId(v string)`

SetResourceId sets ResourceId field to given value.


### GetResourceType

`func (o *GrantCreateIn) GetResourceType() string`

GetResourceType returns the ResourceType field if non-nil, zero value otherwise.

### GetResourceTypeOk

`func (o *GrantCreateIn) GetResourceTypeOk() (*string, bool)`

GetResourceTypeOk returns a tuple with the ResourceType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceType

`func (o *GrantCreateIn) SetResourceType(v string)`

SetResourceType sets ResourceType field to given value.


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
