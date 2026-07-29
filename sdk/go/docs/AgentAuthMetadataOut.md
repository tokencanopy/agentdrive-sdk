# AgentAuthMetadataOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClaimEndpoint** | **string** |  |
**EventsEndpoint** | **NullableString** |  |
**IdentityAssertion** | [**IdentityAssertionMetadataOut**](IdentityAssertionMetadataOut.md) |  |
**IdentityEndpoint** | **string** |  |
**IdentityTypesSupported** | **[]string** |  |
**Skill** | **string** |  |
**SpecVersion** | **string** |  |

## Methods

### NewAgentAuthMetadataOut

`func NewAgentAuthMetadataOut(claimEndpoint string, eventsEndpoint NullableString, identityAssertion IdentityAssertionMetadataOut, identityEndpoint string, identityTypesSupported []string, skill string, specVersion string, ) *AgentAuthMetadataOut`

NewAgentAuthMetadataOut instantiates a new AgentAuthMetadataOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgentAuthMetadataOutWithDefaults

`func NewAgentAuthMetadataOutWithDefaults() *AgentAuthMetadataOut`

NewAgentAuthMetadataOutWithDefaults instantiates a new AgentAuthMetadataOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClaimEndpoint

`func (o *AgentAuthMetadataOut) GetClaimEndpoint() string`

GetClaimEndpoint returns the ClaimEndpoint field if non-nil, zero value otherwise.

### GetClaimEndpointOk

`func (o *AgentAuthMetadataOut) GetClaimEndpointOk() (*string, bool)`

GetClaimEndpointOk returns a tuple with the ClaimEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClaimEndpoint

`func (o *AgentAuthMetadataOut) SetClaimEndpoint(v string)`

SetClaimEndpoint sets ClaimEndpoint field to given value.


### GetEventsEndpoint

`func (o *AgentAuthMetadataOut) GetEventsEndpoint() string`

GetEventsEndpoint returns the EventsEndpoint field if non-nil, zero value otherwise.

### GetEventsEndpointOk

`func (o *AgentAuthMetadataOut) GetEventsEndpointOk() (*string, bool)`

GetEventsEndpointOk returns a tuple with the EventsEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventsEndpoint

`func (o *AgentAuthMetadataOut) SetEventsEndpoint(v string)`

SetEventsEndpoint sets EventsEndpoint field to given value.


### SetEventsEndpointNil

`func (o *AgentAuthMetadataOut) SetEventsEndpointNil(b bool)`

 SetEventsEndpointNil sets the value for EventsEndpoint to be an explicit nil

### UnsetEventsEndpoint
`func (o *AgentAuthMetadataOut) UnsetEventsEndpoint()`

UnsetEventsEndpoint ensures that no value is present for EventsEndpoint, not even an explicit nil
### GetIdentityAssertion

`func (o *AgentAuthMetadataOut) GetIdentityAssertion() IdentityAssertionMetadataOut`

GetIdentityAssertion returns the IdentityAssertion field if non-nil, zero value otherwise.

### GetIdentityAssertionOk

`func (o *AgentAuthMetadataOut) GetIdentityAssertionOk() (*IdentityAssertionMetadataOut, bool)`

GetIdentityAssertionOk returns a tuple with the IdentityAssertion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentityAssertion

`func (o *AgentAuthMetadataOut) SetIdentityAssertion(v IdentityAssertionMetadataOut)`

SetIdentityAssertion sets IdentityAssertion field to given value.


### GetIdentityEndpoint

`func (o *AgentAuthMetadataOut) GetIdentityEndpoint() string`

GetIdentityEndpoint returns the IdentityEndpoint field if non-nil, zero value otherwise.

### GetIdentityEndpointOk

`func (o *AgentAuthMetadataOut) GetIdentityEndpointOk() (*string, bool)`

GetIdentityEndpointOk returns a tuple with the IdentityEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentityEndpoint

`func (o *AgentAuthMetadataOut) SetIdentityEndpoint(v string)`

SetIdentityEndpoint sets IdentityEndpoint field to given value.


### GetIdentityTypesSupported

`func (o *AgentAuthMetadataOut) GetIdentityTypesSupported() []string`

GetIdentityTypesSupported returns the IdentityTypesSupported field if non-nil, zero value otherwise.

### GetIdentityTypesSupportedOk

`func (o *AgentAuthMetadataOut) GetIdentityTypesSupportedOk() (*[]string, bool)`

GetIdentityTypesSupportedOk returns a tuple with the IdentityTypesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentityTypesSupported

`func (o *AgentAuthMetadataOut) SetIdentityTypesSupported(v []string)`

SetIdentityTypesSupported sets IdentityTypesSupported field to given value.


### GetSkill

`func (o *AgentAuthMetadataOut) GetSkill() string`

GetSkill returns the Skill field if non-nil, zero value otherwise.

### GetSkillOk

`func (o *AgentAuthMetadataOut) GetSkillOk() (*string, bool)`

GetSkillOk returns a tuple with the Skill field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSkill

`func (o *AgentAuthMetadataOut) SetSkill(v string)`

SetSkill sets Skill field to given value.


### GetSpecVersion

`func (o *AgentAuthMetadataOut) GetSpecVersion() string`

GetSpecVersion returns the SpecVersion field if non-nil, zero value otherwise.

### GetSpecVersionOk

`func (o *AgentAuthMetadataOut) GetSpecVersionOk() (*string, bool)`

GetSpecVersionOk returns a tuple with the SpecVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecVersion

`func (o *AgentAuthMetadataOut) SetSpecVersion(v string)`

SetSpecVersion sets SpecVersion field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
