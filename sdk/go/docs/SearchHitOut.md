# SearchHitOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ArtId** | **string** |  |
**ContentType** | **string** |  |
**DriveId** | **string** |  |
**FileType** | **string** |  |
**Labels** | Pointer to **[]string** |  | [optional]
**Path** | **string** |  |
**Score** | **float32** |  |
**Snippet** | **string** |  |
**UpdatedAt** | **time.Time** |  |
**Url** | **string** |  |
**VersionNumber** | **int32** |  |

## Methods

### NewSearchHitOut

`func NewSearchHitOut(artId string, contentType string, driveId string, fileType string, path string, score float32, snippet string, updatedAt time.Time, url string, versionNumber int32, ) *SearchHitOut`

NewSearchHitOut instantiates a new SearchHitOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSearchHitOutWithDefaults

`func NewSearchHitOutWithDefaults() *SearchHitOut`

NewSearchHitOutWithDefaults instantiates a new SearchHitOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetArtId

`func (o *SearchHitOut) GetArtId() string`

GetArtId returns the ArtId field if non-nil, zero value otherwise.

### GetArtIdOk

`func (o *SearchHitOut) GetArtIdOk() (*string, bool)`

GetArtIdOk returns a tuple with the ArtId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtId

`func (o *SearchHitOut) SetArtId(v string)`

SetArtId sets ArtId field to given value.


### GetContentType

`func (o *SearchHitOut) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *SearchHitOut) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *SearchHitOut) SetContentType(v string)`

SetContentType sets ContentType field to given value.


### GetDriveId

`func (o *SearchHitOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *SearchHitOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *SearchHitOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetFileType

`func (o *SearchHitOut) GetFileType() string`

GetFileType returns the FileType field if non-nil, zero value otherwise.

### GetFileTypeOk

`func (o *SearchHitOut) GetFileTypeOk() (*string, bool)`

GetFileTypeOk returns a tuple with the FileType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFileType

`func (o *SearchHitOut) SetFileType(v string)`

SetFileType sets FileType field to given value.


### GetLabels

`func (o *SearchHitOut) GetLabels() []string`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *SearchHitOut) GetLabelsOk() (*[]string, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *SearchHitOut) SetLabels(v []string)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *SearchHitOut) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetPath

`func (o *SearchHitOut) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *SearchHitOut) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *SearchHitOut) SetPath(v string)`

SetPath sets Path field to given value.


### GetScore

`func (o *SearchHitOut) GetScore() float32`

GetScore returns the Score field if non-nil, zero value otherwise.

### GetScoreOk

`func (o *SearchHitOut) GetScoreOk() (*float32, bool)`

GetScoreOk returns a tuple with the Score field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScore

`func (o *SearchHitOut) SetScore(v float32)`

SetScore sets Score field to given value.


### GetSnippet

`func (o *SearchHitOut) GetSnippet() string`

GetSnippet returns the Snippet field if non-nil, zero value otherwise.

### GetSnippetOk

`func (o *SearchHitOut) GetSnippetOk() (*string, bool)`

GetSnippetOk returns a tuple with the Snippet field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSnippet

`func (o *SearchHitOut) SetSnippet(v string)`

SetSnippet sets Snippet field to given value.


### GetUpdatedAt

`func (o *SearchHitOut) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *SearchHitOut) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *SearchHitOut) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetUrl

`func (o *SearchHitOut) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *SearchHitOut) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *SearchHitOut) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetVersionNumber

`func (o *SearchHitOut) GetVersionNumber() int32`

GetVersionNumber returns the VersionNumber field if non-nil, zero value otherwise.

### GetVersionNumberOk

`func (o *SearchHitOut) GetVersionNumberOk() (*int32, bool)`

GetVersionNumberOk returns a tuple with the VersionNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionNumber

`func (o *SearchHitOut) SetVersionNumber(v int32)`

SetVersionNumber sets VersionNumber field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
