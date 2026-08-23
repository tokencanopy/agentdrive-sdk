# UploadOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Cleanup** | [**UploadCleanupOut**](UploadCleanupOut.md) |  |
**Content** | [**UploadContentOut**](UploadContentOut.md) |  |
**DriveId** | **string** |  |
**ExpiresAt** | **time.Time** |  |
**Failure** | [**NullableUploadFailureOut**](UploadFailureOut.md) |  |
**Id** | **string** |  |
**RestartRequired** | **bool** |  |
**Result** | [**NullableUploadResultOut**](UploadResultOut.md) |  |
**State** | **string** |  |
**Target** | [**Target**](Target.md) |  |
**TargetDisclosed** | **bool** |  |

## Methods

### NewUploadOut

`func NewUploadOut(cleanup UploadCleanupOut, content UploadContentOut, driveId string, expiresAt time.Time, failure NullableUploadFailureOut, id string, restartRequired bool, result NullableUploadResultOut, state string, target Target, targetDisclosed bool, ) *UploadOut`

NewUploadOut instantiates a new UploadOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUploadOutWithDefaults

`func NewUploadOutWithDefaults() *UploadOut`

NewUploadOutWithDefaults instantiates a new UploadOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCleanup

`func (o *UploadOut) GetCleanup() UploadCleanupOut`

GetCleanup returns the Cleanup field if non-nil, zero value otherwise.

### GetCleanupOk

`func (o *UploadOut) GetCleanupOk() (*UploadCleanupOut, bool)`

GetCleanupOk returns a tuple with the Cleanup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCleanup

`func (o *UploadOut) SetCleanup(v UploadCleanupOut)`

SetCleanup sets Cleanup field to given value.


### GetContent

`func (o *UploadOut) GetContent() UploadContentOut`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *UploadOut) GetContentOk() (*UploadContentOut, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *UploadOut) SetContent(v UploadContentOut)`

SetContent sets Content field to given value.


### GetDriveId

`func (o *UploadOut) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *UploadOut) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *UploadOut) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetExpiresAt

`func (o *UploadOut) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *UploadOut) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *UploadOut) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### GetFailure

`func (o *UploadOut) GetFailure() UploadFailureOut`

GetFailure returns the Failure field if non-nil, zero value otherwise.

### GetFailureOk

`func (o *UploadOut) GetFailureOk() (*UploadFailureOut, bool)`

GetFailureOk returns a tuple with the Failure field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFailure

`func (o *UploadOut) SetFailure(v UploadFailureOut)`

SetFailure sets Failure field to given value.


### SetFailureNil

`func (o *UploadOut) SetFailureNil(b bool)`

 SetFailureNil sets the value for Failure to be an explicit nil

### UnsetFailure
`func (o *UploadOut) UnsetFailure()`

UnsetFailure ensures that no value is present for Failure, not even an explicit nil
### GetId

`func (o *UploadOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UploadOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UploadOut) SetId(v string)`

SetId sets Id field to given value.


### GetRestartRequired

`func (o *UploadOut) GetRestartRequired() bool`

GetRestartRequired returns the RestartRequired field if non-nil, zero value otherwise.

### GetRestartRequiredOk

`func (o *UploadOut) GetRestartRequiredOk() (*bool, bool)`

GetRestartRequiredOk returns a tuple with the RestartRequired field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestartRequired

`func (o *UploadOut) SetRestartRequired(v bool)`

SetRestartRequired sets RestartRequired field to given value.


### GetResult

`func (o *UploadOut) GetResult() UploadResultOut`

GetResult returns the Result field if non-nil, zero value otherwise.

### GetResultOk

`func (o *UploadOut) GetResultOk() (*UploadResultOut, bool)`

GetResultOk returns a tuple with the Result field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResult

`func (o *UploadOut) SetResult(v UploadResultOut)`

SetResult sets Result field to given value.


### SetResultNil

`func (o *UploadOut) SetResultNil(b bool)`

 SetResultNil sets the value for Result to be an explicit nil

### UnsetResult
`func (o *UploadOut) UnsetResult()`

UnsetResult ensures that no value is present for Result, not even an explicit nil
### GetState

`func (o *UploadOut) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *UploadOut) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *UploadOut) SetState(v string)`

SetState sets State field to given value.


### GetTarget

`func (o *UploadOut) GetTarget() Target`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *UploadOut) GetTargetOk() (*Target, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *UploadOut) SetTarget(v Target)`

SetTarget sets Target field to given value.


### GetTargetDisclosed

`func (o *UploadOut) GetTargetDisclosed() bool`

GetTargetDisclosed returns the TargetDisclosed field if non-nil, zero value otherwise.

### GetTargetDisclosedOk

`func (o *UploadOut) GetTargetDisclosedOk() (*bool, bool)`

GetTargetDisclosedOk returns a tuple with the TargetDisclosed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetDisclosed

`func (o *UploadOut) SetTargetDisclosed(v bool)`

SetTargetDisclosed sets TargetDisclosed field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
