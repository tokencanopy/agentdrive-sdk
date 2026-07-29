# ValidationErrorBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** |  |
**Fields** | [**[]ValidationIssue**](ValidationIssue.md) |  |
**Message** | **string** |  |

## Methods

### NewValidationErrorBody

`func NewValidationErrorBody(code string, fields []ValidationIssue, message string, ) *ValidationErrorBody`

NewValidationErrorBody instantiates a new ValidationErrorBody object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewValidationErrorBodyWithDefaults

`func NewValidationErrorBodyWithDefaults() *ValidationErrorBody`

NewValidationErrorBodyWithDefaults instantiates a new ValidationErrorBody object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *ValidationErrorBody) GetCode() string`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *ValidationErrorBody) GetCodeOk() (*string, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *ValidationErrorBody) SetCode(v string)`

SetCode sets Code field to given value.


### GetFields

`func (o *ValidationErrorBody) GetFields() []ValidationIssue`

GetFields returns the Fields field if non-nil, zero value otherwise.

### GetFieldsOk

`func (o *ValidationErrorBody) GetFieldsOk() (*[]ValidationIssue, bool)`

GetFieldsOk returns a tuple with the Fields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFields

`func (o *ValidationErrorBody) SetFields(v []ValidationIssue)`

SetFields sets Fields field to given value.


### GetMessage

`func (o *ValidationErrorBody) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *ValidationErrorBody) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *ValidationErrorBody) SetMessage(v string)`

SetMessage sets Message field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
