# InviteCreateOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Invitation** | Pointer to [**NullableInvitationOut**](InvitationOut.md) |  | [optional] 
**AlreadyMember** | Pointer to **bool** |  | [optional] [default to false]
**EmailDelivered** | Pointer to **bool** |  | [optional] [default to true]

## Methods

### NewInviteCreateOut

`func NewInviteCreateOut() *InviteCreateOut`

NewInviteCreateOut instantiates a new InviteCreateOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInviteCreateOutWithDefaults

`func NewInviteCreateOutWithDefaults() *InviteCreateOut`

NewInviteCreateOutWithDefaults instantiates a new InviteCreateOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInvitation

`func (o *InviteCreateOut) GetInvitation() InvitationOut`

GetInvitation returns the Invitation field if non-nil, zero value otherwise.

### GetInvitationOk

`func (o *InviteCreateOut) GetInvitationOk() (*InvitationOut, bool)`

GetInvitationOk returns a tuple with the Invitation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInvitation

`func (o *InviteCreateOut) SetInvitation(v InvitationOut)`

SetInvitation sets Invitation field to given value.

### HasInvitation

`func (o *InviteCreateOut) HasInvitation() bool`

HasInvitation returns a boolean if a field has been set.

### SetInvitationNil

`func (o *InviteCreateOut) SetInvitationNil(b bool)`

 SetInvitationNil sets the value for Invitation to be an explicit nil

### UnsetInvitation
`func (o *InviteCreateOut) UnsetInvitation()`

UnsetInvitation ensures that no value is present for Invitation, not even an explicit nil
### GetAlreadyMember

`func (o *InviteCreateOut) GetAlreadyMember() bool`

GetAlreadyMember returns the AlreadyMember field if non-nil, zero value otherwise.

### GetAlreadyMemberOk

`func (o *InviteCreateOut) GetAlreadyMemberOk() (*bool, bool)`

GetAlreadyMemberOk returns a tuple with the AlreadyMember field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlreadyMember

`func (o *InviteCreateOut) SetAlreadyMember(v bool)`

SetAlreadyMember sets AlreadyMember field to given value.

### HasAlreadyMember

`func (o *InviteCreateOut) HasAlreadyMember() bool`

HasAlreadyMember returns a boolean if a field has been set.

### GetEmailDelivered

`func (o *InviteCreateOut) GetEmailDelivered() bool`

GetEmailDelivered returns the EmailDelivered field if non-nil, zero value otherwise.

### GetEmailDeliveredOk

`func (o *InviteCreateOut) GetEmailDeliveredOk() (*bool, bool)`

GetEmailDeliveredOk returns a tuple with the EmailDelivered field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmailDelivered

`func (o *InviteCreateOut) SetEmailDelivered(v bool)`

SetEmailDelivered sets EmailDelivered field to given value.

### HasEmailDelivered

`func (o *InviteCreateOut) HasEmailDelivered() bool`

HasEmailDelivered returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


