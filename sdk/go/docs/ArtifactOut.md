# ArtifactOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ContentPreview** | **NullableString** |  |
**ContentType** | **NullableString** |  |
**CreatedAt** | **time.Time** |  |
**DeletedAt** | **NullableTime** |  |
**DriveId** | **string** |  |
**EffectiveVisibility** | **string** | Server-computed exposure summary, resolved over the artifact&#39;s live grants, its whole folder ancestry, and the drive. &#39;public&#39; when any live grant has principal_type &#39;public&#39;; otherwise &#39;shared&#39; when a live grant names a principal other than the drive&#39;s creator; otherwise &#39;private&#39;. Describes exposure, NOT the caller&#39;s own access. |
**HeadVersionId** | **NullableString** |  |
**Id** | **string** |  |
**Labels** | **[]string** |  |
**Metadata** | **map[string]interface{}** |  |
**Name** | **string** |  |
**ParentId** | **string** |  |
**Revision** | **string** |  |
**State** | **string** |  |
**UpdatedAt** | **time.Time** |  |

## Methods

### NewArtifactOut

`func NewArtifactOut(contentPreview NullableString, contentType NullableString, createdAt time.Time, deletedAt NullableTime, driveId string, effectiveVisibility string, headVersionId NullableString, id string, labels []string, metadata map[string]interface{}, name string, parentId string, revision string, state string, updatedAt time.Time, ) *ArtifactOut`

NewArtifactOut instantiates a new ArtifactOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactOutWithDefaults

`func NewArtifactOutWithDefaults() *ArtifactOut`

NewArtifactOutWithDefaults instantiates a new ArtifactOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContentPreview

`func (o *ArtifactOut) GetContentPreview() string`

GetContentPreview returns the ContentPreview field if non-nil, zero value otherwise.

### GetContentPreviewOk

`func (o *ArtifactOut) GetContentPreviewOk() (*string, bool)`

GetContentPreviewOk returns a tuple with the ContentPreview field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentPreview

`func (o *ArtifactOut) SetContentPreview(v string)`

SetContentPreview sets ContentPreview field to given value.


### SetContentPreviewNil

`func (o *ArtifactOut) SetContentPreviewNil(b bool)`

 SetContentPreviewNil sets the value for ContentPreview to be an explicit nil

### UnsetContentPreview
`func (o *ArtifactOut) UnsetContentPreview()`

UnsetContentPreview ensures that no value is present for ContentPreview, not even an explicit nil
### GetContentType

`func (o *ArtifactOut) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *ArtifactOut) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *ArtifactOut) SetContentType(v string)`

SetContentType sets ContentType field to given value.


### SetContentTypeNil

`func (o *ArtifactOut) SetContentTypeNil(b bool)`

 SetContentTypeNil sets the value for ContentType to be an explicit nil

### UnsetContentType
`func (o *ArtifactOut) UnsetContentType()`

UnsetContentType ensures that no value is present for ContentType, not even an explicit nil
### GetCreatedAt

`func (o *ArtifactOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ArtifactOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ArtifactOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetDeletedAt

`func (o *ArtifactOut) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *ArtifactOut) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *ArtifactOut) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.


### SetDeletedAtNil

`func (o *ArtifactOut) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *ArtifactOut) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil
### GetDriveId

`func (o *ArtifactOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *ArtifactOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *ArtifactOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetEffectiveVisibility

`func (o *ArtifactOut) GetEffectiveVisibility() string`

GetEffectiveVisibility returns the EffectiveVisibility field if non-nil, zero value otherwise.

### GetEffectiveVisibilityOk

`func (o *ArtifactOut) GetEffectiveVisibilityOk() (*string, bool)`

GetEffectiveVisibilityOk returns a tuple with the EffectiveVisibility field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEffectiveVisibility

`func (o *ArtifactOut) SetEffectiveVisibility(v string)`

SetEffectiveVisibility sets EffectiveVisibility field to given value.


### GetHeadVersionId

`func (o *ArtifactOut) GetHeadVersionId() string`

GetHeadVersionId returns the HeadVersionId field if non-nil, zero value otherwise.

### GetHeadVersionIdOk

`func (o *ArtifactOut) GetHeadVersionIdOk() (*string, bool)`

GetHeadVersionIdOk returns a tuple with the HeadVersionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeadVersionId

`func (o *ArtifactOut) SetHeadVersionId(v string)`

SetHeadVersionId sets HeadVersionId field to given value.


### SetHeadVersionIdNil

`func (o *ArtifactOut) SetHeadVersionIdNil(b bool)`

 SetHeadVersionIdNil sets the value for HeadVersionId to be an explicit nil

### UnsetHeadVersionId
`func (o *ArtifactOut) UnsetHeadVersionId()`

UnsetHeadVersionId ensures that no value is present for HeadVersionId, not even an explicit nil
### GetId

`func (o *ArtifactOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ArtifactOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ArtifactOut) SetId(v string)`

SetId sets Id field to given value.


### GetLabels

`func (o *ArtifactOut) GetLabels() []string`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *ArtifactOut) GetLabelsOk() (*[]string, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *ArtifactOut) SetLabels(v []string)`

SetLabels sets Labels field to given value.


### GetMetadata

`func (o *ArtifactOut) GetMetadata() map[string]interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ArtifactOut) GetMetadataOk() (*map[string]interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ArtifactOut) SetMetadata(v map[string]interface{})`

SetMetadata sets Metadata field to given value.


### GetName

`func (o *ArtifactOut) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ArtifactOut) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ArtifactOut) SetName(v string)`

SetName sets Name field to given value.


### GetParentId

`func (o *ArtifactOut) GetParentId() string`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *ArtifactOut) GetParentIdOk() (*string, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *ArtifactOut) SetParentId(v string)`

SetParentId sets ParentId field to given value.


### GetRevision

`func (o *ArtifactOut) GetRevision() string`

GetRevision returns the Revision field if non-nil, zero value otherwise.

### GetRevisionOk

`func (o *ArtifactOut) GetRevisionOk() (*string, bool)`

GetRevisionOk returns a tuple with the Revision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevision

`func (o *ArtifactOut) SetRevision(v string)`

SetRevision sets Revision field to given value.


### GetState

`func (o *ArtifactOut) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *ArtifactOut) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *ArtifactOut) SetState(v string)`

SetState sets State field to given value.


### GetUpdatedAt

`func (o *ArtifactOut) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *ArtifactOut) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *ArtifactOut) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
