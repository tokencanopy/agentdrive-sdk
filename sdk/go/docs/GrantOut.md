# GrantOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ArtifactsAffected** | Pointer to **NullableInt32** |  | [optional]
**CreatedAt** | **time.Time** |  |
**ExpiresAt** | Pointer to **NullableTime** |  | [optional]
**GrantedById** | **string** |  |
**GrantedByType** | **string** |  |
**Id** | **string** |  |
**OnBehalfOf** | Pointer to **NullableString** |  | [optional]
**PrincipalEmail** | Pointer to **NullableString** |  | [optional]
**PrincipalId** | Pointer to **NullableString** |  | [optional]
**PrincipalType** | **string** |  |
**ResourceId** | **string** |  |
**ResourceType** | **string** |  |
**Role** | **string** |  |

## Methods

### NewGrantOut

`func NewGrantOut(createdAt time.Time, grantedById string, grantedByType string, id string, principalType string, resourceId string, resourceType string, role string, ) *GrantOut`

NewGrantOut instantiates a new GrantOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGrantOutWithDefaults

`func NewGrantOutWithDefaults() *GrantOut`

NewGrantOutWithDefaults instantiates a new GrantOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetArtifactsAffected

`func (o *GrantOut) GetArtifactsAffected() int32`

GetArtifactsAffected returns the ArtifactsAffected field if non-nil, zero value otherwise.

### GetArtifactsAffectedOk

`func (o *GrantOut) GetArtifactsAffectedOk() (*int32, bool)`

GetArtifactsAffectedOk returns a tuple with the ArtifactsAffected field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtifactsAffected

`func (o *GrantOut) SetArtifactsAffected(v int32)`

SetArtifactsAffected sets ArtifactsAffected field to given value.

### HasArtifactsAffected

`func (o *GrantOut) HasArtifactsAffected() bool`

HasArtifactsAffected returns a boolean if a field has been set.

### SetArtifactsAffectedNil

`func (o *GrantOut) SetArtifactsAffectedNil(b bool)`

 SetArtifactsAffectedNil sets the value for ArtifactsAffected to be an explicit nil

### UnsetArtifactsAffected
`func (o *GrantOut) UnsetArtifactsAffected()`

UnsetArtifactsAffected ensures that no value is present for ArtifactsAffected, not even an explicit nil
### GetCreatedAt

`func (o *GrantOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *GrantOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *GrantOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetExpiresAt

`func (o *GrantOut) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *GrantOut) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *GrantOut) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.

### HasExpiresAt

`func (o *GrantOut) HasExpiresAt() bool`

HasExpiresAt returns a boolean if a field has been set.

### SetExpiresAtNil

`func (o *GrantOut) SetExpiresAtNil(b bool)`

 SetExpiresAtNil sets the value for ExpiresAt to be an explicit nil

### UnsetExpiresAt
`func (o *GrantOut) UnsetExpiresAt()`

UnsetExpiresAt ensures that no value is present for ExpiresAt, not even an explicit nil
### GetGrantedById

`func (o *GrantOut) GetGrantedById() string`

GetGrantedById returns the GrantedById field if non-nil, zero value otherwise.

### GetGrantedByIdOk

`func (o *GrantOut) GetGrantedByIdOk() (*string, bool)`

GetGrantedByIdOk returns a tuple with the GrantedById field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantedById

`func (o *GrantOut) SetGrantedById(v string)`

SetGrantedById sets GrantedById field to given value.


### GetGrantedByType

`func (o *GrantOut) GetGrantedByType() string`

GetGrantedByType returns the GrantedByType field if non-nil, zero value otherwise.

### GetGrantedByTypeOk

`func (o *GrantOut) GetGrantedByTypeOk() (*string, bool)`

GetGrantedByTypeOk returns a tuple with the GrantedByType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantedByType

`func (o *GrantOut) SetGrantedByType(v string)`

SetGrantedByType sets GrantedByType field to given value.


### GetId

`func (o *GrantOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *GrantOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *GrantOut) SetId(v string)`

SetId sets Id field to given value.


### GetOnBehalfOf

`func (o *GrantOut) GetOnBehalfOf() string`

GetOnBehalfOf returns the OnBehalfOf field if non-nil, zero value otherwise.

### GetOnBehalfOfOk

`func (o *GrantOut) GetOnBehalfOfOk() (*string, bool)`

