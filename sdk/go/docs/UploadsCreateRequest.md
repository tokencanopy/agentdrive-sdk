# UploadsCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Target** | [**UploadsCreateRequestTarget**](UploadsCreateRequestTarget.md) |  | 
**Content** | [**UploadsCreateRequestContent**](UploadsCreateRequestContent.md) |  | 

## Methods

### NewUploadsCreateRequest

`func NewUploadsCreateRequest(target UploadsCreateRequestTarget, content UploadsCreateRequestContent, ) *UploadsCreateRequest`

NewUploadsCreateRequest instantiates a new UploadsCreateRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUploadsCreateRequestWithDefaults

`func NewUploadsCreateRequestWithDefaults() *UploadsCreateRequest`

NewUploadsCreateRequestWithDefaults instantiates a new UploadsCreateRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTarget

`func (o *UploadsCreateRequest) GetTarget() UploadsCreateRequestTarget`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *UploadsCreateRequest) GetTargetOk() (*UploadsCreateRequestTarget, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *UploadsCreateRequest) SetTarget(v UploadsCreateRequestTarget)`

SetTarget sets Target field to given value.


### GetContent

`func (o *UploadsCreateRequest) GetContent() UploadsCreateRequestContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *UploadsCreateRequest) GetContentOk() (*UploadsCreateRequestContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *UploadsCreateRequest) SetContent(v UploadsCreateRequestContent)`

SetContent sets Content field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


