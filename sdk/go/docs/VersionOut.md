# VersionOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActorName** | Pointer to **NullableString** |  | [optional]
**ArtId** | **string** |  |
**ChangeSummary** | Pointer to **NullableString** |  | [optional]
**ContentType** | **string** |  |
**CreatedAt** | **time.Time** |  |
**Hash** | **string** |  |
**SizeBytes** | **int32** |  |
**VersionNumber** | **int32** |  |

## Methods

### NewVersionOut

`func NewVersionOut(artId string, contentType string, createdAt time.Time, hash string, sizeBytes int32, versionNumber int32, ) *VersionOut`

NewVersionOut instantiates a new VersionOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewVersionOutWithDefaults

`func NewVersionOutWithDefaults() *VersionOut`

NewVersionOutWithDefaults instantiates a new VersionOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActorName

`func (o *VersionOut) GetActorName() string`

GetActorName returns the ActorName field if non-nil, zero value otherwise.

### GetActorNameOk

`func (o *VersionOut) GetActorNameOk() (*string, bool)`

GetActorNameOk returns a tuple with the ActorName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActorName

`func (o *VersionOut) SetActorName(v string)`

SetActorName sets ActorName field to given value.

### HasActorName

`func (o *VersionOut) HasActorName() bool`

HasActorName returns a boolean if a field has been set.

### SetActorNameNil

`func (o *VersionOut) SetActorNameNil(b bool)`

 SetActorNameNil sets the value for ActorName to be an explicit nil

### UnsetActorName
`func (o *VersionOut) UnsetActorName()`

UnsetActorName ensures that no value is present for ActorName, not even an explicit nil
### GetArtId

`func (o *VersionOut) GetArtId() string`

GetArtId returns the ArtId field if non-nil, zero value otherwise.

### GetArtIdOk

`func (o *VersionOut) GetArtIdOk() (*string, bool)`

GetArtIdOk returns a tuple with the ArtId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtId

`func (o *VersionOut) SetArtId(v string)`

SetArtId sets ArtId field to given value.


### GetChangeSummary

`func (o *VersionOut) GetChangeSummary() string`

GetChangeSummary returns the ChangeSummary field if non-nil, zero value otherwise.

### GetChangeSummaryOk

`func (o *VersionOut) GetChangeSummaryOk() (*string, bool)`

GetChangeSummaryOk returns a tuple with the ChangeSummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangeSummary

`func (o *VersionOut) SetChangeSummary(v string)`

SetChangeSummary sets ChangeSummary field to given value.

### HasChangeSummary

`func (o *VersionOut) HasChangeSummary() bool`

HasChangeSummary returns a boolean if a field has been set.

### SetChangeSummaryNil

`func (o *VersionOut) SetChangeSummaryNil(b bool)`

 SetChangeSummaryNil sets the value for ChangeSummary to be an explicit nil

### UnsetChangeSummary
`func (o *VersionOut) UnsetChangeSummary()`

UnsetChangeSummary ensures that no value is present for ChangeSummary, not even an explicit nil
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
