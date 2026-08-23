# GrantUpdateIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExpiresAt** | Pointer to **NullableTime** |  | [optional]
**Role** | Pointer to **NullableString** |  | [optional]

## Methods

### NewGrantUpdateIn

`func NewGrantUpdateIn() *GrantUpdateIn`

NewGrantUpdateIn instantiates a new GrantUpdateIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGrantUpdateInWithDefaults

`func NewGrantUpdateInWithDefaults() *GrantUpdateIn`

NewGrantUpdateInWithDefaults instantiates a new GrantUpdateIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetExpiresAt

`func (o *GrantUpdateIn) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *GrantUpdateIn) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *GrantUpdateIn) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.

### HasExpiresAt

`func (o *GrantUpdateIn) HasExpiresAt() bool`

HasExpiresAt returns a boolean if a field has been set.

### SetExpiresAtNil

`func (o *GrantUpdateIn) SetExpiresAtNil(b bool)`

 SetExpiresAtNil sets the value for ExpiresAt to be an explicit nil

### UnsetExpiresAt
`func (o *GrantUpdateIn) UnsetExpiresAt()`

UnsetExpiresAt ensures that no value is present for ExpiresAt, not even an explicit nil
### GetRole

`func (o *GrantUpdateIn) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *GrantUpdateIn) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *GrantUpdateIn) SetRole(v string)`

SetRole sets Role field to given value.

### HasRole

`func (o *GrantUpdateIn) HasRole() bool`

HasRole returns a boolean if a field has been set.

### SetRoleNil

`func (o *GrantUpdateIn) SetRoleNil(b bool)`

 SetRoleNil sets the value for Role to be an explicit nil

### UnsetRole
`func (o *GrantUpdateIn) UnsetRole()`

UnsetRole ensures that no value is present for Role, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
