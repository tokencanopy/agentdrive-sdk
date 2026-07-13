# RevokeOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ok** | Pointer to **bool** |  | [optional] [default to true]
**Id** | **string** |  | 
**Revoked** | **int32** |  | 

## Methods

### NewRevokeOut

`func NewRevokeOut(id string, revoked int32, ) *RevokeOut`

NewRevokeOut instantiates a new RevokeOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRevokeOutWithDefaults

`func NewRevokeOutWithDefaults() *RevokeOut`

NewRevokeOutWithDefaults instantiates a new RevokeOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOk

`func (o *RevokeOut) GetOk() bool`

GetOk returns the Ok field if non-nil, zero value otherwise.

### GetOkOk

`func (o *RevokeOut) GetOkOk() (*bool, bool)`

GetOkOk returns a tuple with the Ok field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOk

`func (o *RevokeOut) SetOk(v bool)`

SetOk sets Ok field to given value.

### HasOk

`func (o *RevokeOut) HasOk() bool`

HasOk returns a boolean if a field has been set.

### GetId

`func (o *RevokeOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *RevokeOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *RevokeOut) SetId(v string)`

SetId sets Id field to given value.


### GetRevoked

`func (o *RevokeOut) GetRevoked() int32`

GetRevoked returns the Revoked field if non-nil, zero value otherwise.

### GetRevokedOk

`func (o *RevokeOut) GetRevokedOk() (*int32, bool)`

GetRevokedOk returns a tuple with the Revoked field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevoked

`func (o *RevokeOut) SetRevoked(v int32)`

SetRevoked sets Revoked field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


