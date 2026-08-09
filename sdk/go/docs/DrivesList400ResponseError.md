# DrivesList400ResponseError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** | Stable machine-readable error code (see the error-catalog). |
**Details** | Pointer to **map[string]interface{}** | Error-code-specific context (optional). | [optional]
**Message** | **NullableString** |  |

## Methods

### NewDrivesList400ResponseError

`func NewDrivesList400ResponseError(code string, message NullableString, ) *DrivesList400ResponseError`

NewDrivesList400ResponseError instantiates a new DrivesList400ResponseError object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDrivesList400ResponseErrorWithDefaults

`func NewDrivesList400ResponseErrorWithDefaults() *DrivesList400ResponseError`

NewDrivesList400ResponseErrorWithDefaults instantiates a new DrivesList400ResponseError object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *DrivesList400ResponseError) GetCode() string`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *DrivesList400ResponseError) GetCodeOk() (*string, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *DrivesList400ResponseError) SetCode(v string)`

SetCode sets Code field to given value.


### GetDetails

`func (o *DrivesList400ResponseError) GetDetails() map[string]interface{}`

GetDetails returns the Details field if non-nil, zero value otherwise.

### GetDetailsOk

`func (o *DrivesList400ResponseError) GetDetailsOk() (*map[string]interface{}, bool)`

GetDetailsOk returns a tuple with the Details field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetails

`func (o *DrivesList400ResponseError) SetDetails(v map[string]interface{})`

SetDetails sets Details field to given value.

### HasDetails

`func (o *DrivesList400ResponseError) HasDetails() bool`

HasDetails returns a boolean if a field has been set.

### GetMessage

`func (o *DrivesList400ResponseError) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *DrivesList400ResponseError) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *DrivesList400ResponseError) SetMessage(v string)`

SetMessage sets Message field to given value.


### SetMessageNil

`func (o *DrivesList400ResponseError) SetMessageNil(b bool)`

 SetMessageNil sets the value for Message to be an explicit nil

### UnsetMessage
`func (o *DrivesList400ResponseError) UnsetMessage()`

UnsetMessage ensures that no value is present for Message, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
