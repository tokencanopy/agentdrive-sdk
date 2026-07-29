# UsagePeriodOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ends** | **time.Time** |  |
**Starts** | **time.Time** |  |
**YearMonth** | **string** |  |

## Methods

### NewUsagePeriodOut

`func NewUsagePeriodOut(ends time.Time, starts time.Time, yearMonth string, ) *UsagePeriodOut`

NewUsagePeriodOut instantiates a new UsagePeriodOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUsagePeriodOutWithDefaults

`func NewUsagePeriodOutWithDefaults() *UsagePeriodOut`

NewUsagePeriodOutWithDefaults instantiates a new UsagePeriodOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnds

`func (o *UsagePeriodOut) GetEnds() time.Time`

GetEnds returns the Ends field if non-nil, zero value otherwise.

### GetEndsOk

`func (o *UsagePeriodOut) GetEndsOk() (*time.Time, bool)`

GetEndsOk returns a tuple with the Ends field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnds

`func (o *UsagePeriodOut) SetEnds(v time.Time)`

SetEnds sets Ends field to given value.


### GetStarts

`func (o *UsagePeriodOut) GetStarts() time.Time`

GetStarts returns the Starts field if non-nil, zero value otherwise.

### GetStartsOk

`func (o *UsagePeriodOut) GetStartsOk() (*time.Time, bool)`

GetStartsOk returns a tuple with the Starts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStarts

`func (o *UsagePeriodOut) SetStarts(v time.Time)`

SetStarts sets Starts field to given value.


### GetYearMonth

`func (o *UsagePeriodOut) GetYearMonth() string`

GetYearMonth returns the YearMonth field if non-nil, zero value otherwise.

### GetYearMonthOk

`func (o *UsagePeriodOut) GetYearMonthOk() (*string, bool)`

GetYearMonthOk returns a tuple with the YearMonth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetYearMonth

`func (o *UsagePeriodOut) SetYearMonth(v string)`

SetYearMonth sets YearMonth field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
