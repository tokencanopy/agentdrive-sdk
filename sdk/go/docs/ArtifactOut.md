# ArtifactOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**DriveId** | **string** |  | 
**Path** | **string** |  | 
**Url** | **string** |  | 
**Permalink** | **string** |  | 
**ContentType** | **string** |  | 
**FileType** | **string** |  | 
**SizeBytes** | **int32** |  | 
**Hash** | **string** |  | 
**VersionNumber** | Pointer to **int32** |  | [optional] [default to 1]
**Metageneration** | Pointer to **int32** |  | [optional] [default to 1]
**Etag** | **string** |  | 
**Labels** | Pointer to **[]string** |  | [optional] 
**Metadata** | Pointer to **map[string]interface{}** |  | [optional] 
**Source** | Pointer to [**NullableArtifactSource**](ArtifactSource.md) |  | [optional] 
**IndexedAt** | Pointer to **NullableTime** |  | [optional] 
**EmbeddedAt** | Pointer to **NullableTime** |  | [optional] 
**CreatedAt** | **time.Time** |  | 
**UpdatedAt** | **time.Time** |  | 
**LlmIndex** | Pointer to **map[string]interface{}** |  | [optional] 

## Methods

### NewArtifactOut

`func NewArtifactOut(id string, driveId string, path string, url string, permalink string, contentType string, fileType string, sizeBytes int32, hash string, etag string, createdAt time.Time, updatedAt time.Time, ) *ArtifactOut`

NewArtifactOut instantiates a new ArtifactOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactOutWithDefaults

`func NewArtifactOutWithDefaults() *ArtifactOut`

NewArtifactOutWithDefaults instantiates a new ArtifactOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

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


### GetPath

`func (o *ArtifactOut) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *ArtifactOut) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *ArtifactOut) SetPath(v string)`

SetPath sets Path field to given value.


### GetUrl

`func (o *ArtifactOut) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *ArtifactOut) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *ArtifactOut) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetPermalink

`func (o *ArtifactOut) GetPermalink() string`

GetPermalink returns the Permalink field if non-nil, zero value otherwise.

### GetPermalinkOk

`func (o *ArtifactOut) GetPermalinkOk() (*string, bool)`

GetPermalinkOk returns a tuple with the Permalink field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermalink

`func (o *ArtifactOut) SetPermalink(v string)`

SetPermalink sets Permalink field to given value.


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


### GetFileType

`func (o *ArtifactOut) GetFileType() string`

GetFileType returns the FileType field if non-nil, zero value otherwise.

### GetFileTypeOk

`func (o *ArtifactOut) GetFileTypeOk() (*string, bool)`

GetFileTypeOk returns a tuple with the FileType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFileType

`func (o *ArtifactOut) SetFileType(v string)`

SetFileType sets FileType field to given value.


### GetSizeBytes

`func (o *ArtifactOut) GetSizeBytes() int32`

GetSizeBytes returns the SizeBytes field if non-nil, zero value otherwise.

### GetSizeBytesOk

`func (o *ArtifactOut) GetSizeBytesOk() (*int32, bool)`

GetSizeBytesOk returns a tuple with the SizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSizeBytes

`func (o *ArtifactOut) SetSizeBytes(v int32)`

SetSizeBytes sets SizeBytes field to given value.


### GetHash

`func (o *ArtifactOut) GetHash() string`

GetHash returns the Hash field if non-nil, zero value otherwise.

### GetHashOk

`func (o *ArtifactOut) GetHashOk() (*string, bool)`

GetHashOk returns a tuple with the Hash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHash

`func (o *ArtifactOut) SetHash(v string)`

SetHash sets Hash field to given value.


### GetVersionNumber

`func (o *ArtifactOut) GetVersionNumber() int32`

GetVersionNumber returns the VersionNumber field if non-nil, zero value otherwise.

### GetVersionNumberOk

`func (o *ArtifactOut) GetVersionNumberOk() (*int32, bool)`

GetVersionNumberOk returns a tuple with the VersionNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionNumber

`func (o *ArtifactOut) SetVersionNumber(v int32)`

SetVersionNumber sets VersionNumber field to given value.

### HasVersionNumber

`func (o *ArtifactOut) HasVersionNumber() bool`

HasVersionNumber returns a boolean if a field has been set.

### GetMetageneration

`func (o *ArtifactOut) GetMetageneration() int32`

GetMetageneration returns the Metageneration field if non-nil, zero value otherwise.

### GetMetagenerationOk

`func (o *ArtifactOut) GetMetagenerationOk() (*int32, bool)`

GetMetagenerationOk returns a tuple with the Metageneration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetageneration

`func (o *ArtifactOut) SetMetageneration(v int32)`

SetMetageneration sets Metageneration field to given value.

### HasMetageneration

`func (o *ArtifactOut) HasMetageneration() bool`

HasMetageneration returns a boolean if a field has been set.

### GetEtag

`func (o *ArtifactOut) GetEtag() string`

GetEtag returns the Etag field if non-nil, zero value otherwise.

### GetEtagOk

`func (o *ArtifactOut) GetEtagOk() (*string, bool)`

GetEtagOk returns a tuple with the Etag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEtag

`func (o *ArtifactOut) SetEtag(v string)`

SetEtag sets Etag field to given value.


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

### HasLabels

`func (o *ArtifactOut) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

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

