# ErrorResponseError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** | Stable machine-readable error code (see the error-catalog). |
**Details** | Pointer to **map[string]interface{}** | Error-code-specific context (optional). | [optional]
**Message** | **string** |  |

## Methods

### NewErrorResponseError

`func NewErrorResponseError(code string, message string, ) *ErrorResponseError`

NewErrorResponseError instantiates a new ErrorResponseError object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewErrorResponseErrorWithDefaults

`func NewErrorResponseErrorWithDefaults() *ErrorResponseError`

NewErrorResponseErrorWithDefaults instantiates a new ErrorResponseError object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *ErrorResponseError) GetCode() string`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *ErrorResponseError) GetCodeOk() (*string, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *ErrorResponseError) SetCode(v string)`

SetCode sets Code field to given value.


### GetDetails

`func (o *ErrorResponseError) GetDetails() map[string]interface{}`

GetDetails returns the Details field if non-nil, zero value otherwise.

### GetDetailsOk

`func (o *ErrorResponseError) GetDetailsOk() (*map[string]interface{}, bool)`

GetDetailsOk returns a tuple with the Details field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetails

`func (o *ErrorResponseError) SetDetails(v map[string]interface{})`

SetDetails sets Details field to given value.

### HasDetails

`func (o *ErrorResponseError) HasDetails() bool`

HasDetails returns a boolean if a field has been set.

### GetMessage

`func (o *ErrorResponseError) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *ErrorResponseError) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *ErrorResponseError) SetMessage(v string)`

SetMessage sets Message field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
