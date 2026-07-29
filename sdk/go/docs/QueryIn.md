# QueryIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DryRun** | Pointer to **bool** |  | [optional] [default to false]
**Inputs** | Pointer to **map[string]string** |  | [optional]
**Sql** | **string** |  |

## Methods

### NewQueryIn

`func NewQueryIn(sql string, ) *QueryIn`

NewQueryIn instantiates a new QueryIn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQueryInWithDefaults

`func NewQueryInWithDefaults() *QueryIn`

NewQueryInWithDefaults instantiates a new QueryIn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDryRun

`func (o *QueryIn) GetDryRun() bool`

GetDryRun returns the DryRun field if non-nil, zero value otherwise.

### GetDryRunOk

`func (o *QueryIn) GetDryRunOk() (*bool, bool)`

GetDryRunOk returns a tuple with the DryRun field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDryRun

`func (o *QueryIn) SetDryRun(v bool)`

SetDryRun sets DryRun field to given value.

### HasDryRun

`func (o *QueryIn) HasDryRun() bool`

HasDryRun returns a boolean if a field has been set.

### GetInputs

`func (o *QueryIn) GetInputs() map[string]string`

GetInputs returns the Inputs field if non-nil, zero value otherwise.

### GetInputsOk

`func (o *QueryIn) GetInputsOk() (*map[string]string, bool)`

GetInputsOk returns a tuple with the Inputs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInputs

`func (o *QueryIn) SetInputs(v map[string]string)`

SetInputs sets Inputs field to given value.

### HasInputs

`func (o *QueryIn) HasInputs() bool`

HasInputs returns a boolean if a field has been set.

### GetSql

`func (o *QueryIn) GetSql() string`

GetSql returns the Sql field if non-nil, zero value otherwise.

### GetSqlOk

`func (o *QueryIn) GetSqlOk() (*string, bool)`

GetSqlOk returns a tuple with the Sql field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSql

`func (o *QueryIn) SetSql(v string)`

SetSql sets Sql field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