GetOnBehalfOfOk returns a tuple with the OnBehalfOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOnBehalfOf

`func (o *GrantOut) SetOnBehalfOf(v string)`

SetOnBehalfOf sets OnBehalfOf field to given value.

### HasOnBehalfOf

`func (o *GrantOut) HasOnBehalfOf() bool`

HasOnBehalfOf returns a boolean if a field has been set.

### SetOnBehalfOfNil

`func (o *GrantOut) SetOnBehalfOfNil(b bool)`

 SetOnBehalfOfNil sets the value for OnBehalfOf to be an explicit nil

### UnsetOnBehalfOf
`func (o *GrantOut) UnsetOnBehalfOf()`

UnsetOnBehalfOf ensures that no value is present for OnBehalfOf, not even an explicit nil
### GetPrincipalEmail

`func (o *GrantOut) GetPrincipalEmail() string`

GetPrincipalEmail returns the PrincipalEmail field if non-nil, zero value otherwise.

### GetPrincipalEmailOk

`func (o *GrantOut) GetPrincipalEmailOk() (*string, bool)`

GetPrincipalEmailOk returns a tuple with the PrincipalEmail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrincipalEmail

`func (o *GrantOut) SetPrincipalEmail(v string)`

SetPrincipalEmail sets PrincipalEmail field to given value.

### HasPrincipalEmail

`func (o *GrantOut) HasPrincipalEmail() bool`

HasPrincipalEmail returns a boolean if a field has been set.

### SetPrincipalEmailNil

`func (o *GrantOut) SetPrincipalEmailNil(b bool)`

 SetPrincipalEmailNil sets the value for PrincipalEmail to be an explicit nil

### UnsetPrincipalEmail
`func (o *GrantOut) UnsetPrincipalEmail()`

UnsetPrincipalEmail ensures that no value is present for PrincipalEmail, not even an explicit nil
### GetPrincipalId

`func (o *GrantOut) GetPrincipalId() string`

GetPrincipalId returns the PrincipalId field if non-nil, zero value otherwise.

### GetPrincipalIdOk

`func (o *GrantOut) GetPrincipalIdOk() (*string, bool)`

GetPrincipalIdOk returns a tuple with the PrincipalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrincipalId

`func (o *GrantOut) SetPrincipalId(v string)`

SetPrincipalId sets PrincipalId field to given value.

### HasPrincipalId

`func (o *GrantOut) HasPrincipalId() bool`

HasPrincipalId returns a boolean if a field has been set.

### SetPrincipalIdNil

`func (o *GrantOut) SetPrincipalIdNil(b bool)`

 SetPrincipalIdNil sets the value for PrincipalId to be an explicit nil

### UnsetPrincipalId
`func (o *GrantOut) UnsetPrincipalId()`

UnsetPrincipalId ensures that no value is present for PrincipalId, not even an explicit nil
### GetPrincipalType

`func (o *GrantOut) GetPrincipalType() string`

GetPrincipalType returns the PrincipalType field if non-nil, zero value otherwise.

### GetPrincipalTypeOk

`func (o *GrantOut) GetPrincipalTypeOk() (*string, bool)`

GetPrincipalTypeOk returns a tuple with the PrincipalType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrincipalType

`func (o *GrantOut) SetPrincipalType(v string)`

SetPrincipalType sets PrincipalType field to given value.


### GetResourceId

`func (o *GrantOut) GetResourceId() string`

GetResourceId returns the ResourceId field if non-nil, zero value otherwise.

### GetResourceIdOk

`func (o *GrantOut) GetResourceIdOk() (*string, bool)`

GetResourceIdOk returns a tuple with the ResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceId

`func (o *GrantOut) SetResourceId(v string)`

SetResourceId sets ResourceId field to given value.


### GetResourceType

`func (o *GrantOut) GetResourceType() string`

GetResourceType returns the ResourceType field if non-nil, zero value otherwise.

### GetResourceTypeOk

`func (o *GrantOut) GetResourceTypeOk() (*string, bool)`

GetResourceTypeOk returns a tuple with the ResourceType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceType

`func (o *GrantOut) SetResourceType(v string)`

SetResourceType sets ResourceType field to given value.


### GetRole

`func (o *GrantOut) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *GrantOut) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *GrantOut) SetRole(v string)`

SetRole sets Role field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
