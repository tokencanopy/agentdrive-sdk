# FindHitOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ArtId** | **string** |  |
**CharEnd** | Pointer to **NullableInt32** |  | [optional]
**CharStart** | Pointer to **NullableInt32** |  | [optional]
**ContentType** | **string** |  |
**DriveId** | **string** |  |
**FileType** | **string** |  |
**Labels** | Pointer to **[]string** |  | [optional]
**Modality** | **string** |  |
**Ord** | **int32** |  |
**PageEnd** | Pointer to **NullableInt32** |  | [optional]
**PageStart** | Pointer to **NullableInt32** |  | [optional]
**Path** | **string** |  |
**RankLexical** | Pointer to **NullableInt32** |  | [optional]
**RankSemantic** | Pointer to **NullableInt32** |  | [optional]
**Score** | **float32** |  |
**Snippet** | **string** |  |
**Text** | **string** |  |
**TimeEndMs** | Pointer to **NullableInt32** |  | [optional]
**TimeStartMs** | Pointer to **NullableInt32** |  | [optional]
**UpdatedAt** | **time.Time** |  |
**Url** | **string** |  |
**VersionNumber** | **int32** |  |

## Methods

### NewFindHitOut

`func NewFindHitOut(artId string, contentType string, driveId string, fileType string, modality string, ord int32, path string, score float32, snippet string, text string, updatedAt time.Time, url string, versionNumber int32, ) *FindHitOut`

NewFindHitOut instantiates a new FindHitOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFindHitOutWithDefaults

`func NewFindHitOutWithDefaults() *FindHitOut`

NewFindHitOutWithDefaults instantiates a new FindHitOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetArtId

`func (o *FindHitOut) GetArtId() string`

GetArtId returns the ArtId field if non-nil, zero value otherwise.

### GetArtIdOk

`func (o *FindHitOut) GetArtIdOk() (*string, bool)`

GetArtIdOk returns a tuple with the ArtId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArtId

`func (o *FindHitOut) SetArtId(v string)`

SetArtId sets ArtId field to given value.


### GetCharEnd

`func (o *FindHitOut) GetCharEnd() int32`

GetCharEnd returns the CharEnd field if non-nil, zero value otherwise.

### GetCharEndOk

`func (o *FindHitOut) GetCharEndOk() (*int32, bool)`

GetCharEndOk returns a tuple with the CharEnd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCharEnd

`func (o *FindHitOut) SetCharEnd(v int32)`

SetCharEnd sets CharEnd field to given value.

### HasCharEnd

`func (o *FindHitOut) HasCharEnd() bool`

HasCharEnd returns a boolean if a field has been set.

### SetCharEndNil

`func (o *FindHitOut) SetCharEndNil(b bool)`

 SetCharEndNil sets the value for CharEnd to be an explicit nil

### UnsetCharEnd
`func (o *FindHitOut) UnsetCharEnd()`

UnsetCharEnd ensures that no value is present for CharEnd, not even an explicit nil
### GetCharStart

`func (o *FindHitOut) GetCharStart() int32`

GetCharStart returns the CharStart field if non-nil, zero value otherwise.

### GetCharStartOk

`func (o *FindHitOut) GetCharStartOk() (*int32, bool)`

GetCharStartOk returns a tuple with the CharStart field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCharStart

`func (o *FindHitOut) SetCharStart(v int32)`

SetCharStart sets CharStart field to given value.

### HasCharStart

`func (o *FindHitOut) HasCharStart() bool`

HasCharStart returns a boolean if a field has been set.

### SetCharStartNil

`func (o *FindHitOut) SetCharStartNil(b bool)`

 SetCharStartNil sets the value for CharStart to be an explicit nil

### UnsetCharStart
`func (o *FindHitOut) UnsetCharStart()`

UnsetCharStart ensures that no value is present for CharStart, not even an explicit nil
### GetContentType

`func (o *FindHitOut) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *FindHitOut) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *FindHitOut) SetContentType(v string)`

SetContentType sets ContentType field to given value.


### GetDriveId

