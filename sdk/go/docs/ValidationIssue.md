# ValidationIssue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ctx** | Pointer to **map[string]interface{}** |  | [optional]
**Input** | Pointer to **interface{}** |  | [optional]
**Loc** | **[]interface{}** |  |
**Msg** | **string** |  |
**Type** | **string** |  |

## Methods

### NewValidationIssue

`func NewValidationIssue(loc []interface{}, msg string, type_ string, ) *ValidationIssue`

NewValidationIssue instantiates a new ValidationIssue object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewValidationIssueWithDefaults

`func NewValidationIssueWithDefaults() *ValidationIssue`

NewValidationIssueWithDefaults instantiates a new ValidationIssue object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCtx

`func (o *ValidationIssue) GetCtx() map[string]interface{}`

GetCtx returns the Ctx field if non-nil, zero value otherwise.

### GetCtxOk

`func (o *ValidationIssue) GetCtxOk() (*map[string]interface{}, bool)`

GetCtxOk returns a tuple with the Ctx field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCtx

`func (o *ValidationIssue) SetCtx(v map[string]interface{})`

SetCtx sets Ctx field to given value.

### HasCtx

`func (o *ValidationIssue) HasCtx() bool`

HasCtx returns a boolean if a field has been set.

### SetCtxNil

`func (o *ValidationIssue) SetCtxNil(b bool)`

 SetCtxNil sets the value for Ctx to be an explicit nil

### UnsetCtx
`func (o *ValidationIssue) UnsetCtx()`

UnsetCtx ensures that no value is present for Ctx, not even an explicit nil
### GetInput

`func (o *ValidationIssue) GetInput() interface{}`

GetInput returns the Input field if non-nil, zero value otherwise.

### GetInputOk

`func (o *ValidationIssue) GetInputOk() (*interface{}, bool)`

GetInputOk returns a tuple with the Input field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInput

`func (o *ValidationIssue) SetInput(v interface{})`

SetInput sets Input field to given value.

### HasInput

`func (o *ValidationIssue) HasInput() bool`

HasInput returns a boolean if a field has been set.

### SetInputNil

`func (o *ValidationIssue) SetInputNil(b bool)`

 SetInputNil sets the value for Input to be an explicit nil

### UnsetInput
`func (o *ValidationIssue) UnsetInput()`

UnsetInput ensures that no value is present for Input, not even an explicit nil
### GetLoc

`func (o *ValidationIssue) GetLoc() []interface{}`

GetLoc returns the Loc field if non-nil, zero value otherwise.

### GetLocOk

`func (o *ValidationIssue) GetLocOk() (*[]interface{}, bool)`

GetLocOk returns a tuple with the Loc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLoc

`func (o *ValidationIssue) SetLoc(v []interface{})`

SetLoc sets Loc field to given value.


### GetMsg

`func (o *ValidationIssue) GetMsg() string`

GetMsg returns the Msg field if non-nil, zero value otherwise.

### GetMsgOk

`func (o *ValidationIssue) GetMsgOk() (*string, bool)`

GetMsgOk returns a tuple with the Msg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMsg

`func (o *ValidationIssue) SetMsg(v string)`

SetMsg sets Msg field to given value.


### GetType

`func (o *ValidationIssue) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ValidationIssue) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ValidationIssue) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
