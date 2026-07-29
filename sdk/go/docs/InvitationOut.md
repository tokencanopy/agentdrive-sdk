# InvitationOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAt** | **time.Time** |  |
**Email** | **string** |  |
**ExpiresAt** | **time.Time** |  |
**Id** | **string** |  |
**InvitedBy** | Pointer to **NullableString** |  | [optional]
**OrganizationId** | **string** |  |
**Role** | **string** |  |
**Status** | **string** |  |

## Methods

### NewInvitationOut

`func NewInvitationOut(createdAt time.Time, email string, expiresAt time.Time, id string, organizationId string, role string, status string, ) *InvitationOut`

NewInvitationOut instantiates a new InvitationOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInvitationOutWithDefaults

`func NewInvitationOutWithDefaults() *InvitationOut`

NewInvitationOutWithDefaults instantiates a new InvitationOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreatedAt

`func (o *InvitationOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *InvitationOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *InvitationOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetEmail

`func (o *InvitationOut) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *InvitationOut) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *InvitationOut) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetExpiresAt

`func (o *InvitationOut) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *InvitationOut) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *InvitationOut) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### GetId

`func (o *InvitationOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *InvitationOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *InvitationOut) SetId(v string)`

SetId sets Id field to given value.


### GetInvitedBy

`func (o *InvitationOut) GetInvitedBy() string`

GetInvitedBy returns the InvitedBy field if non-nil, zero value otherwise.

### GetInvitedByOk

`func (o *InvitationOut) GetInvitedByOk() (*string, bool)`

GetInvitedByOk returns a tuple with the InvitedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInvitedBy

`func (o *InvitationOut) SetInvitedBy(v string)`

SetInvitedBy sets InvitedBy field to given value.

### HasInvitedBy

`func (o *InvitationOut) HasInvitedBy() bool`

HasInvitedBy returns a boolean if a field has been set.

### SetInvitedByNil

`func (o *InvitationOut) SetInvitedByNil(b bool)`

 SetInvitedByNil sets the value for InvitedBy to be an explicit nil

### UnsetInvitedBy
`func (o *InvitationOut) UnsetInvitedBy()`

UnsetInvitedBy ensures that no value is present for InvitedBy, not even an explicit nil
### GetOrganizationId

`func (o *InvitationOut) GetOrganizationId() string`

GetOrganizationId returns the OrganizationId field if non-nil, zero value otherwise.

### GetOrganizationIdOk

`func (o *InvitationOut) GetOrganizationIdOk() (*string, bool)`

GetOrganizationIdOk returns a tuple with the OrganizationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrganizationId

`func (o *InvitationOut) SetOrganizationId(v string)`

SetOrganizationId sets OrganizationId field to given value.


### GetRole

`func (o *InvitationOut) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *InvitationOut) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *InvitationOut) SetRole(v string)`

SetRole sets Role field to given value.


### GetStatus

`func (o *InvitationOut) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *InvitationOut) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *InvitationOut) SetStatus(v string)`

SetStatus sets Status field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
