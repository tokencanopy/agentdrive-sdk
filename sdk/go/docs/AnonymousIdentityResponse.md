# AnonymousIdentityResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AgentIdentityId** | **string** |  |
**ClaimMetadata** | [**ClaimMetadata**](ClaimMetadata.md) |  |
**ClaimToken** | **string** | Opaque server-issued secret. Present at POST /agent/identity/claim and at POST /oauth2/token (grant_type&#x3D;claim). |
**DriveId** | **string** |  |
**ExpiresAt** | **time.Time** |  |
**IdentityAssertion** | **string** | JWT signed by AgentDrive, scope&#x3D;pre_claim. 30-day TTL. |

## Methods

### NewAnonymousIdentityResponse

`func NewAnonymousIdentityResponse(agentIdentityId string, claimMetadata ClaimMetadata, claimToken string, driveId string, expiresAt time.Time, identityAssertion string, ) *AnonymousIdentityResponse`

NewAnonymousIdentityResponse instantiates a new AnonymousIdentityResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAnonymousIdentityResponseWithDefaults

`func NewAnonymousIdentityResponseWithDefaults() *AnonymousIdentityResponse`

NewAnonymousIdentityResponseWithDefaults instantiates a new AnonymousIdentityResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAgentIdentityId

`func (o *AnonymousIdentityResponse) GetAgentIdentityId() string`

GetAgentIdentityId returns the AgentIdentityId field if non-nil, zero value otherwise.

### GetAgentIdentityIdOk

`func (o *AnonymousIdentityResponse) GetAgentIdentityIdOk() (*string, bool)`

GetAgentIdentityIdOk returns a tuple with the AgentIdentityId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAgentIdentityId

`func (o *AnonymousIdentityResponse) SetAgentIdentityId(v string)`

SetAgentIdentityId sets AgentIdentityId field to given value.


### GetClaimMetadata

`func (o *AnonymousIdentityResponse) GetClaimMetadata() ClaimMetadata`

GetClaimMetadata returns the ClaimMetadata field if non-nil, zero value otherwise.

### GetClaimMetadataOk

`func (o *AnonymousIdentityResponse) GetClaimMetadataOk() (*ClaimMetadata, bool)`

GetClaimMetadataOk returns a tuple with the ClaimMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClaimMetadata

`func (o *AnonymousIdentityResponse) SetClaimMetadata(v ClaimMetadata)`

SetClaimMetadata sets ClaimMetadata field to given value.


### GetClaimToken

`func (o *AnonymousIdentityResponse) GetClaimToken() string`

GetClaimToken returns the ClaimToken field if non-nil, zero value otherwise.

### GetClaimTokenOk

`func (o *AnonymousIdentityResponse) GetClaimTokenOk() (*string, bool)`

GetClaimTokenOk returns a tuple with the ClaimToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClaimToken

`func (o *AnonymousIdentityResponse) SetClaimToken(v string)`

SetClaimToken sets ClaimToken field to given value.


### GetDriveId

`func (o *AnonymousIdentityResponse) GetDriveId() string`

GetDriveId returns the DriveId field if non-nil, zero value otherwise.

### GetDriveIdOk

`func (o *AnonymousIdentityResponse) GetDriveIdOk() (*string, bool)`

GetDriveIdOk returns a tuple with the DriveId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDriveId

`func (o *AnonymousIdentityResponse) SetDriveId(v string)`

SetDriveId sets DriveId field to given value.


### GetExpiresAt

`func (o *AnonymousIdentityResponse) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *AnonymousIdentityResponse) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *AnonymousIdentityResponse) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### GetIdentityAssertion

`func (o *AnonymousIdentityResponse) GetIdentityAssertion() string`

GetIdentityAssertion returns the IdentityAssertion field if non-nil, zero value otherwise.

### GetIdentityAssertionOk

`func (o *AnonymousIdentityResponse) GetIdentityAssertionOk() (*string, bool)`

GetIdentityAssertionOk returns a tuple with the IdentityAssertion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentityAssertion

`func (o *AnonymousIdentityResponse) SetIdentityAssertion(v string)`

SetIdentityAssertion sets IdentityAssertion field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
