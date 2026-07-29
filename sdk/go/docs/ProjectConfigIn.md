# ProjectConfigIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AutoCompile** | Pointer to **bool** |  | [optional] [default to false]
**Engine** | Pointer to **NullableString** |  | [optional]
**Entrypoint** | **string** |  |

## Methods

### NewProjectConfigIn

`func NewProjectConfigIn(entrypoint string, ) *ProjectConfigIn`

NewProjectConfigIn instantiates a new ProjectConfigIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectConfigInWithDefaults

`func NewProjectConfigInWithDefaults() *ProjectConfigIn`

NewProjectConfigInWithDefaults instantiates a new ProjectConfigIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAutoCompile

`func (o *ProjectConfigIn) GetAutoCompile() bool`

GetAutoCompile returns the AutoCompile field if non-nil, zero value otherwise.

### GetAutoCompileOk

`func (o *ProjectConfigIn) GetAutoCompileOk() (*bool, bool)`

GetAutoCompileOk returns a tuple with the AutoCompile field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoCompile

`func (o *ProjectConfigIn) SetAutoCompile(v bool)`

SetAutoCompile sets AutoCompile field to given value.

### HasAutoCompile

`func (o *ProjectConfigIn) HasAutoCompile() bool`

HasAutoCompile returns a boolean if a field has been set.

### GetEngine

`func (o *ProjectConfigIn) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *ProjectConfigIn) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *ProjectConfigIn) SetEngine(v string)`

SetEngine sets Engine field to given value.

### HasEngine

`func (o *ProjectConfigIn) HasEngine() bool`

HasEngine returns a boolean if a field has been set.

### SetEngineNil

`func (o *ProjectConfigIn) SetEngineNil(b bool)`

 SetEngineNil sets the value for Engine to be an explicit nil

### UnsetEngine
`func (o *ProjectConfigIn) UnsetEngine()`

UnsetEngine ensures that no value is present for Engine, not even an explicit nil
### GetEntrypoint

`func (o *ProjectConfigIn) GetEntrypoint() string`

GetEntrypoint returns the Entrypoint field if non-nil, zero value otherwise.

### GetEntrypointOk

`func (o *ProjectConfigIn) GetEntrypointOk() (*string, bool)`

GetEntrypointOk returns a tuple with the Entrypoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntrypoint

`func (o *ProjectConfigIn) SetEntrypoint(v string)`

SetEntrypoint sets Entrypoint field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
