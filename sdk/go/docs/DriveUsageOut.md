# DriveUsageOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountFootprint** | [**StorageFootprintOut**](StorageFootprintOut.md) |  |
**EgressBytes** | [**UsageCounterOut**](UsageCounterOut.md) |  |
**Footprint** | [**StorageFootprintOut**](StorageFootprintOut.md) |  |
**IndexedBytes** | [**UsageCounterOut**](UsageCounterOut.md) |  |
**IndexingOps** | [**UsageCounterOut**](UsageCounterOut.md) |  |
**OpsThisMonth** | [**OperationUsageOut**](OperationUsageOut.md) |  |
**Period** | [**UsagePeriodOut**](UsagePeriodOut.md) |  |
**RetrievalQueries** | [**UsageCounterOut**](UsageCounterOut.md) |  |
**Storage** | [**UsageCounterOut**](UsageCounterOut.md) |  |
**StorageBreakdown** | Pointer to [**NullableStorageBreakdownOut**](StorageBreakdownOut.md) |  | [optional]
**TokensThisMonth** | [**TokenUsageOut**](TokenUsageOut.md) |  |
**VersionRetention** | [**VersionRetentionOut**](VersionRetentionOut.md) |  |
**WritesThisHour** | [**HourlyUsageCounterOut**](HourlyUsageCounterOut.md) |  |

## Methods

### NewDriveUsageOut

`func NewDriveUsageOut(accountFootprint StorageFootprintOut, egressBytes UsageCounterOut, footprint StorageFootprintOut, indexedBytes UsageCounterOut, indexingOps UsageCounterOut, opsThisMonth OperationUsageOut, period UsagePeriodOut, retrievalQueries UsageCounterOut, storage UsageCounterOut, tokensThisMonth TokenUsageOut, versionRetention VersionRetentionOut, writesThisHour HourlyUsageCounterOut, ) *DriveUsageOut`

NewDriveUsageOut instantiates a new DriveUsageOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDriveUsageOutWithDefaults

`func NewDriveUsageOutWithDefaults() *DriveUsageOut`

NewDriveUsageOutWithDefaults instantiates a new DriveUsageOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountFootprint

`func (o *DriveUsageOut) GetAccountFootprint() StorageFootprintOut`

GetAccountFootprint returns the AccountFootprint field if non-nil, zero value otherwise.

### GetAccountFootprintOk

`func (o *DriveUsageOut) GetAccountFootprintOk() (*StorageFootprintOut, bool)`

GetAccountFootprintOk returns a tuple with the AccountFootprint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountFootprint

`func (o *DriveUsageOut) SetAccountFootprint(v StorageFootprintOut)`

SetAccountFootprint sets AccountFootprint field to given value.


### GetEgressBytes

`func (o *DriveUsageOut) GetEgressBytes() UsageCounterOut`

GetEgressBytes returns the EgressBytes field if non-nil, zero value otherwise.

### GetEgressBytesOk

`func (o *DriveUsageOut) GetEgressBytesOk() (*UsageCounterOut, bool)`

GetEgressBytesOk returns a tuple with the EgressBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEgressBytes

`func (o *DriveUsageOut) SetEgressBytes(v UsageCounterOut)`

SetEgressBytes sets EgressBytes field to given value.


### GetFootprint

`func (o *DriveUsageOut) GetFootprint() StorageFootprintOut`

GetFootprint returns the Footprint field if non-nil, zero value otherwise.

### GetFootprintOk

`func (o *DriveUsageOut) GetFootprintOk() (*StorageFootprintOut, bool)`

GetFootprintOk returns a tuple with the Footprint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFootprint

`func (o *DriveUsageOut) SetFootprint(v StorageFootprintOut)`

SetFootprint sets Footprint field to given value.


### GetIndexedBytes

`func (o *DriveUsageOut) GetIndexedBytes() UsageCounterOut`

GetIndexedBytes returns the IndexedBytes field if non-nil, zero value otherwise.

### GetIndexedBytesOk

`func (o *DriveUsageOut) GetIndexedBytesOk() (*UsageCounterOut, bool)`

GetIndexedBytesOk returns a tuple with the IndexedBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIndexedBytes

`func (o *DriveUsageOut) SetIndexedBytes(v UsageCounterOut)`

SetIndexedBytes sets IndexedBytes field to given value.


### GetIndexingOps

`func (o *DriveUsageOut) GetIndexingOps() UsageCounterOut`

GetIndexingOps returns the IndexingOps field if non-nil, zero value otherwise.

### GetIndexingOpsOk

`func (o *DriveUsageOut) GetIndexingOpsOk() (*UsageCounterOut, bool)`

GetIndexingOpsOk returns a tuple with the IndexingOps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIndexingOps

`func (o *DriveUsageOut) SetIndexingOps(v UsageCounterOut)`

SetIndexingOps sets IndexingOps field to given value.


### GetOpsThisMonth

`func (o *DriveUsageOut) GetOpsThisMonth() OperationUsageOut`

