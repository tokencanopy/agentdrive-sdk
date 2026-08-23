# EntriesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DeletedAt** | **NullableTime** |  |
**Id** | **string** |  |
**Name** | **string** |  |
**Revision** | **string** |  |
**State** | **string** |  |
**Type** | **string** |  |
**UpdatedAt** | **time.Time** |  |
**ContentType** | **NullableString** |  |
**HeadVersionId** | **NullableString** |  |
**SizeBytes** | **int32** |  |

## Methods

### NewEntriesInner

`func NewEntriesInner(deletedAt NullableTime, id string, name string, revision string, state string, type_ string, updatedAt time.Time, contentType NullableString, headVersionId NullableString, sizeBytes int32, ) *EntriesInner`

NewEntriesInner instantiates a new EntriesInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEntriesInnerWithDefaults

`func NewEntriesInnerWithDefaults() *EntriesInner`

NewEntriesInnerWithDefaults instantiates a new EntriesInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDeletedAt

`func (o *EntriesInner) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *EntriesInner) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *EntriesInner) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.


### SetDeletedAtNil

`func (o *EntriesInner) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *EntriesInner) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil
### GetId

`func (o *EntriesInner) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *EntriesInner) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *EntriesInner) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *EntriesInner) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *EntriesInner) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *EntriesInner) SetName(v string)`

SetName sets Name field to given value.


### GetRevision

`func (o *EntriesInner) GetRevision() string`

GetRevision returns the Revision field if non-nil, zero value otherwise.

### GetRevisionOk

`func (o *EntriesInner) GetRevisionOk() (*string, bool)`

GetRevisionOk returns a tuple with the Revision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevision

`func (o *EntriesInner) SetRevision(v string)`

SetRevision sets Revision field to given value.


### GetState

`func (o *EntriesInner) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *EntriesInner) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *EntriesInner) SetState(v string)`

SetState sets State field to given value.


### GetType

`func (o *EntriesInner) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *EntriesInner) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *EntriesInner) SetType(v string)`

SetType sets Type field to given value.


### GetUpdatedAt

`func (o *EntriesInner) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *EntriesInner) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *EntriesInner) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetContentType

`func (o *EntriesInner) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *EntriesInner) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *EntriesInner) SetContentType(v string)`

SetContentType sets ContentType field to given value.


### SetContentTypeNil

`func (o *EntriesInner) SetContentTypeNil(b bool)`

 SetContentTypeNil sets the value for ContentType to be an explicit nil

### UnsetContentType
`func (o *EntriesInner) UnsetContentType()`

UnsetContentType ensures that no value is present for ContentType, not even an explicit nil
### GetHeadVersionId

`func (o *EntriesInner) GetHeadVersionId() string`

GetHeadVersionId returns the HeadVersionId field if non-nil, zero value otherwise.

### GetHeadVersionIdOk

`func (o *EntriesInner) GetHeadVersionIdOk() (*string, bool)`

GetHeadVersionIdOk returns a tuple with the HeadVersionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeadVersionId

`func (o *EntriesInner) SetHeadVersionId(v string)`

SetHeadVersionId sets HeadVersionId field to given value.


### SetHeadVersionIdNil

`func (o *EntriesInner) SetHeadVersionIdNil(b bool)`

 SetHeadVersionIdNil sets the value for HeadVersionId to be an explicit nil

### UnsetHeadVersionId
`func (o *EntriesInner) UnsetHeadVersionId()`

UnsetHeadVersionId ensures that no value is present for HeadVersionId, not even an explicit nil
### GetSizeBytes

`func (o *EntriesInner) GetSizeBytes() int32`

GetSizeBytes returns the SizeBytes field if non-nil, zero value otherwise.

### GetSizeBytesOk

`func (o *EntriesInner) GetSizeBytesOk() (*int32, bool)`

GetSizeBytesOk returns a tuple with the SizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSizeBytes

`func (o *EntriesInner) SetSizeBytes(v int32)`

SetSizeBytes sets SizeBytes field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
