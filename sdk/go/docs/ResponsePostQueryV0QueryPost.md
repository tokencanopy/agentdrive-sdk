# ResponsePostQueryV0QueryPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DryRun** | **bool** |  |
**Engine** | **string** |  |
**EstimatedBytesProcessed** | **int32** |  |
**ResultSchema** | [**[]QueryColumnOut**](QueryColumnOut.md) |  |
**Valid** | **bool** |  |
**BytesProcessed** | **int32** |  |
**CacheHit** | **bool** |  |
**Preview** | **[]map[string]interface{}** |  |
**ResultArtId** | **string** |  |
**RowCount** | **int32** |  |

## Methods

### NewResponsePostQueryV0QueryPost

`func NewResponsePostQueryV0QueryPost(dryRun bool, engine string, estimatedBytesProcessed int32, resultSchema []QueryColumnOut, valid bool, bytesProcessed int32, cacheHit bool, preview []map[string]interface{}, resultArtId string, rowCount int32, ) *ResponsePostQueryV0QueryPost`

NewResponsePostQueryV0QueryPost instantiates a new ResponsePostQueryV0QueryPost object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewResponsePostQueryV0QueryPostWithDefaults

`func NewResponsePostQueryV0QueryPostWithDefaults() *ResponsePostQueryV0QueryPost`

NewResponsePostQueryV0QueryPostWithDefaults instantiates a new ResponsePostQueryV0QueryPost object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDryRun

`func (o *ResponsePostQueryV0QueryPost) GetDryRun() bool`

GetDryRun returns the DryRun field if non-nil, zero value otherwise.

### GetDryRunOk

`func (o *ResponsePostQueryV0QueryPost) GetDryRunOk() (*bool, bool)`

GetDryRunOk returns a tuple with the DryRun field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDryRun

`func (o *ResponsePostQueryV0QueryPost) SetDryRun(v bool)`

SetDryRun sets DryRun field to given value.


### GetEngine

`func (o *ResponsePostQueryV0QueryPost) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *ResponsePostQueryV0QueryPost) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *ResponsePostQueryV0QueryPost) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetEstimatedBytesProcessed

`func (o *ResponsePostQueryV0QueryPost) GetEstimatedBytesProcessed() int32`

GetEstimatedBytesProcessed returns the EstimatedBytesProcessed field if non-nil, zero value otherwise.

### GetEstimatedBytesProcessedOk

`func (o *ResponsePostQueryV0QueryPost) GetEstimatedBytesProcessedOk() (*int32, bool)`

GetEstimatedBytesProcessedOk returns a tuple with the EstimatedBytesProcessed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEstimatedBytesProcessed

`func (o *ResponsePostQueryV0QueryPost) SetEstimatedBytesProcessed(v int32)`

SetEstimatedBytesProcessed sets EstimatedBytesProcessed field to given value.


### GetResultSchema

`func (o *ResponsePostQueryV0QueryPost) GetResultSchema() []QueryColumnOut`

GetResultSchema returns the ResultSchema field if non-nil, zero value otherwise.

### GetResultSchemaOk

`func (o *ResponsePostQueryV0QueryPost) GetResultSchemaOk() (*[]QueryColumnOut, bool)`

GetResultSchemaOk returns a tuple with the ResultSchema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResultSchema

`func (o *ResponsePostQueryV0QueryPost) SetResultSchema(v []QueryColumnOut)`

SetResultSchema sets ResultSchema field to given value.


### GetValid

`func (o *ResponsePostQueryV0QueryPost) GetValid() bool`

GetValid returns the Valid field if non-nil, zero value otherwise.

### GetValidOk

`func (o *ResponsePostQueryV0QueryPost) GetValidOk() (*bool, bool)`

GetValidOk returns a tuple with the Valid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValid

`func (o *ResponsePostQueryV0QueryPost) SetValid(v bool)`

SetValid sets Valid field to given value.


### GetBytesProcessed

`func (o *ResponsePostQueryV0QueryPost) GetBytesProcessed() int32`

GetBytesProcessed returns the BytesProcessed field if non-nil, zero value otherwise.

### GetBytesProcessedOk

`func (o *ResponsePostQueryV0QueryPost) GetBytesProcessedOk() (*int32, bool)`

GetBytesProcessedOk returns a tuple with the BytesProcessed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBytesProcessed

`func (o *ResponsePostQueryV0QueryPost) SetBytesProcessed(v int32)`

SetBytesProcessed sets BytesProcessed field to given value.


### GetCacheHit

`func (o *ResponsePostQueryV0QueryPost) GetCacheHit() bool`

GetCacheHit returns the CacheHit field if non-nil, zero value otherwise.

### GetCacheHitOk

`func (o *ResponsePostQueryV0QueryPost) GetCacheHitOk() (*bool, bool)`

GetCacheHitOk returns a tuple with the CacheHit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCacheHit

`func (o *ResponsePostQueryV0QueryPost) SetCacheHit(v bool)`

SetCacheHit sets CacheHit field to given value.


### GetPreview

`func (o *ResponsePostQueryV0QueryPost) GetPreview() []map[string]interface{}`

GetPreview returns the Preview field if non-nil, zero value otherwise.

### GetPreviewOk

`func (o *ResponsePostQueryV0QueryPost) GetPreviewOk() (*[]map[string]interface{}, bool)`

GetPreviewOk returns a tuple with the Preview field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPreview

`func (o *ResponsePostQueryV0QueryPost) SetPreview(v []map[string]interface{})`

SetPreview sets Preview field to given value.


### GetResultArtId

`func (o *ResponsePostQueryV0QueryPost) GetResultArtId() string`

GetResultArtId returns the ResultArtId field if non-nil, zero value otherwise.

### GetResultArtIdOk

`func (o *ResponsePostQueryV0QueryPost) GetResultArtIdOk() (*string, bool)`

GetResultArtIdOk returns a tuple with the ResultArtId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResultArtId

`func (o *ResponsePostQueryV0QueryPost) SetResultArtId(v string)`

SetResultArtId sets ResultArtId field to given value.


### GetRowCount

`func (o *ResponsePostQueryV0QueryPost) GetRowCount() int32`

GetRowCount returns the RowCount field if non-nil, zero value otherwise.

### GetRowCountOk

`func (o *ResponsePostQueryV0QueryPost) GetRowCountOk() (*int32, bool)`

GetRowCountOk returns a tuple with the RowCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRowCount

`func (o *ResponsePostQueryV0QueryPost) SetRowCount(v int32)`

SetRowCount sets RowCount field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