GetOpsThisMonth returns the OpsThisMonth field if non-nil, zero value otherwise.

### GetOpsThisMonthOk

`func (o *DriveUsageOut) GetOpsThisMonthOk() (*OperationUsageOut, bool)`

GetOpsThisMonthOk returns a tuple with the OpsThisMonth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpsThisMonth

`func (o *DriveUsageOut) SetOpsThisMonth(v OperationUsageOut)`

SetOpsThisMonth sets OpsThisMonth field to given value.


### GetPeriod

`func (o *DriveUsageOut) GetPeriod() UsagePeriodOut`

GetPeriod returns the Period field if non-nil, zero value otherwise.

### GetPeriodOk

`func (o *DriveUsageOut) GetPeriodOk() (*UsagePeriodOut, bool)`

GetPeriodOk returns a tuple with the Period field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPeriod

`func (o *DriveUsageOut) SetPeriod(v UsagePeriodOut)`

SetPeriod sets Period field to given value.


### GetRetrievalQueries

`func (o *DriveUsageOut) GetRetrievalQueries() UsageCounterOut`

GetRetrievalQueries returns the RetrievalQueries field if non-nil, zero value otherwise.

### GetRetrievalQueriesOk

`func (o *DriveUsageOut) GetRetrievalQueriesOk() (*UsageCounterOut, bool)`

GetRetrievalQueriesOk returns a tuple with the RetrievalQueries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRetrievalQueries

`func (o *DriveUsageOut) SetRetrievalQueries(v UsageCounterOut)`

SetRetrievalQueries sets RetrievalQueries field to given value.


### GetStorage

`func (o *DriveUsageOut) GetStorage() UsageCounterOut`

GetStorage returns the Storage field if non-nil, zero value otherwise.

### GetStorageOk

`func (o *DriveUsageOut) GetStorageOk() (*UsageCounterOut, bool)`

GetStorageOk returns a tuple with the Storage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStorage

`func (o *DriveUsageOut) SetStorage(v UsageCounterOut)`

SetStorage sets Storage field to given value.


### GetStorageBreakdown

`func (o *DriveUsageOut) GetStorageBreakdown() StorageBreakdownOut`

GetStorageBreakdown returns the StorageBreakdown field if non-nil, zero value otherwise.

### GetStorageBreakdownOk

`func (o *DriveUsageOut) GetStorageBreakdownOk() (*StorageBreakdownOut, bool)`

GetStorageBreakdownOk returns a tuple with the StorageBreakdown field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStorageBreakdown

`func (o *DriveUsageOut) SetStorageBreakdown(v StorageBreakdownOut)`

SetStorageBreakdown sets StorageBreakdown field to given value.

### HasStorageBreakdown

`func (o *DriveUsageOut) HasStorageBreakdown() bool`

HasStorageBreakdown returns a boolean if a field has been set.

### SetStorageBreakdownNil

`func (o *DriveUsageOut) SetStorageBreakdownNil(b bool)`

 SetStorageBreakdownNil sets the value for StorageBreakdown to be an explicit nil

### UnsetStorageBreakdown
`func (o *DriveUsageOut) UnsetStorageBreakdown()`

UnsetStorageBreakdown ensures that no value is present for StorageBreakdown, not even an explicit nil
### GetTokensThisMonth

`func (o *DriveUsageOut) GetTokensThisMonth() TokenUsageOut`

GetTokensThisMonth returns the TokensThisMonth field if non-nil, zero value otherwise.

### GetTokensThisMonthOk

`func (o *DriveUsageOut) GetTokensThisMonthOk() (*TokenUsageOut, bool)`

GetTokensThisMonthOk returns a tuple with the TokensThisMonth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokensThisMonth

`func (o *DriveUsageOut) SetTokensThisMonth(v TokenUsageOut)`

SetTokensThisMonth sets TokensThisMonth field to given value.


### GetVersionRetention

`func (o *DriveUsageOut) GetVersionRetention() VersionRetentionOut`

GetVersionRetention returns the VersionRetention field if non-nil, zero value otherwise.

### GetVersionRetentionOk

`func (o *DriveUsageOut) GetVersionRetentionOk() (*VersionRetentionOut, bool)`

GetVersionRetentionOk returns a tuple with the VersionRetention field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersionRetention

`func (o *DriveUsageOut) SetVersionRetention(v VersionRetentionOut)`

SetVersionRetention sets VersionRetention field to given value.


### GetWritesThisHour

`func (o *DriveUsageOut) GetWritesThisHour() HourlyUsageCounterOut`

GetWritesThisHour returns the WritesThisHour field if non-nil, zero value otherwise.

### GetWritesThisHourOk

`func (o *DriveUsageOut) GetWritesThisHourOk() (*HourlyUsageCounterOut, bool)`

GetWritesThisHourOk returns a tuple with the WritesThisHour field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWritesThisHour

`func (o *DriveUsageOut) SetWritesThisHour(v HourlyUsageCounterOut)`

SetWritesThisHour sets WritesThisHour field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
