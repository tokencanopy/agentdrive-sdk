# CompileOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Engine** | Pointer to **NullableString** |  | [optional]
**Entrypoint** | Pointer to **NullableString** |  | [optional]
**Wait** | Pointer to **bool** |  | [optional] [default to false]

## Methods

### NewCompileOptions

`func NewCompileOptions() *CompileOptions`

NewCompileOptions instantiates a new CompileOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCompileOptionsWithDefaults

`func NewCompileOptionsWithDefaults() *CompileOptions`

NewCompileOptionsWithDefaults instantiates a new CompileOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEngine

`func (o *CompileOptions) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *CompileOptions) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *CompileOptions) SetEngine(v string)`

SetEngine sets Engine field to given value.

### HasEngine

`func (o *CompileOptions) HasEngine() bool`

HasEngine returns a boolean if a field has been set.

### SetEngineNil

`func (o *CompileOptions) SetEngineNil(b bool)`

 SetEngineNil sets the value for Engine to be an explicit nil

### UnsetEngine
`func (o *CompileOptions) UnsetEngine()`

UnsetEngine ensures that no value is present for Engine, not even an explicit nil
### GetEntrypoint

`func (o *CompileOptions) GetEntrypoint() string`

GetEntrypoint returns the Entrypoint field if non-nil, zero value otherwise.

### GetEntrypointOk

`func (o *CompileOptions) GetEntrypointOk() (*string, bool)`

GetEntrypointOk returns a tuple with the Entrypoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntrypoint

`func (o *CompileOptions) SetEntrypoint(v string)`

SetEntrypoint sets Entrypoint field to given value.

### HasEntrypoint

`func (o *CompileOptions) HasEntrypoint() bool`

HasEntrypoint returns a boolean if a field has been set.

### SetEntrypointNil

`func (o *CompileOptions) SetEntrypointNil(b bool)`

 SetEntrypointNil sets the value for Entrypoint to be an explicit nil

### UnsetEntrypoint
`func (o *CompileOptions) UnsetEntrypoint()`

UnsetEntrypoint ensures that no value is present for Entrypoint, not even an explicit nil
### GetWait

`func (o *CompileOptions) GetWait() bool`

GetWait returns the Wait field if non-nil, zero value otherwise.

### GetWaitOk

`func (o *CompileOptions) GetWaitOk() (*bool, bool)`

GetWaitOk returns a tuple with the Wait field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWait

`func (o *CompileOptions) SetWait(v bool)`

SetWait sets Wait field to given value.

### HasWait

`func (o *CompileOptions) HasWait() bool`

HasWait returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
