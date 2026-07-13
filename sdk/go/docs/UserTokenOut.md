# UserTokenOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Prefix** | **string** |  | 
**Label** | Pointer to **NullableString** |  | [optional] 
**Scope** | **string** |  | 
**DefaultDriveId** | Pointer to **NullableString** |  | [optional] 
**LastUsedAt** | Pointer to **NullableTime** |  | [optional] 
**ExpiresAt** | Pointer to **NullableTime** |  | [optional] 
**CreatedAt** | **time.Time** |  | 
**RevokedAt** | Pointer to **NullableTime** |  | [optional] 

## Methods

### NewUserTokenOut

`func NewUserTokenOut(id string, prefix string, scope string, createdAt time.Time, ) *UserTokenOut`

NewUserTokenOut instantiates a new UserTokenOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserTokenOutWithDefaults

`func NewUserTokenOutWithDefaults() *UserTokenOut`

NewUserTokenOutWithDefaults instantiates a new UserTokenOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UserTokenOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UserTokenOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UserTokenOut) SetId(v string)`

SetId sets Id field to given value.


### GetPrefix

`func (o *UserTokenOut) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *UserTokenOut) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *UserTokenOut) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.


### GetLabel

`func (o *UserTokenOut) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *UserTokenOut) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *UserTokenOut) SetLabel(v string)`

SetLabel sets Label field to given value.

### HasLabel

`func (o *UserTokenOut) HasLabel() bool`

HasLabel returns a boolean if a field has been set.

### SetLabelNil

`func (o *UserTokenOut) SetLabelNil(b bool)`

 SetLabelNil sets the value for Label to be an explicit nil

### UnsetLabel
`func (o *UserTokenOut) UnsetLabel()`

UnsetLabel ensures that no value is present for Label, not even an explicit nil
### GetScope

`func (o *UserTokenOut) GetScope() string`

GetScope returns the Scope field if non-nil, zero value otherwise.

### GetScopeOk

`func (o *UserTokenOut) GetScopeOk() (*string, bool)`

GetScopeOk returns a tuple with the Scope field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScope

`func (o *UserTokenOut) SetScope(v string)`

SetScope sets Scope field to given value.


### GetDefaultDriveId

`func (o *UserTokenOut) GetDefaultDriveId() string`

GetDefaultDriveId returns the DefaultDriveId field if non-nil, zero value otherwise.

### GetDefaultDriveIdOk

`func (o *UserTokenOut) GetDefaultDriveIdOk() (*string, bool)`

GetDefaultDriveIdOk returns a tuple with the DefaultDriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultDriveId

`func (o *UserTokenOut) SetDefaultDriveId(v string)`

SetDefaultDriveId sets DefaultDriveId field to given value.

### HasDefaultDriveId

`func (o *UserTokenOut) HasDefaultDriveId() bool`

HasDefaultDriveId returns a boolean if a field has been set.

### SetDefaultDriveIdNil

`func (o *UserTokenOut) SetDefaultDriveIdNil(b bool)`

 SetDefaultDriveIdNil sets the value for DefaultDriveId to be an explicit nil

### UnsetDefaultDriveId
`func (o *UserTokenOut) UnsetDefaultDriveId()`

UnsetDefaultDriveId ensures that no value is present for DefaultDriveId, not even an explicit nil
### GetLastUsedAt

`func (o *UserTokenOut) GetLastUsedAt() time.Time`

GetLastUsedAt returns the LastUsedAt field if non-nil, zero value otherwise.

### GetLastUsedAtOk

`func (o *UserTokenOut) GetLastUsedAtOk() (*time.Time, bool)`

GetLastUsedAtOk returns a tuple with the LastUsedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUsedAt

`func (o *UserTokenOut) SetLastUsedAt(v time.Time)`

SetLastUsedAt sets LastUsedAt field to given value.

### HasLastUsedAt

`func (o *UserTokenOut) HasLastUsedAt() bool`

HasLastUsedAt returns a boolean if a field has been set.

### SetLastUsedAtNil

`func (o *UserTokenOut) SetLastUsedAtNil(b bool)`

 SetLastUsedAtNil sets the value for LastUsedAt to be an explicit nil

### UnsetLastUsedAt
`func (o *UserTokenOut) UnsetLastUsedAt()`

UnsetLastUsedAt ensures that no value is present for LastUsedAt, not even an explicit nil
### GetExpiresAt

`func (o *UserTokenOut) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *UserTokenOut) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *UserTokenOut) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.

### HasExpiresAt

`func (o *UserTokenOut) HasExpiresAt() bool`

HasExpiresAt returns a boolean if a field has been set.

### SetExpiresAtNil

`func (o *UserTokenOut) SetExpiresAtNil(b bool)`

 SetExpiresAtNil sets the value for ExpiresAt to be an explicit nil

### UnsetExpiresAt
`func (o *UserTokenOut) UnsetExpiresAt()`

UnsetExpiresAt ensures that no value is present for ExpiresAt, not even an explicit nil
### GetCreatedAt

`func (o *UserTokenOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *UserTokenOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *UserTokenOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetRevokedAt

`func (o *UserTokenOut) GetRevokedAt() time.Time`

GetRevokedAt returns the RevokedAt field if non-nil, zero value otherwise.

### GetRevokedAtOk

`func (o *UserTokenOut) GetRevokedAtOk() (*time.Time, bool)`

GetRevokedAtOk returns a tuple with the RevokedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevokedAt

`func (o *UserTokenOut) SetRevokedAt(v time.Time)`

SetRevokedAt sets RevokedAt field to given value.

### HasRevokedAt

`func (o *UserTokenOut) HasRevokedAt() bool`

HasRevokedAt returns a boolean if a field has been set.

### SetRevokedAtNil

`func (o *UserTokenOut) SetRevokedAtNil(b bool)`

 SetRevokedAtNil sets the value for RevokedAt to be an explicit nil

### UnsetRevokedAt
`func (o *UserTokenOut) UnsetRevokedAt()`

UnsetRevokedAt ensures that no value is present for RevokedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


