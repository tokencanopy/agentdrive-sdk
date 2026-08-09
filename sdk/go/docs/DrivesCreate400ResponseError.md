# DrivesCreate400ResponseError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** | Stable machine-readable error code (see the error-catalog). |
**Details** | Pointer to **map[string]interface{}** | Error-code-specific context (optional). | [optional]
**Message** | **string** |  |

## Methods

### NewDrivesCreate400ResponseError

`func NewDrivesCreate400ResponseError(code string, message string, ) *DrivesCreate400ResponseError`

NewDrivesCreate400ResponseError instantiates a new DrivesCreate400ResponseError object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDrivesCreate400ResponseErrorWithDefaults

`func NewDrivesCreate400ResponseErrorWithDefaults() *DrivesCreate400ResponseError`

NewDrivesCreate400ResponseErrorWithDefaults instantiates a new DrivesCreate400ResponseError object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *DrivesCreate400ResponseError) GetCode() string`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *DrivesCreate400ResponseError) GetCodeOk() (*string, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *DrivesCreate400ResponseError) SetCode(v string)`

SetCode sets Code field to given value.


### GetDetails

`func (o *DrivesCreate400ResponseError) GetDetails() map[string]interface{}`

GetDetails returns the Details field if non-nil, zero value otherwise.

### GetDetailsOk

`func (o *DrivesCreate400ResponseError) GetDetailsOk() (*map[string]interface{}, bool)`

GetDetailsOk returns a tuple with the Details field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetails

`func (o *DrivesCreate400ResponseError) SetDetails(v map[string]interface{})`

SetDetails sets Details field to given value.

### HasDetails

`func (o *DrivesCreate400ResponseError) HasDetails() bool`

HasDetails returns a boolean if a field has been set.

### GetMessage

`func (o *DrivesCreate400ResponseError) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *DrivesCreate400ResponseError) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *DrivesCreate400ResponseError) SetMessage(v string)`

SetMessage sets Message field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
