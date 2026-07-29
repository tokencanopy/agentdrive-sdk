# CompileDiagnosticOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Category** | Pointer to **NullableString** |  | [optional]
**File** | Pointer to **NullableString** |  | [optional]
**Line** | Pointer to **NullableInt32** |  | [optional]
**Message** | **string** |  |
**Severity** | **string** |  |
**Suggestion** | Pointer to **NullableString** |  | [optional]

## Methods

### NewCompileDiagnosticOut

`func NewCompileDiagnosticOut(message string, severity string, ) *CompileDiagnosticOut`

NewCompileDiagnosticOut instantiates a new CompileDiagnosticOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCompileDiagnosticOutWithDefaults

`func NewCompileDiagnosticOutWithDefaults() *CompileDiagnosticOut`

NewCompileDiagnosticOutWithDefaults instantiates a new CompileDiagnosticOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCategory

`func (o *CompileDiagnosticOut) GetCategory() string`

GetCategory returns the Category field if non-nil, zero value otherwise.

### GetCategoryOk

`func (o *CompileDiagnosticOut) GetCategoryOk() (*string, bool)`

GetCategoryOk returns a tuple with the Category field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategory

`func (o *CompileDiagnosticOut) SetCategory(v string)`

SetCategory sets Category field to given value.

### HasCategory

`func (o *CompileDiagnosticOut) HasCategory() bool`

HasCategory returns a boolean if a field has been set.

### SetCategoryNil

`func (o *CompileDiagnosticOut) SetCategoryNil(b bool)`

 SetCategoryNil sets the value for Category to be an explicit nil

### UnsetCategory
`func (o *CompileDiagnosticOut) UnsetCategory()`

UnsetCategory ensures that no value is present for Category, not even an explicit nil
### GetFile

`func (o *CompileDiagnosticOut) GetFile() string`

GetFile returns the File field if non-nil, zero value otherwise.

### GetFileOk

`func (o *CompileDiagnosticOut) GetFileOk() (*string, bool)`

GetFileOk returns a tuple with the File field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFile

`func (o *CompileDiagnosticOut) SetFile(v string)`

SetFile sets File field to given value.

### HasFile

`func (o *CompileDiagnosticOut) HasFile() bool`

HasFile returns a boolean if a field has been set.

### SetFileNil

`func (o *CompileDiagnosticOut) SetFileNil(b bool)`

 SetFileNil sets the value for File to be an explicit nil

### UnsetFile
`func (o *CompileDiagnosticOut) UnsetFile()`

UnsetFile ensures that no value is present for File, not even an explicit nil
### GetLine

`func (o *CompileDiagnosticOut) GetLine() int32`

GetLine returns the Line field if non-nil, zero value otherwise.

### GetLineOk

`func (o *CompileDiagnosticOut) GetLineOk() (*int32, bool)`

GetLineOk returns a tuple with the Line field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLine

`func (o *CompileDiagnosticOut) SetLine(v int32)`

SetLine sets Line field to given value.

### HasLine

`func (o *CompileDiagnosticOut) HasLine() bool`

HasLine returns a boolean if a field has been set.

### SetLineNil

`func (o *CompileDiagnosticOut) SetLineNil(b bool)`

 SetLineNil sets the value for Line to be an explicit nil

### UnsetLine
`func (o *CompileDiagnosticOut) UnsetLine()`

UnsetLine ensures that no value is present for Line, not even an explicit nil
### GetMessage

`func (o *CompileDiagnosticOut) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *CompileDiagnosticOut) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *CompileDiagnosticOut) SetMessage(v string)`

SetMessage sets Message field to given value.


### GetSeverity

`func (o *CompileDiagnosticOut) GetSeverity() string`

GetSeverity returns the Severity field if non-nil, zero value otherwise.

### GetSeverityOk

`func (o *CompileDiagnosticOut) GetSeverityOk() (*string, bool)`

GetSeverityOk returns a tuple with the Severity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeverity

`func (o *CompileDiagnosticOut) SetSeverity(v string)`

SetSeverity sets Severity field to given value.


### GetSuggestion

`func (o *CompileDiagnosticOut) GetSuggestion() string`

GetSuggestion returns the Suggestion field if non-nil, zero value otherwise.

### GetSuggestionOk

`func (o *CompileDiagnosticOut) GetSuggestionOk() (*string, bool)`

GetSuggestionOk returns a tuple with the Suggestion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuggestion

`func (o *CompileDiagnosticOut) SetSuggestion(v string)`

SetSuggestion sets Suggestion field to given value.

### HasSuggestion

`func (o *CompileDiagnosticOut) HasSuggestion() bool`

HasSuggestion returns a boolean if a field has been set.

### SetSuggestionNil

`func (o *CompileDiagnosticOut) SetSuggestionNil(b bool)`

 SetSuggestionNil sets the value for Suggestion to be an explicit nil

### UnsetSuggestion
`func (o *CompileDiagnosticOut) UnsetSuggestion()`

UnsetSuggestion ensures that no value is present for Suggestion, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
