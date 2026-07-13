# UploadBeginIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Path** | **string** |  | 
**ContentType** | Pointer to **string** |  | [optional] [default to "application/octet-stream"]
**SizeBytes** | **int32** |  | 
**Crc32c** | Pointer to **NullableString** |  | [optional] 
**Labels** | Pointer to **[]string** |  | [optional] 
**Metadata** | Pointer to **map[string]interface{}** |  | [optional] 
**Source** | Pointer to [**NullableArtifactSource**](ArtifactSource.md) |  | [optional] 
**ActorName** | Pointer to **NullableString** |  | [optional] 
**ChangeSummary** | Pointer to **NullableString** |  | [optional] 
**IfMatch** | Pointer to **NullableInt32** |  | [optional] 
**IfNoneMatch** | Pointer to **bool** |  | [optional] [default to false]
**CorsOrigin** | Pointer to **NullableString** | Web origin (scheme://host[:port]) of the browser that will PUT the bytes, e.g. &#x60;https://app.example.com&#x60;. Set this when the &#x60;upload_url&#x60; is handed to browser code: GCS binds CORS at session initiate, so the returned session only echoes &#x60;Access-Control-Allow-Origin&#x60; (and is thus PUT-able from a browser) when opened with the caller&#39;s origin. A trusted backend relaying a browser upload forwards the browser&#39;s &#x60;Origin&#x60; here. Omit for server/desktop uploads (no CORS enforcement). | [optional] 

## Methods

### NewUploadBeginIn

`func NewUploadBeginIn(path string, sizeBytes int32, ) *UploadBeginIn`

NewUploadBeginIn instantiates a new UploadBeginIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUploadBeginInWithDefaults

`func NewUploadBeginInWithDefaults() *UploadBeginIn`

NewUploadBeginInWithDefaults instantiates a new UploadBeginIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPath

`func (o *UploadBeginIn) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *UploadBeginIn) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *UploadBeginIn) SetPath(v string)`

SetPath sets Path field to given value.


### GetContentType

`func (o *UploadBeginIn) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *UploadBeginIn) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *UploadBeginIn) SetContentType(v string)`

SetContentType sets ContentType field to given value.

### HasContentType

`func (o *UploadBeginIn) HasContentType() bool`

HasContentType returns a boolean if a field has been set.

### GetSizeBytes

`func (o *UploadBeginIn) GetSizeBytes() int32`

GetSizeBytes returns the SizeBytes field if non-nil, zero value otherwise.

### GetSizeBytesOk

`func (o *UploadBeginIn) GetSizeBytesOk() (*int32, bool)`

GetSizeBytesOk returns a tuple with the SizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSizeBytes

`func (o *UploadBeginIn) SetSizeBytes(v int32)`

SetSizeBytes sets SizeBytes field to given value.


### GetCrc32c

`func (o *UploadBeginIn) GetCrc32c() string`

GetCrc32c returns the Crc32c field if non-nil, zero value otherwise.

### GetCrc32cOk

`func (o *UploadBeginIn) GetCrc32cOk() (*string, bool)`

GetCrc32cOk returns a tuple with the Crc32c field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrc32c

`func (o *UploadBeginIn) SetCrc32c(v string)`

SetCrc32c sets Crc32c field to given value.

### HasCrc32c

`func (o *UploadBeginIn) HasCrc32c() bool`

HasCrc32c returns a boolean if a field has been set.

### SetCrc32cNil

`func (o *UploadBeginIn) SetCrc32cNil(b bool)`

 SetCrc32cNil sets the value for Crc32c to be an explicit nil

### UnsetCrc32c
`func (o *UploadBeginIn) UnsetCrc32c()`

UnsetCrc32c ensures that no value is present for Crc32c, not even an explicit nil
### GetLabels

`func (o *UploadBeginIn) GetLabels() []string`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *UploadBeginIn) GetLabelsOk() (*[]string, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *UploadBeginIn) SetLabels(v []string)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *UploadBeginIn) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### SetLabelsNil

`func (o *UploadBeginIn) SetLabelsNil(b bool)`

 SetLabelsNil sets the value for Labels to be an explicit nil

### UnsetLabels
`func (o *UploadBeginIn) UnsetLabels()`

UnsetLabels ensures that no value is present for Labels, not even an explicit nil
### GetMetadata

`func (o *UploadBeginIn) GetMetadata() map[string]interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *UploadBeginIn) GetMetadataOk() (*map[string]interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *UploadBeginIn) SetMetadata(v map[string]interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *UploadBeginIn) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *UploadBeginIn) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *UploadBeginIn) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetSource

`func (o *UploadBeginIn) GetSource() ArtifactSource`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *UploadBeginIn) GetSourceOk() (*ArtifactSource, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *UploadBeginIn) SetSource(v ArtifactSource)`

SetSource sets Source field to given value.

### HasSource

`func (o *UploadBeginIn) HasSource() bool`

HasSource returns a boolean if a field has been set.

