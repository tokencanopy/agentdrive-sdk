# LookupValuesIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Column** | **string** |  |
**Dataset** | **string** |  |
**Limit** | Pointer to **int32** |  | [optional] [default to 50]

## Methods

### NewLookupValuesIn

`func NewLookupValuesIn(column string, dataset string, ) *LookupValuesIn`

NewLookupValuesIn instantiates a new LookupValuesIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLookupValuesInWithDefaults

`func NewLookupValuesInWithDefaults() *LookupValuesIn`

NewLookupValuesInWithDefaults instantiates a new LookupValuesIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetColumn

`func (o *LookupValuesIn) GetColumn() string`

GetColumn returns the Column field if non-nil, zero value otherwise.

### GetColumnOk

`func (o *LookupValuesIn) GetColumnOk() (*string, bool)`

GetColumnOk returns a tuple with the Column field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColumn

`func (o *LookupValuesIn) SetColumn(v string)`

SetColumn sets Column field to given value.


### GetDataset

`func (o *LookupValuesIn) GetDataset() string`

GetDataset returns the Dataset field if non-nil, zero value otherwise.

### GetDatasetOk

`func (o *LookupValuesIn) GetDatasetOk() (*string, bool)`

GetDatasetOk returns a tuple with the Dataset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataset

`func (o *LookupValuesIn) SetDataset(v string)`

SetDataset sets Dataset field to given value.


### GetLimit

`func (o *LookupValuesIn) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *LookupValuesIn) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *LookupValuesIn) SetLimit(v int32)`

SetLimit sets Limit field to given value.

### HasLimit

`func (o *LookupValuesIn) HasLimit() bool`

HasLimit returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
