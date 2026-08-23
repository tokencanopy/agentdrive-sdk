# FolderOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAt** | **time.Time** |  |
**DeletedAt** | **NullableTime** |  |
**DriveId** | **string** |  |
**Id** | **string** |  |
**Metadata** | **map[string]interface{}** |  |
**Name** | **NullableString** |  |
**ParentId** | **NullableString** |  |
**Revision** | **string** |  |
**State** | **string** |  |
**UpdatedAt** | **time.Time** |  |

## Methods

### NewFolderOut

`func NewFolderOut(createdAt time.Time, deletedAt NullableTime, driveId string, id string, metadata map[string]interface{}, name NullableString, parentId NullableString, revision string, state string, updatedAt time.Time, ) *FolderOut`

NewFolderOut instantiates a new FolderOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFolderOutWithDefaults

`func NewFolderOutWithDefaults() *FolderOut`

NewFolderOutWithDefaults instantiates a new FolderOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreatedAt

`func (o *FolderOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *FolderOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *FolderOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetDeletedAt

`func (o *FolderOut) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *FolderOut) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *FolderOut) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.


### SetDeletedAtNil

`func (o *FolderOut) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *FolderOut) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil
### GetDriveId

`func (o *FolderOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *FolderOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *FolderOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetId

`func (o *FolderOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FolderOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FolderOut) SetId(v string)`

SetId sets Id field to given value.


### GetMetadata

`func (o *FolderOut) GetMetadata() map[string]interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *FolderOut) GetMetadataOk() (*map[string]interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *FolderOut) SetMetadata(v map[string]interface{})`

SetMetadata sets Metadata field to given value.


### GetName

`func (o *FolderOut) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *FolderOut) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *FolderOut) SetName(v string)`

SetName sets Name field to given value.


### SetNameNil

`func (o *FolderOut) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *FolderOut) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetParentId

`func (o *FolderOut) GetParentId() string`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *FolderOut) GetParentIdOk() (*string, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *FolderOut) SetParentId(v string)`

SetParentId sets ParentId field to given value.


### SetParentIdNil

`func (o *FolderOut) SetParentIdNil(b bool)`

 SetParentIdNil sets the value for ParentId to be an explicit nil

### UnsetParentId
`func (o *FolderOut) UnsetParentId()`

UnsetParentId ensures that no value is present for ParentId, not even an explicit nil
### GetRevision

`func (o *FolderOut) GetRevision() string`

GetRevision returns the Revision field if non-nil, zero value otherwise.

### GetRevisionOk

`func (o *FolderOut) GetRevisionOk() (*string, bool)`

GetRevisionOk returns a tuple with the Revision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevision

`func (o *FolderOut) SetRevision(v string)`

SetRevision sets Revision field to given value.


### GetState

`func (o *FolderOut) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *FolderOut) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *FolderOut) SetState(v string)`

SetState sets State field to given value.


### GetUpdatedAt

`func (o *FolderOut) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *FolderOut) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *FolderOut) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
