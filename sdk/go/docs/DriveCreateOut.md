# DriveCreateOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Name** | **string** |  | 
**OrganizationId** | **string** |  | 
**OwnerUserId** | Pointer to **NullableString** |  | [optional] 
**OwnerEmail** | Pointer to **NullableString** |  | [optional] 
**StorageBytes** | **int32** |  | 
**CreatedAt** | **time.Time** |  | 
**ApiKey** | **string** |  | 

## Methods

### NewDriveCreateOut

`func NewDriveCreateOut(id string, name string, organizationId string, storageBytes int32, createdAt time.Time, apiKey string, ) *DriveCreateOut`

NewDriveCreateOut instantiates a new DriveCreateOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDriveCreateOutWithDefaults

`func NewDriveCreateOutWithDefaults() *DriveCreateOut`

NewDriveCreateOutWithDefaults instantiates a new DriveCreateOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *DriveCreateOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DriveCreateOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DriveCreateOut) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *DriveCreateOut) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *DriveCreateOut) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *DriveCreateOut) SetName(v string)`

SetName sets Name field to given value.


### GetOrganizationId

`func (o *DriveCreateOut) GetOrganizationId() string`

GetOrganizationId returns the OrganizationId field if non-nil, zero value otherwise.

### GetOrganizationIdOk

`func (o *DriveCreateOut) GetOrganizationIdOk() (*string, bool)`

GetOrganizationIdOk returns a tuple with the OrganizationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganizationId

`func (o *DriveCreateOut) SetOrganizationId(v string)`

SetOrganizationId sets OrganizationId field to given value.


### GetOwnerUserId

`func (o *DriveCreateOut) GetOwnerUserId() string`

GetOwnerUserId returns the OwnerUserId field if non-nil, zero value otherwise.

### GetOwnerUserIdOk

`func (o *DriveCreateOut) GetOwnerUserIdOk() (*string, bool)`

GetOwnerUserIdOk returns a tuple with the OwnerUserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwnerUserId

`func (o *DriveCreateOut) SetOwnerUserId(v string)`

SetOwnerUserId sets OwnerUserId field to given value.

### HasOwnerUserId

`func (o *DriveCreateOut) HasOwnerUserId() bool`

HasOwnerUserId returns a boolean if a field has been set.

### SetOwnerUserIdNil

`func (o *DriveCreateOut) SetOwnerUserIdNil(b bool)`

 SetOwnerUserIdNil sets the value for OwnerUserId to be an explicit nil

### UnsetOwnerUserId
`func (o *DriveCreateOut) UnsetOwnerUserId()`

UnsetOwnerUserId ensures that no value is present for OwnerUserId, not even an explicit nil
### GetOwnerEmail

`func (o *DriveCreateOut) GetOwnerEmail() string`

GetOwnerEmail returns the OwnerEmail field if non-nil, zero value otherwise.

### GetOwnerEmailOk

`func (o *DriveCreateOut) GetOwnerEmailOk() (*string, bool)`

GetOwnerEmailOk returns a tuple with the OwnerEmail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwnerEmail

`func (o *DriveCreateOut) SetOwnerEmail(v string)`

SetOwnerEmail sets OwnerEmail field to given value.

### HasOwnerEmail

`func (o *DriveCreateOut) HasOwnerEmail() bool`

HasOwnerEmail returns a boolean if a field has been set.

### SetOwnerEmailNil

`func (o *DriveCreateOut) SetOwnerEmailNil(b bool)`

 SetOwnerEmailNil sets the value for OwnerEmail to be an explicit nil

### UnsetOwnerEmail
`func (o *DriveCreateOut) UnsetOwnerEmail()`

UnsetOwnerEmail ensures that no value is present for OwnerEmail, not even an explicit nil
### GetStorageBytes

`func (o *DriveCreateOut) GetStorageBytes() int32`

GetStorageBytes returns the StorageBytes field if non-nil, zero value otherwise.

### GetStorageBytesOk

`func (o *DriveCreateOut) GetStorageBytesOk() (*int32, bool)`

GetStorageBytesOk returns a tuple with the StorageBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStorageBytes

`func (o *DriveCreateOut) SetStorageBytes(v int32)`

SetStorageBytes sets StorageBytes field to given value.


### GetCreatedAt

`func (o *DriveCreateOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *DriveCreateOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *DriveCreateOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetApiKey

`func (o *DriveCreateOut) GetApiKey() string`

GetApiKey returns the ApiKey field if non-nil, zero value otherwise.

### GetApiKeyOk

`func (o *DriveCreateOut) GetApiKeyOk() (*string, bool)`

GetApiKeyOk returns a tuple with the ApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApiKey

`func (o *DriveCreateOut) SetApiKey(v string)`

SetApiKey sets ApiKey field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


