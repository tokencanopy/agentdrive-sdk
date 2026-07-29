# CompileJobOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CacheHit** | **bool** |  |
**Diagnostics** | Pointer to [**[]CompileDiagnosticOut**](CompileDiagnosticOut.md) |  | [optional]
**DurationMs** | Pointer to **NullableInt32** |  | [optional]
**Engine** | **string** |  |
**JobId** | **string** |  |
**LogsUrl** | Pointer to **NullableString** |  | [optional]
**Output** | Pointer to **map[string]interface{}** |  | [optional]
**Status** | **string** |  |
**Task** | **string** |  |

## Methods

### NewCompileJobOut

`func NewCompileJobOut(cacheHit bool, engine string, jobId string, status string, task string, ) *CompileJobOut`

NewCompileJobOut instantiates a new CompileJobOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCompileJobOutWithDefaults

`func NewCompileJobOutWithDefaults() *CompileJobOut`

NewCompileJobOutWithDefaults instantiates a new CompileJobOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCacheHit

`func (o *CompileJobOut) GetCacheHit() bool`

GetCacheHit returns the CacheHit field if non-nil, zero value otherwise.

### GetCacheHitOk

`func (o *CompileJobOut) GetCacheHitOk() (*bool, bool)`

GetCacheHitOk returns a tuple with the CacheHit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCacheHit

`func (o *CompileJobOut) SetCacheHit(v bool)`

SetCacheHit sets CacheHit field to given value.


### GetDiagnostics

`func (o *CompileJobOut) GetDiagnostics() []CompileDiagnosticOut`

GetDiagnostics returns the Diagnostics field if non-nil, zero value otherwise.

### GetDiagnosticsOk

`func (o *CompileJobOut) GetDiagnosticsOk() (*[]CompileDiagnosticOut, bool)`

GetDiagnosticsOk returns a tuple with the Diagnostics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiagnostics

`func (o *CompileJobOut) SetDiagnostics(v []CompileDiagnosticOut)`

SetDiagnostics sets Diagnostics field to given value.

### HasDiagnostics

`func (o *CompileJobOut) HasDiagnostics() bool`

HasDiagnostics returns a boolean if a field has been set.

### GetDurationMs

`func (o *CompileJobOut) GetDurationMs() int32`

GetDurationMs returns the DurationMs field if non-nil, zero value otherwise.

### GetDurationMsOk

`func (o *CompileJobOut) GetDurationMsOk() (*int32, bool)`

GetDurationMsOk returns a tuple with the DurationMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDurationMs

`func (o *CompileJobOut) SetDurationMs(v int32)`

SetDurationMs sets DurationMs field to given value.

### HasDurationMs

`func (o *CompileJobOut) HasDurationMs() bool`

HasDurationMs returns a boolean if a field has been set.

### SetDurationMsNil

`func (o *CompileJobOut) SetDurationMsNil(b bool)`

 SetDurationMsNil sets the value for DurationMs to be an explicit nil

### UnsetDurationMs
`func (o *CompileJobOut) UnsetDurationMs()`

UnsetDurationMs ensures that no value is present for DurationMs, not even an explicit nil
### GetEngine

`func (o *CompileJobOut) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *CompileJobOut) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *CompileJobOut) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetJobId

`func (o *CompileJobOut) GetJobId() string`

GetJobId returns the JobId field if non-nil, zero value otherwise.

### GetJobIdOk

`func (o *CompileJobOut) GetJobIdOk() (*string, bool)`

GetJobIdOk returns a tuple with the JobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobId

`func (o *CompileJobOut) SetJobId(v string)`

SetJobId sets JobId field to given value.


### GetLogsUrl

`func (o *CompileJobOut) GetLogsUrl() string`

GetLogsUrl returns the LogsUrl field if non-nil, zero value otherwise.

### GetLogsUrlOk

`func (o *CompileJobOut) GetLogsUrlOk() (*string, bool)`

GetLogsUrlOk returns a tuple with the LogsUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogsUrl

`func (o *CompileJobOut) SetLogsUrl(v string)`

SetLogsUrl sets LogsUrl field to given value.

### HasLogsUrl

`func (o *CompileJobOut) HasLogsUrl() bool`

HasLogsUrl returns a boolean if a field has been set.

### SetLogsUrlNil

`func (o *CompileJobOut) SetLogsUrlNil(b bool)`

 SetLogsUrlNil sets the value for LogsUrl to be an explicit nil

### UnsetLogsUrl
`func (o *CompileJobOut) UnsetLogsUrl()`

UnsetLogsUrl ensures that no value is present for LogsUrl, not even an explicit nil
### GetOutput

`func (o *CompileJobOut) GetOutput() map[string]interface{}`

GetOutput returns the Output field if non-nil, zero value otherwise.

### GetOutputOk

`func (o *CompileJobOut) GetOutputOk() (*map[string]interface{}, bool)`

GetOutputOk returns a tuple with the Output field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutput

`func (o *CompileJobOut) SetOutput(v map[string]interface{})`

SetOutput sets Output field to given value.

### HasOutput

`func (o *CompileJobOut) HasOutput() bool`

HasOutput returns a boolean if a field has been set.

### SetOutputNil

`func (o *CompileJobOut) SetOutputNil(b bool)`

 SetOutputNil sets the value for Output to be an explicit nil

### UnsetOutput
`func (o *CompileJobOut) UnsetOutput()`

UnsetOutput ensures that no value is present for Output, not even an explicit nil
### GetStatus

`func (o *CompileJobOut) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *CompileJobOut) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *CompileJobOut) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetTask

`func (o *CompileJobOut) GetTask() string`

GetTask returns the Task field if non-nil, zero value otherwise.

### GetTaskOk

`func (o *CompileJobOut) GetTaskOk() (*string, bool)`

GetTaskOk returns a tuple with the Task field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTask

`func (o *CompileJobOut) SetTask(v string)`

SetTask sets Task field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
