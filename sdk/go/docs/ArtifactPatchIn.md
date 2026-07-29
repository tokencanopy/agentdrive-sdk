# ArtifactPatchIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Labels** | Pointer to **[]string** |  | [optional]
**Metadata** | Pointer to **map[string]interface{}** |  | [optional]
**Source** | Pointer to [**NullableArtifactSource**](ArtifactSource.md) |  | [optional]

## Methods

### NewArtifactPatchIn

`func NewArtifactPatchIn() *ArtifactPatchIn`

NewArtifactPatchIn instantiates a new ArtifactPatchIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewArtifactPatchInWithDefaults

`func NewArtifactPatchInWithDefaults() *ArtifactPatchIn`

NewArtifactPatchInWithDefaults instantiates a new ArtifactPatchIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLabels

`func (o *ArtifactPatchIn) GetLabels() []string`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *ArtifactPatchIn) GetLabelsOk() (*[]string, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *ArtifactPatchIn) SetLabels(v []string)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *ArtifactPatchIn) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### SetLabelsNil

`func (o *ArtifactPatchIn) SetLabelsNil(b bool)`

 SetLabelsNil sets the value for Labels to be an explicit nil

### UnsetLabels
`func (o *ArtifactPatchIn) UnsetLabels()`

UnsetLabels ensures that no value is present for Labels, not even an explicit nil
### GetMetadata

`func (o *ArtifactPatchIn) GetMetadata() map[string]interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ArtifactPatchIn) GetMetadataOk() (*map[string]interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ArtifactPatchIn) SetMetadata(v map[string]interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *ArtifactPatchIn) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *ArtifactPatchIn) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *ArtifactPatchIn) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetSource

`func (o *ArtifactPatchIn) GetSource() ArtifactSource`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *ArtifactPatchIn) GetSourceOk() (*ArtifactSource, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *ArtifactPatchIn) SetSource(v ArtifactSource)`

SetSource sets Source field to given value.

### HasSource

`func (o *ArtifactPatchIn) HasSource() bool`

HasSource returns a boolean if a field has been set.

### SetSourceNil

`func (o *ArtifactPatchIn) SetSourceNil(b bool)`

 SetSourceNil sets the value for Source to be an explicit nil

### UnsetSource
`func (o *ArtifactPatchIn) UnsetSource()`

UnsetSource ensures that no value is present for Source, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
