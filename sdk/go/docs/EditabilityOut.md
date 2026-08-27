# EditabilityOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Reason** | Pointer to **NullableString** |  | [optional]
**Status** | **string** |  |

## Methods

### NewEditabilityOut

`func NewEditabilityOut(status string, ) *EditabilityOut`

NewEditabilityOut instantiates a new EditabilityOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEditabilityOutWithDefaults

`func NewEditabilityOutWithDefaults() *EditabilityOut`

NewEditabilityOutWithDefaults instantiates a new EditabilityOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetReason

`func (o *EditabilityOut) GetReason() string`

GetReason returns the Reason field if non-nil, zero value otherwise.

### GetReasonOk

`func (o *EditabilityOut) GetReasonOk() (*string, bool)`

GetReasonOk returns a tuple with the Reason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReason

`func (o *EditabilityOut) SetReason(v string)`

SetReason sets Reason field to given value.

### HasReason

`func (o *EditabilityOut) HasReason() bool`

HasReason returns a boolean if a field has been set.

### SetReasonNil

`func (o *EditabilityOut) SetReasonNil(b bool)`

 SetReasonNil sets the value for Reason to be an explicit nil

### UnsetReason
`func (o *EditabilityOut) UnsetReason()`

UnsetReason ensures that no value is present for Reason, not even an explicit nil
### GetStatus

`func (o *EditabilityOut) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *EditabilityOut) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *EditabilityOut) SetStatus(v string)`

SetStatus sets Status field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
