# GrantOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAt** | **time.Time** |  |
**DriveId** | **string** |  |
**ExpiresAt** | **NullableTime** |  |
**Id** | **string** |  |
**PrincipalId** | **NullableString** |  |
**PrincipalType** | **string** |  |
**ResourceId** | **string** |  |
**ResourceType** | **string** |  |
**Revision** | **string** |  |
**RevokedAt** | **NullableTime** |  |
**Role** | **string** |  |
**State** | **string** |  |

## Methods

### NewGrantOut

`func NewGrantOut(createdAt time.Time, driveId string, expiresAt NullableTime, id string, principalId NullableString, principalType string, resourceId string, resourceType string, revision string, revokedAt NullableTime, role string, state string, ) *GrantOut`

NewGrantOut instantiates a new GrantOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGrantOutWithDefaults

`func NewGrantOutWithDefaults() *GrantOut`

NewGrantOutWithDefaults instantiates a new GrantOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

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


### GetDriveId

`func (o *GrantOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *GrantOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *GrantOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


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


### SetExpiresAtNil

`func (o *GrantOut) SetExpiresAtNil(b bool)`

 SetExpiresAtNil sets the value for ExpiresAt to be an explicit nil

### UnsetExpiresAt
`func (o *GrantOut) UnsetExpiresAt()`

UnsetExpiresAt ensures that no value is present for ExpiresAt, not even an explicit nil
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


### GetRevision

`func (o *GrantOut) GetRevision() string`

GetRevision returns the Revision field if non-nil, zero value otherwise.

### GetRevisionOk

`func (o *GrantOut) GetRevisionOk() (*string, bool)`

GetRevisionOk returns a tuple with the Revision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevision

`func (o *GrantOut) SetRevision(v string)`

SetRevision sets Revision field to given value.


### GetRevokedAt

`func (o *GrantOut) GetRevokedAt() time.Time`

GetRevokedAt returns the RevokedAt field if non-nil, zero value otherwise.

### GetRevokedAtOk

`func (o *GrantOut) GetRevokedAtOk() (*time.Time, bool)`

GetRevokedAtOk returns a tuple with the RevokedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevokedAt

`func (o *GrantOut) SetRevokedAt(v time.Time)`

SetRevokedAt sets RevokedAt field to given value.


### SetRevokedAtNil

`func (o *GrantOut) SetRevokedAtNil(b bool)`

 SetRevokedAtNil sets the value for RevokedAt to be an explicit nil

### UnsetRevokedAt
`func (o *GrantOut) UnsetRevokedAt()`

UnsetRevokedAt ensures that no value is present for RevokedAt, not even an explicit nil
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


### GetState

`func (o *GrantOut) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *GrantOut) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *GrantOut) SetState(v string)`

SetState sets State field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
