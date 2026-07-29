# CompileJobListOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]CompileJobOut**](CompileJobOut.md) |  |
**Jobs** | [**[]CompileJobOut**](CompileJobOut.md) | Deprecated same-value alias for &#x60;items&#x60;; retained for compatibility. |
**NextCursor** | Pointer to **NullableString** | Opaque continuation token, or null when the listing is complete. | [optional]

## Methods

### NewCompileJobListOut

`func NewCompileJobListOut(items []CompileJobOut, jobs []CompileJobOut, ) *CompileJobListOut`

NewCompileJobListOut instantiates a new CompileJobListOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCompileJobListOutWithDefaults

`func NewCompileJobListOutWithDefaults() *CompileJobListOut`

NewCompileJobListOutWithDefaults instantiates a new CompileJobListOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *CompileJobListOut) GetItems() []CompileJobOut`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *CompileJobListOut) GetItemsOk() (*[]CompileJobOut, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *CompileJobListOut) SetItems(v []CompileJobOut)`

SetItems sets Items field to given value.


### GetJobs

`func (o *CompileJobListOut) GetJobs() []CompileJobOut`

GetJobs returns the Jobs field if non-nil, zero value otherwise.

### GetJobsOk

`func (o *CompileJobListOut) GetJobsOk() (*[]CompileJobOut, bool)`

GetJobsOk returns a tuple with the Jobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobs

`func (o *CompileJobListOut) SetJobs(v []CompileJobOut)`

SetJobs sets Jobs field to given value.


### GetNextCursor

`func (o *CompileJobListOut) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *CompileJobListOut) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *CompileJobListOut) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.

### HasNextCursor

`func (o *CompileJobListOut) HasNextCursor() bool`

HasNextCursor returns a boolean if a field has been set.

### SetNextCursorNil

`func (o *CompileJobListOut) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *CompileJobListOut) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
