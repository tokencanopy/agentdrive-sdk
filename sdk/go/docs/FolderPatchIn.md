# FolderPatchIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Description** | Pointer to **NullableString** |  | [optional]
**InheritGrants** | Pointer to **NullableBool** |  | [optional]

## Methods

### NewFolderPatchIn

`func NewFolderPatchIn() *FolderPatchIn`

NewFolderPatchIn instantiates a new FolderPatchIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFolderPatchInWithDefaults

`func NewFolderPatchInWithDefaults() *FolderPatchIn`

NewFolderPatchInWithDefaults instantiates a new FolderPatchIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDescription

`func (o *FolderPatchIn) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *FolderPatchIn) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *FolderPatchIn) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *FolderPatchIn) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *FolderPatchIn) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *FolderPatchIn) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetInheritGrants

`func (o *FolderPatchIn) GetInheritGrants() bool`

GetInheritGrants returns the InheritGrants field if non-nil, zero value otherwise.

### GetInheritGrantsOk

`func (o *FolderPatchIn) GetInheritGrantsOk() (*bool, bool)`

GetInheritGrantsOk returns a tuple with the InheritGrants field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInheritGrants

`func (o *FolderPatchIn) SetInheritGrants(v bool)`

SetInheritGrants sets InheritGrants field to given value.

### HasInheritGrants

`func (o *FolderPatchIn) HasInheritGrants() bool`

HasInheritGrants returns a boolean if a field has been set.

### SetInheritGrantsNil

`func (o *FolderPatchIn) SetInheritGrantsNil(b bool)`

 SetInheritGrantsNil sets the value for InheritGrants to be an explicit nil

### UnsetInheritGrants
`func (o *FolderPatchIn) UnsetInheritGrants()`

UnsetInheritGrants ensures that no value is present for InheritGrants, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
