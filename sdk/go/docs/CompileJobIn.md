# CompileJobIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Options** | Pointer to [**CompileOptions**](CompileOptions.md) |  | [optional]
**Task** | Pointer to **string** |  | [optional] [default to "latex.compile"]

## Methods

### NewCompileJobIn

`func NewCompileJobIn() *CompileJobIn`

NewCompileJobIn instantiates a new CompileJobIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCompileJobInWithDefaults

`func NewCompileJobInWithDefaults() *CompileJobIn`

NewCompileJobInWithDefaults instantiates a new CompileJobIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOptions

`func (o *CompileJobIn) GetOptions() CompileOptions`

GetOptions returns the Options field if non-nil, zero value otherwise.

### GetOptionsOk

`func (o *CompileJobIn) GetOptionsOk() (*CompileOptions, bool)`

GetOptionsOk returns a tuple with the Options field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOptions

`func (o *CompileJobIn) SetOptions(v CompileOptions)`

SetOptions sets Options field to given value.

### HasOptions

`func (o *CompileJobIn) HasOptions() bool`

HasOptions returns a boolean if a field has been set.

### GetTask

`func (o *CompileJobIn) GetTask() string`

GetTask returns the Task field if non-nil, zero value otherwise.

### GetTaskOk

`func (o *CompileJobIn) GetTaskOk() (*string, bool)`

GetTaskOk returns a tuple with the Task field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTask

`func (o *CompileJobIn) SetTask(v string)`

SetTask sets Task field to given value.

### HasTask

`func (o *CompileJobIn) HasTask() bool`

HasTask returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
