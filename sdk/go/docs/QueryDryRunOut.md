# QueryDryRunOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DryRun** | **bool** |  |
**Engine** | **string** |  |
**EstimatedBytesProcessed** | **int32** |  |
**ResultSchema** | [**[]QueryColumnOut**](QueryColumnOut.md) |  |
**Valid** | **bool** |  |

## Methods

### NewQueryDryRunOut

`func NewQueryDryRunOut(dryRun bool, engine string, estimatedBytesProcessed int32, resultSchema []QueryColumnOut, valid bool, ) *QueryDryRunOut`

NewQueryDryRunOut instantiates a new QueryDryRunOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQueryDryRunOutWithDefaults

`func NewQueryDryRunOutWithDefaults() *QueryDryRunOut`

NewQueryDryRunOutWithDefaults instantiates a new QueryDryRunOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDryRun

`func (o *QueryDryRunOut) GetDryRun() bool`

GetDryRun returns the DryRun field if non-nil, zero value otherwise.

### GetDryRunOk

`func (o *QueryDryRunOut) GetDryRunOk() (*bool, bool)`

GetDryRunOk returns a tuple with the DryRun field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDryRun

`func (o *QueryDryRunOut) SetDryRun(v bool)`

SetDryRun sets DryRun field to given value.


### GetEngine

`func (o *QueryDryRunOut) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *QueryDryRunOut) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *QueryDryRunOut) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetEstimatedBytesProcessed

`func (o *QueryDryRunOut) GetEstimatedBytesProcessed() int32`

GetEstimatedBytesProcessed returns the EstimatedBytesProcessed field if non-nil, zero value otherwise.

### GetEstimatedBytesProcessedOk

`func (o *QueryDryRunOut) GetEstimatedBytesProcessedOk() (*int32, bool)`

GetEstimatedBytesProcessedOk returns a tuple with the EstimatedBytesProcessed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEstimatedBytesProcessed

`func (o *QueryDryRunOut) SetEstimatedBytesProcessed(v int32)`

SetEstimatedBytesProcessed sets EstimatedBytesProcessed field to given value.


### GetResultSchema

`func (o *QueryDryRunOut) GetResultSchema() []QueryColumnOut`

GetResultSchema returns the ResultSchema field if non-nil, zero value otherwise.

### GetResultSchemaOk

`func (o *QueryDryRunOut) GetResultSchemaOk() (*[]QueryColumnOut, bool)`

GetResultSchemaOk returns a tuple with the ResultSchema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResultSchema

`func (o *QueryDryRunOut) SetResultSchema(v []QueryColumnOut)`

SetResultSchema sets ResultSchema field to given value.


### GetValid

`func (o *QueryDryRunOut) GetValid() bool`

GetValid returns the Valid field if non-nil, zero value otherwise.

### GetValidOk

`func (o *QueryDryRunOut) GetValidOk() (*bool, bool)`

GetValidOk returns a tuple with the Valid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValid

`func (o *QueryDryRunOut) SetValid(v bool)`

SetValid sets Valid field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