### SetSourceNil

`func (o *UploadBeginIn) SetSourceNil(b bool)`

 SetSourceNil sets the value for Source to be an explicit nil

### UnsetSource
`func (o *UploadBeginIn) UnsetSource()`

UnsetSource ensures that no value is present for Source, not even an explicit nil
### GetActorName

`func (o *UploadBeginIn) GetActorName() string`

GetActorName returns the ActorName field if non-nil, zero value otherwise.

### GetActorNameOk

`func (o *UploadBeginIn) GetActorNameOk() (*string, bool)`

GetActorNameOk returns a tuple with the ActorName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActorName

`func (o *UploadBeginIn) SetActorName(v string)`

SetActorName sets ActorName field to given value.

### HasActorName

`func (o *UploadBeginIn) HasActorName() bool`

HasActorName returns a boolean if a field has been set.

### SetActorNameNil

`func (o *UploadBeginIn) SetActorNameNil(b bool)`

 SetActorNameNil sets the value for ActorName to be an explicit nil

### UnsetActorName
`func (o *UploadBeginIn) UnsetActorName()`

UnsetActorName ensures that no value is present for ActorName, not even an explicit nil
### GetChangeSummary

`func (o *UploadBeginIn) GetChangeSummary() string`

GetChangeSummary returns the ChangeSummary field if non-nil, zero value otherwise.

### GetChangeSummaryOk

`func (o *UploadBeginIn) GetChangeSummaryOk() (*string, bool)`

GetChangeSummaryOk returns a tuple with the ChangeSummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangeSummary

`func (o *UploadBeginIn) SetChangeSummary(v string)`

SetChangeSummary sets ChangeSummary field to given value.

### HasChangeSummary

`func (o *UploadBeginIn) HasChangeSummary() bool`

HasChangeSummary returns a boolean if a field has been set.

### SetChangeSummaryNil

`func (o *UploadBeginIn) SetChangeSummaryNil(b bool)`

 SetChangeSummaryNil sets the value for ChangeSummary to be an explicit nil

### UnsetChangeSummary
`func (o *UploadBeginIn) UnsetChangeSummary()`

UnsetChangeSummary ensures that no value is present for ChangeSummary, not even an explicit nil
### GetIfMatch

`func (o *UploadBeginIn) GetIfMatch() int32`

GetIfMatch returns the IfMatch field if non-nil, zero value otherwise.

### GetIfMatchOk

`func (o *UploadBeginIn) GetIfMatchOk() (*int32, bool)`

GetIfMatchOk returns a tuple with the IfMatch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIfMatch

`func (o *UploadBeginIn) SetIfMatch(v int32)`

SetIfMatch sets IfMatch field to given value.

### HasIfMatch

`func (o *UploadBeginIn) HasIfMatch() bool`

HasIfMatch returns a boolean if a field has been set.

### SetIfMatchNil

`func (o *UploadBeginIn) SetIfMatchNil(b bool)`

 SetIfMatchNil sets the value for IfMatch to be an explicit nil

### UnsetIfMatch
`func (o *UploadBeginIn) UnsetIfMatch()`

UnsetIfMatch ensures that no value is present for IfMatch, not even an explicit nil
### GetIfNoneMatch

`func (o *UploadBeginIn) GetIfNoneMatch() bool`

GetIfNoneMatch returns the IfNoneMatch field if non-nil, zero value otherwise.

### GetIfNoneMatchOk

`func (o *UploadBeginIn) GetIfNoneMatchOk() (*bool, bool)`

GetIfNoneMatchOk returns a tuple with the IfNoneMatch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIfNoneMatch

`func (o *UploadBeginIn) SetIfNoneMatch(v bool)`

SetIfNoneMatch sets IfNoneMatch field to given value.

### HasIfNoneMatch

`func (o *UploadBeginIn) HasIfNoneMatch() bool`

HasIfNoneMatch returns a boolean if a field has been set.

### GetCorsOrigin

`func (o *UploadBeginIn) GetCorsOrigin() string`

GetCorsOrigin returns the CorsOrigin field if non-nil, zero value otherwise.

### GetCorsOriginOk

`func (o *UploadBeginIn) GetCorsOriginOk() (*string, bool)`

GetCorsOriginOk returns a tuple with the CorsOrigin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCorsOrigin

`func (o *UploadBeginIn) SetCorsOrigin(v string)`

SetCorsOrigin sets CorsOrigin field to given value.

### HasCorsOrigin

`func (o *UploadBeginIn) HasCorsOrigin() bool`

HasCorsOrigin returns a boolean if a field has been set.

### SetCorsOriginNil

`func (o *UploadBeginIn) SetCorsOriginNil(b bool)`

 SetCorsOriginNil sets the value for CorsOrigin to be an explicit nil

### UnsetCorsOrigin
`func (o *UploadBeginIn) UnsetCorsOrigin()`

UnsetCorsOrigin ensures that no value is present for CorsOrigin, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


