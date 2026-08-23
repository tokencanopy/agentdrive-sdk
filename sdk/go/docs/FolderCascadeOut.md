# FolderCascadeOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Cascade** | **map[string]int32** |  |
**Folder** | [**FolderOut**](FolderOut.md) |  |

## Methods

### NewFolderCascadeOut

`func NewFolderCascadeOut(cascade map[string]int32, folder FolderOut, ) *FolderCascadeOut`

NewFolderCascadeOut instantiates a new FolderCascadeOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFolderCascadeOutWithDefaults

`func NewFolderCascadeOutWithDefaults() *FolderCascadeOut`

NewFolderCascadeOutWithDefaults instantiates a new FolderCascadeOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCascade

`func (o *FolderCascadeOut) GetCascade() map[string]int32`

GetCascade returns the Cascade field if non-nil, zero value otherwise.

### GetCascadeOk

`func (o *FolderCascadeOut) GetCascadeOk() (*map[string]int32, bool)`

GetCascadeOk returns a tuple with the Cascade field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCascade

`func (o *FolderCascadeOut) SetCascade(v map[string]int32)`

SetCascade sets Cascade field to given value.


### GetFolder

`func (o *FolderCascadeOut) GetFolder() FolderOut`

GetFolder returns the Folder field if non-nil, zero value otherwise.

### GetFolderOk

`func (o *FolderCascadeOut) GetFolderOk() (*FolderOut, bool)`

GetFolderOk returns a tuple with the Folder field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFolder

`func (o *FolderCascadeOut) SetFolder(v FolderOut)`

SetFolder sets Folder field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
