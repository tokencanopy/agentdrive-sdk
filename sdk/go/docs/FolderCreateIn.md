# FolderCreateIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**GrantInheritance** | Pointer to **string** |  | [optional] [default to "inherit"]
**Metadata** | Pointer to **map[string]interface{}** |  | [optional]
**Name** | **string** |  |
**ParentId** | **string** |  |

## Methods

### NewFolderCreateIn

`func NewFolderCreateIn(name string, parentId string, ) *FolderCreateIn`

NewFolderCreateIn instantiates a new FolderCreateIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFolderCreateInWithDefaults

`func NewFolderCreateInWithDefaults() *FolderCreateIn`

NewFolderCreateInWithDefaults instantiates a new FolderCreateIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGrantInheritance

`func (o *FolderCreateIn) GetGrantInheritance() string`

GetGrantInheritance returns the GrantInheritance field if non-nil, zero value otherwise.

### GetGrantInheritanceOk

`func (o *FolderCreateIn) GetGrantInheritanceOk() (*string, bool)`

GetGrantInheritanceOk returns a tuple with the GrantInheritance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantInheritance

`func (o *FolderCreateIn) SetGrantInheritance(v string)`

SetGrantInheritance sets GrantInheritance field to given value.

### HasGrantInheritance

`func (o *FolderCreateIn) HasGrantInheritance() bool`

HasGrantInheritance returns a boolean if a field has been set.

### GetMetadata

`func (o *FolderCreateIn) GetMetadata() map[string]interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *FolderCreateIn) GetMetadataOk() (*map[string]interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *FolderCreateIn) SetMetadata(v map[string]interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *FolderCreateIn) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetName

`func (o *FolderCreateIn) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *FolderCreateIn) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *FolderCreateIn) SetName(v string)`

SetName sets Name field to given value.


### GetParentId

`func (o *FolderCreateIn) GetParentId() string`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *FolderCreateIn) GetParentIdOk() (*string, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *FolderCreateIn) SetParentId(v string)`

SetParentId sets ParentId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
