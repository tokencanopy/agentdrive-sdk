# VersionOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ArtifactId** | **string** |  |
**ContentType** | **string** |  |
**CreatedAt** | **time.Time** |  |
**CreatedBy** | **NullableString** |  |
**Hash** | **string** |  |
**Id** | **string** |  |
**OriginMessage** | Pointer to **NullableString** |  | [optional]
**OriginSessionId** | Pointer to **NullableString** |  | [optional]
**ParentVersionId** | **NullableString** |  |
**SizeBytes** | **int32** |  |
**VersionNumber** | **int32** |  |

## Methods

### NewVersionOut

`func NewVersionOut(artifactId string, contentType string, createdAt time.Time, createdBy NullableString, hash string, id string, parentVersionId NullableString, sizeBytes int32, versionNumber int32, ) *VersionOut`

NewVersionOut instantiates a new VersionOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewVersionOutWithDefaults

`func NewVersionOutWithDefaults() *VersionOut`

NewVersionOutWithDefaults instantiates a new VersionOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetArtifactId

`func (o *VersionOut) GetArtifactId() string`

GetArtifactId returns the ArtifactId field if non-nil, zero value otherwise.

### GetArtifactIdOk

`func (o *VersionOut) GetArtifactIdOk() (*string, bool)`

GetArtifactIdOk returns a tuple with the ArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtifactId

`func (o *VersionOut) SetArtifactId(v string)`

SetArtifactId sets ArtifactId field to given value.


### GetContentType

`func (o *VersionOut) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *VersionOut) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *VersionOut) SetContentType(v string)`

SetContentType sets ContentType field to given value.


### GetCreatedAt

`func (o *VersionOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *VersionOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *VersionOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetCreatedBy

`func (o *VersionOut) GetCreatedBy() string`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *VersionOut) GetCreatedByOk() (*string, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *VersionOut) SetCreatedBy(v string)`

SetCreatedBy sets CreatedBy field to given value.


### SetCreatedByNil

`func (o *VersionOut) SetCreatedByNil(b bool)`

 SetCreatedByNil sets the value for CreatedBy to be an explicit nil

### UnsetCreatedBy
`func (o *VersionOut) UnsetCreatedBy()`

UnsetCreatedBy ensures that no value is present for CreatedBy, not even an explicit nil
### GetHash

`func (o *VersionOut) GetHash() string`

GetHash returns the Hash field if non-nil, zero value otherwise.

### GetHashOk

`func (o *VersionOut) GetHashOk() (*string, bool)`

GetHashOk returns a tuple with the Hash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHash

`func (o *VersionOut) SetHash(v string)`

SetHash sets Hash field to given value.


### GetId

`func (o *VersionOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *VersionOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *VersionOut) SetId(v string)`

SetId sets Id field to given value.


### GetOriginMessage

`func (o *VersionOut) GetOriginMessage() string`

GetOriginMessage returns the OriginMessage field if non-nil, zero value otherwise.

### GetOriginMessageOk

`func (o *VersionOut) GetOriginMessageOk() (*string, bool)`

GetOriginMessageOk returns a tuple with the OriginMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginMessage

`func (o *VersionOut) SetOriginMessage(v string)`

SetOriginMessage sets OriginMessage field to given value.

### HasOriginMessage

`func (o *VersionOut) HasOriginMessage() bool`

HasOriginMessage returns a boolean if a field has been set.

### SetOriginMessageNil

`func (o *VersionOut) SetOriginMessageNil(b bool)`

 SetOriginMessageNil sets the value for OriginMessage to be an explicit nil

### UnsetOriginMessage
`func (o *VersionOut) UnsetOriginMessage()`

UnsetOriginMessage ensures that no value is present for OriginMessage, not even an explicit nil
### GetOriginSessionId

`func (o *VersionOut) GetOriginSessionId() string`

GetOriginSessionId returns the OriginSessionId field if non-nil, zero value otherwise.

### GetOriginSessionIdOk

`func (o *VersionOut) GetOriginSessionIdOk() (*string, bool)`

GetOriginSessionIdOk returns a tuple with the OriginSessionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginSessionId

`func (o *VersionOut) SetOriginSessionId(v string)`

SetOriginSessionId sets OriginSessionId field to given value.

### HasOriginSessionId

`func (o *VersionOut) HasOriginSessionId() bool`

HasOriginSessionId returns a boolean if a field has been set.

### SetOriginSessionIdNil

`func (o *VersionOut) SetOriginSessionIdNil(b bool)`

 SetOriginSessionIdNil sets the value for OriginSessionId to be an explicit nil

### UnsetOriginSessionId
`func (o *VersionOut) UnsetOriginSessionId()`

UnsetOriginSessionId ensures that no value is present for OriginSessionId, not even an explicit nil
### GetParentVersionId

`func (o *VersionOut) GetParentVersionId() string`

GetParentVersionId returns the ParentVersionId field if non-nil, zero value otherwise.

### GetParentVersionIdOk

`func (o *VersionOut) GetParentVersionIdOk() (*string, bool)`

GetParentVersionIdOk returns a tuple with the ParentVersionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentVersionId

`func (o *VersionOut) SetParentVersionId(v string)`

SetParentVersionId sets ParentVersionId field to given value.


### SetParentVersionIdNil

`func (o *VersionOut) SetParentVersionIdNil(b bool)`

 SetParentVersionIdNil sets the value for ParentVersionId to be an explicit nil

### UnsetParentVersionId
`func (o *VersionOut) UnsetParentVersionId()`

UnsetParentVersionId ensures that no value is present for ParentVersionId, not even an explicit nil
### GetSizeBytes

`func (o *VersionOut) GetSizeBytes() int32`

GetSizeBytes returns the SizeBytes field if non-nil, zero value otherwise.

### GetSizeBytesOk

`func (o *VersionOut) GetSizeBytesOk() (*int32, bool)`

GetSizeBytesOk returns a tuple with the SizeBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSizeBytes

`func (o *VersionOut) SetSizeBytes(v int32)`

SetSizeBytes sets SizeBytes field to given value.


### GetVersionNumber

`func (o *VersionOut) GetVersionNumber() int32`

GetVersionNumber returns the VersionNumber field if non-nil, zero value otherwise.

### GetVersionNumberOk

`func (o *VersionOut) GetVersionNumberOk() (*int32, bool)`

GetVersionNumberOk returns a tuple with the VersionNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionNumber

`func (o *VersionOut) SetVersionNumber(v int32)`

SetVersionNumber sets VersionNumber field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
