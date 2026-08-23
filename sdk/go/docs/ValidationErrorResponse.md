# ValidationErrorResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Error** | [**ValidationErrorResponseError**](ValidationErrorResponseError.md) |  |

## Methods

### NewValidationErrorResponse

`func NewValidationErrorResponse(error_ ValidationErrorResponseError, ) *ValidationErrorResponse`

NewValidationErrorResponse instantiates a new ValidationErrorResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewValidationErrorResponseWithDefaults

`func NewValidationErrorResponseWithDefaults() *ValidationErrorResponse`

NewValidationErrorResponseWithDefaults instantiates a new ValidationErrorResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetError

`func (o *ValidationErrorResponse) GetError() ValidationErrorResponseError`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *ValidationErrorResponse) GetErrorOk() (*ValidationErrorResponseError, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *ValidationErrorResponse) SetError(v ValidationErrorResponseError)`

SetError sets Error field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
