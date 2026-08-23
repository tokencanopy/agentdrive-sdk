# UploadInitiationOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExpiresAt** | **time.Time** |  |
**Method** | **string** |  |
**RequiredHeaders** | **map[string]string** |  |
**Url** | **string** |  |

## Methods

### NewUploadInitiationOut

`func NewUploadInitiationOut(expiresAt time.Time, method string, requiredHeaders map[string]string, url string, ) *UploadInitiationOut`

NewUploadInitiationOut instantiates a new UploadInitiationOut object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUploadInitiationOutWithDefaults

`func NewUploadInitiationOutWithDefaults() *UploadInitiationOut`

NewUploadInitiationOutWithDefaults instantiates a new UploadInitiationOut object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetExpiresAt

`func (o *UploadInitiationOut) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *UploadInitiationOut) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *UploadInitiationOut) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### GetMethod

`func (o *UploadInitiationOut) GetMethod() string`

GetMethod returns the Method field if non-nil, zero value otherwise.

### GetMethodOk

`func (o *UploadInitiationOut) GetMethodOk() (*string, bool)`

GetMethodOk returns a tuple with the Method field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMethod

`func (o *UploadInitiationOut) SetMethod(v string)`

SetMethod sets Method field to given value.


### GetRequiredHeaders

`func (o *UploadInitiationOut) GetRequiredHeaders() map[string]string`

GetRequiredHeaders returns the RequiredHeaders field if non-nil, zero value otherwise.

### GetRequiredHeadersOk

`func (o *UploadInitiationOut) GetRequiredHeadersOk() (*map[string]string, bool)`

GetRequiredHeadersOk returns a tuple with the RequiredHeaders field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequiredHeaders

`func (o *UploadInitiationOut) SetRequiredHeaders(v map[string]string)`

SetRequiredHeaders sets RequiredHeaders field to given value.


### GetUrl

`func (o *UploadInitiationOut) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *UploadInitiationOut) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *UploadInitiationOut) SetUrl(v string)`

SetUrl sets Url field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
