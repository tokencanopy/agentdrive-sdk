# CopyIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Path** | **string** |  | 
**Source** | Pointer to [**NullableArtifactSource**](ArtifactSource.md) |  | [optional] 
**FromGeneration** | Pointer to **NullableInt32** |  | [optional] 

## Methods

### NewCopyIn

`func NewCopyIn(path string, ) *CopyIn`

NewCopyIn instantiates a new CopyIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCopyInWithDefaults

`func NewCopyInWithDefaults() *CopyIn`

NewCopyInWithDefaults instantiates a new CopyIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPath

`func (o *CopyIn) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *CopyIn) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *CopyIn) SetPath(v string)`

SetPath sets Path field to given value.


### GetSource

`func (o *CopyIn) GetSource() ArtifactSource`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *CopyIn) GetSourceOk() (*ArtifactSource, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *CopyIn) SetSource(v ArtifactSource)`

SetSource sets Source field to given value.

### HasSource

`func (o *CopyIn) HasSource() bool`

HasSource returns a boolean if a field has been set.

### SetSourceNil

`func (o *CopyIn) SetSourceNil(b bool)`

 SetSourceNil sets the value for Source to be an explicit nil

### UnsetSource
`func (o *CopyIn) UnsetSource()`

UnsetSource ensures that no value is present for Source, not even an explicit nil
### GetFromGeneration

`func (o *CopyIn) GetFromGeneration() int32`

GetFromGeneration returns the FromGeneration field if non-nil, zero value otherwise.

### GetFromGenerationOk

`func (o *CopyIn) GetFromGenerationOk() (*int32, bool)`

GetFromGenerationOk returns a tuple with the FromGeneration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFromGeneration

`func (o *CopyIn) SetFromGeneration(v int32)`

SetFromGeneration sets FromGeneration field to given value.

### HasFromGeneration

`func (o *CopyIn) HasFromGeneration() bool`

HasFromGeneration returns a boolean if a field has been set.

### SetFromGenerationNil

`func (o *CopyIn) SetFromGenerationNil(b bool)`

 SetFromGenerationNil sets the value for FromGeneration to be an explicit nil

### UnsetFromGeneration
`func (o *CopyIn) UnsetFromGeneration()`

UnsetFromGeneration ensures that no value is present for FromGeneration, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


