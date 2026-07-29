# ShareMintOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccessCount** | Pointer to **int32** |  | [optional] [default to 0]
**Audience** | **string** |  |
**CreatedAt** | **time.Time** |  |
**ExpiresAt** | Pointer to **NullableTime** |  | [optional]
**HasPassword** | **bool** |  |
**Id** | **string** |  |
**LastAccessedAt** | Pointer to **NullableTime** |  | [optional]
**ResourceId** | **string** |  |
**ResourceType** | **string** |  |
**Role** | **string** |  |
**ShareKey** | **string** |  |
**Url** | **string** |  |

## Methods

### NewShareMintOut

`func NewShareMintOut(audience string, createdAt time.Time, hasPassword bool, id string, resourceId string, resourceType string, role string, shareKey string, url string, ) *ShareMintOut`

NewShareMintOut instantiates a new ShareMintOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewShareMintOutWithDefaults

`func NewShareMintOutWithDefaults() *ShareMintOut`

NewShareMintOutWithDefaults instantiates a new ShareMintOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccessCount

`func (o *ShareMintOut) GetAccessCount() int32`

GetAccessCount returns the AccessCount field if non-nil, zero value otherwise.

### GetAccessCountOk

`func (o *ShareMintOut) GetAccessCountOk() (*int32, bool)`

GetAccessCountOk returns a tuple with the AccessCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccessCount

`func (o *ShareMintOut) SetAccessCount(v int32)`

SetAccessCount sets AccessCount field to given value.

### HasAccessCount

`func (o *ShareMintOut) HasAccessCount() bool`

HasAccessCount returns a boolean if a field has been set.

### GetAudience

`func (o *ShareMintOut) GetAudience() string`

GetAudience returns the Audience field if non-nil, zero value otherwise.

### GetAudienceOk

`func (o *ShareMintOut) GetAudienceOk() (*string, bool)`

GetAudienceOk returns a tuple with the Audience field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAudience

`func (o *ShareMintOut) SetAudience(v string)`

SetAudience sets Audience field to given value.


### GetCreatedAt

`func (o *ShareMintOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ShareMintOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ShareMintOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetExpiresAt

`func (o *ShareMintOut) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *ShareMintOut) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *ShareMintOut) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.

### HasExpiresAt

`func (o *ShareMintOut) HasExpiresAt() bool`

HasExpiresAt returns a boolean if a field has been set.

### SetExpiresAtNil

`func (o *ShareMintOut) SetExpiresAtNil(b bool)`

 SetExpiresAtNil sets the value for ExpiresAt to be an explicit nil

### UnsetExpiresAt
`func (o *ShareMintOut) UnsetExpiresAt()`

UnsetExpiresAt ensures that no value is present for ExpiresAt, not even an explicit nil
### GetHasPassword

`func (o *ShareMintOut) GetHasPassword() bool`

GetHasPassword returns the HasPassword field if non-nil, zero value otherwise.

### GetHasPasswordOk

`func (o *ShareMintOut) GetHasPasswordOk() (*bool, bool)`

GetHasPasswordOk returns a tuple with the HasPassword field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasPassword

`func (o *ShareMintOut) SetHasPassword(v bool)`

SetHasPassword sets HasPassword field to given value.


### GetId

`func (o *ShareMintOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ShareMintOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ShareMintOut) SetId(v string)`

SetId sets Id field to given value.


### GetLastAccessedAt

`func (o *ShareMintOut) GetLastAccessedAt() time.Time`

GetLastAccessedAt returns the LastAccessedAt field if non-nil, zero value otherwise.

### GetLastAccessedAtOk

`func (o *ShareMintOut) GetLastAccessedAtOk() (*time.Time, bool)`

GetLastAccessedAtOk returns a tuple with the LastAccessedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastAccessedAt

`func (o *ShareMintOut) SetLastAccessedAt(v time.Time)`

SetLastAccessedAt sets LastAccessedAt field to given value.

### HasLastAccessedAt

`func (o *ShareMintOut) HasLastAccessedAt() bool`

HasLastAccessedAt returns a boolean if a field has been set.

### SetLastAccessedAtNil

`func (o *ShareMintOut) SetLastAccessedAtNil(b bool)`

 SetLastAccessedAtNil sets the value for LastAccessedAt to be an explicit nil

### UnsetLastAccessedAt
`func (o *ShareMintOut) UnsetLastAccessedAt()`

UnsetLastAccessedAt ensures that no value is present for LastAccessedAt, not even an explicit nil
### GetResourceId

`func (o *ShareMintOut) GetResourceId() string`

GetResourceId returns the ResourceId field if non-nil, zero value otherwise.

### GetResourceIdOk

`func (o *ShareMintOut) GetResourceIdOk() (*string, bool)`

GetResourceIdOk returns a tuple with the ResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceId

`func (o *ShareMintOut) SetResourceId(v string)`

SetResourceId sets ResourceId field to given value.


### GetResourceType

`func (o *ShareMintOut) GetResourceType() string`

GetResourceType returns the ResourceType field if non-nil, zero value otherwise.

### GetResourceTypeOk

`func (o *ShareMintOut) GetResourceTypeOk() (*string, bool)`

GetResourceTypeOk returns a tuple with the ResourceType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceType

`func (o *ShareMintOut) SetResourceType(v string)`

SetResourceType sets ResourceType field to given value.


### GetRole

`func (o *ShareMintOut) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *ShareMintOut) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *ShareMintOut) SetRole(v string)`

SetRole sets Role field to given value.


### GetShareKey

`func (o *ShareMintOut) GetShareKey() string`

GetShareKey returns the ShareKey field if non-nil, zero value otherwise.

### GetShareKeyOk

`func (o *ShareMintOut) GetShareKeyOk() (*string, bool)`

GetShareKeyOk returns a tuple with the ShareKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShareKey

`func (o *ShareMintOut) SetShareKey(v string)`

SetShareKey sets ShareKey field to given value.


### GetUrl

`func (o *ShareMintOut) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *ShareMintOut) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *ShareMintOut) SetUrl(v string)`

SetUrl sets Url field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
