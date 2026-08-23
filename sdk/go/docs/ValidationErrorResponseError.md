# ValidationErrorResponseError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** |  |
**Details** | Pointer to [**ValidationErrorResponseErrorDetails**](ValidationErrorResponseErrorDetails.md) |  | [optional]
**Message** | **string** |  |

## Methods

### NewValidationErrorResponseError

`func NewValidationErrorResponseError(code string, message string, ) *ValidationErrorResponseError`

NewValidationErrorResponseError instantiates a new ValidationErrorResponseError object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewValidationErrorResponseErrorWithDefaults

`func NewValidationErrorResponseErrorWithDefaults() *ValidationErrorResponseError`

NewValidationErrorResponseErrorWithDefaults instantiates a new ValidationErrorResponseError object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *ValidationErrorResponseError) GetCode() string`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *ValidationErrorResponseError) GetCodeOk() (*string, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *ValidationErrorResponseError) SetCode(v string)`

SetCode sets Code field to given value.


### GetDetails

`func (o *ValidationErrorResponseError) GetDetails() ValidationErrorResponseErrorDetails`

GetDetails returns the Details field if non-nil, zero value otherwise.

### GetDetailsOk

`func (o *ValidationErrorResponseError) GetDetailsOk() (*ValidationErrorResponseErrorDetails, bool)`

GetDetailsOk returns a tuple with the Details field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetails

`func (o *ValidationErrorResponseError) SetDetails(v ValidationErrorResponseErrorDetails)`

SetDetails sets Details field to given value.

### HasDetails

`func (o *ValidationErrorResponseError) HasDetails() bool`

HasDetails returns a boolean if a field has been set.

### GetMessage

`func (o *ValidationErrorResponseError) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *ValidationErrorResponseError) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *ValidationErrorResponseError) SetMessage(v string)`

SetMessage sets Message field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
