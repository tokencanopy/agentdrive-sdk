# FeedbackCreateOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Contact** | **bool** |  |
**Id** | **string** |  |
**Note** | Pointer to **NullableString** |  | [optional]
**Status** | **string** |  |

## Methods

### NewFeedbackCreateOut

`func NewFeedbackCreateOut(contact bool, id string, status string, ) *FeedbackCreateOut`

NewFeedbackCreateOut instantiates a new FeedbackCreateOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFeedbackCreateOutWithDefaults

`func NewFeedbackCreateOutWithDefaults() *FeedbackCreateOut`

NewFeedbackCreateOutWithDefaults instantiates a new FeedbackCreateOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContact

`func (o *FeedbackCreateOut) GetContact() bool`

GetContact returns the Contact field if non-nil, zero value otherwise.

### GetContactOk

`func (o *FeedbackCreateOut) GetContactOk() (*bool, bool)`

GetContactOk returns a tuple with the Contact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContact

`func (o *FeedbackCreateOut) SetContact(v bool)`

SetContact sets Contact field to given value.


### GetId

`func (o *FeedbackCreateOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FeedbackCreateOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FeedbackCreateOut) SetId(v string)`

SetId sets Id field to given value.


### GetNote

`func (o *FeedbackCreateOut) GetNote() string`

GetNote returns the Note field if non-nil, zero value otherwise.

### GetNoteOk

`func (o *FeedbackCreateOut) GetNoteOk() (*string, bool)`

GetNoteOk returns a tuple with the Note field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNote

`func (o *FeedbackCreateOut) SetNote(v string)`

SetNote sets Note field to given value.

### HasNote

`func (o *FeedbackCreateOut) HasNote() bool`

HasNote returns a boolean if a field has been set.

### SetNoteNil

`func (o *FeedbackCreateOut) SetNoteNil(b bool)`

 SetNoteNil sets the value for Note to be an explicit nil

### UnsetNote
`func (o *FeedbackCreateOut) UnsetNote()`

UnsetNote ensures that no value is present for Note, not even an explicit nil
### GetStatus

`func (o *FeedbackCreateOut) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *FeedbackCreateOut) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *FeedbackCreateOut) SetStatus(v string)`

SetStatus sets Status field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
