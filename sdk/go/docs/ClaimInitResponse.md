# ClaimInitResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClaimAttemptToken** | **string** | Per-attempt opaque token; the agent does not need to present it. |
**ExpiresAt** | **time.Time** |  |
**UserCode** | **string** | Human-readable code the user types/sees on /claim. |
**VerificationUri** | **string** | URL to direct the human to. |
**VerificationUriComplete** | **string** | Convenience: same as &#x60;verification_uri&#x60; but with the user_code pre-baked so the human doesn&#39;t have to type it. RFC 8628 idiom. |

## Methods

### NewClaimInitResponse

`func NewClaimInitResponse(claimAttemptToken string, expiresAt time.Time, userCode string, verificationUri string, verificationUriComplete string, ) *ClaimInitResponse`

NewClaimInitResponse instantiates a new ClaimInitResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewClaimInitResponseWithDefaults

`func NewClaimInitResponseWithDefaults() *ClaimInitResponse`

NewClaimInitResponseWithDefaults instantiates a new ClaimInitResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClaimAttemptToken

`func (o *ClaimInitResponse) GetClaimAttemptToken() string`

GetClaimAttemptToken returns the ClaimAttemptToken field if non-nil, zero value otherwise.

### GetClaimAttemptTokenOk

`func (o *ClaimInitResponse) GetClaimAttemptTokenOk() (*string, bool)`

GetClaimAttemptTokenOk returns a tuple with the ClaimAttemptToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClaimAttemptToken

`func (o *ClaimInitResponse) SetClaimAttemptToken(v string)`

SetClaimAttemptToken sets ClaimAttemptToken field to given value.


### GetExpiresAt

`func (o *ClaimInitResponse) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *ClaimInitResponse) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *ClaimInitResponse) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### GetUserCode

`func (o *ClaimInitResponse) GetUserCode() string`

GetUserCode returns the UserCode field if non-nil, zero value otherwise.

### GetUserCodeOk

`func (o *ClaimInitResponse) GetUserCodeOk() (*string, bool)`

GetUserCodeOk returns a tuple with the UserCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserCode

`func (o *ClaimInitResponse) SetUserCode(v string)`

SetUserCode sets UserCode field to given value.


### GetVerificationUri

`func (o *ClaimInitResponse) GetVerificationUri() string`

GetVerificationUri returns the VerificationUri field if non-nil, zero value otherwise.

### GetVerificationUriOk

`func (o *ClaimInitResponse) GetVerificationUriOk() (*string, bool)`

GetVerificationUriOk returns a tuple with the VerificationUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerificationUri

`func (o *ClaimInitResponse) SetVerificationUri(v string)`

SetVerificationUri sets VerificationUri field to given value.


### GetVerificationUriComplete

`func (o *ClaimInitResponse) GetVerificationUriComplete() string`

GetVerificationUriComplete returns the VerificationUriComplete field if non-nil, zero value otherwise.

### GetVerificationUriCompleteOk

`func (o *ClaimInitResponse) GetVerificationUriCompleteOk() (*string, bool)`

GetVerificationUriCompleteOk returns a tuple with the VerificationUriComplete field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerificationUriComplete

`func (o *ClaimInitResponse) SetVerificationUriComplete(v string)`

SetVerificationUriComplete sets VerificationUriComplete field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
