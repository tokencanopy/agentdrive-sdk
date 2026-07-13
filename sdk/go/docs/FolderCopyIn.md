# FolderCopyIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Path** | **string** |  | 
**FromMetageneration** | Pointer to **NullableInt32** |  | [optional] 

## Methods

### NewFolderCopyIn

`func NewFolderCopyIn(path string, ) *FolderCopyIn`

NewFolderCopyIn instantiates a new FolderCopyIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFolderCopyInWithDefaults

`func NewFolderCopyInWithDefaults() *FolderCopyIn`

NewFolderCopyInWithDefaults instantiates a new FolderCopyIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPath

`func (o *FolderCopyIn) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *FolderCopyIn) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *FolderCopyIn) SetPath(v string)`

SetPath sets Path field to given value.


### GetFromMetageneration

`func (o *FolderCopyIn) GetFromMetageneration() int32`

GetFromMetageneration returns the FromMetageneration field if non-nil, zero value otherwise.

### GetFromMetagenerationOk

`func (o *FolderCopyIn) GetFromMetagenerationOk() (*int32, bool)`

GetFromMetagenerationOk returns a tuple with the FromMetageneration field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFromMetageneration

`func (o *FolderCopyIn) SetFromMetageneration(v int32)`

SetFromMetageneration sets FromMetageneration field to given value.

### HasFromMetageneration

`func (o *FolderCopyIn) HasFromMetageneration() bool`

HasFromMetageneration returns a boolean if a field has been set.

### SetFromMetagenerationNil

`func (o *FolderCopyIn) SetFromMetagenerationNil(b bool)`

 SetFromMetagenerationNil sets the value for FromMetageneration to be an explicit nil

### UnsetFromMetageneration
`func (o *FolderCopyIn) UnsetFromMetageneration()`

UnsetFromMetageneration ensures that no value is present for FromMetageneration, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


