# UploadTransferOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ChunkProtocol** | **string** |  |
**Chunks** | [**UploadChunksOut**](UploadChunksOut.md) |  |
**Initiation** | [**UploadInitiationOut**](UploadInitiationOut.md) |  |

## Methods

### NewUploadTransferOut

`func NewUploadTransferOut(chunkProtocol string, chunks UploadChunksOut, initiation UploadInitiationOut, ) *UploadTransferOut`

NewUploadTransferOut instantiates a new UploadTransferOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUploadTransferOutWithDefaults

`func NewUploadTransferOutWithDefaults() *UploadTransferOut`

NewUploadTransferOutWithDefaults instantiates a new UploadTransferOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetChunkProtocol

`func (o *UploadTransferOut) GetChunkProtocol() string`

GetChunkProtocol returns the ChunkProtocol field if non-nil, zero value otherwise.

### GetChunkProtocolOk

`func (o *UploadTransferOut) GetChunkProtocolOk() (*string, bool)`

GetChunkProtocolOk returns a tuple with the ChunkProtocol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChunkProtocol

`func (o *UploadTransferOut) SetChunkProtocol(v string)`

SetChunkProtocol sets ChunkProtocol field to given value.


### GetChunks

`func (o *UploadTransferOut) GetChunks() UploadChunksOut`

GetChunks returns the Chunks field if non-nil, zero value otherwise.

### GetChunksOk

`func (o *UploadTransferOut) GetChunksOk() (*UploadChunksOut, bool)`

GetChunksOk returns a tuple with the Chunks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChunks

`func (o *UploadTransferOut) SetChunks(v UploadChunksOut)`

SetChunks sets Chunks field to given value.


### GetInitiation

`func (o *UploadTransferOut) GetInitiation() UploadInitiationOut`

GetInitiation returns the Initiation field if non-nil, zero value otherwise.

### GetInitiationOk

`func (o *UploadTransferOut) GetInitiationOk() (*UploadInitiationOut, bool)`

GetInitiationOk returns a tuple with the Initiation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInitiation

`func (o *UploadTransferOut) SetInitiation(v UploadInitiationOut)`

SetInitiation sets Initiation field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
