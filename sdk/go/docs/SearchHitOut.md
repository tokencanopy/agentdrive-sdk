# SearchHitOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**DriveId** | **string** |  | 
**ParentId** | **NullableString** |  | 
**Name** | **string** |  | 
**VersionId** | **NullableString** |  | 
**Rank** | **float32** |  | 
**Snippet** | **string** | HTML-safe highlighted excerpt. The ONLY markup it may contain is the server&#39;s own &lt;mark&gt;...&lt;/mark&gt; highlight pair; artifact content is entity-escaped, so this may be rendered as HTML. | 
**ContentType** | **NullableString** |  | 
**UpdatedAt** | **time.Time** |  | 

## Methods

### NewSearchHitOut

`func NewSearchHitOut(id string, driveId string, parentId NullableString, name string, versionId NullableString, rank float32, snippet string, contentType NullableString, updatedAt time.Time, ) *SearchHitOut`

NewSearchHitOut instantiates a new SearchHitOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSearchHitOutWithDefaults

`func NewSearchHitOutWithDefaults() *SearchHitOut`

NewSearchHitOutWithDefaults instantiates a new SearchHitOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SearchHitOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SearchHitOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SearchHitOut) SetId(v string)`

SetId sets Id field to given value.


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


### GetParentId

`func (o *SearchHitOut) GetParentId() string`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *SearchHitOut) GetParentIdOk() (*string, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *SearchHitOut) SetParentId(v string)`

SetParentId sets ParentId field to given value.


### SetParentIdNil

`func (o *SearchHitOut) SetParentIdNil(b bool)`

 SetParentIdNil sets the value for ParentId to be an explicit nil

### UnsetParentId
`func (o *SearchHitOut) UnsetParentId()`

UnsetParentId ensures that no value is present for ParentId, not even an explicit nil
### GetName

`func (o *SearchHitOut) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SearchHitOut) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SearchHitOut) SetName(v string)`

SetName sets Name field to given value.


### GetVersionId

`func (o *SearchHitOut) GetVersionId() string`

GetVersionId returns the VersionId field if non-nil, zero value otherwise.

### GetVersionIdOk

`func (o *SearchHitOut) GetVersionIdOk() (*string, bool)`

GetVersionIdOk returns a tuple with the VersionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionId

`func (o *SearchHitOut) SetVersionId(v string)`

SetVersionId sets VersionId field to given value.


### SetVersionIdNil

`func (o *SearchHitOut) SetVersionIdNil(b bool)`

 SetVersionIdNil sets the value for VersionId to be an explicit nil

### UnsetVersionId
`func (o *SearchHitOut) UnsetVersionId()`

UnsetVersionId ensures that no value is present for VersionId, not even an explicit nil
### GetRank

`func (o *SearchHitOut) GetRank() float32`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *SearchHitOut) GetRankOk() (*float32, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *SearchHitOut) SetRank(v float32)`

SetRank sets Rank field to given value.


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


### SetContentTypeNil

`func (o *SearchHitOut) SetContentTypeNil(b bool)`

 SetContentTypeNil sets the value for ContentType to be an explicit nil

### UnsetContentType
`func (o *SearchHitOut) UnsetContentType()`

UnsetContentType ensures that no value is present for ContentType, not even an explicit nil
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



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