`func (o *FindHitOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *FindHitOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *FindHitOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetFileType

`func (o *FindHitOut) GetFileType() string`

GetFileType returns the FileType field if non-nil, zero value otherwise.

### GetFileTypeOk

`func (o *FindHitOut) GetFileTypeOk() (*string, bool)`

GetFileTypeOk returns a tuple with the FileType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFileType

`func (o *FindHitOut) SetFileType(v string)`

SetFileType sets FileType field to given value.


### GetLabels

`func (o *FindHitOut) GetLabels() []string`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *FindHitOut) GetLabelsOk() (*[]string, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *FindHitOut) SetLabels(v []string)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *FindHitOut) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetModality

`func (o *FindHitOut) GetModality() string`

GetModality returns the Modality field if non-nil, zero value otherwise.

### GetModalityOk

`func (o *FindHitOut) GetModalityOk() (*string, bool)`

GetModalityOk returns a tuple with the Modality field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModality

`func (o *FindHitOut) SetModality(v string)`

SetModality sets Modality field to given value.


### GetOrd

`func (o *FindHitOut) GetOrd() int32`

GetOrd returns the Ord field if non-nil, zero value otherwise.

### GetOrdOk

`func (o *FindHitOut) GetOrdOk() (*int32, bool)`

GetOrdOk returns a tuple with the Ord field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrd

`func (o *FindHitOut) SetOrd(v int32)`

SetOrd sets Ord field to given value.


### GetPageEnd

`func (o *FindHitOut) GetPageEnd() int32`

GetPageEnd returns the PageEnd field if non-nil, zero value otherwise.

### GetPageEndOk

`func (o *FindHitOut) GetPageEndOk() (*int32, bool)`

GetPageEndOk returns a tuple with the PageEnd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPageEnd

`func (o *FindHitOut) SetPageEnd(v int32)`

SetPageEnd sets PageEnd field to given value.

### HasPageEnd

`func (o *FindHitOut) HasPageEnd() bool`

HasPageEnd returns a boolean if a field has been set.

### SetPageEndNil

`func (o *FindHitOut) SetPageEndNil(b bool)`

 SetPageEndNil sets the value for PageEnd to be an explicit nil

### UnsetPageEnd
`func (o *FindHitOut) UnsetPageEnd()`

UnsetPageEnd ensures that no value is present for PageEnd, not even an explicit nil
### GetPageStart

`func (o *FindHitOut) GetPageStart() int32`

GetPageStart returns the PageStart field if non-nil, zero value otherwise.

### GetPageStartOk

`func (o *FindHitOut) GetPageStartOk() (*int32, bool)`

GetPageStartOk returns a tuple with the PageStart field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPageStart

`func (o *FindHitOut) SetPageStart(v int32)`

SetPageStart sets PageStart field to given value.

### HasPageStart

`func (o *FindHitOut) HasPageStart() bool`

HasPageStart returns a boolean if a field has been set.

### SetPageStartNil

`func (o *FindHitOut) SetPageStartNil(b bool)`

 SetPageStartNil sets the value for PageStart to be an explicit nil

### UnsetPageStart
`func (o *FindHitOut) UnsetPageStart()`

UnsetPageStart ensures that no value is present for PageStart, not even an explicit nil
### GetPath

`func (o *FindHitOut) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *FindHitOut) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *FindHitOut) SetPath(v string)`

SetPath sets Path field to given value.


### GetRankLexical

`func (o *FindHitOut) GetRankLexical() int32`

GetRankLexical returns the RankLexical field if non-nil, zero value otherwise.

### GetRankLexicalOk

`func (o *FindHitOut) GetRankLexicalOk() (*int32, bool)`

GetRankLexicalOk returns a tuple with the RankLexical field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRankLexical

`func (o *FindHitOut) SetRankLexical(v int32)`

SetRankLexical sets RankLexical field to given value.

### HasRankLexical

`func (o *FindHitOut) HasRankLexical() bool`

HasRankLexical returns a boolean if a field has been set.

### SetRankLexicalNil

`func (o *FindHitOut) SetRankLexicalNil(b bool)`

 SetRankLexicalNil sets the value for RankLexical to be an explicit nil

### UnsetRankLexical
`func (o *FindHitOut) UnsetRankLexical()`

UnsetRankLexical ensures that no value is present for RankLexical, not even an explicit nil
### GetRankSemantic

`func (o *FindHitOut) GetRankSemantic() int32`

GetRankSemantic returns the RankSemantic field if non-nil, zero value otherwise.

### GetRankSemanticOk

`func (o *FindHitOut) GetRankSemanticOk() (*int32, bool)`

GetRankSemanticOk returns a tuple with the RankSemantic field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRankSemantic

`func (o *FindHitOut) SetRankSemantic(v int32)`

SetRankSemantic sets RankSemantic field to given value.

### HasRankSemantic

`func (o *FindHitOut) HasRankSemantic() bool`

HasRankSemantic returns a boolean if a field has been set.

### SetRankSemanticNil

`func (o *FindHitOut) SetRankSemanticNil(b bool)`

 SetRankSemanticNil sets the value for RankSemantic to be an explicit nil

### UnsetRankSemantic
`func (o *FindHitOut) UnsetRankSemantic()`

UnsetRankSemantic ensures that no value is present for RankSemantic, not even an explicit nil
### GetScore

`func (o *FindHitOut) GetScore() float32`

GetScore returns the Score field if non-nil, zero value otherwise.

### GetScoreOk

`func (o *FindHitOut) GetScoreOk() (*float32, bool)`

GetScoreOk returns a tuple with the Score field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScore

`func (o *FindHitOut) SetScore(v float32)`

SetScore sets Score field to given value.


### GetSnippet

`func (o *FindHitOut) GetSnippet() string`

GetSnippet returns the Snippet field if non-nil, zero value otherwise.

### GetSnippetOk

`func (o *FindHitOut) GetSnippetOk() (*string, bool)`

GetSnippetOk returns a tuple with the Snippet field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSnippet

`func (o *FindHitOut) SetSnippet(v string)`

SetSnippet sets Snippet field to given value.


### GetText

`func (o *FindHitOut) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *FindHitOut) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *FindHitOut) SetText(v string)`

SetText sets Text field to given value.


### GetTimeEndMs

`func (o *FindHitOut) GetTimeEndMs() int32`

GetTimeEndMs returns the TimeEndMs field if non-nil, zero value otherwise.

### GetTimeEndMsOk

`func (o *FindHitOut) GetTimeEndMsOk() (*int32, bool)`

GetTimeEndMsOk returns a tuple with the TimeEndMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeEndMs

`func (o *FindHitOut) SetTimeEndMs(v int32)`

SetTimeEndMs sets TimeEndMs field to given value.

### HasTimeEndMs

`func (o *FindHitOut) HasTimeEndMs() bool`

HasTimeEndMs returns a boolean if a field has been set.

### SetTimeEndMsNil

`func (o *FindHitOut) SetTimeEndMsNil(b bool)`

 SetTimeEndMsNil sets the value for TimeEndMs to be an explicit nil

### UnsetTimeEndMs
`func (o *FindHitOut) UnsetTimeEndMs()`

UnsetTimeEndMs ensures that no value is present for TimeEndMs, not even an explicit nil
### GetTimeStartMs

`func (o *FindHitOut) GetTimeStartMs() int32`

GetTimeStartMs returns the TimeStartMs field if non-nil, zero value otherwise.

### GetTimeStartMsOk

`func (o *FindHitOut) GetTimeStartMsOk() (*int32, bool)`

GetTimeStartMsOk returns a tuple with the TimeStartMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimeStartMs

`func (o *FindHitOut) SetTimeStartMs(v int32)`

SetTimeStartMs sets TimeStartMs field to given value.

### HasTimeStartMs

`func (o *FindHitOut) HasTimeStartMs() bool`

HasTimeStartMs returns a boolean if a field has been set.

### SetTimeStartMsNil

`func (o *FindHitOut) SetTimeStartMsNil(b bool)`

 SetTimeStartMsNil sets the value for TimeStartMs to be an explicit nil

### UnsetTimeStartMs
`func (o *FindHitOut) UnsetTimeStartMs()`

UnsetTimeStartMs ensures that no value is present for TimeStartMs, not even an explicit nil
### GetUpdatedAt

`func (o *FindHitOut) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *FindHitOut) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *FindHitOut) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetUrl

`func (o *FindHitOut) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *FindHitOut) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *FindHitOut) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetVersionNumber

`func (o *FindHitOut) GetVersionNumber() int32`

GetVersionNumber returns the VersionNumber field if non-nil, zero value otherwise.

### GetVersionNumberOk

`func (o *FindHitOut) GetVersionNumberOk() (*int32, bool)`

GetVersionNumberOk returns a tuple with the VersionNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionNumber

`func (o *FindHitOut) SetVersionNumber(v int32)`

SetVersionNumber sets VersionNumber field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
