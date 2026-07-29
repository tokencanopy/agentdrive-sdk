# QueryResultOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BytesProcessed** | **int32** |  |
**CacheHit** | **bool** |  |
**Engine** | **string** |  |
**Preview** | **[]map[string]interface{}** |  |
**ResultArtId** | **string** |  |
**ResultSchema** | [**[]QueryColumnOut**](QueryColumnOut.md) |  |
**RowCount** | **int32** |  |

## Methods

### NewQueryResultOut

`func NewQueryResultOut(bytesProcessed int32, cacheHit bool, engine string, preview []*map[string]interface{}, resultArtId string, resultSchema []QueryColumnOut, rowCount int32, ) *QueryResultOut`

NewQueryResultOut instantiates a new QueryResultOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQueryResultOutWithDefaults

`func NewQueryResultOutWithDefaults() *QueryResultOut`

NewQueryResultOutWithDefaults instantiates a new QueryResultOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBytesProcessed

`func (o *QueryResultOut) GetBytesProcessed() int32`

GetBytesProcessed returns the BytesProcessed field if non-nil, zero value otherwise.

### GetBytesProcessedOk

`func (o *QueryResultOut) GetBytesProcessedOk() (*int32, bool)`

GetBytesProcessedOk returns a tuple with the BytesProcessed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBytesProcessed

`func (o *QueryResultOut) SetBytesProcessed(v int32)`

SetBytesProcessed sets BytesProcessed field to given value.


### GetCacheHit

`func (o *QueryResultOut) GetCacheHit() bool`

GetCacheHit returns the CacheHit field if non-nil, zero value otherwise.

### GetCacheHitOk

`func (o *QueryResultOut) GetCacheHitOk() (*bool, bool)`

GetCacheHitOk returns a tuple with the CacheHit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCacheHit

`func (o *QueryResultOut) SetCacheHit(v bool)`

SetCacheHit sets CacheHit field to given value.


### GetEngine

`func (o *QueryResultOut) GetEngine() string`

GetEngine returns the Engine field if non-nil, zero value otherwise.

### GetEngineOk

`func (o *QueryResultOut) GetEngineOk() (*string, bool)`

GetEngineOk returns a tuple with the Engine field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEngine

`func (o *QueryResultOut) SetEngine(v string)`

SetEngine sets Engine field to given value.


### GetPreview

`func (o *QueryResultOut) GetPreview() []*map[string]interface{}`

GetPreview returns the Preview field if non-nil, zero value otherwise.

### GetPreviewOk

`func (o *QueryResultOut) GetPreviewOk() (*[]*map[string]interface{}, bool)`

GetPreviewOk returns a tuple with the Preview field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPreview

`func (o *QueryResultOut) SetPreview(v []*map[string]interface{})`

SetPreview sets Preview field to given value.


### GetResultArtId

`func (o *QueryResultOut) GetResultArtId() string`

GetResultArtId returns the ResultArtId field if non-nil, zero value otherwise.

### GetResultArtIdOk

`func (o *QueryResultOut) GetResultArtIdOk() (*string, bool)`

GetResultArtIdOk returns a tuple with the ResultArtId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResultArtId

`func (o *QueryResultOut) SetResultArtId(v string)`

SetResultArtId sets ResultArtId field to given value.


### GetResultSchema

`func (o *QueryResultOut) GetResultSchema() []QueryColumnOut`

GetResultSchema returns the ResultSchema field if non-nil, zero value otherwise.

### GetResultSchemaOk

`func (o *QueryResultOut) GetResultSchemaOk() (*[]QueryColumnOut, bool)`

GetResultSchemaOk returns a tuple with the ResultSchema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResultSchema

`func (o *QueryResultOut) SetResultSchema(v []QueryColumnOut)`

SetResultSchema sets ResultSchema field to given value.


### GetRowCount

`func (o *QueryResultOut) GetRowCount() int32`

GetRowCount returns the RowCount field if non-nil, zero value otherwise.

### GetRowCountOk

`func (o *QueryResultOut) GetRowCountOk() (*int32, bool)`

GetRowCountOk returns a tuple with the RowCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRowCount

`func (o *QueryResultOut) SetRowCount(v int32)`

SetRowCount sets RowCount field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
