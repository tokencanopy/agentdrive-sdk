# DriveApiKeyOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Prefix** | **string** |  | 
**Label** | **NullableString** |  | 
**LastUsedAt** | **NullableTime** |  | 
**CreatedAt** | **time.Time** |  | 
**RevokedAt** | **NullableTime** |  | 

## Methods

### NewDriveApiKeyOut

`func NewDriveApiKeyOut(id string, prefix string, label NullableString, lastUsedAt NullableTime, createdAt time.Time, revokedAt NullableTime, ) *DriveApiKeyOut`

NewDriveApiKeyOut instantiates a new DriveApiKeyOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDriveApiKeyOutWithDefaults

`func NewDriveApiKeyOutWithDefaults() *DriveApiKeyOut`

NewDriveApiKeyOutWithDefaults instantiates a new DriveApiKeyOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *DriveApiKeyOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DriveApiKeyOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DriveApiKeyOut) SetId(v string)`

SetId sets Id field to given value.


### GetPrefix

`func (o *DriveApiKeyOut) GetPrefix() string`

GetPrefix returns the Prefix field if non-nil, zero value otherwise.

### GetPrefixOk

`func (o *DriveApiKeyOut) GetPrefixOk() (*string, bool)`

GetPrefixOk returns a tuple with the Prefix field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrefix

`func (o *DriveApiKeyOut) SetPrefix(v string)`

SetPrefix sets Prefix field to given value.


### GetLabel

`func (o *DriveApiKeyOut) GetLabel() string`

GetLabel returns the Label field if non-nil, zero value otherwise.

### GetLabelOk

`func (o *DriveApiKeyOut) GetLabelOk() (*string, bool)`

GetLabelOk returns a tuple with the Label field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabel

`func (o *DriveApiKeyOut) SetLabel(v string)`

SetLabel sets Label field to given value.


### SetLabelNil

`func (o *DriveApiKeyOut) SetLabelNil(b bool)`

 SetLabelNil sets the value for Label to be an explicit nil

### UnsetLabel
`func (o *DriveApiKeyOut) UnsetLabel()`

UnsetLabel ensures that no value is present for Label, not even an explicit nil
### GetLastUsedAt

`func (o *DriveApiKeyOut) GetLastUsedAt() time.Time`

GetLastUsedAt returns the LastUsedAt field if non-nil, zero value otherwise.

### GetLastUsedAtOk

`func (o *DriveApiKeyOut) GetLastUsedAtOk() (*time.Time, bool)`

GetLastUsedAtOk returns a tuple with the LastUsedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUsedAt

`func (o *DriveApiKeyOut) SetLastUsedAt(v time.Time)`

SetLastUsedAt sets LastUsedAt field to given value.


### SetLastUsedAtNil

`func (o *DriveApiKeyOut) SetLastUsedAtNil(b bool)`

 SetLastUsedAtNil sets the value for LastUsedAt to be an explicit nil

### UnsetLastUsedAt
`func (o *DriveApiKeyOut) UnsetLastUsedAt()`

UnsetLastUsedAt ensures that no value is present for LastUsedAt, not even an explicit nil
### GetCreatedAt

`func (o *DriveApiKeyOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *DriveApiKeyOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *DriveApiKeyOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetRevokedAt

`func (o *DriveApiKeyOut) GetRevokedAt() time.Time`

GetRevokedAt returns the RevokedAt field if non-nil, zero value otherwise.

### GetRevokedAtOk

`func (o *DriveApiKeyOut) GetRevokedAtOk() (*time.Time, bool)`

GetRevokedAtOk returns a tuple with the RevokedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevokedAt

`func (o *DriveApiKeyOut) SetRevokedAt(v time.Time)`

SetRevokedAt sets RevokedAt field to given value.


### SetRevokedAtNil

`func (o *DriveApiKeyOut) SetRevokedAtNil(b bool)`

 SetRevokedAtNil sets the value for RevokedAt to be an explicit nil

### UnsetRevokedAt
`func (o *DriveApiKeyOut) UnsetRevokedAt()`

UnsetRevokedAt ensures that no value is present for RevokedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


