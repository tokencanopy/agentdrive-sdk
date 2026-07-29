# FeedbackStatusOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Contact** | **bool** |  |
**CreatedAt** | **time.Time** |  |
**DuplicateOf** | Pointer to **NullableString** |  | [optional]
**Id** | **string** |  |
**Kind** | **string** |  |
**Status** | **string** |  |
**StatusChangedAt** | **time.Time** |  |
**Title** | **string** |  |

## Methods

### NewFeedbackStatusOut

`func NewFeedbackStatusOut(contact bool, createdAt time.Time, id string, kind string, status string, statusChangedAt time.Time, title string, ) *FeedbackStatusOut`

NewFeedbackStatusOut instantiates a new FeedbackStatusOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFeedbackStatusOutWithDefaults

`func NewFeedbackStatusOutWithDefaults() *FeedbackStatusOut`

NewFeedbackStatusOutWithDefaults instantiates a new FeedbackStatusOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContact

`func (o *FeedbackStatusOut) GetContact() bool`

GetContact returns the Contact field if non-nil, zero value otherwise.

### GetContactOk

`func (o *FeedbackStatusOut) GetContactOk() (*bool, bool)`

GetContactOk returns a tuple with the Contact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContact

`func (o *FeedbackStatusOut) SetContact(v bool)`

SetContact sets Contact field to given value.


### GetCreatedAt

`func (o *FeedbackStatusOut) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *FeedbackStatusOut) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *FeedbackStatusOut) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetDuplicateOf

`func (o *FeedbackStatusOut) GetDuplicateOf() string`

GetDuplicateOf returns the DuplicateOf field if non-nil, zero value otherwise.

### GetDuplicateOfOk

`func (o *FeedbackStatusOut) GetDuplicateOfOk() (*string, bool)`

GetDuplicateOfOk returns a tuple with the DuplicateOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDuplicateOf

`func (o *FeedbackStatusOut) SetDuplicateOf(v string)`

SetDuplicateOf sets DuplicateOf field to given value.

### HasDuplicateOf

`func (o *FeedbackStatusOut) HasDuplicateOf() bool`

HasDuplicateOf returns a boolean if a field has been set.

### SetDuplicateOfNil

`func (o *FeedbackStatusOut) SetDuplicateOfNil(b bool)`

 SetDuplicateOfNil sets the value for DuplicateOf to be an explicit nil

### UnsetDuplicateOf
`func (o *FeedbackStatusOut) UnsetDuplicateOf()`

UnsetDuplicateOf ensures that no value is present for DuplicateOf, not even an explicit nil
### GetId

`func (o *FeedbackStatusOut) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FeedbackStatusOut) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FeedbackStatusOut) SetId(v string)`

SetId sets Id field to given value.


### GetKind

`func (o *FeedbackStatusOut) GetKind() string`

GetKind returns the Kind field if non-nil, zero value otherwise.

### GetKindOk

`func (o *FeedbackStatusOut) GetKindOk() (*string, bool)`

GetKindOk returns a tuple with the Kind field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKind

`func (o *FeedbackStatusOut) SetKind(v string)`

SetKind sets Kind field to given value.


### GetStatus

`func (o *FeedbackStatusOut) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *FeedbackStatusOut) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *FeedbackStatusOut) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetStatusChangedAt

`func (o *FeedbackStatusOut) GetStatusChangedAt() time.Time`

GetStatusChangedAt returns the StatusChangedAt field if non-nil, zero value otherwise.

### GetStatusChangedAtOk

`func (o *FeedbackStatusOut) GetStatusChangedAtOk() (*time.Time, bool)`

GetStatusChangedAtOk returns a tuple with the StatusChangedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusChangedAt

`func (o *FeedbackStatusOut) SetStatusChangedAt(v time.Time)`

SetStatusChangedAt sets StatusChangedAt field to given value.


### GetTitle

`func (o *FeedbackStatusOut) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *FeedbackStatusOut) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *FeedbackStatusOut) SetTitle(v string)`

SetTitle sets Title field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
