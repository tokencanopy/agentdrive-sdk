# MemberRemoveOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  |
**Ok** | Pointer to **bool** |  | [optional] [default to true]
**OrganizationId** | **string** |  |

## Methods

### NewMemberRemoveOut

`func NewMemberRemoveOut(id string, organizationId string, ) *MemberRemoveOut`

NewMemberRemoveOut instantiates a new MemberRemoveOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMemberRemoveOutWithDefaults

`func NewMemberRemoveOutWithDefaults() *MemberRemoveOut`

NewMemberRemoveOutWithDefaults instantiates a new MemberRemoveOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *MemberRemoveOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *MemberRemoveOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *MemberRemoveOut) SetId(v string)`

SetId sets Id field to given value.


### GetOk

`func (o *MemberRemoveOut) GetOk() bool`

GetOk returns the Ok field if non-nil, zero value otherwise.

### GetOkOk

`func (o *MemberRemoveOut) GetOkOk() (*bool, bool)`

GetOkOk returns a tuple with the Ok field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOk

`func (o *MemberRemoveOut) SetOk(v bool)`

SetOk sets Ok field to given value.

### HasOk

`func (o *MemberRemoveOut) HasOk() bool`

HasOk returns a boolean if a field has been set.

### GetOrganizationId

`func (o *MemberRemoveOut) GetOrganizationId() string`

GetOrganizationId returns the OrganizationId field if non-nil, zero value otherwise.

### GetOrganizationIdOk

`func (o *MemberRemoveOut) GetOrganizationIdOk() (*string, bool)`

GetOrganizationIdOk returns a tuple with the OrganizationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganizationId

`func (o *MemberRemoveOut) SetOrganizationId(v string)`

SetOrganizationId sets OrganizationId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
