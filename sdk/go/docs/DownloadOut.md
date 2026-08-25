# DownloadOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ArtifactId** | **string** |  | 
**VersionId** | **string** |  | 
**ExpiresAt** | **time.Time** |  | 
**Target** | [**DownloadTargetOut**](DownloadTargetOut.md) |  | 

## Methods

### NewDownloadOut

`func NewDownloadOut(artifactId string, versionId string, expiresAt time.Time, target DownloadTargetOut, ) *DownloadOut`

NewDownloadOut instantiates a new DownloadOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDownloadOutWithDefaults

`func NewDownloadOutWithDefaults() *DownloadOut`

NewDownloadOutWithDefaults instantiates a new DownloadOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetArtifactId

`func (o *DownloadOut) GetArtifactId() string`

GetArtifactId returns the ArtifactId field if non-nil, zero value otherwise.

### GetArtifactIdOk

`func (o *DownloadOut) GetArtifactIdOk() (*string, bool)`

GetArtifactIdOk returns a tuple with the ArtifactId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtifactId

`func (o *DownloadOut) SetArtifactId(v string)`

SetArtifactId sets ArtifactId field to given value.


### GetVersionId

`func (o *DownloadOut) GetVersionId() string`

GetVersionId returns the VersionId field if non-nil, zero value otherwise.

### GetVersionIdOk

`func (o *DownloadOut) GetVersionIdOk() (*string, bool)`

GetVersionIdOk returns a tuple with the VersionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionId

`func (o *DownloadOut) SetVersionId(v string)`

SetVersionId sets VersionId field to given value.


### GetExpiresAt

`func (o *DownloadOut) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *DownloadOut) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *DownloadOut) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### GetTarget

`func (o *DownloadOut) GetTarget() DownloadTargetOut`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *DownloadOut) GetTargetOk() (*DownloadTargetOut, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *DownloadOut) SetTarget(v DownloadTargetOut)`

SetTarget sets Target field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