### HasMetadata

`func (o *ArtifactOut) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetSource

`func (o *ArtifactOut) GetSource() ArtifactSource`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *ArtifactOut) GetSourceOk() (*ArtifactSource, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *ArtifactOut) SetSource(v ArtifactSource)`

SetSource sets Source field to given value.

### HasSource

`func (o *ArtifactOut) HasSource() bool`

HasSource returns a boolean if a field has been set.

### SetSourceNil

`func (o *ArtifactOut) SetSourceNil(b bool)`

 SetSourceNil sets the value for Source to be an explicit nil

### UnsetSource
`func (o *ArtifactOut) UnsetSource()`

UnsetSource ensures that no value is present for Source, not even an explicit nil
### GetIndexedAt

`func (o *ArtifactOut) GetIndexedAt() time.Time`

GetIndexedAt returns the IndexedAt field if non-nil, zero value otherwise.

### GetIndexedAtOk

`func (o *ArtifactOut) GetIndexedAtOk() (*time.Time, bool)`

GetIndexedAtOk returns a tuple with the IndexedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIndexedAt

`func (o *ArtifactOut) SetIndexedAt(v time.Time)`

SetIndexedAt sets IndexedAt field to given value.

### HasIndexedAt

`func (o *ArtifactOut) HasIndexedAt() bool`

HasIndexedAt returns a boolean if a field has been set.

### SetIndexedAtNil

`func (o *ArtifactOut) SetIndexedAtNil(b bool)`

 SetIndexedAtNil sets the value for IndexedAt to be an explicit nil

### UnsetIndexedAt
`func (o *ArtifactOut) UnsetIndexedAt()`

UnsetIndexedAt ensures that no value is present for IndexedAt, not even an explicit nil
### GetEmbeddedAt

`func (o *ArtifactOut) GetEmbeddedAt() time.Time`

GetEmbeddedAt returns the EmbeddedAt field if non-nil, zero value otherwise.

### GetEmbeddedAtOk

`func (o *ArtifactOut) GetEmbeddedAtOk() (*time.Time, bool)`

GetEmbeddedAtOk returns a tuple with the EmbeddedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmbeddedAt

`func (o *ArtifactOut) SetEmbeddedAt(v time.Time)`

SetEmbeddedAt sets EmbeddedAt field to given value.

### HasEmbeddedAt

`func (o *ArtifactOut) HasEmbeddedAt() bool`

HasEmbeddedAt returns a boolean if a field has been set.

### SetEmbeddedAtNil

`func (o *ArtifactOut) SetEmbeddedAtNil(b bool)`

 SetEmbeddedAtNil sets the value for EmbeddedAt to be an explicit nil

### UnsetEmbeddedAt
`func (o *ArtifactOut) UnsetEmbeddedAt()`

UnsetEmbeddedAt ensures that no value is present for EmbeddedAt, not even an explicit nil
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


### GetLlmIndex

`func (o *ArtifactOut) GetLlmIndex() map[string]interface{}`

GetLlmIndex returns the LlmIndex field if non-nil, zero value otherwise.

### GetLlmIndexOk

`func (o *ArtifactOut) GetLlmIndexOk() (*map[string]interface{}, bool)`

GetLlmIndexOk returns a tuple with the LlmIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLlmIndex

`func (o *ArtifactOut) SetLlmIndex(v map[string]interface{})`

SetLlmIndex sets LlmIndex field to given value.

### HasLlmIndex

`func (o *ArtifactOut) HasLlmIndex() bool`

HasLlmIndex returns a boolean if a field has been set.

### SetLlmIndexNil

`func (o *ArtifactOut) SetLlmIndexNil(b bool)`

 SetLlmIndexNil sets the value for LlmIndex to be an explicit nil

### UnsetLlmIndex
`func (o *ArtifactOut) UnsetLlmIndex()`

UnsetLlmIndex ensures that no value is present for LlmIndex, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


