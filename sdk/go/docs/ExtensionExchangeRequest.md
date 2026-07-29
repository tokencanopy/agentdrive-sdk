# ExtensionExchangeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExtId** | **string** | The extension&#39;s ID (Chrome Web Store ID or unpacked dev ID). |
**Ticket** | **string** | The opaque ticket from the /auth/callback handoff. |

## Methods

### NewExtensionExchangeRequest

`func NewExtensionExchangeRequest(extId string, ticket string, ) *ExtensionExchangeRequest`

NewExtensionExchangeRequest instantiates a new ExtensionExchangeRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewExtensionExchangeRequestWithDefaults

`func NewExtensionExchangeRequestWithDefaults() *ExtensionExchangeRequest`

NewExtensionExchangeRequestWithDefaults instantiates a new ExtensionExchangeRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetExtId

`func (o *ExtensionExchangeRequest) GetExtId() string`

GetExtId returns the ExtId field if non-nil, zero value otherwise.

### GetExtIdOk

`func (o *ExtensionExchangeRequest) GetExtIdOk() (*string, bool)`

GetExtIdOk returns a tuple with the ExtId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExtId

`func (o *ExtensionExchangeRequest) SetExtId(v string)`

SetExtId sets ExtId field to given value.


### GetTicket

`func (o *ExtensionExchangeRequest) GetTicket() string`

GetTicket returns the Ticket field if non-nil, zero value otherwise.

### GetTicketOk

`func (o *ExtensionExchangeRequest) GetTicketOk() (*string, bool)`

GetTicketOk returns a tuple with the Ticket field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTicket

`func (o *ExtensionExchangeRequest) SetTicket(v string)`

SetTicket sets Ticket field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
