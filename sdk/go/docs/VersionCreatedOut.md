# VersionCreatedOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ArtifactId** | **string** |  |
**ArtifactRevision** | **string** | The artifact&#39;s revision after this version became head — the If-Match value for the next mutation. |
**ContentType** | **string** |  |
**CreatedAt** | **time.Time** |  |
**CreatedBy** | **NullableString** |  |
**Hash** | **string** |  |
**Id** | **string** |  |
**ParentVersionId** | **NullableString** |  |
**SizeBytes** | **int32** |  |
**VersionNumber** | **int32** |  |

## Methods

### NewVersionCreatedOut

`func NewVersionCreatedOut(artifactId string, artifactRevision string, contentType string, createdAt time.Time, createdBy NullableString, hash string, id string, parentVersionId NullableString, sizeBytes int32, versionNumber int32, ) *VersionCreatedOut`

NewVersionCreatedOut instantiates a new VersionCreatedOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewVersionCreatedOutWithDefaults

`func NewVersionCreatedOutWithDefaults() *VersionCreatedOut`

NewVersionCreatedOutWithDefaults instantiates a new VersionCreatedOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetArtifactId

`func (o *VersionCreatedOut) GetArtifactId() string`

GetArtifactId returns the ArtifactId field if non-nil, zero value otherwise.

### GetArtifactIdOk

`func (o *VersionCreatedOut) GetArtifactIdOk() (*string, bool)`

GetArtifactIdOk returns a tuple with the ArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtifactId

`func (o *VersionCreatedOut) SetArtifactId(v string)`

SetArtifactId sets ArtifactId field to given value.


### GetArtifactRevision

`func (o *VersionCreatedOut) GetArtifactRevision() string`

GetArtifactRevision returns the ArtifactRevision field if non-nil, zero value otherwise.

### GetArtifactRevisionOk

`func (o *VersionCreatedOut) GetArtifactRevisionOk() (*string, bool)`

GetArtifactRevisionOk returns a tuple with the ArtifactRevision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtifactRevision

`func (o *VersionCreatedOut) SetArtifactRevision(v string)`

SetArtifactRevision sets ArtifactRevision field to given value.


### GetContentType

`func (o *VersionCreatedOut) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *VersionCreatedOut) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *VersionCreatedOut) SetContentType(v string)`

SetContentType sets ContentType field to given value.


### GetCreatedAt

`func (o *VersionCreatedOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *VersionCreatedOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *VersionCreatedOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetCreatedBy

`func (o *VersionCreatedOut) GetCreatedBy() string`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *VersionCreatedOut) GetCreatedByOk() (*string, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *VersionCreatedOut) SetCreatedBy(v string)`

SetCreatedBy sets CreatedBy field to given value.


### SetCreatedByNil

`func (o *VersionCreatedOut) SetCreatedByNil(b bool)`

 SetCreatedByNil sets the value for CreatedBy to be an explicit nil

### UnsetCreatedBy
`func (o *VersionCreatedOut) UnsetCreatedBy()`

UnsetCreatedBy ensures that no value is present for CreatedBy, not even an explicit nil
### GetHash

`func (o *VersionCreatedOut) GetHash() string`

GetHash returns the Hash field if non-nil, zero value otherwise.

### GetHashOk

`func (o *VersionCreatedOut) GetHashOk() (*string, bool)`

GetHashOk returns a tuple with the Hash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHash

`func (o *VersionCreatedOut) SetHash(v string)`

SetHash sets Hash field to given value.


### GetId

`func (o *VersionCreatedOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *VersionCreatedOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *VersionCreatedOut) SetId(v string)`

SetId sets Id field to given value.


### GetParentVersionId

`func (o *VersionCreatedOut) GetParentVersionId() string`

GetParentVersionId returns the ParentVersionId field if non-nil, zero value otherwise.

### GetParentVersionIdOk

`func (o *VersionCreatedOut) GetParentVersionIdOk() (*string, bool)`

GetParentVersionIdOk returns a tuple with the ParentVersionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentVersionId

`func (o *VersionCreatedOut) SetParentVersionId(v string)`

SetParentVersionId sets ParentVersionId field to given value.


### SetParentVersionIdNil

`func (o *VersionCreatedOut) SetParentVersionIdNil(b bool)`

 SetParentVersionIdNil sets the value for ParentVersionId to be an explicit nil

### UnsetParentVersionId
`func (o *VersionCreatedOut) UnsetParentVersionId()`

UnsetParentVersionId ensures that no value is present for ParentVersionId, not even an explicit nil
### GetSizeBytes

`func (o *VersionCreatedOut) GetSizeBytes() int32`

GetSizeBytes returns the SizeBytes field if non-nil, zero value otherwise.

### GetSizeBytesOk

`func (o *VersionCreatedOut) GetSizeBytesOk() (*int32, bool)`

GetSizeBytesOk returns a tuple with the SizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSizeBytes

`func (o *VersionCreatedOut) SetSizeBytes(v int32)`

SetSizeBytes sets SizeBytes field to given value.


### GetVersionNumber

`func (o *VersionCreatedOut) GetVersionNumber() int32`

GetVersionNumber returns the VersionNumber field if non-nil, zero value otherwise.

### GetVersionNumberOk

`func (o *VersionCreatedOut) GetVersionNumberOk() (*int32, bool)`

GetVersionNumberOk returns a tuple with the VersionNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionNumber

`func (o *VersionCreatedOut) SetVersionNumber(v int32)`

SetVersionNumber sets VersionNumber field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
