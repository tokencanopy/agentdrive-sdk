# ArtifactEntryOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ContentType** | **NullableString** |  |
**DeletedAt** | **NullableTime** |  |
**HeadVersionId** | **NullableString** |  |
**Id** | **string** |  |
**Name** | **string** |  |
**Revision** | **string** |  |
**SizeBytes** | **int32** |  |
**State** | **string** |  |
**Type** | **string** |  |
**UpdatedAt** | **time.Time** |  |

## Methods

### NewArtifactEntryOut

`func NewArtifactEntryOut(contentType NullableString, deletedAt NullableTime, headVersionId NullableString, id string, name string, revision string, sizeBytes int32, state string, type_ string, updatedAt time.Time, ) *ArtifactEntryOut`

NewArtifactEntryOut instantiates a new ArtifactEntryOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactEntryOutWithDefaults

`func NewArtifactEntryOutWithDefaults() *ArtifactEntryOut`

NewArtifactEntryOutWithDefaults instantiates a new ArtifactEntryOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContentType

`func (o *ArtifactEntryOut) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *ArtifactEntryOut) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *ArtifactEntryOut) SetContentType(v string)`

SetContentType sets ContentType field to given value.


### SetContentTypeNil

`func (o *ArtifactEntryOut) SetContentTypeNil(b bool)`

 SetContentTypeNil sets the value for ContentType to be an explicit nil

### UnsetContentType
`func (o *ArtifactEntryOut) UnsetContentType()`

UnsetContentType ensures that no value is present for ContentType, not even an explicit nil
### GetDeletedAt

`func (o *ArtifactEntryOut) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *ArtifactEntryOut) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *ArtifactEntryOut) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.


### SetDeletedAtNil

`func (o *ArtifactEntryOut) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *ArtifactEntryOut) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil
### GetHeadVersionId

`func (o *ArtifactEntryOut) GetHeadVersionId() string`

GetHeadVersionId returns the HeadVersionId field if non-nil, zero value otherwise.

### GetHeadVersionIdOk

`func (o *ArtifactEntryOut) GetHeadVersionIdOk() (*string, bool)`

GetHeadVersionIdOk returns a tuple with the HeadVersionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeadVersionId

`func (o *ArtifactEntryOut) SetHeadVersionId(v string)`

SetHeadVersionId sets HeadVersionId field to given value.


### SetHeadVersionIdNil

`func (o *ArtifactEntryOut) SetHeadVersionIdNil(b bool)`

 SetHeadVersionIdNil sets the value for HeadVersionId to be an explicit nil

### UnsetHeadVersionId
`func (o *ArtifactEntryOut) UnsetHeadVersionId()`

UnsetHeadVersionId ensures that no value is present for HeadVersionId, not even an explicit nil
### GetId

`func (o *ArtifactEntryOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ArtifactEntryOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ArtifactEntryOut) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *ArtifactEntryOut) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ArtifactEntryOut) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ArtifactEntryOut) SetName(v string)`

SetName sets Name field to given value.


### GetRevision

`func (o *ArtifactEntryOut) GetRevision() string`

GetRevision returns the Revision field if non-nil, zero value otherwise.

### GetRevisionOk

`func (o *ArtifactEntryOut) GetRevisionOk() (*string, bool)`

GetRevisionOk returns a tuple with the Revision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevision

`func (o *ArtifactEntryOut) SetRevision(v string)`

SetRevision sets Revision field to given value.


### GetSizeBytes

`func (o *ArtifactEntryOut) GetSizeBytes() int32`

GetSizeBytes returns the SizeBytes field if non-nil, zero value otherwise.

### GetSizeBytesOk

`func (o *ArtifactEntryOut) GetSizeBytesOk() (*int32, bool)`

GetSizeBytesOk returns a tuple with the SizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSizeBytes

`func (o *ArtifactEntryOut) SetSizeBytes(v int32)`

SetSizeBytes sets SizeBytes field to given value.


### GetState

`func (o *ArtifactEntryOut) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *ArtifactEntryOut) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *ArtifactEntryOut) SetState(v string)`

SetState sets State field to given value.


### GetType

`func (o *ArtifactEntryOut) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ArtifactEntryOut) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ArtifactEntryOut) SetType(v string)`

SetType sets Type field to given value.


### GetUpdatedAt

`func (o *ArtifactEntryOut) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *ArtifactEntryOut) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *ArtifactEntryOut) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
