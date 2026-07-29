# DriveReadOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAt** | **time.Time** |  |
**Email** | Pointer to **NullableString** |  | [optional]
**Etag** | **string** |  |
**Id** | **string** |  |
**Metageneration** | **int32** |  |
**OrganizationId** | **string** |  |
**StorageBytes** | **int32** |  |
**StorageLimit** | **int32** |  |

## Methods

### NewDriveReadOut

`func NewDriveReadOut(createdAt time.Time, etag string, id string, metageneration int32, organizationId string, storageBytes int32, storageLimit int32, ) *DriveReadOut`

NewDriveReadOut instantiates a new DriveReadOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDriveReadOutWithDefaults

`func NewDriveReadOutWithDefaults() *DriveReadOut`

NewDriveReadOutWithDefaults instantiates a new DriveReadOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreatedAt

`func (o *DriveReadOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *DriveReadOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *DriveReadOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetEmail

`func (o *DriveReadOut) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *DriveReadOut) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *DriveReadOut) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *DriveReadOut) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### SetEmailNil

`func (o *DriveReadOut) SetEmailNil(b bool)`

 SetEmailNil sets the value for Email to be an explicit nil

### UnsetEmail
`func (o *DriveReadOut) UnsetEmail()`

UnsetEmail ensures that no value is present for Email, not even an explicit nil
### GetEtag

`func (o *DriveReadOut) GetEtag() string`

GetEtag returns the Etag field if non-nil, zero value otherwise.

### GetEtagOk

`func (o *DriveReadOut) GetEtagOk() (*string, bool)`

GetEtagOk returns a tuple with the Etag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEtag

`func (o *DriveReadOut) SetEtag(v string)`

SetEtag sets Etag field to given value.


### GetId

`func (o *DriveReadOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DriveReadOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DriveReadOut) SetId(v string)`

SetId sets Id field to given value.


### GetMetageneration

`func (o *DriveReadOut) GetMetageneration() int32`

GetMetageneration returns the Metageneration field if non-nil, zero value otherwise.

### GetMetagenerationOk

`func (o *DriveReadOut) GetMetagenerationOk() (*int32, bool)`

GetMetagenerationOk returns a tuple with the Metageneration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetageneration

`func (o *DriveReadOut) SetMetageneration(v int32)`

SetMetageneration sets Metageneration field to given value.


### GetOrganizationId

`func (o *DriveReadOut) GetOrganizationId() string`

GetOrganizationId returns the OrganizationId field if non-nil, zero value otherwise.

### GetOrganizationIdOk

`func (o *DriveReadOut) GetOrganizationIdOk() (*string, bool)`

GetOrganizationIdOk returns a tuple with the OrganizationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganizationId

`func (o *DriveReadOut) SetOrganizationId(v string)`

SetOrganizationId sets OrganizationId field to given value.


### GetStorageBytes

`func (o *DriveReadOut) GetStorageBytes() int32`

GetStorageBytes returns the StorageBytes field if non-nil, zero value otherwise.

### GetStorageBytesOk

`func (o *DriveReadOut) GetStorageBytesOk() (*int32, bool)`

GetStorageBytesOk returns a tuple with the StorageBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStorageBytes

`func (o *DriveReadOut) SetStorageBytes(v int32)`

SetStorageBytes sets StorageBytes field to given value.


### GetStorageLimit

`func (o *DriveReadOut) GetStorageLimit() int32`

GetStorageLimit returns the StorageLimit field if non-nil, zero value otherwise.

### GetStorageLimitOk

`func (o *DriveReadOut) GetStorageLimitOk() (*int32, bool)`

GetStorageLimitOk returns a tuple with the StorageLimit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStorageLimit

`func (o *DriveReadOut) SetStorageLimit(v int32)`

SetStorageLimit sets StorageLimit field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
