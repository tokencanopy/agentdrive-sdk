# ShareCreateOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAt** | **time.Time** |  |
**CreatedBy** | **NullableString** |  |
**DriveId** | **string** |  |
**ExpiresAt** | **NullableTime** |  |
**Id** | **string** |  |
**ResourceId** | **string** |  |
**ResourceType** | **string** |  |
**Revision** | **string** |  |
**RevokedAt** | **NullableTime** |  |
**RotatedAt** | **NullableTime** |  |
**Secret** | Pointer to **NullableString** | Plaintext share secret. Present only on first execution of a create or rotate; null on idempotent replay — rotate to obtain a new secret. | [optional]
**State** | **string** |  |

## Methods

### NewShareCreateOut

`func NewShareCreateOut(createdAt time.Time, createdBy NullableString, driveId string, expiresAt NullableTime, id string, resourceId string, resourceType string, revision string, revokedAt NullableTime, rotatedAt NullableTime, state string, ) *ShareCreateOut`

NewShareCreateOut instantiates a new ShareCreateOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewShareCreateOutWithDefaults

`func NewShareCreateOutWithDefaults() *ShareCreateOut`

NewShareCreateOutWithDefaults instantiates a new ShareCreateOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreatedAt

`func (o *ShareCreateOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ShareCreateOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ShareCreateOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetCreatedBy

`func (o *ShareCreateOut) GetCreatedBy() string`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *ShareCreateOut) GetCreatedByOk() (*string, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *ShareCreateOut) SetCreatedBy(v string)`

SetCreatedBy sets CreatedBy field to given value.


### SetCreatedByNil

`func (o *ShareCreateOut) SetCreatedByNil(b bool)`

 SetCreatedByNil sets the value for CreatedBy to be an explicit nil

### UnsetCreatedBy
`func (o *ShareCreateOut) UnsetCreatedBy()`

UnsetCreatedBy ensures that no value is present for CreatedBy, not even an explicit nil
### GetDriveId

`func (o *ShareCreateOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *ShareCreateOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *ShareCreateOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetExpiresAt

`func (o *ShareCreateOut) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *ShareCreateOut) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *ShareCreateOut) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### SetExpiresAtNil

`func (o *ShareCreateOut) SetExpiresAtNil(b bool)`

 SetExpiresAtNil sets the value for ExpiresAt to be an explicit nil

### UnsetExpiresAt
`func (o *ShareCreateOut) UnsetExpiresAt()`

UnsetExpiresAt ensures that no value is present for ExpiresAt, not even an explicit nil
### GetId

`func (o *ShareCreateOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ShareCreateOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ShareCreateOut) SetId(v string)`

SetId sets Id field to given value.


### GetResourceId

`func (o *ShareCreateOut) GetResourceId() string`

GetResourceId returns the ResourceId field if non-nil, zero value otherwise.

### GetResourceIdOk

`func (o *ShareCreateOut) GetResourceIdOk() (*string, bool)`

GetResourceIdOk returns a tuple with the ResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceId

`func (o *ShareCreateOut) SetResourceId(v string)`

SetResourceId sets ResourceId field to given value.


### GetResourceType

`func (o *ShareCreateOut) GetResourceType() string`

GetResourceType returns the ResourceType field if non-nil, zero value otherwise.

### GetResourceTypeOk

`func (o *ShareCreateOut) GetResourceTypeOk() (*string, bool)`

GetResourceTypeOk returns a tuple with the ResourceType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceType

`func (o *ShareCreateOut) SetResourceType(v string)`

SetResourceType sets ResourceType field to given value.


### GetRevision

`func (o *ShareCreateOut) GetRevision() string`

GetRevision returns the Revision field if non-nil, zero value otherwise.

### GetRevisionOk

`func (o *ShareCreateOut) GetRevisionOk() (*string, bool)`

GetRevisionOk returns a tuple with the Revision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevision

`func (o *ShareCreateOut) SetRevision(v string)`

SetRevision sets Revision field to given value.


### GetRevokedAt

`func (o *ShareCreateOut) GetRevokedAt() time.Time`

GetRevokedAt returns the RevokedAt field if non-nil, zero value otherwise.

### GetRevokedAtOk

`func (o *ShareCreateOut) GetRevokedAtOk() (*time.Time, bool)`

GetRevokedAtOk returns a tuple with the RevokedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevokedAt

`func (o *ShareCreateOut) SetRevokedAt(v time.Time)`

SetRevokedAt sets RevokedAt field to given value.


### SetRevokedAtNil

`func (o *ShareCreateOut) SetRevokedAtNil(b bool)`

 SetRevokedAtNil sets the value for RevokedAt to be an explicit nil

### UnsetRevokedAt
`func (o *ShareCreateOut) UnsetRevokedAt()`

UnsetRevokedAt ensures that no value is present for RevokedAt, not even an explicit nil
### GetRotatedAt

`func (o *ShareCreateOut) GetRotatedAt() time.Time`

GetRotatedAt returns the RotatedAt field if non-nil, zero value otherwise.

### GetRotatedAtOk

`func (o *ShareCreateOut) GetRotatedAtOk() (*time.Time, bool)`

GetRotatedAtOk returns a tuple with the RotatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRotatedAt

`func (o *ShareCreateOut) SetRotatedAt(v time.Time)`

SetRotatedAt sets RotatedAt field to given value.


### SetRotatedAtNil

`func (o *ShareCreateOut) SetRotatedAtNil(b bool)`

 SetRotatedAtNil sets the value for RotatedAt to be an explicit nil

### UnsetRotatedAt
`func (o *ShareCreateOut) UnsetRotatedAt()`

UnsetRotatedAt ensures that no value is present for RotatedAt, not even an explicit nil
### GetSecret

`func (o *ShareCreateOut) GetSecret() string`

GetSecret returns the Secret field if non-nil, zero value otherwise.

### GetSecretOk

`func (o *ShareCreateOut) GetSecretOk() (*string, bool)`

GetSecretOk returns a tuple with the Secret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecret

`func (o *ShareCreateOut) SetSecret(v string)`

SetSecret sets Secret field to given value.

### HasSecret

`func (o *ShareCreateOut) HasSecret() bool`

HasSecret returns a boolean if a field has been set.

### SetSecretNil

`func (o *ShareCreateOut) SetSecretNil(b bool)`

 SetSecretNil sets the value for Secret to be an explicit nil

### UnsetSecret
`func (o *ShareCreateOut) UnsetSecret()`

UnsetSecret ensures that no value is present for Secret, not even an explicit nil
### GetState

`func (o *ShareCreateOut) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *ShareCreateOut) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *ShareCreateOut) SetState(v string)`

SetState sets State field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
