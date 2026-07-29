# ClaimInitRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClaimToken** | **string** | The per-identity claim_token returned by POST /agent/identity. |
**Email** | Pointer to **NullableString** | Optional hint to display on the /claim page so the human knows which account the agent expected. Not enforced (design §14 question #3). | [optional]

## Methods

### NewClaimInitRequest

`func NewClaimInitRequest(claimToken string, ) *ClaimInitRequest`

NewClaimInitRequest instantiates a new ClaimInitRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewClaimInitRequestWithDefaults

`func NewClaimInitRequestWithDefaults() *ClaimInitRequest`

NewClaimInitRequestWithDefaults instantiates a new ClaimInitRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClaimToken

`func (o *ClaimInitRequest) GetClaimToken() string`

GetClaimToken returns the ClaimToken field if non-nil, zero value otherwise.

### GetClaimTokenOk

`func (o *ClaimInitRequest) GetClaimTokenOk() (*string, bool)`

GetClaimTokenOk returns a tuple with the ClaimToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClaimToken

`func (o *ClaimInitRequest) SetClaimToken(v string)`

SetClaimToken sets ClaimToken field to given value.


### GetEmail

`func (o *ClaimInitRequest) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *ClaimInitRequest) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *ClaimInitRequest) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *ClaimInitRequest) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### SetEmailNil

`func (o *ClaimInitRequest) SetEmailNil(b bool)`

 SetEmailNil sets the value for Email to be an explicit nil

### UnsetEmail
`func (o *ClaimInitRequest) UnsetEmail()`

UnsetEmail ensures that no value is present for Email, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
