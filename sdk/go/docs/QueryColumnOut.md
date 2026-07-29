# QueryColumnOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  |
**Type** | Pointer to **NullableString** |  | [optional]

## Methods

### NewQueryColumnOut

`func NewQueryColumnOut(name string, ) *QueryColumnOut`

NewQueryColumnOut instantiates a new QueryColumnOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQueryColumnOutWithDefaults

`func NewQueryColumnOutWithDefaults() *QueryColumnOut`

NewQueryColumnOutWithDefaults instantiates a new QueryColumnOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *QueryColumnOut) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *QueryColumnOut) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *QueryColumnOut) SetName(v string)`

SetName sets Name field to given value.


### GetType

`func (o *QueryColumnOut) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *QueryColumnOut) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *QueryColumnOut) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *QueryColumnOut) HasType() bool`

HasType returns a boolean if a field has been set.

### SetTypeNil

`func (o *QueryColumnOut) SetTypeNil(b bool)`

 SetTypeNil sets the value for Type to be an explicit nil

### UnsetType
`func (o *QueryColumnOut) UnsetType()`

UnsetType ensures that no value is present for Type, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
