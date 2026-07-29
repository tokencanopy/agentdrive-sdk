# DatasetDescriptionOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Columns** | [**[]QueryColumnOut**](QueryColumnOut.md) |  |
**Dataset** | **string** |  |

## Methods

### NewDatasetDescriptionOut

`func NewDatasetDescriptionOut(columns []QueryColumnOut, dataset string, ) *DatasetDescriptionOut`

NewDatasetDescriptionOut instantiates a new DatasetDescriptionOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDatasetDescriptionOutWithDefaults

`func NewDatasetDescriptionOutWithDefaults() *DatasetDescriptionOut`

NewDatasetDescriptionOutWithDefaults instantiates a new DatasetDescriptionOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetColumns

`func (o *DatasetDescriptionOut) GetColumns() []QueryColumnOut`

GetColumns returns the Columns field if non-nil, zero value otherwise.

### GetColumnsOk

`func (o *DatasetDescriptionOut) GetColumnsOk() (*[]QueryColumnOut, bool)`

GetColumnsOk returns a tuple with the Columns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColumns

`func (o *DatasetDescriptionOut) SetColumns(v []QueryColumnOut)`

SetColumns sets Columns field to given value.


### GetDataset

`func (o *DatasetDescriptionOut) GetDataset() string`

GetDataset returns the Dataset field if non-nil, zero value otherwise.

### GetDatasetOk

`func (o *DatasetDescriptionOut) GetDatasetOk() (*string, bool)`

GetDatasetOk returns a tuple with the Dataset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataset

`func (o *DatasetDescriptionOut) SetDataset(v string)`

SetDataset sets Dataset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
